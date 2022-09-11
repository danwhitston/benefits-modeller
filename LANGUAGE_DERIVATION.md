# Elements of rules

Now that we have a set of sample benefit rules, we can identify the types of relation and operator that we need to represent the rules.

## Relations

The benefit rules as described are a set of statements relating outputs (a claimant or couple's benefit entitlement) to inputs (their household circumstances, employment etc). While the rules described the results as deriving from the inputs, part of the point of the model is to take a combination of known and unknown inputs and results and use the relations to find the missing values throughout the model.

Taking a bottom-up approach, we can identify the individual pieces of data and logical operators required to capture the sample benefit rules, then build representations of these in EBNF form.

## Datatypes - types of operand

### Integer

Example: number of children is a non-negative integer used to determine whether a claimant comes under UC in rule 1, UC work allowance (rule 5), UC children's allowance (rule 8), childcare allowance (rule 11).

There do not appear to be any situations in the model where a negative number is carried forward from a calculation. For example, the earnings tape in rule 5 has a cut-off at 0, which I've implemented by taking the maximum of 0 or the calculated amount.

In EBNF form, we can represent a non-negative integer by the following:

```antlr
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
```

### Money


### Fraction
### Date
### Boolean
### Enum

## Operators

### ==

### < and >

### <= and >=

### + and -

### *

### /

### max()

### Splitting operands 



