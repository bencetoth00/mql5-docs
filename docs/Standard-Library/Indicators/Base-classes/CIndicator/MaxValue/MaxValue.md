# MaxValue

MaxValue

Returns the value of maximal element of the specified buffer in a specified range.

|  |
| --- |
| double  MaxValue(     const int   buffer\_num,     // buffer number     const int   start,          // starting index     const int   count,          // number     int&        index           // reference     ) const |

Parameters

buffer\_num

[in]  Buffer number to search the value in.

start

[in]  Search range initial index.

count

[in]  Search range size (number of elements).

index

[out]  Reference to the variable for storing the found element index value.

Return Value

The value of the maximal element of the specified buffer in a specified range.

Note

The index of maximal buffer element is stored by index reference.
