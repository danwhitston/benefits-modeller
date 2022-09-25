# Based on https://github.com/antlr/antlr4/blob/4.6/doc/python-target.md
from ast import For
from symbol import for_stmt
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
        # pdb.set_trace()
        return self.visitChildren(ctx)

    # Visit a parse tree produced by BENEFIT_LANGUAGEParser#declare_function.
    def visitDeclare_function(self, ctx: BENEFIT_LANGUAGEParser.Declare_functionContext):
        return self.visitChildren(ctx)

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

        # We return the newly created variable, in case it forms part of a
        # function declaration, and the parent wants to use what we've
        # declared to make an assertion, in SMT-LIB-speak
        return self.visitChildren(ctx)

    # Visit a parse tree produced by BENEFIT_LANGUAGEParser#declare_enum_type.
    def visitDeclare_enum_type(self, ctx: BENEFIT_LANGUAGEParser.Declare_enum_typeContext):
        # Using a global dictionary as a central namespace
        # for storing Z3 variables, constants etc
        global solver_objects
        enum_name = ctx.children[1].getText()
        solver_objects[enum_name] = Datatype(enum_name)
        number_of_enum_values = (ctx.getChildCount() - 3)//2
        for x in range(number_of_enum_values):
            # Note this is 0 to number_of_enum_values -1
            solver_objects[enum_name].declare(ctx.children[(x * 2) + 3].getText())
        solver_objects[enum_name] = solver_objects[enum_name].create()
        # We don't return anything!
        # return self.visitChildren(ctx)

    # Visit a parse tree produced by BENEFIT_LANGUAGEParser#bracketed_expression.
    def visitBracketed_expression(self, ctx: BENEFIT_LANGUAGEParser.Bracketed_expressionContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by BENEFIT_LANGUAGEParser#if_then_else.
    def visitIf_then_else(self, ctx: BENEFIT_LANGUAGEParser.If_then_elseContext):
        # In the current definition, if, then, else are elements 0, 2, 4
        return If(self.visit(ctx.children[1]), self.visit(ctx.children[3]), self.visit(ctx.children[5]))

    # Visit a parse tree produced by BENEFIT_LANGUAGEParser#expression.
    def visitExpression(self, ctx: BENEFIT_LANGUAGEParser.ExpressionContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by BENEFIT_LANGUAGEParser#unbracketed_expression.
    def visitUnbracketed_expression(self, ctx: BENEFIT_LANGUAGEParser.Unbracketed_expressionContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by BENEFIT_LANGUAGEParser#term.
    def visitTerm(self, ctx: BENEFIT_LANGUAGEParser.TermContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by BENEFIT_LANGUAGEParser#value.
    def visitValue(self, ctx: BENEFIT_LANGUAGEParser.ValueContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by BENEFIT_LANGUAGEParser#comment.
    def visitComment(self, ctx: BENEFIT_LANGUAGEParser.CommentContext):
        return self.visitChildren(ctx)


if __name__ == '__main__':
    main(sys.argv)
