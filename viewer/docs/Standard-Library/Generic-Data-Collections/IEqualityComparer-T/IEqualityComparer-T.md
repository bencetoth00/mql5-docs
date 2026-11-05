# IEqualityComparer<T>


IEqualityComparer<T> is an interface for implementing a generic class that compares two object of the T type.

### Description

The IEqualityComparer<T> interface defines methods to retrieve the hash code of a T type object and to check whether two objects of type T are equal.

### Declaration

```cpp
   template<typename T>
   interface IEqualityComparer
```

### Header

```cpp
   #include <Generic\Interfaces\IEqualityComparer.mqh>
```

|  |
| --- |
| Inheritance Hierarchy    IEqualityComparer  Direct descendants  [CDefaultEqualityComparer](../CDefaultEqualityComparer-T/CDefaultEqualityComparer-T.md) |

### Class Methods

| Method | Description |
| --- | --- |
| [Equals](Equals/Equals.md) | Compares two values of type T |
| [HashCode](HashCode/HashCode.md) | Calculates the hash code value based on the T type object |