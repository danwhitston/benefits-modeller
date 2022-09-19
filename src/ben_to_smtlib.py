# Based on https://github.com/antlr/antlr4/blob/4.6/doc/python-target.md
import sys
from pathlib import Path
from z3 import *

# Add lib to system path so we can import the generated files
# They're kept in a separate directory to prevent mixing of generated
# and written code. This path setting fails if the execution
# directory is different from the script location in src
lib_path = Path("../lib/")
sys.path.append(str(lib_path)) # TODO: replace this with __init__.py ?
from antlr4 import *
from BENEFIT_LANGUAGELexer import BENEFIT_LANGUAGELexer
from BENEFIT_LANGUAGEParser import BENEFIT_LANGUAGEParser
from BENEFIT_LANGUAGEListener import BENEFIT_LANGUAGEListener


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
    walker = ParseTreeWalker()
    walker.walk(smt_lib_converter, tree)


class SmtLibConverter(BENEFIT_LANGUAGEListener):
    # Enter a parse tree produced by BENEFIT_LANGUAGEParser#file.
    def enterFile(self, ctx: BENEFIT_LANGUAGEParser.FileContext):
        # SMT-LIB 2 normally requires set-logic <symbol>, but Z3
        # automatically tries to determine the best to use
        pass

    # Exit a parse tree produced by BENEFIT_LANGUAGEParser#file.
    def exitFile(self, ctx: BENEFIT_LANGUAGEParser.FileContext):
        # Z3 also doesn't appear to need an exit statement
        pass

    # Enter a parse tree produced by BENEFIT_LANGUAGEParser#statements.
    def enterStatements(self, ctx: BENEFIT_LANGUAGEParser.StatementsContext):
        pass

    # Exit a parse tree produced by BENEFIT_LANGUAGEParser#statements.
    def exitStatements(self, ctx: BENEFIT_LANGUAGEParser.StatementsContext):
        pass

    # Enter a parse tree produced by BENEFIT_LANGUAGEParser#statement.
    def enterStatement(self, ctx: BENEFIT_LANGUAGEParser.StatementContext):
        pass

    # Exit a parse tree produced by BENEFIT_LANGUAGEParser#statement.
    def exitStatement(self, ctx: BENEFIT_LANGUAGEParser.StatementContext):
        pass

    # Enter a parse tree produced by BENEFIT_LANGUAGEParser#declare_function.
    def enterDeclare_function(self, ctx: BENEFIT_LANGUAGEParser.Declare_functionContext):
        pass

    # Exit a parse tree produced by BENEFIT_LANGUAGEParser#declare_function.
    def exitDeclare_function(self, ctx: BENEFIT_LANGUAGEParser.Declare_functionContext):
        pass

    # Enter a parse tree produced by BENEFIT_LANGUAGEParser#declare_enum_variable.
    def enterDeclare_enum_variable(self, ctx: BENEFIT_LANGUAGEParser.Declare_enum_variableContext):
        pass

    # Exit a parse tree produced by BENEFIT_LANGUAGEParser#declare_enum_variable.
    def exitDeclare_enum_variable(self, ctx: BENEFIT_LANGUAGEParser.Declare_enum_variableContext):
        pass

    # Enter a parse tree produced by BENEFIT_LANGUAGEParser#declare_variable.
    def enterDeclare_variable(self, ctx: BENEFIT_LANGUAGEParser.Declare_variableContext):
        pass

    # Exit a parse tree produced by BENEFIT_LANGUAGEParser#declare_variable.
    def exitDeclare_variable(self, ctx: BENEFIT_LANGUAGEParser.Declare_variableContext):
        pass

    # Enter a parse tree produced by BENEFIT_LANGUAGEParser#declare_enum_type.
    def enterDeclare_enum_type(self, ctx: BENEFIT_LANGUAGEParser.Declare_enum_typeContext):
        pass

    # Exit a parse tree produced by BENEFIT_LANGUAGEParser#declare_enum_type.
    def exitDeclare_enum_type(self, ctx: BENEFIT_LANGUAGEParser.Declare_enum_typeContext):
        pass

    # Enter a parse tree produced by BENEFIT_LANGUAGEParser#bracketed_expression.
    def enterBracketed_expression(self, ctx: BENEFIT_LANGUAGEParser.Bracketed_expressionContext):
        pass

    # Exit a parse tree produced by BENEFIT_LANGUAGEParser#bracketed_expression.
    def exitBracketed_expression(self, ctx: BENEFIT_LANGUAGEParser.Bracketed_expressionContext):
        pass

    # Enter a parse tree produced by BENEFIT_LANGUAGEParser#if_then_else.
    def enterIf_then_else(self, ctx: BENEFIT_LANGUAGEParser.If_then_elseContext):
        pass

    # Exit a parse tree produced by BENEFIT_LANGUAGEParser#if_then_else.
    def exitIf_then_else(self, ctx: BENEFIT_LANGUAGEParser.If_then_elseContext):
        pass

    # Enter a parse tree produced by BENEFIT_LANGUAGEParser#expression.
    def enterExpression(self, ctx: BENEFIT_LANGUAGEParser.ExpressionContext):
        pass

    # Exit a parse tree produced by BENEFIT_LANGUAGEParser#expression.
    def exitExpression(self, ctx: BENEFIT_LANGUAGEParser.ExpressionContext):
        pass

    # Enter a parse tree produced by BENEFIT_LANGUAGEParser#unbracketed_expression.
    def enterUnbracketed_expression(self, ctx: BENEFIT_LANGUAGEParser.Unbracketed_expressionContext):
        pass

    # Exit a parse tree produced by BENEFIT_LANGUAGEParser#unbracketed_expression.
    def exitUnbracketed_expression(self, ctx: BENEFIT_LANGUAGEParser.Unbracketed_expressionContext):
        pass

    # Enter a parse tree produced by BENEFIT_LANGUAGEParser#term.
    def enterTerm(self, ctx: BENEFIT_LANGUAGEParser.TermContext):
        pass

    # Exit a parse tree produced by BENEFIT_LANGUAGEParser#term.
    def exitTerm(self, ctx: BENEFIT_LANGUAGEParser.TermContext):
        pass

    # Enter a parse tree produced by BENEFIT_LANGUAGEParser#value.
    def enterValue(self, ctx: BENEFIT_LANGUAGEParser.ValueContext):
        pass

    # Exit a parse tree produced by BENEFIT_LANGUAGEParser#value.
    def exitValue(self, ctx: BENEFIT_LANGUAGEParser.ValueContext):
        pass

    # Enter a parse tree produced by BENEFIT_LANGUAGEParser#comment.
    def enterComment(self, ctx: BENEFIT_LANGUAGEParser.CommentContext):
        print(ctx.COMMENT())

    # Exit a parse tree produced by BENEFIT_LANGUAGEParser#comment.
    def exitComment(self, ctx: BENEFIT_LANGUAGEParser.CommentContext):
        pass


if __name__ == '__main__':
    main(sys.argv)
