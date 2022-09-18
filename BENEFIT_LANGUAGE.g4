grammar BENEFIT_LANGUAGE;

/*
 * Parser
 * We do not enforce type consistency in the parser. This is possible to do
 * as there are very few types and operators, but complex validation is best
 * left to the visitor.
 */

// Top-level structure
// from https://tomassetti.me/best-practices-for-antlr-parsers/
file
  : statements EOF
  ;

statements
  : statement+
  ;

statement
  : (comment | declare_function | declare_variable | declare_enum_type | declare_enum_variable)
  ;

/*
 * Test file / solver statements
 * These are commented out until we have a test file and a way
 * of handling them, as there's nothing to parse until then
 * They'll also need fixing before they actually work
 */

// assign_variable
//   : VARIABLE_NAME ASSIGN_EQUAL_TO value
//   ;

// assert_value
//   : 'assert' VARIABLE_NAME IS_EQUAL_TO value
//   ;

// BEN statements

declare_function
  : declare_variable '=' OPEN_CURLY_BRACKET (expression | if_then_else) CLOSE_CURLY_BRACKET
  ;

declare_enum_variable
  : ENUM_VARIABLE_NAME VARIABLE_NAME
  ;

declare_variable
  : VARIABLE_TYPE VARIABLE_NAME
  ;

declare_enum_type
  : 'Enum' ENUM_VARIABLE_NAME OPEN_BRACKET VARIABLE_NAME (LIST_SEPARATOR VARIABLE_NAME)* CLOSE_BRACKET
  ;

bracketed_expression
  : OPEN_BRACKET expression CLOSE_BRACKET
  ;

if_then_else
  : 'if' expression 'then' expression 'else' expression
  ;

expression
  : (bracketed_expression | unbracketed_expression | if_then_else | term)
  ;

unbracketed_expression
  : (term | bracketed_expression) (COMPARATOR | LOGICAL_OPERATOR) expression
  ;

term
  : ENUM_REFERENCE | VARIABLE_NAME | value
  ;

value
  : PERCENT | MONEY | DATE | INTEGER | BOOLEAN
  ;

// Everything from a # to end of line is marked as a comment
// Note that this DOES NOT WORK if a comment is placed inside a statement
// To do that well, we'd need to either manually add comment matches at all
// points in every statement, or use channels which are not available in
// combined lexer / parser
comment
  : COMMENT
  ;

/* 
 * Lexer
 */

// Data representations

PERCENT
  : INTEGER '%'
  ;

MONEY
  : CURRENCY_SYMBOL INTEGER (DECIMAL_POINT PENCE_VALUE)?
  ;

DATE
  : SINGLE_QUOTE YEAR '-' MONTH '-' DAY SINGLE_QUOTE
  ;

INTEGER
  : NON_ZERO_DIGIT DIGIT*
  | '0'+
  ;

BOOLEAN
  : 'true'
  | 'false'
  ;

YEAR
  : NON_ZERO_DIGIT DIGIT DIGIT DIGIT
  ;

MONTH
  : DIGIT DIGIT
  ;

DAY
  : DIGIT DIGIT
  ;

// Punctuation and structure

LIST_SEPARATOR
  : ','
  ;

OPEN_CURLY_BRACKET
  : '{'
  ;

CLOSE_CURLY_BRACKET
  : '}'
  ;

OPEN_BRACKET
  : '('
  ;

CLOSE_BRACKET
  : ')'
  ;

COMMENT
  : HASH_SYMBOL REST_OF_LINE
  ;

// Operators - precedence order is important

COMPARATOR
  : IS_EQUAL_TO | IS_LESS_THAN_OR_EQUAL_TO | IS_LESS_THAN | IS_GREATER_THAN_OR_EQUAL_TO | IS_GREATER_THAN | ADD | BOUNDED_SUBTRACT | MULTIPLY | DIVIDE | MIN
  ;

LOGICAL_OPERATOR
  : AND | OR
  ;

IS_EQUAL_TO
  : '=='
  ;

IS_LESS_THAN_OR_EQUAL_TO
  : '<='
  ;

IS_LESS_THAN
  : '<'
  ;

IS_GREATER_THAN_OR_EQUAL_TO
  : '>='
  ;

IS_GREATER_THAN
  : '>'
  ;

ASSIGN_EQUAL_TO
  : '='
  ;

ADD
  : '+'
  ;

BOUNDED_SUBTRACT
  : '~-'
  ;

MULTIPLY
  : '*'
  ;

DIVIDE
  : '/'
  ;

MIN // This operator goes above VARIABLE_NAME to establish precedence
  : 'min'
  ;

AND // likewise
  : 'and'
  ;

OR // likewise
  : 'or'
  ;

// Data types

VARIABLE_TYPE // Excludes Enum as that is defined at time of declaration
  : 'Integer' | 'Money' | 'Percent' | 'Date' | 'Boolean'
  ;

ENUM_REFERENCE
  : ENUM_VARIABLE_NAME DECIMAL_POINT VARIABLE_NAME
  ;

ENUM_VARIABLE_NAME
  : UPPER_CASE_LETTER (LOWER_CASE_LETTER | UNDERSCORE)*
  ;

VARIABLE_NAME
  : (LOWER_CASE_LETTER | UNDERSCORE)+
  ;

// This potentially skips all
WHITESPACE
  : [ \t]+ -> skip
  ;

NEWLINE
  : ('\r' | '\n')+ -> skip
  ;

// from https://tomassetti.me/best-practices-for-antlr-parsers/
ANY
  : .
  ;

// Fragments

fragment SINGLE_QUOTE
  : '\''
  ;

fragment PENCE_VALUE
  : DIGIT DIGIT
  ;

fragment DECIMAL_POINT
  : '.'
  ;

fragment NON_ZERO_DIGIT
  : [1-9]
  ;

fragment DIGIT
  : '0' | NON_ZERO_DIGIT
  ;

fragment CURRENCY_SYMBOL
  : '£'
  ;

fragment UNDERSCORE
  : '_'
  ;

fragment UPPER_CASE_LETTER
  : [A-Z]
  ;

fragment LOWER_CASE_LETTER
  : [a-z]
  ;


fragment HASH_SYMBOL
  : '#'
  ;

fragment REST_OF_LINE
  : ANY*? NEWLINE
  ;
