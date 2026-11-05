# BufferWrite

BufferWrite

Writes an array of values into buffer at the specified index.

|  |
| --- |
| template<typename T>  bool  BufferWrite(     const int   buffer\_index,          // buffer index     T           &data[],               // array of values     const uint  cl\_buffer\_offset,      // offset in the OpenCL buffer, in bytes     const uint  data\_array\_offset,     // shift in the array elements     const uint  data\_array\_count       // number of values from the array to write     ); |

Parameters

buffer\_index

[in]  Index buffer.

&data[]

[in]  An array of values to be written into the OpenCL buffer.

cl\_buffer\_offset

[in]  Offset in the OpenCL buffer in bytes, from which to start writing values.

data\_array\_offset

[in]  Index of the first element of the array, starting from which the array values are written to the OpenCL buffer.

data\_array\_count

[in] The number of values to be written.

Return Value

In case of successful execution, returns true, otherwise - false.
