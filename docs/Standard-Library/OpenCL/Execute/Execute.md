# Execute

Execute

Executes the OpenCL program at the specified index.

|  |
| --- |
| bool  Execute(     const int   kernel\_index,           // index of the kernel     const int   work\_dim,               // dimension of the tasks space     const uint  &work\_offset[],         // initial offset in the tasks space     const uint  &work\_size[]            // total number of tasks     ); |

Executes the OpenCL kernel with the specified index and number of tasks in the local group.

|  |
| --- |
| bool  Execute(     const int   kernel\_index,           // index of the kernel     const int   work\_dim,               // dimension of the tasks space     const uint  &work\_offset[],         // initial offset in the tasks space     const uint  &work\_size[],           // total number of tasks     const uint  &local\_work\_size[]      // number of tasks in the local group     ); |

Parameters

kernel\_index

[in]  Index of the kernel object.

work\_dim

[in]  Dimension of the tasks space.

&work\_offset[]

[in][out]  Initial offset in the tasks space. Passed by reference.

&work\_size[]

[in][out]  The size of the tasks subset. Passed by reference.

&local\_work\_size[]

[in][out]  The size of the local tasks subset in the group. Passed by reference.

Return Value

In case of successful execution, returns true, otherwise - false.
