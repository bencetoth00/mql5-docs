# CHashSet<T>

CHashSet<T>

CHashSet<T> is a generic class that implements the ISet<T> interface.

Description

The CHashSet<T> class is an implementation of the unordered dynamic data set of type T, with the required uniqueness of each value. This class provides basic methods to work with sets and related operations, such as: the union and intersection of sets, definition of strict and non-strict subsets, and others.

Declaration

|  |
| --- |
| template<typename T>     class CHashSet : public ISet<T> |

Header

|  |
| --- |
| #include <Generic\HashSet.mqh> |

|  |
| --- |
| Inheritance Hierarchy    [ICollection](../ICollection-T/ICollection-T.md)        [ISet](../ISet-T/ISet-T.md)            CHashSet |

Class Methods

| Method | Description |
| --- | --- |
| [Add](Add/Add.md) | Adds an element to a set |
| [Count](Count/Count.md) | Returns the number of elements in a set |
| [Comparer](Comparer/Comparer.md) | Determines whether a set contains an element with the specified value |
| [Contains](Contains/Contains.md) | Returns a pointer to the IEqualityComparer<T> interface, used to organize a set |
| [TrimExcess](TrimExcess/TrimExcess.md) | Sets the capacity of a set to the actual number of elements, and thus frees up unused memory |
| [CopyTo](CopyTo/CopyTo.md) | Copies all elements of a set to the specified array starting at the specified index |
| [Clear](Clear/Clear.md) | Removes all elements from a set |
| [Remove](Remove/Remove.md) | Removes the specified element from a set |
| [ExceptWith](ExceptWith/ExceptWith.md) | Produces the operation of difference between the current collection and a passed collection (array) |
| [IntersectWith](IntersectWith/IntersectWith.md) | Produces the operation of intersection of the current collection and a passed collection (array) |
| [SymmetricExceptWith](SymmetricExceptWith/SymmetricExceptWith.md) | Produces the operation of symmetrical difference between the current collection and a passed collection (array) |
| [UnionWith](UnionWith/UnionWith.md) | Produces the union of the current collection and a passed collection (array) |
| [IsProperSubsetOf](IsProperSubsetOf/IsProperSubsetOf.md) | Determines whether the current set is a proper subset of the specified collection or array |
| [IsProperSupersetOf](IsProperSupersetOf/IsProperSupersetOf.md) | Determines whether the current set is a proper superset of the specified collection or array |
| [IsSubsetOf](IsSubsetOf/IsSubsetOf.md) | Determines whether the current set is a subset of the specified collection or array |
| [IsSupersetOf](IsSupersetOf/IsSupersetOf.md) | Determines whether the current set is a superset of the specified collection or array |
| [Overlaps](Overlaps/Overlaps.md) | Determines whether the current set overlaps the specified collection or array |
| [SetEquals](SetEquals/SetEquals.md) | Determines whether the current set contains all elements of the specified collection or array |
