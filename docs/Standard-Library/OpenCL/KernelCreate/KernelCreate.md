# KernelCreate

KernelCreate

Creates an entry point into the OpenCL program at the specified index.

|  |
| --- |
| bool  KernelCreate(     const int     kernel\_index,     // index of the kernel     const string  kernel\_name       // name of the kernel     ); |

Parameters

kernel\_index

[in]  Index of the kernel object.

kernel\_name

[in]  Name of the kernel object.

Return Value

In case of successful execution, returns true, otherwise - false.
