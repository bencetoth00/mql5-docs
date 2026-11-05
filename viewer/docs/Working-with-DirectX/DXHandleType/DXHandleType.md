# DXHandleType


Returns a handle type.

```cpp
ENUM_DX_HANDLE_TYPE  DXHandleType(
   int  handle      // handle
   );
```

Parameters

handle

[in]     Handle.

Return Value

The value from the [ENUM\_DX\_HANDLE\_TYPE](DXHandleType.md#enum_dx_handle_type) enumeration

 

ENUM\_DX\_HANDLE\_TYPE

| ID | Value | Description |
| --- | --- | --- |
| DX\_HANDLE\_INVALID | 0 | Invalid handle |
| DX\_HANDLE\_CONTEXT | 1 | Graphic context handle |
| DX\_HANDLE\_SHADER | 2 | Shader handle |
| DX\_HANDLE\_BUFFER | 3 | Vertex or index buffer handle |
| DX\_HANDLE\_INPUT | 4 | Handle for shader inputs |
| DX\_HANDLE\_TEXTURE | 5 | Texture handle |