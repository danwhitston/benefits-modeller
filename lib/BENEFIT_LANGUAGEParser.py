# Generated from BENEFIT_LANGUAGE.g4 by ANTLR 4.11.1
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,40,105,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        1,0,1,0,1,0,1,1,4,1,33,8,1,11,1,12,1,34,1,2,1,2,1,2,1,2,1,2,3,2,
        42,8,2,1,3,1,3,1,3,1,3,1,3,3,3,49,8,3,1,3,1,3,1,4,1,4,1,4,1,5,1,
        5,1,5,1,6,1,6,1,6,1,6,1,6,1,6,5,6,65,8,6,10,6,12,6,68,9,6,1,6,1,
        6,1,7,1,7,1,7,1,7,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,9,1,9,1,9,1,9,3,
        9,87,8,9,1,10,1,10,3,10,91,8,10,1,10,1,10,1,10,1,11,1,11,1,11,3,
        11,99,8,11,1,12,1,12,1,13,1,13,1,13,0,0,14,0,2,4,6,8,10,12,14,16,
        18,20,22,24,26,0,2,1,0,19,20,1,0,5,9,103,0,28,1,0,0,0,2,32,1,0,0,
        0,4,41,1,0,0,0,6,43,1,0,0,0,8,52,1,0,0,0,10,55,1,0,0,0,12,58,1,0,
        0,0,14,71,1,0,0,0,16,75,1,0,0,0,18,86,1,0,0,0,20,90,1,0,0,0,22,98,
        1,0,0,0,24,100,1,0,0,0,26,102,1,0,0,0,28,29,3,2,1,0,29,30,5,0,0,
        1,30,1,1,0,0,0,31,33,3,4,2,0,32,31,1,0,0,0,33,34,1,0,0,0,34,32,1,
        0,0,0,34,35,1,0,0,0,35,3,1,0,0,0,36,42,3,26,13,0,37,42,3,6,3,0,38,
        42,3,10,5,0,39,42,3,12,6,0,40,42,3,8,4,0,41,36,1,0,0,0,41,37,1,0,
        0,0,41,38,1,0,0,0,41,39,1,0,0,0,41,40,1,0,0,0,42,5,1,0,0,0,43,44,
        3,10,5,0,44,45,5,26,0,0,45,48,5,14,0,0,46,49,3,18,9,0,47,49,3,16,
        8,0,48,46,1,0,0,0,48,47,1,0,0,0,49,50,1,0,0,0,50,51,5,15,0,0,51,
        7,1,0,0,0,52,53,5,36,0,0,53,54,5,37,0,0,54,9,1,0,0,0,55,56,5,34,
        0,0,56,57,5,37,0,0,57,11,1,0,0,0,58,59,5,1,0,0,59,60,5,36,0,0,60,
        61,5,16,0,0,61,66,5,37,0,0,62,63,5,13,0,0,63,65,5,37,0,0,64,62,1,
        0,0,0,65,68,1,0,0,0,66,64,1,0,0,0,66,67,1,0,0,0,67,69,1,0,0,0,68,
        66,1,0,0,0,69,70,5,17,0,0,70,13,1,0,0,0,71,72,5,16,0,0,72,73,3,18,
        9,0,73,74,5,17,0,0,74,15,1,0,0,0,75,76,5,2,0,0,76,77,3,18,9,0,77,
        78,5,3,0,0,78,79,3,18,9,0,79,80,5,4,0,0,80,81,3,18,9,0,81,17,1,0,
        0,0,82,87,3,14,7,0,83,87,3,20,10,0,84,87,3,16,8,0,85,87,3,22,11,
        0,86,82,1,0,0,0,86,83,1,0,0,0,86,84,1,0,0,0,86,85,1,0,0,0,87,19,
        1,0,0,0,88,91,3,22,11,0,89,91,3,14,7,0,90,88,1,0,0,0,90,89,1,0,0,
        0,91,92,1,0,0,0,92,93,7,0,0,0,93,94,3,18,9,0,94,21,1,0,0,0,95,99,
        5,35,0,0,96,99,5,37,0,0,97,99,3,24,12,0,98,95,1,0,0,0,98,96,1,0,
        0,0,98,97,1,0,0,0,99,23,1,0,0,0,100,101,7,1,0,0,101,25,1,0,0,0,102,
        103,5,18,0,0,103,27,1,0,0,0,7,34,41,48,66,86,90,98
    ]

