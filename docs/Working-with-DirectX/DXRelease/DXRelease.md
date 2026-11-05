# DXRelease

DXRelease

Releases a handle.

|  |
| --- |
| bool  DXRelease(     int  handle      // handle      ); |

Parameters

context

[in]  Released handle.

Return Value

In case of successful execution, returns true, otherwise - false. To receive an [error](../../Constants,-Enumerations-and-Structures/Codes-of-Errors-and-Warnings/Runtime-Errors/Runtime-Errors.md) code, the [GetLastError()](../../Checkup/GetLastError/GetLastError.md) function should be called.

Note

All created handles that are no longer in use should be explicitly released by the DXRelease() function.
