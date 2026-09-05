# Based on Parr (2016)
import sys
from pathlib import Path
from z3 import *
import pdb

# Add lib to system path so we can import the generated files
# They're kept in a separate directory to prevent mixing of generated
# and written code. This path setting fails if the execution
# directory is different from the script location in src
lib_path = Path("../lib/")
sys.path.append(str(lib_path))  # TODO: replace this with __init__.py ?
from antlr4 import *
from BENEFIT_LANGUAGELexer import BENEFIT_LANGUAGELexer
from BENEFIT_LANGUAGEParser import BENEFIT_LANGUAGEParser
from BENEFIT_LANGUAGEVisitor import BENEFIT_LANGUAGEVisitor

# Holds declared Z3 objects, e.g. variables, in a global namespace
solver_objects = {}
s = Solver()


def main(argv):
    '''
    Takes a BEN file as input, outputs to SMT-LIB2 with same filename,
    different extension
    '''
    global s
    program = FileStream(fileName=argv[1], encoding='utf-8')
    lexer = BENEFIT_LANGUAGELexer(program)
    stream = CommonTokenStream(lexer)
    parser = BENEFIT_LANGUAGEParser(stream)
    tree = parser.file_()
    smt_lib_converter = SmtLibConverter()
    print("Begun solver setup")
    output = smt_lib_converter.visit(tree)
    print("Completed solver setup")
    if s.check() == sat:
        print("\nThe system is satisfiable.")
    else:
        print("\nThe system is not satisfiable.")
    # Optionally drop to a debugger REPL to inspect the solver state,
    # e.g. python3 ben_to_z3.py SAMPLE_BENEFIT_RULES.ben --debug
    if "--debug" in argv[2:]:
        pdb.set_trace()


