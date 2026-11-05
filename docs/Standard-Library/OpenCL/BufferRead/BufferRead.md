# BufferRead

BufferRead

Reads an OpenCL buffer at the specified index into an array.

|  |
| --- |
| template<typename T>  bool  BufferRead(     const int   buffer\_index,          // buffer index     T           &data[],               // array of values     const uint  cl\_buffer\_offset,      // offset in the OpenCL buffer, in bytes     const uint  data\_array\_offset,     // shift in the array elements     const uint  data\_array\_count       // number of values from the buffer to read     ); |

Parameters

buffer\_index

[in]  Index buffer.

&data[]

[in]  Array to obtain the values of the OpenCL buffer.

cl\_buffer\_offset

[in]  Offset in the OpenCL buffer in bytes, from which to start reading values.

data\_array\_offset

[in]  Index of the first element of the array to write values of the OpenCL buffer.

data\_array\_count

[in]  The number of values to be read.

Return Value

In case of successful execution, returns true, otherwise - false.
