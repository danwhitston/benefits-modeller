grammar BENEFIT_LANGUAGE;

/*
 * Parser
 */

declare_variable
  : VARIABLE_TYPE VARIABLE_NAME
  ;

assign_variable
  : VARIABLE_NAME EQUAL_SIGN
  ;

/* 
 * Lexer
 */


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

fragment LOWER_CASE_LETTER
  : [a-z]
  ;

EQUAL_SIGN
  : '='
  ;

INTEGER
  : NON_ZERO_DIGIT DIGIT*
  | '0'+
  ;

fragment PENCE_VALUE
  : DIGIT DIGIT
  ;

fragment DECIMAL_POINT
  : '.'
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

fragment WHITESPACE
  : (' ')+
  ;

fragment NEWLINE
  : ('\r' | '\n')+
  ;
