# Based on https://github.com/antlr/antlr4/blob/4.6/doc/python-target.md
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
        return self.visitChildren(ctx)

    # Visit a parse tree produced by BENEFIT_LANGUAGEParser#declare_enum_variable.
    def visitDeclare_enum_variable(self, ctx: BENEFIT_LANGUAGEParser.Declare_enum_variableContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by BENEFIT_LANGUAGEParser#declare_variable.
    def visitDeclare_variable(self, ctx: BENEFIT_LANGUAGEParser.Declare_variableContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by BENEFIT_LANGUAGEParser#declare_enum_type.
    def visitDeclare_enum_type(self, ctx: BENEFIT_LANGUAGEParser.Declare_enum_typeContext):
        return self.visitChildren(ctx)

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