class SmtLibConverter(BENEFIT_LANGUAGEVisitor):
    '''
    Each node either visits its children, or processes the content
    of itself and its immediate children if it's at the lowest
    level. We use globals throughout, partly because we want to
    define objects in statements and then access them in later,
    non-children statements, partly because the Ben language
    has no namespaces, at present.
    '''
    # Helper functions
    def Min(self, a, b):
        return If(a < b, a, b)

    def Max(self, a, b):
        return If(a > b, a, b)

    # Visit a parse tree produced by BENEFIT_LANGUAGEParser#file.
    def visitFile(self, ctx: BENEFIT_LANGUAGEParser.FileContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by BENEFIT_LANGUAGEParser#statements.
    def visitStatements(self, ctx: BENEFIT_LANGUAGEParser.StatementsContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by BENEFIT_LANGUAGEParser#statement.
    def visitStatement(self, ctx: BENEFIT_LANGUAGEParser.StatementContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by BENEFIT_LANGUAGEParser#test_statement.
    def visitTest_statement(self, ctx: BENEFIT_LANGUAGEParser.Test_statementContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by BENEFIT_LANGUAGEParser#assign_variable.
    def visitAssign_variable(self, ctx: BENEFIT_LANGUAGEParser.Assign_variableContext):
        '''
        Let a variable = a value, as part of test case setup
        '''
        global s
        global solver_objects
        var_name = ctx.VARIABLE_NAME().getText()
        if ctx.value() is not None:
            var_value = self.visit(ctx.value())
        else:
            var_value = self.visit(ctx.enum_reference())
        print(solver_objects[var_name], " == ", var_value)
        s.add(solver_objects[var_name] == var_value)

    # Visit a parse tree produced by BENEFIT_LANGUAGEParser#verify_value.
    def visitVerify_value(self, ctx: BENEFIT_LANGUAGEParser.Verify_valueContext):
        '''
        Verify that a variable == a value, i.e. must be that value, to confirm test case output
        '''
        global s
        global solver_objects
        var_name = ctx.VARIABLE_NAME().getText()
        if ctx.value() is not None:
            var_value = self.visit(ctx.value())
        else:
            var_value = self.visit(ctx.enum_reference())

        if s.check() == sat:
            print("\nThe system is satisfiable.")
        else:
            print("\nThe system is not satisfiable.")
        print("\nResult of validity check:")
        print(prove(solver_objects[var_name] == var_value))

    # Visit a parse tree produced by BENEFIT_LANGUAGEParser#declare_function.
    def visitDeclare_function(self, ctx: BENEFIT_LANGUAGEParser.Declare_functionContext):
        global s
        declared_var = self.visit(ctx.getChild(0))
        inside_brackets = self.visit(ctx.getChild(3))
        s.add(declared_var == inside_brackets)

    # Visit a parse tree produced by BENEFIT_LANGUAGEParser#declare_enum_variable.
    def visitDeclare_enum_variable(self, ctx: BENEFIT_LANGUAGEParser.Declare_enum_variableContext):
        global solver_objects
        enum_name = ctx.children[0].getText()
        var_name = ctx.children[1].getText()
        # This declares a constant rather than variable, which is
        # not strictly incorrect - it's an unknown constant
        solver_objects[var_name] = Const(var_name, solver_objects[enum_name])

    # Visit a parse tree produced by BENEFIT_LANGUAGEParser#declare_variable.
    def visitDeclare_variable(self, ctx: BENEFIT_LANGUAGEParser.Declare_variableContext):
        global solver_objects
        global s
        var_type = ctx.getChild(0).getText()
        var_name = ctx.getChild(1).getText()
        # There is currently no way of carrying out type checking
        # TODO: Create and use custom types to ensure type safety?
        if var_type == "Integer":
            solver_objects[var_name] = Int(var_name)
            # To force non-negative integer, we assert a constraint on values taken
            s.add(solver_objects[var_name] >= 0)
        elif var_type == "Money":
            solver_objects[var_name] = Int(var_name)
        elif var_type == "Percent":
            # Not currently needed, and would require a fair amount of
            # implementation logic to handle well
            raise NotImplementedError("Unsupported behaviour: Percent variables not currently supported.")
        elif var_type == "Date":
            solver_objects[var_name] = String(var_name)
        else:
            solver_objects[var_name] = Bool(var_name)
        # We return the newly created variable, in case it forms part of a
        # function declaration, and the parent wants to use what we've
        # declared to make an assertion, in SMT-LIB-speak
        return solver_objects[var_name]

    # Visit a parse tree produced by BENEFIT_LANGUAGEParser#declare_enum_type.
    def visitDeclare_enum_type(self, ctx: BENEFIT_LANGUAGEParser.Declare_enum_typeContext):
        # Using a global dictionary as a central namespace
        # for storing Z3 variables, constants etc
        global solver_objects
        enum_name = ctx.children[1].getText()
        solver_objects[enum_name] = Datatype(enum_name)
        number_of_enum_values = (ctx.getChildCount() - 3) // 2
        for x in range(number_of_enum_values):
            # Note this is 0 to number_of_enum_values -1
            solver_objects[enum_name].declare(ctx.children[(x * 2) + 3].getText())
        solver_objects[enum_name] = solver_objects[enum_name].create()

    # Visit a parse tree produced by BENEFIT_LANGUAGEParser#expression.
    def visitExpression(self, ctx: BENEFIT_LANGUAGEParser.ExpressionContext):
        if ctx.left is not None:
            left = self.visit(ctx.left)

        if ctx.right is not None:
            right = self.visit(ctx.right)

        if ctx.unbracket is not None:
            return self.visit(ctx.unbracket)

        if ctx.multdiv is not None:
            if ctx.multdiv.text == "*":
                return left * right
            else:
                return left / right

        if ctx.plusminus is not None:
            if ctx.plusminus.text == "+":
                return left + right
            else:  # ctx.plusminus.text == "~-"
                # Add a zero-lower bound, the manual way
                return self.Max(left - right, Int(0))

        if ctx.comparison is not None:
            op_text = ctx.comparison.text
            if op_text == "==":
                return left == right
            elif op_text == "<=":
                return left <= right
            elif op_text == "<":
                return left < right
            elif op_text == ">=":
                return left >= right
            else:  # op_text == ">"
                return left > right

        if ctx.and_ is not None:
            return And(left, right)

        if ctx.or_ is not None:
            return Or(left, right)

        if ctx.min_ is not None:
            return self.Min(left, right)

        if ctx.ite is not None:
            return self.visit(ctx.ite)

        if ctx.atom is not None:
            return self.visit(ctx.atom)

        raise ValueError("Somehow, an expression doesn't match any of the possible expression tokenisations")

    # Visit a parse tree produced by BENEFIT_LANGUAGEParser#if_then_else.
    def visitIf_then_else(self, ctx: BENEFIT_LANGUAGEParser.If_then_elseContext):
        # In the current definition, if, then, else are elements 0, 2, 4
        return If(self.visit(ctx.children[1]), self.visit(ctx.children[3]), self.visit(ctx.children[5]))

    # Visit a parse tree produced by BENEFIT_LANGUAGEParser#term.
    def visitTerm(self, ctx: BENEFIT_LANGUAGEParser.TermContext):
        global solver_objects
        # A term is either a value, or the name of a variable, or an enum reference
        if ctx.value() is not None:
            return self.visitChildren(ctx)  # Does this return an object or an array?
        elif ctx.VARIABLE_NAME() is not None:
            var_name = ctx.getText()
            return solver_objects[var_name]
        else:  # ctx.enum_reference() is not None
            return self.visit(ctx.enum_reference())

    # Visit a parse tree produced by BENEFIT_LANGUAGEParser#value.
    def visitValue(self, ctx: BENEFIT_LANGUAGEParser.ValueContext):
        '''
        Parses a value and returns it as a Z3Py value. This reimplements
        the lexer splitting of text into different elements. I can't
        find a way to bring the individual tokens into the parser without
        breaking lexing, which relies on having the full combination of
        tokens present in the ordering to ensure that a value is
        matched and tokenised appropriately.
        '''
        # TODO: This also could use some type safety
        if ctx.PERCENT() is not None:
            # Treating x% as x / 100, both Z3 ints
            return IntVal(ctx.getText()[:-1]) / IntVal(100)
        elif ctx.MONEY() is not None:
            # Treat money as an IntVal of total in pence
            money_array = ctx.MONEY().getText()[1:].split(".")
            money_val = int(money_array[0]) * 100
            if len(money_array) == 2:
                money_val += int(money_array[1])
            return IntVal(money_val)
        elif ctx.DATE() is not None:
            # We save the full date as a string value in Z3Py,
            # because Z3Py supports < <= > >= on strings nowadays
            return StringVal(ctx.DATE().getText().strip("'"))
        elif ctx.INTEGER() is not None:
            return IntVal(ctx.getText())
        else:  # ctx.BOOLEAN() is not None
            # Note that lower() is strictly unnecessary; True doesn't parse
            return BoolVal(ctx.getText().lower() == 'true')

    # Visit a parse tree produced by BENEFIT_LANGUAGEParser#enum_reference.
    def visitEnum_reference(self, ctx: BENEFIT_LANGUAGEParser.Enum_referenceContext):
        enum_var = solver_objects[ctx.ENUM_VARIABLE_NAME().getText()]
        enum_attribute = ctx.VARIABLE_NAME().getText()
        return getattr(enum_var, enum_attribute)

    # Visit a parse tree produced by BENEFIT_LANGUAGEParser#comment.
    def visitComment(self, ctx: BENEFIT_LANGUAGEParser.CommentContext):
        # We return nothing
        # print(ctx.getText())
        pass


if __name__ == '__main__':
    main(sys.argv)
