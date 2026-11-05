# CLSetKernelArgMem


Sets an OpenCL buffer as a parameter of the OpenCL function.

```cpp
bool  CLSetKernelArgMem(
   int   kernel,           // Handle to the kernel of an OpenCL program
   uint  arg_index,        // The number of the argument of the OpenCL function
   int   cl_mem_handle     // Handle to OpenCL buffer
   );
```

Parameters

kernel

[in]  Handle to a kernel of the OpenCL program.

arg\_index

[in]  The number of the function argument, numbering starts with zero.

cl\_mem\_handle

[in]  A handle to an OpenCL buffer.

Return Value

Returns true if successful, otherwise returns false. For information about the error, use the [GetLastError()](../../Checkup/GetLastError/GetLastError.md) function.