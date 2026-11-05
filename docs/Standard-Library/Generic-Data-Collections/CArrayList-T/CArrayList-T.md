# CArrayList<T>

CArrayList<T>

CArrayList<T> is a generic class that implements the IList<T> interface.

Description

The CArrayList<T> class is an implementation of the dynamic data list of the T type. This class provides the basic methods to work with the list, such as to access an element by index, to search and delete elements, sort, and others.

Declaration

|  |
| --- |
| template<typename T>     class CArrayList : public IList<T> |

Header

|  |
| --- |
| #include <Generic\ArrayList.mqh> |

|  |
| --- |
| Inheritance Hierarchy    [ICollection](../ICollection-T/ICollection-T.md)        [IList](../IList-T/IList-T.md)            CArrayList |

Class Methods

| Method | Description |
| --- | --- |
| [Capacity](Capacity/Capacity.md) | Gets and sets the current capacity of a list |
| [Count](Count/Count.md) | Returns the number of elements in the list |
| [Contains](Contains/Contains.md) | Determines whether a list contains an element with the specified value |
| [TrimExcess](TrimExcess/TrimExcess.md) | Sets the capacity of a list to the actual number of elements |
| [TryGetValue](TryGetValue/TryGetValue.md) | Gets an element of the list at the specified index |
| [TrySetValue](TrySetValue/TrySetValue.md) | Sets the value of the list element at the specified index |
| [Add](Add/Add.md) | Adds an element to the list |
| [AddRange](AddRange/AddRange.md) | Adds a collection or an array of elements to the list |
| [Insert](Insert/Insert.md) | Inserts an element into the list at the specified index |
| [InsertRange](InsertRange/InsertRange.md) | Inserts a collection or an array of elements into the list at the specified index |
| [CopyTo](CopyTo/CopyTo.md) | Copies all elements of a list to the specified array starting at the specified index |
| [BinarySearch](BinarySearch/BinarySearch.md) | Searches for the specified value in an ascending-sorted list |
| [IndexOf](IndexOf/IndexOf.md) | Searches for the first occurrence of a value in a list |
| [LastIndexOf](LastIndexOf/LastIndexOf.md) | Searches for the last occurrence of a value in a list |
| [Clear](Clear/Clear.md) | Removes all elements from a collection |
| [Remove](Remove/Remove.md) | Removes the first occurrence of the specified element from the list |
| [RemoveAt](RemoveAt/RemoveAt.md) | Removes an element at the specified index of the list |
| [RemoveRange](RemoveRange/RemoveRange.md) | Removes a range of elements from the list |
| [Reverse](Reverse/Reverse.md) | Reverses the order of elements in the list |
| [Sort](Sort/Sort.md) | Sorts elements in the list |
