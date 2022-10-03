# Sample benefit rules

Objective 1 of the project is to create a sample set of benefit rules and test cases. The source used for both is The Welfare Benefits and Tax Credits Handbook (Child Poverty Action Group, 2018). The rules are expressed in the author's own language, with references, to mitigate any risk of questions around copyright and plagiarism.

The original plan was to model a random sample of rules from the book, but by inspection, this would have had no real modelling value when it to understanding the behaviour of a more complex system of rules. Thus, the model starts with one regulation and spread outwards to cover an interconnected set of dependent rules. This will enable the modelling of a system of rules instead of just running them in isolation, which will make it easier to test the behaviour of the system and the SMT solver with more complex models. The SMT solver would be of no benefit in 'solving' individual rules.

## Limits to the model

The main limitation of the model is that we are modelling a subset of the overal benefits rules, to establish household benefits eligibility at the date of first claim, where the first claim date is in the period of validity of the handbook, i.e. 5/3/2018 to 4/3/2019. For now, the subset is Universal Credit, in full service areas. These limitations are explained further in the descriptions of benefits rules.

### Location

Per Child Poverty Action Group (2018, pp.3-4), the handbook's rules apply to England and Wales. Scotland has broadly the same legislation but has the power to diverge. Northern Ireland has separate legislation on benefits and tax credits, although the systems are similar in practice. Beyond this, where a claimant lives has further impact on several aspects of benefits - there are local taxes and benefits such as council tax and discretionary housing payments; the council tax also varies according to the designated property band of the claimant's home and their household status.

### Dates

In common with all rules being discussed, the rules have changed in the years since the handbook was published. In this case the change is particularly acute: no new claims can be made for the benefits classed as legacy benefits, since all new claims are for Universal Credit. This does not affect the correctness of the rules being modelled, *for the period in which those rules were in effect*. All benefit rules have the same issue of time dependence. Not only the conditions of eligibility but also the payment amounts and even the existence of rules changes over time. Not only do claimants' circumstances change, but people get older, which changes their eligibility in and of itself.

Since the handbook we're using as a basis for our modelling only applies to a limited timespan, we will limit our modelling to claims with a date of new claim falling within the period of validity. The handbook's acknowledgements (Child Poverty Action Group, 2018, p.iv) state that the law covered in the book was correct on 5/3/2018, so we shall set the limit for new claim dates to between 5/3/2018 and 4/3/2019, for now. Likewise, we will not model payment dates outside of those lower and upper limits.

### Payments vs eligibility

There are situations in which someone's eligibility for a benefit is not established until after the point where that benefit should have been paid. Sometimes this results in payment being backdated, i.e. paid at a later point. In other circumstances, the payment may not be made up at a later point. Either way, we're looking to model benefit eligibility rather than the payment of eligible and claimed benefits, which has many rules of its own and relies implicitly on the history of payments made to a claimant.

## Ruleset 1 - When you come under the universal credit system

Source: Child Poverty Action Group (2018, pp.20-22)

The handbook was published during transition between two benefit systems: moving from a legacy system consisting of several sets of benefits and tax credits, to Universal Credit (UC). Whether claimants would be assessed under the legacy system or UC was dependent on date of initial claim, the area their home address was in, and several other conditions.

A claimant comes under UC if either:

1. Their date of claim for UC is after the rollout date for the Jobcentre area in which they're claiming, as listed in the PDF files at Department for Work and Pensions (2016). The rollout areas are often known as 'full service' areas. We know from the linked URL that rollout completed in December 2018, in accordance with the target date stated on p22 of the handbook.
2. Their date of claim for UC is before 1/1/2018, and after April 2016, and the Jobcentre area in which they're claiming is a UC gateway area, and they meet a long list of gateway conditions that are fully detailed in Chapter 2 of the 2017/18 edition of the handbook. An immediate consequence of the date limitations discussed earlier on is that our model completely excludes UC gateway claimants, since we're taking new claims from 5/3/2018.

