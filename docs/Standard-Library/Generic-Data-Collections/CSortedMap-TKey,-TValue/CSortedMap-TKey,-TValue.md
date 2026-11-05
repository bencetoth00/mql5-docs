# CSortedMap<TKey, TValue>

CSortedMap<TKey,TValue>

CSortedMap<TKey,TValue> is a generic class that implements the IMap<TKey,TValue> interface.

Description

The CSortedMap<TKey,TValue> class is an implementation of a dynamic hash table whose data are stored as key/value pairs sorted by key and taking into account the key uniqueness requirement. This class provides basic methods to work with a hash table, such as to access a value by key, to search and delete a key/value pair, and others.

Declaration

|  |
| --- |
| template<typename TKey, typename TValue>     class CSortedMap : public IMap<TKey, TValue> |

Header

|  |
| --- |
| #include <Generic\SortedMap.mqh> |

|  |
| --- |
| Inheritance Hierarchy    [ICollection](../ICollection-T/ICollection-T.md)        [IMap](../IMap-TKey,TValue/IMap-TKey,TValue.md)            CSortedMap |

Class Methods

| Method | Description |
| --- | --- |
| [Add](Add/Add.md) | Adds a key/value pair to the hash table |
| [Count](Count/Count.md) | Returns the number of elements in the sorted hash table |
| [Contains](Contains/Contains.md) | Determines whether the sorted hash table contains the specified key/value table |
| [ContainsKey](ContainsKey/ContainsKey.md) | Determines whether the sorted hash table contains the key/value table with the specified key |
| [ContainsValue](ContainsValue/ContainsValue.md) | Determines whether the sorted hash table contains the key/value table with the specified value |
| [Comparer](Comparer/Comparer.md) | Returns a pointer to the IComparer<T> interface, used to organize a sorted hash table |
| [CopyTo](CopyTo/CopyTo.md) | Copies all key/value pairs from the sorted hash table to the specified arrays, starting at the specified index |
| [Clear](Clear/Clear.md) | Removes all elements from the sorted hash table |
| [Remove](Remove/Remove.md) | Removes the first occurrence of the key/value pair from the sorted hash table |
| [TryGetValue](TryGetValue/TryGetValue.md) | Gets an element with the specified key from the sorted hash table |
| [TrySetValue](TrySetValue/TrySetValue.md) | Changes a key/value pair with the specified key from the sorted hash table |
