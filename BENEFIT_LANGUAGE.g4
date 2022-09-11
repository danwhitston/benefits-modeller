INTEGER
  : NON_ZERO_DIGIT DIGIT*
  | '0'+
  ;

fragment NON_ZERO_DIGIT
  : [1-9]
  ;

fragment DIGIT
  : [0-9]
  ;
