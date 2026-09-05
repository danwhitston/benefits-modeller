# Sample test cases

Objective 1 of the project is to create a sample set of benefit rules and test cases. The benefit rules are described in the [project report](./PROJECT_REPORT.pdf), under Objective 1, and expressed in Ben in [./src/SAMPLE_BENEFIT_RULES.ben](./src/SAMPLE_BENEFIT_RULES.ben). This document provides a set of example benefit calculations and hypotheses with known truth values. While they do not provide comprehensive coverage of the sample rules, any system that correctly models the described benefit rules should match the test cases in this document.

## Example 1 - UC maximum amount, with Gail and Joe

Source: p36

Situation: Gail and Joe are a couple, both over 25 years old and under pension age. Their UC date of claim is May 2018. Their two children are both born after 6th April 2017. Gail works. Joe has limited capability for work and work-related activity through an existing finding, so does not have a waiting period to become eligible. They have no eligible housing or childcare costs, and no unearned income.

Inference: Their UC maximum amount is £1290.55.

## Example 2 - UC entitlement, with Gail and Joe

Source: p38

Situation: Gail and Joe are a couple, both over 25 years old and under pension age. Gail's monthly earnings are £1200. Joe has limited capability for work and work-related activity, for which he receives a non-UC benefit with unearned monthly income of £479.91. They have no eligible housing or childcare costs, and no other unearned income.

Joe's ESA counts for both the maximum UC and the unearned income!

Inference: Their monthly UC entitlement is £312.31
