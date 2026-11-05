# CSugenoVariable


Class for creating fuzzy Sugeno-type variables.  

### Description

Fuzzy Sugeno-type variable is different from the general linguistic variable since it is not set by a term set but by a set of linear functions.

### Declaration

```cpp
   class CSugenoVariable : public CNamedVariableImpl
```

### Title

```cpp
   #include <Math\Fuzzy\sugenovariable.mqh>
```

|  |
| --- |
| Inheritance hierarchy    [CObject](../../../../Basic-Class-CObject/Basic-Class-CObject.md)        INamedValue            INamedVariable                CNamedVariableImpl                    CSugenoVariable |

### Class methods

| Class method | Description |
| --- | --- |
| [Functions](Functions/Functions.md) | Gets the list of linear functions of the fuzzy Sugeno variable. |
| [GetFuncByName](GetFuncByName/GetFuncByName.md) | Gets the linear function by a specified name. |
| [Values](Values/Values.md) | Gets the list of linear functions of the fuzzy Sugeno variable. |

| Methods inherited from class CObject  Prev, Prev, Next, Next, [Save](../../../../Basic-Class-CObject/Save/Save.md), [Load](../../../../Basic-Class-CObject/Load/Load.md), [Type](../../../../Basic-Class-CObject/Type/Type.md), [Compare](../../../../Basic-Class-CObject/Compare/Compare.md) |
| --- |
| Methods inherited from class CNamedVariableImpl  Name, Name |