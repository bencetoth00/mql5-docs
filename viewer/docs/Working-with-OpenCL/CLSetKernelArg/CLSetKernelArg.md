# CLSetKernelArg


Sets a parameter for the OpenCL function.

```cpp
bool  CLSetKernelArg(
   int   kernel,        // Handle to the kernel of an OpenCL program
   uint  arg_index,     // The number of the argument of the OpenCL function
   void  arg_value      // Source code
   );
```

Parameters

kernel

[in]  Handle to a kernel of the OpenCL program.

arg\_index

[in]  The number of the function argument, numbering starts with zero.

arg\_value

[in]  The value of the function argument.

Return Value

Returns true if successful, otherwise returns false. For information about the error, use the [GetLastError()](../../Checkup/GetLastError/GetLastError.md) function.

Note

At the moment, the following error codes are used:

- ERR\_INVALID\_PARAMETER,
- ERR\_OPENCL\_INVALID\_HANDLE – invalid handle to the OpenCL kernel.
- ERR\_OPENCL\_SET\_KERNEL\_PARAMETER - internal error of OpenCL.