# IEqualityComparable<T>

IEqualityComparable<T>

IEqualityComparable<T> is an interface for implementing objects that can be compared.

Description

The IEqualityComparable<T> interface defines methods to retrieve the hash code of the current object and to check whether it is equal to another object of the same type.

Declaration

|  |
| --- |
| template<typename T>     interface IEqualityComparable |

Header

|  |
| --- |
| #include <Generic\Interfaces\IEqualityComparable.mqh> |

|  |
| --- |
| Inheritance Hierarchy    IEqualityComparable  Direct descendants  [IComparable](../IComparable-T/IComparable-T.md) |

Class Methods

| Method | Description |
| --- | --- |
| [Equals](Equals/Equals.md) | Compares the current object with the specified value |
| [HashCode](HashCode/HashCode.md) | Calculates the hash code value for the current object |
