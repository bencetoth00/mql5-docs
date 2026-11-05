# CLKernelFree


Removes an OpenCL start function.

```cpp
void  CLKernelFree(
   int  kernel     // Handle to the kernel of an OpenCL program
   );
```

Parameters

kernel\_name

[in]  Handle of the kernel object.

Return Value

None. In the case of an internal error the value of [\_LastError](../../Predefined-Variables/_LastError/_LastError.md) changes. For information about the error, use the [GetLastError()](../../Checkup/GetLastError/GetLastError.md) function.