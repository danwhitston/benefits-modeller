# Elements of rules

Now that we have a set of sample benefit rules, we can identify the types of relation and operator that we need to represent the rules.

## Relations

The benefit rules as described are a set of statements relating outputs (a claimant or couple's benefit entitlement) to inputs (their household circumstances, employment etc). While the rules described the results as deriving from the inputs, part of the point of the model is to take a combination of known and unknown inputs and results and use the relations to find the missing values throughout the model.

Taking a bottom-up approach, we can identify the individual pieces of data and logical operators required to capture the sample benefit rules. This plus some function definitions, and program flow methods, should be enough to model the sample benefit rules.

The test cases rely on (i) setting known values, which could be inputs or outputs, and (ii) asserting that one or more unknown values can be inferred from those that are known.

## Datatypes

The rules as described lend themselves to representation using strongly typed objects, since each rule always applies to the same type of value and produces the same type of output.

One cause of uncertainty is that, for some calculations, it is unclear how best to communicate either (i) the amount of a benefit, or (ii) that the claimant is not eligible for the benefit in question. The options seem to be:

* If we use two variables, e.g. ucEligible and ucAmount, then it would be possible to represent impossible combinations, for example ucEligible = false and ucAmount = £300.
* If we use a combined variable, returning either the value or false, we could get meaningless calculations like `false - 50`.
* If we treat ucAmount = £0 as meaning that a claimant is not eligible for UC, then we could theoretically find a failure mode where someone is eligible but their eligible amount is £0, and a further piece of logic that relies on eligibility status incorrectly assumes ineligibility.

The simplest way around this is to take care to follow the actual benefit logic when defining eligibility and amount of benefit. Where the two are calculated differently, such that a claimant could be eligible but for £0, we should define two separate functions, as per ucEligible and ucAmount. Where ineligibility is determined by a £0 amount, we can choose from just using ucAmount, or define ucEligible = (ucAmount == £0). It should never be possible for the definitions to be so misaligned that ucEligible is false but ucAmount is non-zero.

### Integer

Example: number of children is a non-negative integer used to determine whether a claimant comes under UC in rule 1, UC work allowance (rule 5), UC children's allowance (rule 8), childcare allowance (rule 11).

There do not appear to be any situations in the model where a negative number is carried forward from a calculation. For example, the earnings tape in rule 5 has a cut-off at 0, which I've implemented by taking the maximum of 0 or the calculated amount.

I also can't immediately find situations where an integer is divided, which removes the need to consider fractions of integers.

Values of type integer will be just the numeric digits, e.g. `123`, with no leading zeroes and the value zero represented by `0`. Negative integer representation can be added in later, if necessary.

### Money

All money in the sample rules is in pounds and pence, normally written like £123.45. For the purposes of this model, we assume that any multiplication or division of money results in another money value in pounds and pence, rounded to the nearest penny. This introduces a minor source of error, since by this approach, 3.01 / 4 is 0.75, but 0.75 * 4 is 3.00.

We need to support addition and subtraction (where both operands are money), and also multiplication (where one operand is an integer or a fraction) and division (where the denominator is an integer).

We define a variable as Money by writing `Money housing_costs_element`.

Values of type money are formatted as `£1234.56`, with no leading 0s. The pence element is optional, so e.g. `£1234` is also valid.

### Percent

Percentages are used in rule 5 and in the social landlord calculation of rule 12. In both cases, the function of the number is to take a percentage of a monetary value, thus returning another monetary value.

We define a percentage object by writing `Percent one_bedroom`.

To represent a percentage, we use the form `45%` where the number is an integer.

### Date

Dates in benefit modelling follow the Gregorian calendar, hence following ISO 8601. They are used directly (e.g. a limit of the model is that date of claim must be between 5/3/2018 and 4/3/2019), and in more complex ways (age in years is a non-negative integer, calculated by comparing date of claim to date of birth following a set of rules).

We define a variable as Date by writing `Date date_of_birth`.

We will refer to dates in the standard ISO format YYYY-MM-DD, for example `'1977-03-13'`.

### Boolean

Whenever eligibility is being determined, or a check is made as to whether something is the case or not, the required value is Boolean. For example, rule 1 determines whether a claimant comes under UC or not, so is either true or false.

We define a variable as Boolean by writing `Boolean is_under_UC`. To represent Boolean values, we use `true` and `false`.

### Enum

There are rules that can place a claim in one of a list of situations, rather than just being true or false. In rule 12, housing costs could be one of ineligible or unclaimed, private tenant, registered social landlord tenant, or owner-occupier, each with its own eligibility requirements and calculation to determine the value of the housing costs element.

To represent Enum values, we define the possible values of an Enum variable, using e.g. `Enum housing_type(none, private, social, owner_occupier)`, and reference a specific value by writing `housing_type.private`.

### Fraction - not implemented

There are places in the model where values are divided. It is possible for SMT solvers to handle values as fractions, which enables lossless comparison and presentation of results. Currently, there is no plan to deliberately incorporate that into modelling. Where division does occur, for example when calculating the core rent for private tenants in rule 12, the numerator is a money value, and the result is therefore a money value whose accuracy is limited to the nearest penny.

### List or array - not implemented

The wider benefit system models eligibility for an arbitrary number of household members, including an arbitrary number of children. Eligibility and amounts vary both with the characteristics of each individual, and by their position in the overall list, ordered on some characteristic.

## Operators

### Equality: ==

### Less-than and greater-than: < and >

Compare two operands of the same type, in the form `a < b`. The expression is true if the left-hand operand is less than the right-hand one, otherwise false. The expression `a > b` returns the same result as `b < a`.

Supported types include Date (for example, we know that in this model `date_of_claim < '2019-03-04'` is true), Integer. Both operands must be the same type.

### Less-than-or-equal-to and greater-than-or-equal-to: <= and >=

Compare two operands of the same type, in the form `a <= b`. The expression is true if the left hand operand is equal to or less than the right-hand one, otherwise false. The expression `a <= b` is the same as `b >= a`.

Supported types include Date, Integer. Both operands must be the same type.

### Addition: +

`a + b` returns the sum of the two operands. Both operands must be the same type. Supported types include Integer, Money.

### Zero-bounded subtraction: ~-

A noteworthy aspect of the current set of rules is that any expression involving subtraction treats a negative result as 0 (Integer) or £0 (Money). It's possible to support this by allowing negative values for Integer and Money types, then defining a `max(a, 0)` function to manually round up negative values to 0. I've decided instead to try replacing the standard minus operator with `~-`. This is the only operator that is substantially out of alignment with common operator definitions in other languages.

`a ~- b` returns the left-hand operand minus the right-hand operand if `b < a`, otherwise it returns 0 or £0. Both operands must be the same type and the result is the same type as the operands. Supported types include Integer, Money.

### Multiplication: *

`a * b` returns the product of the two values. Supported types include Integer, Percent, Money, in the following combinations:

* Both operands are Integer, and the result is Integer.
* One operand is Money, the other is Integer, and the result is Money.
* One operand is Money, the other is Percent, and the result is Money. This implies that the result is rounded to the nearest penny.

### Division: /

`a / b` is required for the private tenant calculation in rule 12, and returns the left-hand side divided by the right-hand side. 

### Minimum: min()

Rule 11 has an upper bound for the childcare allowance, which can be represented with `min(a, £646.35)` for one child, where `a` is a Money value representing 85% of the childcare cost and £646.35 is the maximum repayment for one child. It can also be thought of as `if (a < b) then a else b`.

Supported types include Integer, Money, and potentially Date.

### Conditional: if then else

A conditional expression takes the form `if a then b else c`, where `a` is Boolean, and `b` and `c` must have the same type as each other, which in turn is the same type as the return value of the expression. There's no reason to limit what that type is.

### Conditional: case when when not implemented

A form of `if then else` with an arbitrary number of comparisons, specifically adapted for ranges of values in this context. I've yet to find rules that require this in the current model, though.

### Maximum: max() - not implemented

As discussed earlier, `max(a, b)` would be needed to set a zero lower bound on subtraction if we didn't use zero-bounded subtraction. There don't appear to be any other uses in the present model, so there is no need to implement this operator at present.

### Splitting operands 



