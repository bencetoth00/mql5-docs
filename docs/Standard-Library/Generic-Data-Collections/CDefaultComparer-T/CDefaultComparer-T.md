# CDefaultComparer<T>

CDefaultComparer<T>

CDefaultComparer<T> is a helper class that implements the IComparer<T> generic interface based on Compare global methods.

Description

The CDefaultComparer<T> class is used by default in generic data collections, unless the user implicitly uses another class implementing the IComparer<T> interface.

Declaration

|  |
| --- |
| template<typename T>     class CDefaultComparer : public IComparer<T> |

Header

|  |
| --- |
| #include <Generic\Internal\DefaultComparer.mqh> |

|  |
| --- |
| Inheritance Hierarchy    [IComparer](../IComparer-T/IComparer-T.md)        CDefaultComparer |

Class Methods

| Method | Description |
| --- | --- |
| [Compare](Compare/Compare.md) | Compares two values of type T |
