# Based on https://github.com/antlr/antlr4/blob/4.6/doc/python-target.md
from symbol import for_stmt
import sys
from pathlib import Path
from unittest import case
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
    program = FileStream(fileName=argv[1], encoding='utf-8')
    lexer = BENEFIT_LANGUAGELexer(program)
    stream = CommonTokenStream(lexer)
    parser = BENEFIT_LANGUAGEParser(stream)
    tree = parser.file_()
    smt_lib_converter = SmtLibConverter()
    output = smt_lib_converter.visit(tree)
    print(output)


class SmtLibConverter(BENEFIT_LANGUAGEVisitor):
    '''
    Each node either visits its children, or processes the content
    of itself and its immediate children if it's at the lowest
    level. We use globals throughout, partly because we want to
    define objects in statements and then access them in later,
    non-children statements, partly because the Ben language
    has no namespaces, at present.
    '''
    # Visit a parse tree produced by BENEFIT_LANGUAGEParser#file.
    def visitFile(self, ctx: BENEFIT_LANGUAGEParser.FileContext):
        print("Begun solver setup")
        return self.visitChildren(ctx)

    # Visit a parse tree produced by BENEFIT_LANGUAGEParser#statements.
    def visitStatements(self, ctx: BENEFIT_LANGUAGEParser.StatementsContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by BENEFIT_LANGUAGEParser#statement.
    def visitStatement(self, ctx: BENEFIT_LANGUAGEParser.StatementContext):
        return self.visitChildren(ctx)

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
        # return self.visitChildren(ctx)

    # Visit a parse tree produced by BENEFIT_LANGUAGEParser#declare_variable.
    def visitDeclare_variable(self, ctx: BENEFIT_LANGUAGEParser.Declare_variableContext):
        global solver_objects
        var_type = ctx.getChild(0).getText()
        var_name = ctx.getChild(1).getText()
        # TODO: Create Money, Percent, Dayte datatypes, or just treat as Int?
        if var_type == "Integer":
            solver_objects[var_name] = Int(var_name)
        elif var_type == "Money":
            solver_objects[var_name] = Int(var_name)
            # solver_objects[var_name] = Money(var_name)
        elif var_type == "Percent":
            solver_objects[var_name] = Int(var_name)
            # solver_objects[var_name] = Percent(var_name)
        elif var_type == "Date":
            solver_objects[var_name] = Int(var_name)
            # solver_objects[var_name] = Dayte(var_name)
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
        # We don't return anything!

    # Visit a parse tree produced by BENEFIT_LANGUAGEParser#bracketed_expression.
    def visitBracketed_expression(self, ctx: BENEFIT_LANGUAGEParser.Bracketed_expressionContext):
        # Return the expression result, specifically
        # If we don't do this, the brackets lead to a None return value
        return self.visit(ctx.expression())

    # Visit a parse tree produced by BENEFIT_LANGUAGEParser#if_then_else.
    def visitIf_then_else(self, ctx: BENEFIT_LANGUAGEParser.If_then_elseContext):
        if_value = self.visit(ctx.children[1])
        # Temporary pickup of errors before they happen
        if not isinstance(if_value, (bool)):
            pdb.set_trace()
        # In the current definition, if, then, else are elements 0, 2, 4
        return If(self.visit(ctx.children[1]), self.visit(ctx.children[3]), self.visit(ctx.children[5]))

    # Visit a parse tree produced by BENEFIT_LANGUAGEParser#expression.
    def visitExpression(self, ctx: BENEFIT_LANGUAGEParser.ExpressionContext):
        # No need to do anything here
        # All possibilities are themselves stops in the tree visitor
        return self.visitChildren(ctx)

    # Visit a parse tree produced by BENEFIT_LANGUAGEParser#unbracketed_expression.
    def visitUnbracketed_expression(self, ctx: BENEFIT_LANGUAGEParser.Unbracketed_expressionContext):
        # TODO: This is the big one! Get three elements, return two terms w/ operator
        left = self.visit(ctx.children[0])
        right = self.visit(ctx.children[2])
        # THE BIG ONE!
        if ctx.COMPARATOR() is not None:
            op_text = ctx.COMPARATOR().getText()
            if op_text == "==":
                return left == right
            elif op_text == "<=":
                return left <= right
            elif op_text == "<":
                return left < right
            elif op_text == ">=":
                return left >= right
            elif op_text == ">":
                return left > right
            elif op_text == "+":
                return left + right
            elif op_text == "~-":
                # TODO: Implement bounded subtract
                pdb.set_trace()
                return left + right
            elif op_text == "*":
                return left * right
            elif op_text == "/":
                # TODO: DOES THIS WORK?
                return left / right
            else:
                # TODO: Implement min
                pdb.set_trace()
                return left - right
        else:
            # Has to be 'LOGICAL_OPERATOR()'
            if ctx.LOGICAL_OPERATOR().getText() == "and":
                print("and: ", left, right)
                return And(left, right)
            else:
                # Has to be 'or'
                return Or(left, right)

    # Visit a parse tree produced by BENEFIT_LANGUAGEParser#term.
    def visitTerm(self, ctx: BENEFIT_LANGUAGEParser.TermContext):
        global solver_objects
        # A term is either a value, or the name of a variable, or an enum reference
        if ctx.value() is not None:
            return self.visitChildren(ctx)  # Does this return an object or an array?
        elif ctx.VARIABLE_NAME() is not None:
            var_name = ctx.getText()
            return solver_objects[var_name]
        else:
            # This MUST be an enum reference
            # TODO: Work out how to parse and set this
            pdb.set_trace()
            enum_name = 5
            enum_reference = solver_objects[4]

    # Visit a parse tree produced by BENEFIT_LANGUAGEParser#value.
    def visitValue(self, ctx: BENEFIT_LANGUAGEParser.ValueContext):
        # TODO Return an actual value, of correct sort
        if ctx.PERCENT() is not None:
            # TODO: Return a percent value
            return 24
        elif ctx.MONEY() is not None:
            # TODO: Return a money value
            return 24
        elif ctx.DATE() is not None:
            # TODO: Return a date value
            return 24
        elif ctx.INTEGER() is not None:
            return IntVal(ctx.getText())
        else:
            # The only option left is Boolean
            # Note that lower() is strictly unnecessary; True doesn't parse
            return BoolVal(ctx.getText().lower() == 'true')

    # Visit a parse tree produced by BENEFIT_LANGUAGEParser#comment.
    def visitComment(self, ctx: BENEFIT_LANGUAGEParser.CommentContext):
        # We return nothing, but print for information
        print(ctx.getText())


if __name__ == '__main__':
    main(sys.argv)
