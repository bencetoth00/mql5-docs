# Fuzzy systems rules


A fuzzy system (fuzzy logical inference system) is a receipt of conclusion in the form of a fuzzy set corresponding to the current values of the inputs with the use of a set of fuzzy rules and fuzzy operations.

The fuzzy rules determine the relationship between inputs and outputs of an examined object. Amount of rules in the system is unlimited. The generalized format of fuzzy rules is as follows:

if rule condition, then rule conclusion.

Rule condition describes the current state of the object. Rule conclusion describes how the condition affects the object.  

| Class of rules for fuzzy systems | Description |
| --- | --- |
| [CMamdaniFuzzyRule](CMamdaniFuzzyRule/CMamdaniFuzzyRule.md) | Class for implementing a fuzzy logic rule for the Mamdani algorithm |
| [CSugenoFuzzyRule](CSugenoFuzzyRule/CSugenoFuzzyRule.md) | Class for implementing a fuzzy logic rule for the Sugeno algorithm |
| [CSingleCondition](CSingleCondition/CSingleCondition.md) | The class sets a fuzzy condition expressed by "Fuzzy variable — Fuzzy term" pair. |
| [CConditions](CConditions/CConditions.md) | Class defines a set of fuzzy conditions connected to each other by an operator. |
| [CGenericFuzzyRule](CGenericFuzzyRule/CGenericFuzzyRule.md) | Base class for implementing the both types of fuzzy rules. |
