# IMap<TKey,TValue>

# IMap<TKey, TValue>

IMap<TKey, TValue> is an interface for implementing generic collections of key/value pairs.

### Description

The IMap<TKey, TValue> interface defines basic methods to work with collections whose data are stored as key/value pairs.

### Declaration

```cpp
   template<typename TKey, typename TValue>
   interface IMap : public ICollection<TKey>
```

### Header

```cpp
   #include <Generic\Interfaces\IMap.mqh>
```

|  |
| --- |
| Inheritance Hierarchy    [ICollection](../ICollection-T/ICollection-T.md)        IMap  Direct descendants  [CHashMap](../CHashMap-TKey,TValue/CHashMap-TKey,TValue.md), [CSortedMap](../CSortedMap-TKey,-TValue/CSortedMap-TKey,-TValue.md) |

### Class Methods

| Method | Description |
| --- | --- |
| [Add](Add/Add.md) | Adds a key/value pair to a collection |
| [Contains](Contains/Contains.md) | Determines whether a collection contains the key/value table with the specified key |
| [Remove](Remove/Remove.md) | Removes the first occurrence of a key/value pair from a collection |
| [TryGetValue](TryGetValue/TryGetValue.md) | Gets an element with the specified key from a collection |
| [TrySetValue](TrySetValue/TrySetValue.md) | Changes the value of the key/value pair from a collection at the specified key |
| [CopyTo](CopyTo/CopyTo.md) | Copies all key/value pairs from a collection to specified arrays, starting at the specified index |