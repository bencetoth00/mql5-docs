# DXShaderCreate

DXShaderCreate

Creates a shader of a specified type.

|  |
| --- |
| int  DXShaderCreate(     int                  context,           // graphic context handle        ENUM\_DX\_SHADER\_TYPE  shader\_type,       // shader type      const string         source,            // shader source code     const string         entry\_point,       // entry point     string&              compile\_error      // string for receiving compiler messages     ); |

Parameters

context

[in]  Handle for a graphic context created in [DXContextCreate()](../DXContextCreate/DXContextCreate.md).

shader\_type

[out]  The value from the [ENUM\_DX\_SHADER\_TYPE](DXShaderCreate.md#enum_dx_shader_type) enumeration.

source

[in]  Shader source code in [HLSL 5](https://en.wikipedia.org/wiki/High-Level_Shading_Language).

entry\_point

[in]  Entry point – function name in a source code.

compile\_error

[in]  String for receiving compilation errors.

Return Value

Handle for shader or INVALID\_HANDLE in case of an error. To receive an [error](../../Constants,-Enumerations-and-Structures/Codes-of-Errors-and-Warnings/Runtime-Errors/Runtime-Errors.md) code, the [GetLastError()](../../Checkup/GetLastError/GetLastError.md) function should be called.

Note

A created handle that is no longer in use should be explicitly released by the [DXRelease()](../DXRelease/DXRelease.md) function.

ENUM\_DX\_SHADER\_TYPE

| ID | Value | Description |
| --- | --- | --- |
| DX\_SHADER\_VERTEX | 0 | Vertex shader |
| DX\_SHADER\_GEOMETRY | 1 | Geometry shader |
| DX\_SHADER\_PIXEL | 2 | Pixel shader |
