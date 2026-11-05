# DXContextClearDepth

DXContextClearDepth

Clears the depth buffer.

|  |
| --- |
| bool  DXContextClearDepth(     int  context      // graphic context handle      ); |

Parameters

context

[in]  Handle for a graphic context created in [DXContextCreate()](../DXContextCreate/DXContextCreate.md).

Return Value

In case of successful execution, returns true, otherwise - false. To receive an [error](../../Constants,-Enumerations-and-Structures/Codes-of-Errors-and-Warnings/Runtime-Errors/Runtime-Errors.md) code, the [GetLastError()](../../Checkup/GetLastError/GetLastError.md) function should be called.

Note

The DXContextClearDepth() function can be used for clearing the depth buffer before rendering the next frame.
