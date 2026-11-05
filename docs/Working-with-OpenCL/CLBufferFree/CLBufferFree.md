# CLBufferFree

CLBufferFree

Deletes an OpenCL buffer.

|  |
| --- |
| void  CLBufferFree(     int   buffer     // Handle to an OpenCL buffer     ); |

Parameters

buffer

[in]  A handle to an OpenCL buffer.

Return Value

None. In the case of an internal error the value of [\_LastError](../../Predefined-Variables/_LastError/_LastError.md) changes. For information about the error, use the [GetLastError()](../../Checkup/GetLastError/GetLastError.md) function.
