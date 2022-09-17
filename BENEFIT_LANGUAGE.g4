grammar BENEFIT_LANGUAGE;

/*
 * Parser
 * We do not enforce type consistency in the parser. This is possible to do
 * as there are very few types and operators, but complex validation is best
 * left to the visitor.
 */

declare_function
  : declare_variable OPEN_CURLY_BRACKET expression CLOSE_CURLY_BRACKET
  ;

// Conflicts with declare_function so must come below it
declare_variable
  : VARIABLE_TYPE VARIABLE_NAME
  ;

// assign_variable
//   : VARIABLE_NAME EQUAL_SIGN // TODO
//   ;

declare_enum_type
  : 'Enum' ENUM_VARIABLE_NAME OPEN_BRACKET VARIABLE_NAME (LIST_SEPARATOR VARIABLE_NAME)* CLOSE_BRACKET
  ;

// We've regularised min syntax to match the other operators, making this obsolete
// minimum
//   : 'min' OPEN_BRACKET expression LIST_SEPARATOR expression CLOSE_BRACKET
//   ;

if_then_else
  : 'if' expression 'then' expression 'else' expression
  ;

expression
  : (term | bracketed_expression) OPERATOR (term | expression | bracketed_expression)
  ;

bracketed_expression
  : OPEN_BRACKET expression CLOSE_BRACKET
  ;

term
  : ENUM_REFERENCE | VARIABLE_NAME | value
  ;

value
  : PERCENT | MONEY | DATE | INTEGER | BOOLEAN
  ;

// Everything from a # to end of line is marked as a comment
comment
  : '#' .*? NEWLINE
  ;

/* 
 * Lexer
 */

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

NEWLINE
  : ('\r' | '\n')+
  ;

// Operators - note the precedence order is important here

OPERATOR
  : ASSIGNER | COMPARATOR
  ;

ASSIGNER
  : ASSIGN_EQUAL_TO
  ;

COMPARATOR
  : IS_EQUAL_TO | IS_LESS_THAN_OR_EQUAL_TO | IS_LESS_THAN | IS_GREATER_THAN_OR_EQUAL_TO | IS_GREATER_THAN | ADD | BOUNDED_SUBTRACT | MULTIPLY | DIVIDE
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

MIN // Does this get gazumped by VARIABLE_NAME?
  : 'min'
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

fragment WHITESPACE
  : (' ')+
  ;
