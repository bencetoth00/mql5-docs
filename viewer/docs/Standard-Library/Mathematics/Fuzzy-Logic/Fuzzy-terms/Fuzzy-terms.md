# Fuzzy terms

# CFuzzyTerm (fuzzy terms)

Class for implementing fuzzy terms.

### Description

A term is any element of a term set.  A term is defined by two components:

- fuzzy term name;
- membership function.

### Declaration

```cpp
   class CFuzzyTerm : public CNamedValueImpl
```

### Title

```cpp
   #include <Math\Fuzzy\fuzzyterm.mqh>
```

|  |
| --- |
| Inheritance hierarchy    [CObject](../../../Basic-Class-CObject/Basic-Class-CObject.md)        INamedValue            CNamedValueImpl                CFuzzyTerm |

### Class methods

| Class method | Description |
| --- | --- |
| [MembershipFunction](MembershipFunction/MembershipFunction.md) | Gets a membership function for the fuzzy term. |

| Methods inherited from class CObject  Prev, Prev, Next, Next, [Save](../../../Basic-Class-CObject/Save/Save.md), [Load](../../../Basic-Class-CObject/Load/Load.md), [Type](../../../Basic-Class-CObject/Type/Type.md), [Compare](../../../Basic-Class-CObject/Compare/Compare.md) |
| --- |
| Methods inherited from class CNamedValueImpl  Name, Name |