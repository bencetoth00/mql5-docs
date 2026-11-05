# CList

CList

CList Class is a class of dynamic list of instances of the CObject class and its derived classes.

Description

Class CList provides the ability to work with a list of instances of [CObject](../../Basic-Class-CObject/Basic-Class-CObject.md) and its derived classes. The class allows adding/inserting/deleting array elements, performing an array sorting, and searching in a sorted array. In addition, methods of working with files have been implemented.

There are some subtleties of working with the CList class. The class has a mechanism to control dynamic memory, so be careful when working with elements of the list.

[Subtleties](../CArrayObj/CArrayObj.md#carrayobjfeatures) of the mechanism of memory management similar to those described in CArrayObj.

Declaration

|  |
| --- |
| class CList : public CObject |

Title

|  |
| --- |
| #include <Arrays\List.mqh> |

|  |
| --- |
| Inheritance hierarchy    [CObject](../../Basic-Class-CObject/Basic-Class-CObject.md)        CList |

Class Methods by Groups

| Attributes |  |
| --- | --- |
| [FreeMode](FreeMode/FreeMode.md) | Gets the flag of memory management when deleting list elements |
| [FreeMode](FreeMode/FreeMode-1774.md) | Sets the flag of memory management when deleting list elements |
| [Total](Total/Total.md) | Gets the number of elements in the list |
| [IsSorted](IsSorted/IsSorted.md) | Gets sorted list flag |
| [SortMode](SortMode/SortMode.md) | Gets the sorting mode |
| Create methods |  |
| [CreateElement](CreateElement/CreateElement.md) | Creates a new list element |
| Add methods |  |
| [Add](Add/Add.md) | Adds an element to the end of the list |
| [Insert](Insert/Insert.md) | Inserts an element to the specified position of the list |
| Delete methods |  |
| [DetachCurrent](DetachCurrent/DetachCurrent.md) | Removes an element from the current position in the list without deleting it "physically" |
| [DeleteCurrent](DeleteCurrent/DeleteCurrent.md) | Removes the element from the current position in the list |
| [Delete](Delete/Delete.md) | Removes the element from the specified position in the list |
| [Clear](Clear/Clear.md) | Removes all list elements |
| Navigation |  |
| [IndexOf](IndexOf/IndexOf.md) | Gets the index of the specified list element |
| [GetNodeAtIndex](GetNodeAtIndex/GetNodeAtIndex.md) | Gets an item with the specified index of the list |
| [GetFirstNode](GetFirstNode/GetFirstNode.md) | Gets the first element of the list |
| [GetPrevNode](GetPrevNode/GetPrevNode.md) | Gets the previous element of the list |
| [GetCurrentNode](GetCurrentNode/GetCurrentNode.md) | Gets the current list element |
| [GetNextNode](GetNextNode/GetNextNode.md) | Gets the next element in the list |
| [GetLastNode](GetLastNode/GetLastNode.md) | Gets the last element in the list |
| Ordering methods |  |
| [Sort](Sort/Sort.md) | Sorts the list |
| [MoveToIndex](MoveToIndex/MoveToIndex.md) | Moves the current element in the list to the specified position |
| [Exchange](Exchange/Exchange.md) | Swaps two elements in the list |
| Compare methods |  |
| [CompareList](CompareList/CompareList.md) | Compares the list with another one |
| Search methods |  |
| [Search](Search/Search.md) | Searches for an element equal to the sample in sorted list |
| Input/output |  |
| virtual [Save](Save/Save.md) | Saves list data in the file |
| virtual [Load](Load/Load.md) | Loads list data from the file |
| virtual [Type](Type/Type.md) | Gets the list type identifier |

|  |
| --- |
| Methods inherited from class CObject  Prev, Prev, Next, Next, [Compare](../../Basic-Class-CObject/Compare/Compare.md) |
