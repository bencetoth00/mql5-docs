# CGenericFuzzyRule


Base class for both types of fuzzy rules.

### Declaration

```cpp
   class CGenericFuzzyRule : public IParsableRule
```

### Title

```cpp
   #include <Math\Fuzzy\fuzzyrule.mqh>
```

|  |
| --- |
| Inheritance hierarchy    [CObject](../../../../Basic-Class-CObject/Basic-Class-CObject.md)        IParsableRule            CGenericFuzzyRule  Direct descendants  [CMamdaniFuzzyRule](../CMamdaniFuzzyRule/CMamdaniFuzzyRule.md), [CSugenoFuzzyRule](../CSugenoFuzzyRule/CSugenoFuzzyRule.md) |

### Class methods

| Class method | Description |
| --- | --- |
| [Conclusion](Conclusion/Conclusion.md) | Gets and sets the fuzzy rule conclusion |
| [Condition](Condition/Condition.md) | Gets and sets the 'if' condition (set of conditions) for a fuzzy rule |
| [CreateCondition](CreateCondition/CreateCondition.md) | Creates a condition for a fuzzy rule by specified parameters |

|  |
| --- |
| Methods inherited from class CObject  Prev, Prev, Next, Next, [Save](../../../../Basic-Class-CObject/Save/Save.md), [Load](../../../../Basic-Class-CObject/Load/Load.md), [Type](../../../../Basic-Class-CObject/Type/Type.md), [Compare](../../../../Basic-Class-CObject/Compare/Compare.md) |