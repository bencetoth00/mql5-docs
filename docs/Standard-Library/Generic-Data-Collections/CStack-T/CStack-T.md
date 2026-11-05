# CStack<T>

CStack<T>

CStack<T> is a generic class that implements the ICollection<T> interface.

Description

The CStack<T> class is a dynamic collection of T type data, which is organized as a stack that operates on the LIFO (last in, first out) principle.

Declaration

|  |
| --- |
| template<typename T>     class CStack : public ICollection<T> |

Header

|  |
| --- |
| #include <Generic\Stack.mqh> |

|  |
| --- |
| Inheritance Hierarchy    [ICollection](../ICollection-T/ICollection-T.md)        CStack |

Class Methods

| Method | Description |
| --- | --- |
| [Add](Add/Add.md) | Adds an element to a stack |
| [Count](Count/Count.md) | Returns the number of elements in a stack |
| [Contains](Contains/Contains.md) | Determines whether a stack contains an element with the specified value |
| [TrimExcess](TrimExcess/TrimExcess.md) | Sets the capacity of a stack to the actual number of elements |
| [CopyTo](CopyTo/CopyTo.md) | Copies all elements of a stack to the specified array starting at the specified index |
| [Clear](Clear/Clear.md) | Removes all elements from a stack |
| [Remove](Remove/Remove.md) | Removes the first occurrence of the specified element from a stack |
| [Push](Push/Push.md) | Adds an element to a stack |
| [Peek](Peek/Peek.md) | Returns the head element without removing it from a stack |
| [Pop](Pop/Pop.md) | Returns the head element and removes it from a stack |
