# ReadDoubleArray

ReadDoubleArray

Reads an array of double type variables from file.

|  |
| --- |
| bool  ReadDoubleArray(     double&  array[],            // array     int      start\_item=0,       // start element     int      items\_count=-1      // number of elements     ) |

Parameters

array[]

[in]  Reference to the variable for placing read data.

start\_item=0

[in]  Start element to read from.

items\_count=-1

[in]  Number of elements to read (-1 - read to the end of file).

Return Value

true - successful, false - cannot read the data.
