# CLProgramFree

CLProgramFree

Removes an OpenCL program.

|  |
| --- |
| void  CLProgramFree(     int  program     // Handle to an OpenCL object     ); |

Parameters

program

[in]  Handle of the OpenCL object.

Return Value

None. In the case of an internal error the value of [\_LastError](../../Predefined-Variables/_LastError/_LastError.md) changes. For information about the error, use the [GetLastError()](../../Checkup/GetLastError/GetLastError.md) function.