class BENEFIT_LANGUAGEParser ( Parser ):

    grammarFileName = "BENEFIT_LANGUAGE.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'Enum'", "'if'", "'then'", "'else'", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "','", "'{'", "'}'", "'('", "')'", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "'=='", "'<='", "'<'", "'>='", "'>'", 
                     "'='", "'+'", "'~-'", "'*'", "'/'", "'min'", "'and'", 
                     "'or'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "PERCENT", "MONEY", "DATE", "INTEGER", 
                      "BOOLEAN", "YEAR", "MONTH", "DAY", "LIST_SEPARATOR", 
                      "OPEN_CURLY_BRACKET", "CLOSE_CURLY_BRACKET", "OPEN_BRACKET", 
                      "CLOSE_BRACKET", "COMMENT", "COMPARATOR", "LOGICAL_OPERATOR", 
                      "IS_EQUAL_TO", "IS_LESS_THAN_OR_EQUAL_TO", "IS_LESS_THAN", 
                      "IS_GREATER_THAN_OR_EQUAL_TO", "IS_GREATER_THAN", 
                      "ASSIGN_EQUAL_TO", "ADD", "BOUNDED_SUBTRACT", "MULTIPLY", 
                      "DIVIDE", "MIN", "AND", "OR", "VARIABLE_TYPE", "ENUM_REFERENCE", 
                      "ENUM_VARIABLE_NAME", "VARIABLE_NAME", "WHITESPACE", 
                      "NEWLINE", "ANY" ]

    RULE_file = 0
    RULE_statements = 1
    RULE_statement = 2
    RULE_declare_function = 3
    RULE_declare_enum_variable = 4
    RULE_declare_variable = 5
    RULE_declare_enum_type = 6
    RULE_bracketed_expression = 7
    RULE_if_then_else = 8
    RULE_expression = 9
    RULE_unbracketed_expression = 10
    RULE_term = 11
    RULE_value = 12
    RULE_comment = 13

    ruleNames =  [ "file", "statements", "statement", "declare_function", 
                   "declare_enum_variable", "declare_variable", "declare_enum_type", 
                   "bracketed_expression", "if_then_else", "expression", 
                   "unbracketed_expression", "term", "value", "comment" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    PERCENT=5
    MONEY=6
    DATE=7
    INTEGER=8
    BOOLEAN=9
    YEAR=10
    MONTH=11
    DAY=12
    LIST_SEPARATOR=13
    OPEN_CURLY_BRACKET=14
    CLOSE_CURLY_BRACKET=15
    OPEN_BRACKET=16
    CLOSE_BRACKET=17
    COMMENT=18
    COMPARATOR=19
    LOGICAL_OPERATOR=20
    IS_EQUAL_TO=21
    IS_LESS_THAN_OR_EQUAL_TO=22
    IS_LESS_THAN=23
    IS_GREATER_THAN_OR_EQUAL_TO=24
    IS_GREATER_THAN=25
    ASSIGN_EQUAL_TO=26
    ADD=27
    BOUNDED_SUBTRACT=28
    MULTIPLY=29
    DIVIDE=30
    MIN=31
    AND=32
    OR=33
    VARIABLE_TYPE=34
    ENUM_REFERENCE=35
    ENUM_VARIABLE_NAME=36
    VARIABLE_NAME=37
    WHITESPACE=38
    NEWLINE=39
    ANY=40

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.11.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class FileContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def statements(self):
            return self.getTypedRuleContext(BENEFIT_LANGUAGEParser.StatementsContext,0)


        def EOF(self):
            return self.getToken(BENEFIT_LANGUAGEParser.EOF, 0)

        def getRuleIndex(self):
            return BENEFIT_LANGUAGEParser.RULE_file

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFile" ):
                return visitor.visitFile(self)
            else:
                return visitor.visitChildren(self)




    def file_(self):

        localctx = BENEFIT_LANGUAGEParser.FileContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_file)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 28
            self.statements()
            self.state = 29
            self.match(BENEFIT_LANGUAGEParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatementsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BENEFIT_LANGUAGEParser.StatementContext)
            else:
                return self.getTypedRuleContext(BENEFIT_LANGUAGEParser.StatementContext,i)


        def getRuleIndex(self):
            return BENEFIT_LANGUAGEParser.RULE_statements

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStatements" ):
                return visitor.visitStatements(self)
            else:
                return visitor.visitChildren(self)




    def statements(self):

        localctx = BENEFIT_LANGUAGEParser.StatementsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_statements)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 32 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 31
                self.statement()
                self.state = 34 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (((_la) & ~0x3f) == 0 and ((1 << _la) & 85899608066) != 0):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def comment(self):
            return self.getTypedRuleContext(BENEFIT_LANGUAGEParser.CommentContext,0)


        def declare_function(self):
            return self.getTypedRuleContext(BENEFIT_LANGUAGEParser.Declare_functionContext,0)


        def declare_variable(self):
            return self.getTypedRuleContext(BENEFIT_LANGUAGEParser.Declare_variableContext,0)


        def declare_enum_type(self):
            return self.getTypedRuleContext(BENEFIT_LANGUAGEParser.Declare_enum_typeContext,0)


        def declare_enum_variable(self):
            return self.getTypedRuleContext(BENEFIT_LANGUAGEParser.Declare_enum_variableContext,0)


        def getRuleIndex(self):
            return BENEFIT_LANGUAGEParser.RULE_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStatement" ):
                return visitor.visitStatement(self)
            else:
                return visitor.visitChildren(self)




    def statement(self):

        localctx = BENEFIT_LANGUAGEParser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 41
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                self.state = 36
                self.comment()
                pass

            elif la_ == 2:
                self.state = 37
                self.declare_function()
                pass

            elif la_ == 3:
                self.state = 38
                self.declare_variable()
                pass

            elif la_ == 4:
                self.state = 39
                self.declare_enum_type()
                pass

            elif la_ == 5:
                self.state = 40
                self.declare_enum_variable()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Declare_functionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def declare_variable(self):
            return self.getTypedRuleContext(BENEFIT_LANGUAGEParser.Declare_variableContext,0)


        def ASSIGN_EQUAL_TO(self):
            return self.getToken(BENEFIT_LANGUAGEParser.ASSIGN_EQUAL_TO, 0)

        def OPEN_CURLY_BRACKET(self):
            return self.getToken(BENEFIT_LANGUAGEParser.OPEN_CURLY_BRACKET, 0)

        def CLOSE_CURLY_BRACKET(self):
            return self.getToken(BENEFIT_LANGUAGEParser.CLOSE_CURLY_BRACKET, 0)

        def expression(self):
            return self.getTypedRuleContext(BENEFIT_LANGUAGEParser.ExpressionContext,0)


        def if_then_else(self):
            return self.getTypedRuleContext(BENEFIT_LANGUAGEParser.If_then_elseContext,0)


        def getRuleIndex(self):
            return BENEFIT_LANGUAGEParser.RULE_declare_function

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDeclare_function" ):
                return visitor.visitDeclare_function(self)
            else:
                return visitor.visitChildren(self)




    def declare_function(self):

        localctx = BENEFIT_LANGUAGEParser.Declare_functionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_declare_function)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 43
            self.declare_variable()
            self.state = 44
            self.match(BENEFIT_LANGUAGEParser.ASSIGN_EQUAL_TO)
            self.state = 45
            self.match(BENEFIT_LANGUAGEParser.OPEN_CURLY_BRACKET)
            self.state = 48
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
            if la_ == 1:
                self.state = 46
                self.expression()
                pass

            elif la_ == 2:
                self.state = 47
                self.if_then_else()
                pass


            self.state = 50
            self.match(BENEFIT_LANGUAGEParser.CLOSE_CURLY_BRACKET)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Declare_enum_variableContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ENUM_VARIABLE_NAME(self):
            return self.getToken(BENEFIT_LANGUAGEParser.ENUM_VARIABLE_NAME, 0)

        def VARIABLE_NAME(self):
            return self.getToken(BENEFIT_LANGUAGEParser.VARIABLE_NAME, 0)

        def getRuleIndex(self):
            return BENEFIT_LANGUAGEParser.RULE_declare_enum_variable

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDeclare_enum_variable" ):
                return visitor.visitDeclare_enum_variable(self)
            else:
                return visitor.visitChildren(self)




    def declare_enum_variable(self):

        localctx = BENEFIT_LANGUAGEParser.Declare_enum_variableContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_declare_enum_variable)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 52
            self.match(BENEFIT_LANGUAGEParser.ENUM_VARIABLE_NAME)
            self.state = 53
            self.match(BENEFIT_LANGUAGEParser.VARIABLE_NAME)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Declare_variableContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def VARIABLE_TYPE(self):
            return self.getToken(BENEFIT_LANGUAGEParser.VARIABLE_TYPE, 0)

        def VARIABLE_NAME(self):
            return self.getToken(BENEFIT_LANGUAGEParser.VARIABLE_NAME, 0)

        def getRuleIndex(self):
            return BENEFIT_LANGUAGEParser.RULE_declare_variable

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDeclare_variable" ):
                return visitor.visitDeclare_variable(self)
            else:
                return visitor.visitChildren(self)




    def declare_variable(self):

        localctx = BENEFIT_LANGUAGEParser.Declare_variableContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_declare_variable)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 55
            self.match(BENEFIT_LANGUAGEParser.VARIABLE_TYPE)
            self.state = 56
            self.match(BENEFIT_LANGUAGEParser.VARIABLE_NAME)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Declare_enum_typeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ENUM_VARIABLE_NAME(self):
            return self.getToken(BENEFIT_LANGUAGEParser.ENUM_VARIABLE_NAME, 0)

        def OPEN_BRACKET(self):
            return self.getToken(BENEFIT_LANGUAGEParser.OPEN_BRACKET, 0)

        def VARIABLE_NAME(self, i:int=None):
            if i is None:
                return self.getTokens(BENEFIT_LANGUAGEParser.VARIABLE_NAME)
            else:
                return self.getToken(BENEFIT_LANGUAGEParser.VARIABLE_NAME, i)

        def CLOSE_BRACKET(self):
            return self.getToken(BENEFIT_LANGUAGEParser.CLOSE_BRACKET, 0)

        def LIST_SEPARATOR(self, i:int=None):
            if i is None:
                return self.getTokens(BENEFIT_LANGUAGEParser.LIST_SEPARATOR)
            else:
                return self.getToken(BENEFIT_LANGUAGEParser.LIST_SEPARATOR, i)

        def getRuleIndex(self):
            return BENEFIT_LANGUAGEParser.RULE_declare_enum_type

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDeclare_enum_type" ):
                return visitor.visitDeclare_enum_type(self)
            else:
                return visitor.visitChildren(self)




    def declare_enum_type(self):

        localctx = BENEFIT_LANGUAGEParser.Declare_enum_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_declare_enum_type)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 58
            self.match(BENEFIT_LANGUAGEParser.T__0)
            self.state = 59
            self.match(BENEFIT_LANGUAGEParser.ENUM_VARIABLE_NAME)
            self.state = 60
            self.match(BENEFIT_LANGUAGEParser.OPEN_BRACKET)
            self.state = 61
            self.match(BENEFIT_LANGUAGEParser.VARIABLE_NAME)
            self.state = 66
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==13:
                self.state = 62
                self.match(BENEFIT_LANGUAGEParser.LIST_SEPARATOR)
                self.state = 63
                self.match(BENEFIT_LANGUAGEParser.VARIABLE_NAME)
                self.state = 68
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 69
            self.match(BENEFIT_LANGUAGEParser.CLOSE_BRACKET)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Bracketed_expressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def OPEN_BRACKET(self):
            return self.getToken(BENEFIT_LANGUAGEParser.OPEN_BRACKET, 0)

        def expression(self):
            return self.getTypedRuleContext(BENEFIT_LANGUAGEParser.ExpressionContext,0)


        def CLOSE_BRACKET(self):
            return self.getToken(BENEFIT_LANGUAGEParser.CLOSE_BRACKET, 0)

        def getRuleIndex(self):
            return BENEFIT_LANGUAGEParser.RULE_bracketed_expression

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBracketed_expression" ):
                return visitor.visitBracketed_expression(self)
            else:
                return visitor.visitChildren(self)




    def bracketed_expression(self):

        localctx = BENEFIT_LANGUAGEParser.Bracketed_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_bracketed_expression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 71
            self.match(BENEFIT_LANGUAGEParser.OPEN_BRACKET)
            self.state = 72
            self.expression()
            self.state = 73
            self.match(BENEFIT_LANGUAGEParser.CLOSE_BRACKET)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class If_then_elseContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BENEFIT_LANGUAGEParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(BENEFIT_LANGUAGEParser.ExpressionContext,i)


        def getRuleIndex(self):
            return BENEFIT_LANGUAGEParser.RULE_if_then_else

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIf_then_else" ):
                return visitor.visitIf_then_else(self)
            else:
                return visitor.visitChildren(self)




    def if_then_else(self):

        localctx = BENEFIT_LANGUAGEParser.If_then_elseContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_if_then_else)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 75
            self.match(BENEFIT_LANGUAGEParser.T__1)
            self.state = 76
            self.expression()
            self.state = 77
            self.match(BENEFIT_LANGUAGEParser.T__2)
            self.state = 78
            self.expression()
            self.state = 79
            self.match(BENEFIT_LANGUAGEParser.T__3)
            self.state = 80
            self.expression()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def bracketed_expression(self):
            return self.getTypedRuleContext(BENEFIT_LANGUAGEParser.Bracketed_expressionContext,0)


        def unbracketed_expression(self):
            return self.getTypedRuleContext(BENEFIT_LANGUAGEParser.Unbracketed_expressionContext,0)


        def if_then_else(self):
            return self.getTypedRuleContext(BENEFIT_LANGUAGEParser.If_then_elseContext,0)


        def term(self):
            return self.getTypedRuleContext(BENEFIT_LANGUAGEParser.TermContext,0)


        def getRuleIndex(self):
            return BENEFIT_LANGUAGEParser.RULE_expression

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpression" ):
                return visitor.visitExpression(self)
            else:
                return visitor.visitChildren(self)




    def expression(self):

        localctx = BENEFIT_LANGUAGEParser.ExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_expression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 86
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
            if la_ == 1:
                self.state = 82
                self.bracketed_expression()
                pass

            elif la_ == 2:
                self.state = 83
                self.unbracketed_expression()
                pass

            elif la_ == 3:
                self.state = 84
                self.if_then_else()
                pass

            elif la_ == 4:
                self.state = 85
                self.term()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Unbracketed_expressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self):
            return self.getTypedRuleContext(BENEFIT_LANGUAGEParser.ExpressionContext,0)


        def COMPARATOR(self):
            return self.getToken(BENEFIT_LANGUAGEParser.COMPARATOR, 0)

        def LOGICAL_OPERATOR(self):
            return self.getToken(BENEFIT_LANGUAGEParser.LOGICAL_OPERATOR, 0)

        def term(self):
            return self.getTypedRuleContext(BENEFIT_LANGUAGEParser.TermContext,0)


        def bracketed_expression(self):
            return self.getTypedRuleContext(BENEFIT_LANGUAGEParser.Bracketed_expressionContext,0)


        def getRuleIndex(self):
            return BENEFIT_LANGUAGEParser.RULE_unbracketed_expression

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitUnbracketed_expression" ):
                return visitor.visitUnbracketed_expression(self)
            else:
                return visitor.visitChildren(self)




    def unbracketed_expression(self):

        localctx = BENEFIT_LANGUAGEParser.Unbracketed_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_unbracketed_expression)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 90
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [5, 6, 7, 8, 9, 35, 37]:
                self.state = 88
                self.term()
                pass
            elif token in [16]:
                self.state = 89
                self.bracketed_expression()
                pass
            else:
                raise NoViableAltException(self)

            self.state = 92
            _la = self._input.LA(1)
            if not(_la==19 or _la==20):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 93
            self.expression()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TermContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ENUM_REFERENCE(self):
            return self.getToken(BENEFIT_LANGUAGEParser.ENUM_REFERENCE, 0)

        def VARIABLE_NAME(self):
            return self.getToken(BENEFIT_LANGUAGEParser.VARIABLE_NAME, 0)

        def value(self):
            return self.getTypedRuleContext(BENEFIT_LANGUAGEParser.ValueContext,0)


        def getRuleIndex(self):
            return BENEFIT_LANGUAGEParser.RULE_term

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTerm" ):
                return visitor.visitTerm(self)
            else:
                return visitor.visitChildren(self)




    def term(self):

        localctx = BENEFIT_LANGUAGEParser.TermContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_term)
        try:
            self.state = 98
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [35]:
                self.enterOuterAlt(localctx, 1)
                self.state = 95
                self.match(BENEFIT_LANGUAGEParser.ENUM_REFERENCE)
                pass
            elif token in [37]:
                self.enterOuterAlt(localctx, 2)
                self.state = 96
                self.match(BENEFIT_LANGUAGEParser.VARIABLE_NAME)
                pass
            elif token in [5, 6, 7, 8, 9]:
                self.enterOuterAlt(localctx, 3)
                self.state = 97
                self.value()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ValueContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def PERCENT(self):
            return self.getToken(BENEFIT_LANGUAGEParser.PERCENT, 0)

        def MONEY(self):
            return self.getToken(BENEFIT_LANGUAGEParser.MONEY, 0)

        def DATE(self):
            return self.getToken(BENEFIT_LANGUAGEParser.DATE, 0)

        def INTEGER(self):
            return self.getToken(BENEFIT_LANGUAGEParser.INTEGER, 0)

        def BOOLEAN(self):
            return self.getToken(BENEFIT_LANGUAGEParser.BOOLEAN, 0)

        def getRuleIndex(self):
            return BENEFIT_LANGUAGEParser.RULE_value

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitValue" ):
                return visitor.visitValue(self)
            else:
                return visitor.visitChildren(self)




    def value(self):

        localctx = BENEFIT_LANGUAGEParser.ValueContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_value)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 100
            _la = self._input.LA(1)
            if not(((_la) & ~0x3f) == 0 and ((1 << _la) & 992) != 0):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CommentContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def COMMENT(self):
            return self.getToken(BENEFIT_LANGUAGEParser.COMMENT, 0)

        def getRuleIndex(self):
            return BENEFIT_LANGUAGEParser.RULE_comment

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitComment" ):
                return visitor.visitComment(self)
            else:
                return visitor.visitChildren(self)




    def comment(self):

        localctx = BENEFIT_LANGUAGEParser.CommentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_comment)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 102
            self.match(BENEFIT_LANGUAGEParser.COMMENT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





