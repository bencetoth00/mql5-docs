# BufferFromArray

BufferFromArray

Creates a buffer at the specified index from an array of values.

|  |
| --- |
| template<typename T>  bool  BufferFromArray(     const int   buffer\_index,          // buffer index     T           &data[],               // array of values     const uint  data\_array\_offset,     // offset in the array of values, in bytes     const uint  data\_array\_count,      // number of values from the array to write     const uint  flags                  // combination of flags that define the buffer properties     ); |

Parameters

buffer\_index

[in]  Index buffer.

&data[]

[in]  An array of values to be written into the OpenCL buffer.

data\_array\_offset

[in]  Offset in the array of values in bytes, from which writing of values begins.

data\_array\_count

[in] The number of values to be written.

flags

[in]  Buffer properties that are set using a combination of flags.

Return Value

In case of successful execution, returns true, otherwise - false.
