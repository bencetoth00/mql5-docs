# CFuzzyVariable

CFuzzyVariable

Class for creating general fuzzy variables.  

Description

Here, a fuzzy variable is created with the following parameters:

- maximum variable value;
- minimum variable value;
- fuzzy variable name;
- term set (set of all possible values, which a linguistic variable is capable of receiving).

Declaration

|  |
| --- |
| class CFuzzyVariable : public CNamedVariableImpl |

Title

|  |
| --- |
| #include <Math\Fuzzy\fuzzyvariable.mqh> |

|  |
| --- |
| Inheritance hierarchy    [CObject](../../../../Basic-Class-CObject/Basic-Class-CObject.md)        INamedValue            INamedVariable                CNamedVariableImpl                    CFuzzyVariable |

Class methods

| Class method | Description |
| --- | --- |
| [AddTerm](AddTerm/AddTerm.md) | Adds a single fuzzy term to a fuzzy variable. |
| [GetTermByName](GetTermByName/GetTermByName.md) | Gets a fuzzy term by a specified name. |
| [Max](Max/Max.md) | Gets and sets a maximum value for a fuzzy variable. |
| [Min](Min/Min.md) | Gets and sets a minimum value for a fuzzy variable. |
| [Terms](Terms/Terms.md) | Gets and sets a list of fuzzy terms for the given fuzzy variable. |
| [Values](Values/Values.md) | Gets and sets a list of fuzzy terms for the given fuzzy variable. |

| Methods inherited from class CObject  Prev, Prev, Next, Next, [Save](../../../../Basic-Class-CObject/Save/Save.md), [Load](../../../../Basic-Class-CObject/Load/Load.md), [Type](../../../../Basic-Class-CObject/Type/Type.md), [Compare](../../../../Basic-Class-CObject/Compare/Compare.md) |
| --- |
| Methods inherited from class CNamedVariableImpl  Name, Name |
