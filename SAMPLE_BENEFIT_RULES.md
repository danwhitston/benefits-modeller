# Sample benefit rules

Objective 1 of the project is to create a sample set of benefit rules and test cases. I'm using The Welfare Benefits and Tax Credits Handbook (Child Poverty Action Group, 2018) as a source of rules, and will express the rules in my own language, with references, to mitigate any risk of questions around copyright and plagiarism. Rather than taking a random sample, I've decided to start with one regulation and spread outwards to cover an interconnected set of dependent rules. This will enable the modelling of a system of rules instead of just running them in isolation, which will make it easier to test the behaviour of the system and the SMT solver with more complex models. The SMT solver would be of no benefit in 'solving' individual rules.

## Rule 1 - When you come under the universal credit system

Source: p20-22

The handbook was published during transition between two benefit systems: moving from a legacy system consisting of several sets of benefits and tax credits, to Universal Credit (UC). Whether claimants would be assessed under the legacy system or UC was dependent on date of initial claim, the area their home address was in, and several other conditions.

A claimant comes under UC if either:

1. Their date of claim for UC is after the rollout date for the Jobcentre area in which they're claiming, as listed in the PDF files linked at <https://www.gov.uk/government/publications/universal-credit-transition-to-full-service>.
2. Their date of claim for UC is before 1/1/2018, and after April 2016, and the Jobcentre area in which they're claiming is a UC gateway area, and they meet a long list of gateway conditions that are fully detailed in Chapter 2 of the 2017/18 edition of the handbook.

The rules before April 2016 are not covered, and the rollout dates for Jobcentre areas at the linked website were updated during rollout. We know from the linked URL that rollout completed in December 2018, in accordance with the target date stated on p22 of the handbook.

### Sidenote regarding the impact of date of claim on rules

In common with all rules being discussed, the rules have changed in the years since the handbook was published. In this case the change is particularly acute: no new claims can be made for the benefits classed as legacy benefits, since all new claims are for Universal Credit. This does not affect the correctness of the rules being modelled, *for the period in which those rules were in effect*. This applies to all benefit rules.

Since the handbook we're using as a basis for our modelling only applies to a limited timespan, and we do not have handbooks covering other periods, we will limit our modelling to claims with a date of new claim falling within the period of validity. The handbook's acknowledgements (p.iv) state that the law covered in the book was correct on 5/3/2018, so we shall set the limit for new claim dates to between 5/3/2018 and 4/3/2019, for now.

## Rule 2 - Are you eligible for Universal Credit?

