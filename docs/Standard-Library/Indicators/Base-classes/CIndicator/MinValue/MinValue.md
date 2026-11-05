# MinValue

MinValue

Returns the value of minimal element of the specified buffer in a specified range.

|  |
| --- |
| double  MinValue(     const int   buffer\_num,     // buffer number     const int   start,          // starting index     const int   count,          // number     int&        index           // reference     ) const |

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

The value of the minimal element of the specified buffer in a specified range.

Note

The index of the found element is stored by index reference.
