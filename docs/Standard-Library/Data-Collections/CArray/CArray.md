# CArray

CArray

CArray class is the base class of a dynamic array of variables.

Description

Class CArray is intended to operate on dynamic arrays of variables: memory allocation, sorting, and working with files.

Declaration

|  |
| --- |
| class CArray : public CObject |

Title

|  |
| --- |
| #include <Arrays\Array.mqh> |

|  |
| --- |
| Inheritance hierarchy    [CObject](../../Basic-Class-CObject/Basic-Class-CObject.md)        CArray  Direct descendants  [CArrayChar](../CArrayChar/CArrayChar.md), [CArrayDouble](../CArrayDouble/CArrayDouble.md), [CArrayFloat](../CArrayFloat/CArrayFloat.md), [CArrayInt](../CArrayInt/CArrayInt.md), [CArrayLong](../CArrayLong/CArrayLong.md), [CArrayObj](../CArrayObj/CArrayObj.md), [CArrayShort](../CArrayShort/CArrayShort.md), [CArrayString](../CArrayString/CArrayString.md) |

Class Methods by Groups

| Attributes |  |
| --- | --- |
| [Step](Step/Step.md) | Gets the increment size of the array |
| [Step](Step/Step-1510.md) | Sets the increment size of the array |
| [Total](Total/Total.md) | Gets the number of elements in the array |
| [Available](Available/Available.md) | Gets the number of free elements of the array that are available without additional memory allocation |
| [Max](Max/Max.md) | Gets the maximum possible size of the array without memory reallocation |
| [IsSorted](IsSorted/IsSorted.md) | Gets the flag of array being sorted using specified sorting mode |
| [SortMode](SortMode/SortMode.md) | Gets the sorting mode for an array |
| Clear methods |  |
| [Clear](Clear/Clear.md) | Deletes all of the array elements without memory release |
| Sort methods |  |
| [Sort](Sort/Sort.md) | Sorts an array to the specified option |
| Input/output |  |
| virtual [Save](Save/Save.md) | Saves data array in a file |
| virtual [Load](Load/Load.md) | Loads data array from a file |

|  |
| --- |
| Methods inherited from class CObject  Prev, Prev, Next, Next, [Type](../../Basic-Class-CObject/Type/Type.md), [Compare](../../Basic-Class-CObject/Compare/Compare.md) |
