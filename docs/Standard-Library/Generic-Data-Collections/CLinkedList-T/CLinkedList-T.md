# CLinkedList<T>

CLinkedList<T>

CLinkedList<T> is a generic class that implements the ICollection<T> interface.

Description

The CLinkedList<T> class is an implementation of the dynamic doubly linked data list of the T type. This class provides basic methods to work with doubly linked lists, such as to add, delete, search elements, and others.

Declaration

|  |
| --- |
| template<typename T>     class CLinkedList : public ICollection<T> |

Header

|  |
| --- |
| #include <Generic\LinkedList.mqh> |

|  |
| --- |
| Inheritance Hierarchy    [ICollection](../ICollection-T/ICollection-T.md)        CLinkedList |

Class Methods

| Method | Description |
| --- | --- |
| [Add](Add/Add.md) | Adds an element to a linked list |
| [AddAfter](AddAfter/AddAfter.md) | Adds an element after the specified node in the linked list |
| [AddBefore](AddBefore/AddBefore.md) | Adds an element before the specified node in the linked list |
| [AddFirst](AddFirst/AddFirst.md) | Adds an element at the beginning of the linked list |
| [AddLast](AddLast/AddLast.md) | Adds an element at the end of the linked list |
| [Count](Count/Count.md) | Returns the number of elements in the linked list |
| [Head](Head/Head.md) | Returns a pointer to the first node of the linked list |
| [First](First/First.md) | Returns a pointer to the first node of the linked list |
| [Last](Last/Last.md) | Returns a pointer to the last node of the linked list |
| [Contains](Contains/Contains.md) | Determines whether the linked list contains an element with the specified value |
| [CopyTo](CopyTo/CopyTo.md) | Copies all elements of the linked list to the specified array starting at the specified index |
| [Clear](Clear/Clear.md) | Removes all elements from a linked list |
| [Remove](Remove/Remove.md) | Removes the first occurrence of the specified element from the linked list |
| [RemoveFirst](RemoveFirst/RemoveFirst.md) | Removes the first element of the linked list |
| [RemoveLast](RemoveLast/RemoveLast.md) | Removes the last element of the linked list |
| [Find](Find/Find.md) | Searches for the first occurrence of the specified value in the linked list |
| [FindLast](FindLast/FindLast.md) | Searches for the last occurrence of the specified value in the linked list |