There is an exception to the rule for full service areas: claimants with three or more children, and who meet certain other conditions, should continue to claim legacy benefits for claims between 6/04/2017 and 31/01/2019 (i.e. during the modelled period).

As with other rules, there are inputs to this decision which are themselves subject to modelling. In this model, those are:

* The date of claim, which is a date input between 5/3/2018 and 4/3/2019.
* The date at which their Jobcentre area becomes a 'full service' area, which is a date between November 2015 and December 2018
* Whether a claimant meets the three-or-more-children-based exception criteria for UC rollout.

## Ruleset 2 - Are you eligible for Universal Credit?

Source: Child Poverty Action Group (2018, pp.31-33)

There are several requirements which must *all* be true for a claimant to be eligible for UC. UC normally treats a couple as a single unit for claim purposes, i.e. they make a single claim and are paid jointly. For a couple to be eligible to claim UC normally, all requirements must be true for both partners.

The basic requirements to claim UC are that the claimant(s) are:

* coming under UC, i.e. that rule 1 is true
* aged 18 or over, or aged 16-17 and meet special young person UC eligibility criteria
* aged below the qualifying age for Pension Credit (PC)
* not receiving education unless you are exempted from this requirement
* in habitual residence in Great Britain and have the right to reside in Great Britain
* either physically in or can be treated as being in Great Britain
* not a person subject to immigration control
* in acceptance of the claimant commitment

It is possible for one member of a couple to claim as a single person if they meet the basic requirements themselves, but their partner fails to meet basic requirements in a certain, limited set of ways. In this situation, the claim works as if the claimant is a single person, *except* that both partners' income, savings and capital are still included in calculations.

The financial requirements to claim UC are that claimant(s) do not have:

* too high an income
* savings and capital above £16000

The income ceiling ('too high an income') is not a fixed number - instead it refers to an income which is high enough that no UC would be paid, due to the reduction in UC payments that results from income. This introduces a dependency between this ruleset and rule 3, the expected amount.

## Ruleset 3 - How much Universal Credit do you get?

Source: Child Poverty Action Group (2018, pp.34-38)

Much of the detail on calculation of amounts in this section of the handbook simply repeats information from elsewhere in less detail, leaving a relatively simple ruleset. Within an assessment period, per steps four and five on Child Poverty Action Group (2018, p.38):

`Universal Credit entitlement = maximum amount - earnings taper - unearned income`

The terms are defined in rules 4, 5 and 6, respectively. There is also a set of rules for something called Transitional Protection, but this only applies after July 2019, so is not a concern for our model. Where relevant, the time period used for any value calculated over time in UC (e.g. rent being paid, childcare cost) is £ per month.

## Ruleset 4 - How much is your maximum amount of UC?

Source: Child Poverty Action Group (2018, p.59)

The UC maximum amount is the sum of:

* The standard UC allowance for the person or couple that are claiming (rule 7)
* An allowance for children (rule 8)
* An element for adults with limited capability for work or work-related activity due to illness (rule 9)
* A carer element if one of the recipients cares for a severely disabled person (rule 10)
* An allowance for childcare (rule 11)
* A housing costs element (rule 12)

## Ruleset 5 - What is the earnings taper?

Source: Child Poverty Action Group (2018, pp.36-37)

`Earnings taper = maximum of 0 or (net earnings - work allowance) x 0.63`

where

`net earnings` is the monthly earned income after tax, national insurance, and pension contributions. If a couple are claiming, the sum of the net earnings of both claimants is used.

`work allowance` is counted if the claimant(s) are responsible for a child or have limited capacity to work. If counted, then the value is £198 if there is a housing costs element (i.e. rule 12 has a greater-than-zero result) or £409 if there is no housing costs element. Otherwise, it's £0.

## Ruleset 6 - What is unearned income for UC?

Source: Child Poverty Action Group (2018, p.37)

This can include income from a large range of unearned sources, including certain other benefits, income from capital including rental income, and so on. No taper is applied to unearned income, so the full value is counted against the UC maximum amount.

## Ruleset 7 - The standard UC allowance

Source: Child Poverty Action Group (2018, pp.59-60)

