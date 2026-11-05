# ISet<T>


ISet<T> is an interface for implementing generic data sets.

### Description

The ISet interface defines basic methods to work with sets, such as: the union and intersection of sets, definition of strict and non-strict subsets, and others.

### Declaration

```cpp
   template<typename T>
   interface ISet : public ICollection<T>
```

### Header

```cpp
   #include <Generic\Interfaces\ISet.mqh>
```

|  |
| --- |
| Inheritance Hierarchy    [ICollection](../ICollection-T/ICollection-T.md)        ISet  Direct descendants  [CHashSet](../CHashSet-T/CHashSet-T.md), [CSortedSet](../CSortedSet-T/CSortedSet-T.md) |

### Class Methods

| Method | Description |
| --- | --- |
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