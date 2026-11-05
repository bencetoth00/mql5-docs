# ReadShortArray

ReadShortArray

Reads an array of short or ushort type variables from file.

|  |
| --- |
| bool  ReadShortArray(     short&  array[],            // array     int     start\_item=0,       // start element     int     items\_count=-1      // number of elements     ) |

Parameters

array[]

[in]  Reference to the variable for placing read data.

start\_item=0

[in]  Start element to read from.

items\_count=-1

[in]  Number of elements to read (-1 - read to the end of file).

Return Value

true - successful, false - cannot read the data.
