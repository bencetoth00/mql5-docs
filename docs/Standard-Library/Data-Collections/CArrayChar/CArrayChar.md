# CArrayChar

CArrayChar

CArrayChar is a class of dynamic array of char or uchar variables.

Description

CArrayChar class provides the ability to work with a dynamic array of char or uchar variables. The class allows adding/inserting/deleting array elements, performing an array sorting, and searching in a sorted array. In addition, methods of working with files have been implemented.

Declaration

|  |
| --- |
| class CArrayChar : public CArray |

Title

|  |
| --- |
| #include <Arrays\ArrayChar.mqh> |

|  |
| --- |
| Inheritance hierarchy    [CObject](../../Basic-Class-CObject/Basic-Class-CObject.md)        [CArray](../CArray/CArray.md)            CArrayChar |

Class Methods

| Memory control |  |
| --- | --- |
| [Reserve](Reserve/Reserve.md) | Allocates memory to increase the size of the array |
| [Resize](Resize/Resize.md) | Sets a new (smaller) size of the array |
| [Shutdown](Shutdown/Shutdown.md) | Clears the array with a full memory release |
| Add methods |  |
| [Add](Add/Add.md) | Adds an element to the end of the array |
| [AddArray](AddArray/AddArray.md) | Adds elements of one array to the end of another |
| [AddArray](AddArray/AddArray-1526.md) | Adds elements of one array to the end of another |
| [Insert](Insert/Insert.md) | Inserts an element to the specified position in the array |
| [InsertArray](InsertArray/InsertArray.md) | Inserts to an array elements from another array from the specified position |
| [InsertArray](InsertArray/InsertArray-1529.md) | Inserts to an array elements from another array from the specified position |
| [AssignArray](AssignArray/AssignArray.md) | Copies the elements of one array to another |
| [AssignArray](AssignArray/AssignArray-1531.md) | Copies the elements of one array to another |
| Modify methods |  |
| [Update](Update/Update.md) | Changes the element at the specified array position |
| [Shift](Shift/Shift.md) | Moves an element from a given position in the array to the specified offset |
| Delete methods |  |
| [Delete](Delete/Delete.md) | Removes the element from the specified array position |
| [DeleteRange](DeleteRange/DeleteRange.md) | Deletes a group of elements from the specified array position |
| Access methods |  |
| [At](At/At.md) | Gets the element from the specified array position |
| Compare methods |  |
| [CompareArray](CompareArray/CompareArray.md) | Compares the array with another one |
| [CompareArray](CompareArray/CompareArray-1538.md) | Compares the array with another one |
| Sorted array methods |  |
| [InsertSort](InsertSort/InsertSort.md) | Inserts an element in a sorted array |
| [Search](Search/Search.md) | Searches for an element equal to the sample in the sorted array |
| [SearchGreat](SearchGreat/SearchGreat.md) | Searches for an element with a value exceeding the value of the sample in the sorted array |
| [SearchLess](SearchLess/SearchLess.md) | Searches for an element with a value less than the value of the sample in the sorted array |
| [SearchGreatOrEqual](SearchGreatOrEqual/SearchGreatOrEqual.md) | Searches for an element with a value greater than or equal to the value of the sample in the sorted array |
| [SearchLessOrEqual](SearchLessOrEqual/SearchLessOrEqual.md) | Searches for an element with a value less than or equal to the value of the sample in the sorted array |
| [SearchFirst](SearchFirst/SearchFirst.md) | Searches for the first element equal to the sample in the sorted array |
| [SearchLast](SearchLast/SearchLast.md) | Searches for the last element equal to the sample in the sorted array |
| [SearchLinear](SearchLinear/SearchLinear.md) | Searches for the element equal to the sample in the array |
| Input/output |  |
| virtual [Save](../CArray/Save/Save.md) | Saves data array in the file |
| virtual [Load](Load/Load.md) | Loads data array from the file |
| virtual [Type](Type/Type.md) | Gets the array type identifier |

| Methods inherited from class CObject  Prev, Prev, Next, Next, [Compare](../../Basic-Class-CObject/Compare/Compare.md) |
| --- |
| Methods inherited from class CArray  [Step](../CArray/Step/Step.md), [Step](../CArray/Step/Step.md), [Total](../CArray/Total/Total.md), [Available](../CArray/Available/Available.md), [Max](../CArray/Max/Max.md), [IsSorted](../CArray/IsSorted/IsSorted.md), [SortMode](../CArray/SortMode/SortMode.md), [Clear](../CArray/Clear/Clear.md), [Sort](../CArray/Sort/Sort.md) |
