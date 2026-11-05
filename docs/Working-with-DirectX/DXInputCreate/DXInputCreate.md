# DXInputCreate

DXInputCreate

Creates shader inputs.

|  |
| --- |
| int  DXInputCreate(     int   context,        // graphic context handle     uint  input\_size      // size of inputs in bytes      ); |

Parameters

context

[in]  Handle for a graphic context created in [DXContextCreate()](../DXContextCreate/DXContextCreate.md).

input\_size

[in]  Size of the parameter structure in bytes.

Return Value

The handle for shader inputs or INVALID\_HANDLE in case of an error. To receive an [error](../../Constants,-Enumerations-and-Structures/Codes-of-Errors-and-Warnings/Runtime-Errors/Runtime-Errors.md) code, the [GetLastError()](../../Checkup/GetLastError/GetLastError.md) function should be called.

A created handle that is no longer in use should be explicitly released by the [DXRelease()](../DXRelease/DXRelease.md) function.
