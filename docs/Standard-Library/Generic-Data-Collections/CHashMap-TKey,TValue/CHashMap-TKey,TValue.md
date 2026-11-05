# CHashMap<TKey,TValue>

CHashMap<TKey, TValue>

CHashMap<TKey, TValue> is a generic class that implements the IMap<TKey, TValue> interface.

Description

The CHashMap<TKey, TValue> class is an implementation of the dynamic hash table, the data of which are stored in the form of unordered key/value pairs taking into account the key uniqueness requirement. This class provides basic methods to work with a hash table, such as to access a value by key, to search and delete a key/value pair, and others.

Declaration

|  |
| --- |
| template<typename TKey, typename TValue>     class CHashMap : public IMap<TKey, TValue> |

Header

|  |
| --- |
| #include <Generic\HashMap.mqh> |

|  |
| --- |
| Inheritance Hierarchy    [ICollection](../ICollection-T/ICollection-T.md)        [IMap](../IMap-TKey,TValue/IMap-TKey,TValue.md)            CHashMap |

Class Methods

| Method | Description |
| --- | --- |
| [Add](Add/Add.md) | Adds a key/value pair to the hash table |
| [Count](Count/Count.md) | Returns the number of elements in the hash table |
| [Comparer](Comparer/Comparer.md) | Returns a pointer to the IEqualityComparer<T> interface, used to organize a hash table |
| [Contains](Contains/Contains.md) | Determines whether the hash table contains the specified key/value pair |
| [ContainsKey](ContainsKey/ContainsKey.md) | Determines whether the hash table contains the key/value pair with the specified key |
| [ContainsValue](ContainsValue/ContainsValue.md) | CHashMap<TKey, TValue> is a generic class that implements the IMap<TKey, TValue> interface |
| [CopyTo](CopyTo/CopyTo.md) | Copies all key/value pairs from the hash table to the specified arrays, starting at the specified index |
| [Clear](Clear/Clear.md) | Removes all elements from the hash table |
| [Remove](Remove/Remove.md) | Removes the first occurrence of the key/value pair from the hash table |
| [TryGetValue](TryGetValue/TryGetValue.md) | Gets an element with the specified key from the hash table |
| [TrySetValue](TrySetValue/TrySetValue.md) | Changes the value of a key/value pair from the hash table at the specified key |
