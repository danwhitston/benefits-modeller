# Sample benefit rules

Objective 1 of the project is to create a sample set of benefit rules and test cases. I'm using The Welfare Benefits and Tax Credits Handbook (Child Poverty Action Group, 2018) as a source of rules, and will express the rules in my own language, with references, to mitigate any risk of questions around copyright and plagiarism. Rather than taking a random sample, I've decided to start with one regulation and spread outwards to cover an interconnected set of dependent rules. This will enable the modelling of a system of rules instead of just running them in isolation, which will make it easier to test the behaviour of the system and the SMT solver with more complex models. The SMT solver would be of no benefit in 'solving' individual rules.

## Limits to the model

### Location

Per p3-4 of the handbook, the handbook's rules apply to England and Wales. Scotland has broadly the same legislation but has the power to diverge. Northern Ireland has separate legislation on benefits and tax credits, although the systems are similar in practice. Beyond this, where a claimant lives has further impact on several aspects of benefits - there are local taxes and benefits such as council tax and discretionary housing payments; the council tax also varies according to the designated property band of the claimant's home and their household status. (p XX)

### Dates

In common with all rules being discussed, the rules have changed in the years since the handbook was published. In this case the change is particularly acute: no new claims can be made for the benefits classed as legacy benefits, since all new claims are for Universal Credit. This does not affect the correctness of the rules being modelled, *for the period in which those rules were in effect*. All benefit rules have the same issue of time dependence. Not only the conditions of eligibility but also the payment amounts and even the existence of rules changes over time. Not only do claimants' circumstances change, but people get older, which changes their eligibility in and of itself.

Since the handbook we're using as a basis for our modelling only applies to a limited timespan, we will limit our modelling to claims with a date of new claim falling within the period of validity. The handbook's acknowledgements (p.iv) state that the law covered in the book was correct on 5/3/2018, so we shall set the limit for new claim dates to between 5/3/2018 and 4/3/2019, for now. Likewise, we will not model payment dates outside of those lower and upper limits.

## Rule 1 - When you come under the universal credit system

Source: p20-22

The handbook was published during transition between two benefit systems: moving from a legacy system consisting of several sets of benefits and tax credits, to Universal Credit (UC). Whether claimants would be assessed under the legacy system or UC was dependent on date of initial claim, the area their home address was in, and several other conditions.

A claimant comes under UC if either:

1. Their date of claim for UC is after the rollout date for the Jobcentre area in which they're claiming, as listed in the PDF files linked at <https://www.gov.uk/government/publications/universal-credit-transition-to-full-service>. The rollout areas are often known as 'full service' areas. We know from the linked URL that rollout completed in December 2018, in accordance with the target date stated on p22 of the handbook.
2. Their date of claim for UC is before 1/1/2018, and after April 2016, and the Jobcentre area in which they're claiming is a UC gateway area, and they meet a long list of gateway conditions that are fully detailed in Chapter 2 of the 2017/18 edition of the handbook. An immediate consequence of the date limitations discussed earlier on is that our model completely excludes UC gateway claimants, since we're taking new claims from 5/3/2018.

There is an exception to the rule for full service areas: claimants with three or more children, and who meet certain other conditions, should continue to claim legacy benefits for claims between 6/04/2017 and 31/01/2019 (i.e. during the modelled period).

As with other rules, there are inputs to this decision which are themselves subject to modelling. In this model, those are:

* The date of claim, which is a date input between 5/3/2018 and 4/3/2019.
* The date at which their Jobcentre area becomes a 'full service' area, which is a date between November 2015 and December 2018
* Whether a claimant meets the three-or-more-children-based exception criteria for UC rollout.

## Rule 2 - Are you eligible for Universal Credit?

Source: p31-33

There are several requirements which must *all* be true for a claimant to be eligible for UC. UC normally treats a couple as a single unit for claim purposes, i.e. they make a single claim and are paid jointly. For a couple to be eligible to claim UC normally, all requirements must be true for both partners.

The basic requirements to claim UC are that the claimant(s) are:

* coming under UC, i.e. that rule 1 is true
* aged 18 or over, or aged 16-17 and meet special young person UC eligibility criteria (detailed on p32-33)
* aged below the qualifying age for Pension Credit (PC)
* not receiving education (as defined on p32 and p566) unless you are exempted from this requirement (chapter 41)
* in habitual residence in Great Britain and have the right to reside in Great Britain (both detailed in chapter 68)
* either physically in or can be treated as being in Great Britain (chapter 68-69)
* not a person subject to immigration control (p1529)
* in acceptance of the claimant commitment (p1026)

It is possible for one member of a couple to claim as a single person if they meet the basic requirements themselves, but their partner fails to meet basic requirements in a certain, limited set of ways. In this situation, the claim works as if the claimant is a single person, *except* that both partners' income, savings and capital are still included in calculations.

The financial requirements to claim UC are that claimant(s) do not have:

* too high an income
* savings and capital above £16000

The income ceiling ('too high an income') is not a fixed number - instead it refers to an income which is high enough that no UC would be paid, due to the reduction in UC payments that results from income.

## Rule 3 - 