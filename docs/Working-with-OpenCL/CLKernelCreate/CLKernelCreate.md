# CLKernelCreate

CLKernelCreate

Creates the OpenCL program kernel and returns its handle.

|  |
| --- |
| int  CLKernelCreate(     int           program,        // Handle to an OpenCL object     const string  kernel\_name     // Kernel name     ); |

Parameters

program

[in]  Handle to an object of the OpenCL program.

kernel\_name

[in]  The name of the kernel function in the appropriate OpenCL program, in which execution begins.

Return Value

A handle to an OpenCL object if successful. In case of error -1 is returned. For information about the error, use the [GetLastError()](../../Checkup/GetLastError/GetLastError.md) function.

Note

At the moment, the following error codes are used:

- ERR\_OPENCL\_INVALID\_HANDLE - invalid handle to OpenCL program.
- ERR\_INVALID\_PARAMETER - invalid string parameter.
- ERR\_OPENCL\_TOO\_LONG\_KERNEL\_NAME - kernel name contains more than 127 characters.
- ERR\_OPENCL\_KERNEL\_CREATE - internal error occurred while creating an OpenCL object.
