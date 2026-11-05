# CSortedSet<T>


CSortedSet<T> is a generic class that implements the ISet<T> interface.

### Description

The CSortedSet<T> class is an implementation of the sorted dynamic data set of type T, with the required uniqueness of each value. This class provides basic methods to work with sets and related operations, such as: the union and intersection of sets, definition of strict and non-strict subsets, and others.

### Declaration

```cpp
   template<typename T>
   class CSortedSet : public ISet<T>
```

### Header

```cpp
   #include <Generic\SortedSet.mqh>
```

|  |
| --- |
| Inheritance Hierarchy    [ICollection](../ICollection-T/ICollection-T.md)        [ISet](../ISet-T/ISet-T.md)            CSortedSet |

### Class Methods

| Method | Description |
| --- | --- |
| [Add](Add/Add.md) | Adds an element to a sorted set |
| [Count](Count/Count.md) | Returns the number of elements in a sorted set |
| [Contains](Contains/Contains.md) | Determines whether a sorted set contains an element with the specified value |
| [Comparer](Comparer/Comparer.md) | Returns a pointer to the IComparer<T> interface, used to organize a sorted set |
| [TryGetMin](TryGetMin/TryGetMin.md) | Gets the minimum element from a sorted set |
| [TryGetMax](TryGetMax/TryGetMax.md) | Gets the maximum element from a sorted set |
| [CopyTo](CopyTo/CopyTo.md) | Copies all elements of a sorted set to the specified array starting at the specified index |
| [Clear](Clear/Clear.md) | Removes all elements from a sorted set |
| [Remove](Remove/Remove.md) | Removes the occurrence of the specified element from a sorted set |
| [ExceptWith](ExceptWith/ExceptWith.md) | Produces the operation of difference between the current collection and a passed collection (array) |
| [IntersectWith](IntersectWith/IntersectWith.md) | Produces the operation of intersection of the current collection and a passed collection (array) |
| [SymmetricExceptWith](SymmetricExceptWith/SymmetricExceptWith.md) | Produces the operation of symmetrical difference between the current collection and a passed collection (array) |
| [UnionWith](UnionWith/UnionWith.md) | Produces the union of the current collection and a passed collection (array) |
| [IsProperSubsetOf](IsProperSubsetOf/IsProperSubsetOf.md) | Determines whether the current sorted set is a proper subset of the specified collection or array |
| [IsProperSupersetOf](IsProperSupersetOf/IsProperSupersetOf.md) | Determines whether the current sorted set is a proper superset of the specified collection or array |
| [IsSubsetOf](IsSubsetOf/IsSubsetOf.md) | Determines whether the current sorted set is a subset of the specified collection or array |
| [IsSupersetOf](IsSupersetOf/IsSupersetOf.md) | Determines whether the current sorted set is a superset of the specified collection or array |
| [Overlaps](Overlaps/Overlaps.md) | Determines whether the current sorted set overlaps the specified collection or array |
| [SetEquals](SetEquals/SetEquals.md) | Determines whether the current sorted set contains all elements of the specified collection or array |
| [GetViewBetween](GetViewBetween/GetViewBetween.md) | Gets from the current sorted set a subset specified by the minimum and maximum values |
| [GetReverse](GetReverse/GetReverse.md) | Gets a copy of the current sorted set, in which all the elements are arranged in a reverse order |