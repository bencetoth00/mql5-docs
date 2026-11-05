# CLContextFree

CLContextFree

Removes an OpenCL context.

|  |
| --- |
| void  CLContextFree(     int  context     // Handle to an OpenCL context     ); |

Parameters

context

[in]  Handle of the OpenCL context.

Return Value

None. In the case of an internal error the value of [\_LastError](../../Predefined-Variables/_LastError/_LastError.md) changes. For information about the error, use the [GetLastError()](../../Checkup/GetLastError/GetLastError.md) function.
