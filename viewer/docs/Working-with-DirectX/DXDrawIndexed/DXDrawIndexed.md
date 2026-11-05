# DXDrawIndexed


Renders graphic primitives described by the index buffer from [DXBufferSet()](../DXBufferSet/DXBufferSet.md).

```cpp
bool  DXDrawIndexed(
   int   context,               // graphic context handle
   uint  start=0,               // first primitive index
   uint  count=WHOLE_ARRAY      // number of primitives
   );
```

Parameters

context

[in]  Handle for a graphic context created in [DXContextCreate()](../DXContextCreate/DXContextCreate.md).

start=0

[in]  Index of the first primitive for rendering.

count=WHOLE\_ARRAY

[in]  Number of primitives for rendering.

Return Value

In case of successful execution, returns true, otherwise - false. To receive an [error](../../Constants,-Enumerations-and-Structures/Codes-of-Errors-and-Warnings/Runtime-Errors/Runtime-Errors.md) code, the [GetLastError()](../../Checkup/GetLastError/GetLastError.md) function should be called.

Note

The type of primitives described by the index buffer is set using [DXPrimiveTopologySet()](../DXPrimiveTopologySet/DXPrimiveTopologySet.md).

The vertex buffer in [DXBufferSet()](../DXBufferSet/DXBufferSet.md) should be preliminarily set to render primitives.

Also, shaders should be preliminarily set using [DXShaderSet()](../DXShaderSet/DXShaderSet.md).