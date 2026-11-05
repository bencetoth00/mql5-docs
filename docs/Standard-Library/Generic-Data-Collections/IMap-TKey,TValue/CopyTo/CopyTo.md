# CopyTo

CopyTo

Copies all key/value pairs from a collection to the specified arrays, starting at the specified index.

|  |
| --- |
| int CopyTo(     TKey&      dst\_keys[],       // an array for writing keys     TValue&    dst\_values[],     // an array for writing values     const int  dst\_start=0       // the starting index for writing     ); |

Parameters

&dst\_keys[]

[out] An array to which all keys from the collection will be written.

&dst\_values[]

[out] An array to which values of corresponding keys from the collection will be written.

dst\_start=0

[in] An index in the array from which copying starts.

Return Value

Returns the number of copied key/value pairs.
