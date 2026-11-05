# DXDraw

DXDraw

Renders the vertices of the vertex buffer set in [DXBufferSet()](../DXBufferSet/DXBufferSet.md).

|  |
| --- |
| bool  DXDraw(     int   context,               // graphic context handle      uint  start=0,               // first vertex index     uint  count=WHOLE\_ARRAY      // number of vertices     ); |

Parameters

context

[in]  Handle for a graphic context created in [DXContextCreate()](../DXContextCreate/DXContextCreate.md).

start=0

[in]  Index of the first vertex for rendering.

count=WHOLE\_ARRAY

[in]  Number of vertices to render.

Return Value

In case of successful execution, returns true, otherwise - false. To receive an [error](../../Constants,-Enumerations-and-Structures/Codes-of-Errors-and-Warnings/Runtime-Errors/Runtime-Errors.md) code, the [GetLastError()](../../Checkup/GetLastError/GetLastError.md) function should be called.

Note

Shaders should be preliminarily set using [DXShaderSet()](../DXShaderSet/DXShaderSet.md) for rendering vertices.