The standard UC allowance is £251.77 for a single claimant aged under 25, £317.82 for a single claimant aged 25 or over, £395.20 for a claiming couple both aged under 25, £498.89 for a claiming couple where at least one person is aged 25 or over.

## Ruleset 8 - An allowance for children under UC

Source: Child Poverty Action Group (2018, pp.60-61)

A claimant or their partner are responsible for a child if the child 'normally' lives with them. A child counts toward the allowance if they are (i) under 16 years old, or (ii) if they are above or equal to 16 years old, below 20 years old, and meet the criteria for a 'qualifying young person' per Child Poverty Action Group (2018, p.56).

If the eldest qualifying child (i.e. the one with the earliest date of birth) was born before 06/04/2017, then the allowance element for that child is £277.08 per month (i.e. per assessment period). Otherwise, the allowance element for them is £231.67.

If there is a second qualifying child, the allowance element for them is £231.67 per month (i.e. per assessment period).

There is a two-child limit for new UC claims, which adds considerable complexity:

* Claimants / couples with more than two qualifying children at time of claim do not come under UC and should claim legacy benefits instead, for new claims starting between 06/04/2017 and 01/02/2019. This requirement is described in Ruleset 1, and would *normally* mean that new claimants with more than 2 eligible children did not come under UC, and so did not need to be modelled.
* However, there are several exceptions to the two-child limit for special circumstances such as multiple births (i.e. twins or triplets). It would take more investigation to determine whether these would take effect on claimants that come under UC, or whether any such claims would be diverted to legacy benefits. For example, a claimant with two eligible children claims early in the period under modelling, comes under UC and is successful in their claim, then has another child. Do they remain under UC and hit the two-child limit, or are they switched to legacy benefits?
* At the time of publication of the handbook, there was also a legal challenge under way against the two-child limit, which would potentially have required backdated eligibility and benefit payment if it had succeeded. It's unclear how this kind of retrospective alteration to eligibility could be modelled.

For the sake of simplicity, it is assumed for now that there can be no UC claimants / couples with three or more eligible children.

Separately to the normal child elements, a claimant receives a disabled child addition for each child in their or their partner's care. This is based on assessment of the child's health and disability status. Each child awarded a lower rate addition contributes an element worth £126.11 per assessment period. Each child awarded a higher rate addition contributes an element worth £383.86 per assessment period. The two-child limit does not affect these values, although, again, we are limiting consideration of claims involving more than two children for this model.

The total allowance for children under UC is the sum of the allowance elements.

## Ruleset 9 - An element for adults with limited capability for work or work-related activity due to illness under UC

Source: Child Poverty Action Group (2018, pp.64-67)

There are two parts to this element:

1. Limited capability for work - This does not exist for new UC claims from 03/04/2017, but is still possible to receive for ongoing claims from before that date, or if covered by a long list of related edge cases to do with existing claims. It is assumed that none of these apply to the model under development, as it only deals with new claims in the period under modelling.
2. Limited capability for work-related activity - This is a more strictly defined status than limited capability for work, and is normally awarded following a Work Capability Assessment (WCA) that may include medical examination at an approved assessment centre. The criteria for deciding on an award are complex and ambiguous, with frequent appeals and reversals of initial assessment decisions.

Dealing purely with limited capability for work-related activity, if a claimant or their partner are found to have limited capability for work-related activity, then they receive £328.32 per month (i.e. per assessment period). There is no extra award if both members of a couple are assessed as having limited capability for work-related activity.

There is complexity to the timing of eligibility - a newly qualifying claimant should only have the award counted from the first assessment period beginning more than three months from the date of first providing medical evidence of a health condition that leads to Work Capability Assessment. So a claimant provides evidence such as a medical certificate from their GP, this triggers the Work Capability Assessment process, and eligibility starts on the first assessment period that begins more than three months after that date. If the WCA process takes longer than that, then payment will be backdated following award.

## Ruleset 10 - A carer element if one of the recipients cares for a severely disabled person under UC

Source: Child Poverty Action Group (2018, pp.67-68)

