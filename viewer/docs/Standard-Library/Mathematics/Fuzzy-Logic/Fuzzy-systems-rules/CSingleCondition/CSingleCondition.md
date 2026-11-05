# CSingleCondition


The class sets a fuzzy condition expressed by "Fuzzy variable — Fuzzy term" pair.

### Description

According to a fuzzy condition, one variable corresponds to one term. A fuzzy condition can be described by the following expression: X is a,

where:

- X is a fuzzy variable;
- a  is a fuzzy variable value (fuzzy term).

### Declaration

```cpp
   class CSingleCondition : public ICondition
```

### Title

```cpp
   #include <Math\Fuzzy\fuzzyrule.mqh>
```

|  |
| --- |
| Inheritance hierarchy    [CObject](../../../../Basic-Class-CObject/Basic-Class-CObject.md)        ICondition            CSingleCondition  Direct descendants  CFuzzyCondition |

### Class methods

| Class method | Description |
| --- | --- |
| [Not](Not/Not.md) | Gets and sets the flag indicating whether it is necessary to apply negation to this condition. |
| [Term](Term/Term.md) | Gets and sets a fuzzy term for this condition. |
| [Var](Var/Var.md) | Gets and sets a fuzzy variable for this condition. |

|  |
| --- |
| Methods inherited from class CObject  Prev, Prev, Next, Next, [Save](../../../../Basic-Class-CObject/Save/Save.md), [Load](../../../../Basic-Class-CObject/Load/Load.md), [Type](../../../../Basic-Class-CObject/Type/Type.md), [Compare](../../../../Basic-Class-CObject/Compare/Compare.md) |