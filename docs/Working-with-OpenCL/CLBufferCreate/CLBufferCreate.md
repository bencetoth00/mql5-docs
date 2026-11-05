# CLBufferCreate

CLBufferCreate

Creates an OpenCL buffer and returns its handle.

|  |
| --- |
| int  CLBufferCreate(     int   context,     // Handle to an OpenCL context     uint  size,        // Buffer size     uint  flags        // Flags combination which specify properties of OpenCL buffer      ); |

Parameters

context

[in]  A handle to context OpenCL.

size

[in]  Buffer size in bytes.

flags

[in]  Buffer properties that are set using a combination of flags: CL\_MEM\_READ\_WRITE, CL\_MEM\_WRITE\_ONLY, CL\_MEM\_READ\_ONLY, CL\_MEM\_ALLOC\_HOST\_PTR.

Return Value

A handle to an OpenCL buffer if successful. In case of error -1 is returned. For information about the error, use the [GetLastError()](../../Checkup/GetLastError/GetLastError.md) function.

Note

At the moment, the following error codes are used:

- ERR\_OPENCL\_INVALID\_HANDLE  - invalid handle to OpenCL context.
- ERR\_NOT\_ENOUGH\_MEMORY – insufficient memory.
- ERR\_OPENCL\_BUFFER\_CREATE – internal error creating buffers.
