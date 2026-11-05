# DXShaderSet

DXShaderSet

Sets a shader for rendering.

|  |
| --- |
| bool  DXShaderSet(     int  context,      // graphic context handle     int  shader        // shader handle     ); |

Parameters

context

[in]  Handle for a graphic context created in [DXContextCreate()](../DXContextCreate/DXContextCreate.md).

shader

[in]  Handle of a shader created in [DXShaderCreate()](../DXShaderCreate/DXShaderCreate.md).

Return Value

In case of successful execution, returns true, otherwise - false. To receive an [error](../../Constants,-Enumerations-and-Structures/Codes-of-Errors-and-Warnings/Runtime-Errors/Runtime-Errors.md) code, the [GetLastError()](../../Checkup/GetLastError/GetLastError.md) function should be called.

Note

Several types of shaders can simultaneously be used for rendering (vertex, geometry and pixel ones).
