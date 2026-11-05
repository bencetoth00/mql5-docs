# CKeyValuePair<TKey,TValue>


The CKeyValuePair<TKey,TValue> class implements a key/value pair.

### Description

The CKeyValuePair<TKey,TValue> class implements methods for working with the key and the value of the key/value pair.

### Declaration

```cpp
   template<typename TKey, typename TValue>
   class CKeyValuePair : public IComparable<CKeyValuePair<TKey,TValue>*>
```

### Header

```cpp
   #include <Generic\HashMap.mqh>
```

|  |
| --- |
| Inheritance Hierarchy    [IEqualityComparable](../IEqualityComparable-T/IEqualityComparable-T.md)        [IComparable](../IComparable-T/IComparable-T.md)            CKeyValuePair |

### Class Methods

| Method | Description |
| --- | --- |
| [Key](Key/Key.md) | Gets and sets the key in the key/value pair |
| [Value](Value/Value.md) | Gets and sets the value in the key/value pair |
| [Clone](Clone/Clone.md) | Creates a new key/value pair whose key and value are equal to the current ones |
| [Compare](Compare/Compare.md) | Compares the current key/value pair to the specified one |
| [Equals](Equals/Equals.md) | Checks whether the current key/value pair and the specified one are equal |
| [HashCode](HashCode/HashCode.md) | Calculates the hash value based on the key/value pair |