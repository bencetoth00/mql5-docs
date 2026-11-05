# ICollection<T>

ICollection<T>

ICollection<T> is an interface for implementing generic data collections.

Description

The ICollection<T> interface determines basic methods to work with collections, including methods to count elements, to clear a collection, to add or delete elements, and others.

Declaration

|  |
| --- |
| template<typename T>     interface ICollection |

Header

|  |
| --- |
| #include <Generic\Interfaces\ICollection.mqh> |

|  |
| --- |
| Inheritance Hierarchy    ICollection  Direct descendants  [CLinkedList](../CLinkedList-T/CLinkedList-T.md), [CQueue](../CQueue-T/CQueue-T.md), [CRedBlackTree](../CRedBlackTree-T/CRedBlackTree-T.md), [CStack](../CStack-T/CStack-T.md), [IList](../IList-T/IList-T.md), [IMap](../IMap-TKey,TValue/IMap-TKey,TValue.md), [ISet](../ISet-T/ISet-T.md) |

Class Methods

| Method | Description |
| --- | --- |
| [Add](Add/Add.md) | Adds an element to a collection |
| [Count](Count/Count.md) | Returns the number of elements in a collection |
| [Contains](Contains/Contains.md) | Determines whether a collection contains an element with the specified value |
| [CopyTo](CopyTo/CopyTo.md) | Copies all elements of a collection to the specified array starting at the specified index |
| [Clear](Clear/Clear.md) | Removes all elements from a collection |
| [Remove](Remove/Remove.md) | Removes the first occurrence of the specified element from a collection |
