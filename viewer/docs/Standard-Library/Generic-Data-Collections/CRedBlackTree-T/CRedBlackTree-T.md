# CRedBlackTree<T>


CRedBlackTree<T> is a generic class that implements the ICollection<T> interface.

### Description

The CRedBlackTree<T> class is an implementation of a dynamic red–black tree whose nodes store T type data. The class provides basic methods to work with red–black trees, such as to add, delete, search for the maximum and minimum value, and more.

### Declaration

```cpp
   template<typename T>
   class CRedBlackTree : public ICollection<T>
```

### Header

```cpp
   #include <Generic\RedBlackTree.mqh>
```

|  |
| --- |
| Inheritance Hierarchy    [ICollection](../ICollection-T/ICollection-T.md)        CRedBlackTree |

### Class Methods

| Method | Description |
| --- | --- |
| [Add](Add/Add.md) | Adds an element to a red–black tree |
| [Root](Root/Root.md) | Returns a pointer to the root of the red–black tree |
| [Count](Count/Count.md) | Returns the number of elements in the red–black tree |
| [Contains](Contains/Contains.md) | Determines whether the red–black tree contains an element with the specified value |
| [Comparer](Comparer/Comparer.md) | Returns a pointer to the IComparer<T> interface used to organize a red–black tree |
| [TryGetMin](TryGetMin/TryGetMin.md) | Gets the minimum element of a red–black tree |
| [TryGetMax](TryGetMax/TryGetMax.md) | Gets the maximum element of a red–black tree |
| [CopyTo](CopyTo/CopyTo.md) | Copies all elements of a red–black tree to the specified array starting at the specified index |
| [Clear](Clear/Clear.md) | Removes all elements from a red–black tree |
| [Remove](Remove/Remove.md) | Removes the occurrence of the specified element from a red–black tree |
| [RemoveMin](RemoveMin/RemoveMin.md) | Removes an element with the minimum value from a red–black tree |
| [RemoveMax](RemoveMax/RemoveMax.md) | Removes an element with the maximum value from a red–black tree |
| [Find](Find/Find.md) | Searches for the occurrence of a specified value in a red–black tree |
| [FindMax](FindMax/FindMax.md) | Searches for an element with the maximum value in a red–black tree |
| [FindMin](FindMin/FindMin.md) | Searches for an element with the minimum value in a red–black tree |