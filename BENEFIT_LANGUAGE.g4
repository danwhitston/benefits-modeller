grammar BENEFIT_LANGUAGE;

/*
 * Parser
 */

declare_function
  : declare_variable OPEN_CURLY_BRACKET expression CLOSE_CURLY_BRACKET
  ;

declare_variable
  : VARIABLE_TYPE VARIABLE_NAME
  ;

// assign_variable
//   : VARIABLE_NAME EQUAL_SIGN // THIS NEEDS FINISHING!
//   ;

declare_enum_type
  : 'Enum' ENUM_TYPE_NAME OPEN_BRACKET VARIABLE_NAME (LIST_SEPARATOR VARIABLE_NAME)* CLOSE_BRACKET
  ;

/* 
 * Lexer
 */

LIST_SEPARATOR
  : ','
  ;

EQUAL_SIGN
  : '='
  ;

INTEGER
  : NON_ZERO_DIGIT DIGIT*
  | '0'+
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

MONEY
  : CURRENCY_SYMBOL INTEGER (DECIMAL_POINT PENCE_VALUE)?
  ;

BOOLEAN
  : 'true'
  | 'false'
  ;

VARIABLE_TYPE
  : 'Integer' | 'Money' | 'Percent' | 'Date' | 'Boolean'
  ;

VARIABLE_NAME
  : (LOWER_CASE_LETTER | UNDERSCORE)+
  ;

ENUM_TYPE_NAME
  : UPPER_CASE_LETTER (LOWER_CASE_LETTER | UNDERSCORE)*
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
  : [0-9]
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

fragment NEWLINE
  : ('\r' | '\n')+
  ;
