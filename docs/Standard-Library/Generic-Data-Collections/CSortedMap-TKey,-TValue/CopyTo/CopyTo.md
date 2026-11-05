# CopyTo

CopyTo

Copies all key/value pairs from the sorted hash table to the specified arrays, starting at the specified index.

The version that copies a hash table to the array of key/value pairs.

|  |
| --- |
| int CopyTo(     CKeyValuePair<TKeyTValue>\*&  dst\_array[],     // an array for writing key/value pairs     const int                    dst\_start=0      // the starting index for writing     ); |

The version that copies a hash table to separate arrays for keys and values.

|  |
| --- |
| int CopyTo(     TKey&      dst\_keys[],                        // an array for writing keys     TValue&    dst\_values[],                      // an array for writing values     const int  dst\_start=0                        // the starting index for writing     ); |

Parameters

\*&dst\_array[]

[out] An array to which all pairs from the hash table will be written.

&dst\_keys[]

[out] An array to which all keys from the hash table will be written.

&dst\_values[]

[out] An array to which all values from the hash table will be written.

dst\_start=0

[in] An index in the array from which copying starts.

Return Value

Returns the number of copied key/value pairs.
