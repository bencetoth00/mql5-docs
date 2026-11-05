# SetArgumentBuffer

SetArgumentBuffer

Sets an OpenCL buffer as a parameter of the OpenCL function at the specified index.

|  |
| --- |
| bool  SetArgumentBuffer(     const int  kernel\_index,     // index of the kernel     const int  arg\_index,        // index of the function argument     const int  buffer\_index      // buffer index     ); |

Parameters

kernel\_index

[in]  Index of the kernel object.

arg\_index

[in]  Index of the function argument.

buffer\_index

[in]  Index buffer.

Return Value

In case of successful execution, returns true, otherwise - false.
