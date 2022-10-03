# Generated from BENEFIT_LANGUAGE.g4 by ANTLR 4.11.1
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .BENEFIT_LANGUAGEParser import BENEFIT_LANGUAGEParser
else:
    from BENEFIT_LANGUAGEParser import BENEFIT_LANGUAGEParser

# This class defines a complete generic visitor for a parse tree produced by BENEFIT_LANGUAGEParser.

class BENEFIT_LANGUAGEVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by BENEFIT_LANGUAGEParser#file.
    def visitFile(self, ctx:BENEFIT_LANGUAGEParser.FileContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BENEFIT_LANGUAGEParser#statements.
    def visitStatements(self, ctx:BENEFIT_LANGUAGEParser.StatementsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BENEFIT_LANGUAGEParser#statement.
    def visitStatement(self, ctx:BENEFIT_LANGUAGEParser.StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BENEFIT_LANGUAGEParser#test_statement.
    def visitTest_statement(self, ctx:BENEFIT_LANGUAGEParser.Test_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BENEFIT_LANGUAGEParser#assign_variable.
    def visitAssign_variable(self, ctx:BENEFIT_LANGUAGEParser.Assign_variableContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BENEFIT_LANGUAGEParser#verify_value.
    def visitVerify_value(self, ctx:BENEFIT_LANGUAGEParser.Verify_valueContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BENEFIT_LANGUAGEParser#declare_function.
    def visitDeclare_function(self, ctx:BENEFIT_LANGUAGEParser.Declare_functionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BENEFIT_LANGUAGEParser#declare_enum_variable.
    def visitDeclare_enum_variable(self, ctx:BENEFIT_LANGUAGEParser.Declare_enum_variableContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BENEFIT_LANGUAGEParser#declare_variable.
    def visitDeclare_variable(self, ctx:BENEFIT_LANGUAGEParser.Declare_variableContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BENEFIT_LANGUAGEParser#declare_enum_type.
    def visitDeclare_enum_type(self, ctx:BENEFIT_LANGUAGEParser.Declare_enum_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BENEFIT_LANGUAGEParser#expression.
    def visitExpression(self, ctx:BENEFIT_LANGUAGEParser.ExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BENEFIT_LANGUAGEParser#if_then_else.
    def visitIf_then_else(self, ctx:BENEFIT_LANGUAGEParser.If_then_elseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BENEFIT_LANGUAGEParser#term.
    def visitTerm(self, ctx:BENEFIT_LANGUAGEParser.TermContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BENEFIT_LANGUAGEParser#value.
    def visitValue(self, ctx:BENEFIT_LANGUAGEParser.ValueContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BENEFIT_LANGUAGEParser#enum_reference.
    def visitEnum_reference(self, ctx:BENEFIT_LANGUAGEParser.Enum_referenceContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BENEFIT_LANGUAGEParser#comment.
    def visitComment(self, ctx:BENEFIT_LANGUAGEParser.CommentContext):
        return self.visitChildren(ctx)



del BENEFIT_LANGUAGEParser