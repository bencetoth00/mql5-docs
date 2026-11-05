# KernelCreate


Creates an entry point into the OpenCL program at the specified index.

```cpp
bool  KernelCreate(
   const int     kernel_index,     // index of the kernel
   const string  kernel_name       // name of the kernel
   );
```

Parameters

kernel\_index

[in]  Index of the kernel object.

kernel\_name

[in]  Name of the kernel object.

Return Value

In case of successful execution, returns true, otherwise - false.