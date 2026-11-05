# Generic Data Collections

Generic Data Collections

The library provides classes and interfaces that define generic collections, which allow users to create strongly typed collections. These collections provide greater convenience and data handling performance than non-generic typed collections.

The library is available in the Include\Generic folder of the terminal working directory.

Objects:

| Object | Description | Type |
| --- | --- | --- |
| [ICollection](ICollection-T/ICollection-T.md) | Interface for implementing generic data collections | INTERFACE |
| [IEqualityComparable](IEqualityComparable-T/IEqualityComparable-T.md) | Interface for implementing objects that can be compared | INTERFACE |
| [IComparable](IComparable-T/IComparable-T.md) | Interface for implementing objects that can be compared in terms of "greater than, less than or equal to" | INTERFACE |
| [IComparer](IComparer-T/IComparer-T.md) | Interface for implementing a generic class that compares two object of the T type, whether one is "greater than, less than or equal to" the other one | INTERFACE |
| [IEqualityComparer](IEqualityComparer-T/IEqualityComparer-T.md) | Interface for implementing a generic class that compares two object of the T type for equality | INTERFACE |
| [IList](IList-T/IList-T.md) | Interface for implementing generic data lists | INTERFACE |
| [IMap](IMap-TKey,TValue/IMap-TKey,TValue.md) | Interface for implementing generic collections of key/value pairs | INTERFACE |
| [ISet](ISet-T/ISet-T.md) | Interface for implementing generic data sets | INTERFACE |
| [CDefaultComparer](CDefaultComparer-T/CDefaultComparer-T.md) | A helper class that implements the IComparer<T> generic interface based on Compare global methods | CLASS |
| [CDefaultEqualityComparer](CDefaultEqualityComparer-T/CDefaultEqualityComparer-T.md) | A helper class that implements the IEqualityComparer<T> generic interface using Equals<T> and GetHashCode global methods | CLASS |
| [CArrayList](CArrayList-T/CArrayList-T.md) | A generic class that implements the IList<T> interface | CLASS |
| [CKeyValuePair](CKeyValuePair-TKey,TValue/CKeyValuePair-TKey,TValue.md) | The class implements the key/value pair | CLASS |
| [CHashMap](CHashMap-TKey,TValue/CHashMap-TKey,TValue.md) | A generic class that implements the IMap<TKey, TValue> interface | CLASS |
| [CHashSet](CHashSet-T/CHashSet-T.md) | A generic class that implements the ISet<T> interface | CLASS |
| [CLinkedListNode](CLinkedListNode-T/CLinkedListNode-T.md) | A helper class for implementing the CLinkedListNode<T> class | CLASS |
| [CLinkedList](CLinkedList-T/CLinkedList-T.md) | A generic class that implements the ICollection<T> interface | CLASS |
| [CQueue](CQueue-T/CQueue-T.md) | A generic class that implements the ICollection<T> interface | CLASS |
| [CRedBlackTreeNode](CRedBlackTreeNode-T/CRedBlackTreeNode-T.md) | A helper class used in implementing the CRedBlackTree<T> class | CLASS |
| [CRedBlackTree](CRedBlackTree-T/CRedBlackTree-T.md) | A generic class that implements the ICollection<T> interface | CLASS |
| [CSortedMap](CSortedMap-TKey,-TValue/CSortedMap-TKey,-TValue.md) | A generic class that implements the IMap<TKey, TValue> interface | CLASS |
| [CSortedSet](CSortedSet-T/CSortedSet-T.md) | A generic class that implements the ISet<T> interface | CLASS |
| [CStack](CStack-T/CStack-T.md) | A generic class that implements the ICollection<T> interface | CLASS |

Global methods:

| Method | Description |
| --- | --- |
| [ArrayBinarySearch](ArrayBinarySearch-T/ArrayBinarySearch-T.md) | Searches for the specified value in an ascending-sorted one-dimensional array using the IComparable<T> interface to compare elements |
| [ArrayIndexOf](ArrayIndexOf-T/ArrayIndexOf-T.md) | Searches for the first occurrence of a value in a one-dimensional array |
| [ArrayLastIndexOf](ArrayLastIndexOf-T/ArrayLastIndexOf-T.md) | Searches for the last occurrence of a value in a one-dimensional array |
| [ArrayReverse](ArrayReverse-T/ArrayReverse-T.md) | Changes the sequence of elements in a one-dimensional array |
| [Compare](Compare/Compare.md) | Compares two values, whether one of them is greater than, less than or equal to the other one |
| [Equals](Equals-T/Equals-T.md) | Compares two values ​​for equality |
| [GetHashCode](GetHashCode/GetHashCode.md) | Calculates the hash code value |
