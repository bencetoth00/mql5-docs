# CLExecute

CLExecute

The function runs an OpenCL program. There are 3 versions of the function:

1. Launching kernel functions using one kernel

|  |
| --- |
| bool  CLExecute(     int          kernel                    // Handle to the kernel of an OpenCL program     ); |

2. Launching several kernel copies (OpenCL function) with task space description

|  |
| --- |
| bool  CLExecute(     int          kernel,                   // Handle to the kernel of an OpenCL program     uint         work\_dim,                 // Dimension of the tasks space     const uint&  global\_work\_offset[],     // Initial offset in the tasks space     const uint&  global\_work\_size[]        // Total number of tasks     ); |

3. Launching several kernel copies (OpenCL function) with task space description and specification of the size of the group's local task subset

|  |
| --- |
| bool  CLExecute(     int          kernel,                   // Handle to the kernel of an OpenCL program     uint         work\_dim,                 // Dimension of the tasks space     const uint&  global\_work\_offset[],     // Initial offset in the tasks space     const uint&  global\_work\_size[],       // Total number of tasks     const uint&  local\_work\_size[]         // Number of tasks in the local group     ); |

Parameters

kernel

[in]  Handle to the OpenCL kernel.

work\_dim

[in]  Dimension of the tasks space.

global\_work\_offset[]

[in]  Initial offset in the tasks space.

global\_work\_size[]

[in]  The size of a subset of tasks.

local\_work\_size[]

[in]  The size of the group's local task subset.

Return Value

Returns true if successful, otherwise returns false. For information about the error, use the [GetLastError()](../../Checkup/GetLastError/GetLastError.md) function.

Note

Consider the use of the parameters in the following example:

- work\_dim specifies the size of work\_items[] array that describes the tasks. If work\_dim=3, three-dimensional array work\_items[N1, N2, N3] is used.
- global\_work\_size[] contains the values that set the work\_items[] array size. If work\_dim=3, global\_work\_size[3] array can be {40, 100, 320}. Then we have work\_items[40, 100, 320]. So, the total number of tasks is 40 x 100 x 320 = 1 280 000.
- local\_work\_size[] sets the subset of the tasks that will be executed by the specified kernel of OpenCL program. Its size is equal to work\_items[] size and allows to split the common task subset into smaller subsets without loss of remainder in division. In fact, the size of local\_work\_size[] array should be selected so that the work\_items[] global task set will be split into smaller subsets. In this example local\_work\_size[3]={10, 10, 10} will be OK, as work\_items[40, 100, 320] can be gathered from local\_items[10, 10, 10] array without division remainder.