If a claimant or their partner provides unpaid care for someone, for at least 35 hours per week, they are eligible for the carer element. Along with a range of criteria to establish whether someone actually is a carer in this definition, there are several caveats:

* The element for adults with limited capability for work-related activity takes precedence. If a carer is also eligible for the work-related activity element, they get that and not the carer element.
* If a claiming couple both care for the same person, they are only eligible for the element once. If they meet carer conditions for a separate person each, they are eligible for two carer elements.

The carer element is £156.45 per month (i.e. per assessment period), or twice that if both partners are caring for different people.

## Ruleset 11 - An allowance for childcare under UC

Source: Child Poverty Action Group (2018, pp.68-70)

If a claimant pays for childcare in order to carry out paid work, then they are eligible for repayment of 85% of childcare costs, up to a maximum of £646.35 per month (i.e. per assessment period) for one child, or £1108.04 per month for two or more children. This comes with conditions, including:

* There is no minimum number of hours, but it must be declared, paid work.
* If a couple are claiming, then either both partners must be in work, or the non-working person must be assessed as incapable of work-related activity or a full-time carer.
* The childcare has to be by a recognised provider.
* The child has to be under 16, or aged 16 and the childcare period is before the 1st September after their 16th birthday.

There are further conditions, but they do not affect the basic rules. There is also a help scheme called tax-free childcare payments, but claiming it removes eligibility for UC.

## Ruleset 12 - A housing costs element under UC

Source: Child Poverty Action Group (2018, pp.72-106)

The rules surrounding housing costs eligibility are complex, and would be unrewarding to include in our current model, since they largely consist of a long array of conditions which would exclude a claimant from eligibility, and our modelling interest is primarily in the interaction of rules. Accordingly, a basic model is described in the following sections, which assumes those conditions are satisfied and a claimant is eligible.

A claimant / claimant couple may have the following statuses:

* Ineligible for housing costs or not claiming them
* Private tenant
* Tenant of a registered social landlord
* Owner-occupier paying mandatory service charges

A claimant / couple who do not or cannot claim for housing costs get no contribution from this to their UC maximum amount. Some of the statuses that lead to ineligibility introduce requirements on other rules, and these are not modelled. For example an 18-22 year old claimant is usually ineligible for a housing element, and not modelling this means that it's possible for a claim modelled in our subset of the rules to break rules that are present in the full benefit system.

If any of the remaining three status return a value that is 0 or less than 0, then this has the same effect as being ineligible for housing costs.

### Private tenant

Source: Child Poverty Action Group (2018, pp.94-95)

The housing costs element for a private tenant is calculated as:

`Private tenant housing costs element = minimum of ('core rent' and 'cap rent') - non-dependent deduction`

where

`core rent = liable rent x number of relevant family members / total number of liable people` (Child Poverty Action Group, 2018, p.96)

`cap rent = local housing allowance for property with your allowed number of bedrooms` (Child Poverty Action Group, 2018, p.97)

`non-dependent deduction = £72.16 for each non-dependent who is resident and in your extended benefit unit` (Child Poverty Action Group, 2018, p.93)

The local housing allowance is an amount that varies by Broad Rental Market Area, i.e. house location, and by allowed number of bedrooms, i.e. the number of bedrooms deemed appropriate for the occupants of the house.

### Tenant of a registered social landlord

Source: Child Poverty Action Group (2018, pp.98-99)

The calculation for a social tenancy is:

`Social tenant housing costs element = rent - bedroom tax`

where bedroom tax is 0 if you have the allowed number of bedrooms for your family size, rent x 0.14 if you have one bedroom more than allowed, and rent x 0.25 if you have two or more bedrooms above your allowance.

### Owner-occupier paying mandatory service charges

Source: Child Poverty Action Group (2018, pp.101-104)

While e.g. mortgage repayments are not covered by UC, unavoidable service charges excluding charges for utilities such as water and electricity can be covered. However, there is a nine month qualifying period, so UC claimants who are owner-occupiers of their home will not receive any housing costs element until they have been claiming UC for nine months. There are several caveats to this rule, as always.
