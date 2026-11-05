# IList<T>

IList<T>

IList<T> is an interface for implementing generic data lists.

Description

The IList<T> interface defines basic methods to work with lists, such as to access an element by index, to search and delete elements, sort, and others.

Declaration

|  |
| --- |
| template<typename T>     interface IList : public ICollection<T> |

Header

|  |
| --- |
| #include <Generic\Interfaces\IList.mqh> |

|  |
| --- |
| Inheritance Hierarchy    [ICollection](../ICollection-T/ICollection-T.md)        IList  Direct descendants  [CArrayList](../CArrayList-T/CArrayList-T.md) |

Class Methods

| Method | Description |
| --- | --- |
| [TryGetValue](TryGetValue/TryGetValue.md) | Gets a list element at the specified index |
| [TrySetValue](TrySetValue/TrySetValue.md) | Changes a value from the list at the specified index |
| [Insert](Insert/Insert.md) | Inserts an element into the list at the specified index |
| [IndexOf](IndexOf/IndexOf.md) | Searches for the first occurrence of a value in a list |
| [LastIndexOf](LastIndexOf/LastIndexOf.md) | Searches for the last occurrence of a value in a list |
| [RemoveAt](RemoveAt/RemoveAt.md) | Removes a list element at the specified index |
