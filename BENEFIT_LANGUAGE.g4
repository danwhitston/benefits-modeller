grammar BENEFIT_LANGUAGE;

/*
 * Parser
 * We do not enforce type consistency in the parser. This is possible to do
 * as there are very few types and operators, but complex validation is best
 * left to the visitor.
 */

// Top-level structure
// from Tomassetti (2021)
file
  : statements EOF
  ;

statements
  : (statement | test_statement)+
  ;

statement
  : (comment | declare_function | declare_variable | declare_enum_type | declare_enum_variable)
  ;

test_statement
  : (assign_variable | verify_value)
  ;

/*
 * Test file / solver statements
 */

// Set a variable equal to a value
assign_variable
  : LET VARIABLE_NAME '=' (value | enum_reference)
  ;

// Verify that a variable is equal to a value
verify_value
  : 'verify' VARIABLE_NAME '==' (value | enum_reference)
  ;

/*
 * Ben model statements
 */

declare_function
  : declare_variable '=' '{' expression '}'
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

expression
  : '(' unbracket=expression ')'
  | left=expression multdiv=('*'|'/') right=expression
  | left=expression plusminus=('+'|'~-') right=expression
  | left=expression comparison=('=='|'<='|'<'|'>='|'>') right=expression
  | left=expression and='and' right=expression
  | left=expression or='or' right=expression
  | left=expression min=MIN right=expression
  | ite=if_then_else
  | atom=term
  ;

if_then_else
  : 'if' expression 'then' expression 'else' expression
  ;

term
  : enum_reference | VARIABLE_NAME | value
  ;

value
  : PERCENT | MONEY | DATE | INTEGER | BOOLEAN
  ;

enum_reference
  : ENUM_VARIABLE_NAME '.' VARIABLE_NAME
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

LET // Above VARIABLE_NAME
  : 'let'
  ;

MIN // This operator goes above VARIABLE_NAME to establish precedence
  : 'min'
  ;

// Data types

VARIABLE_TYPE // Excludes Enum as that is defined at time of declaration
  : 'Integer' | 'Money' | 'Percent' | 'Date' | 'Boolean'
  ;

ENUM_VARIABLE_NAME
  : UPPER_CASE_LETTER (LOWER_CASE_LETTER | UNDERSCORE)*
  ;

VARIABLE_NAME
  : (LOWER_CASE_LETTER | UNDERSCORE)+
  ;

WHITESPACE
  : [ \t]+ -> skip
  ;

NEWLINE
  : ('\r' | '\n')+ -> skip
  ;

// from Tomassetti (2021)
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
