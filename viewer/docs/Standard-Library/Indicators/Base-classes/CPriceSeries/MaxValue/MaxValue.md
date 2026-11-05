# MaxValue


Gets the maximal value in the specified range.

```cpp
virtual double  MaxValue(
   const int   start,     // size
   const int   count,     // amount
   int&        index      // reference
   ) const
```

Parameters

start

[in]  Search range initial index.

count

[in]  Search range size (number of elements).

index

[out]  Reference to the variable for placing the found element's index value.

Return Value

The maximal value of a series buffer in the specified range, or [EMPTY\_VALUE](../../../../../Constants,-Enumerations-and-Structures/Named-Constants/Other-Constants/Other-Constants.md).

Note

The index of the found element is stored by index reference.