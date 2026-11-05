# DXShaderSetLayout

DXShaderSetLayout

Sets vertex layout for the vertex shader.

|  |
| --- |
| bool  DXShaderSetLayout(     int                    shader,       // shader handle     const DXVertexLayout&  layout[]      //      ); |

Parameters

shader

[in]  Handle of a vertex shader created in [DXShaderCreate()](../DXShaderCreate/DXShaderCreate.md).

layout[]

[in]  Array of vertex fields description. The description is set by the DXVertexLayout structure:

|  |
| --- |
| struct DXVertexLayout    {     string         semantic\_name;       // The HLSL semantic associated with this element in a shader input-signature.     uint           semantic\_index;      // The semantic index for the element. A semantic index modifies a semantic, with an integer index number. A semantic index is only needed in a case where there is more than one element with the same semantic     ENUM\_DX\_FORMAT format;              // The data type of the element data.    }; |

Return Value

In case of successful execution, returns true, otherwise - false. To receive an [error](../../Constants,-Enumerations-and-Structures/Codes-of-Errors-and-Warnings/Runtime-Errors/Runtime-Errors.md) code, the [GetLastError()](../../Checkup/GetLastError/GetLastError.md) function should be called.

Note

The layout should match the type of vertices in a specified vertex buffer. It should also match the input type of vertices used at the entry point in the vertex shader code.

The vertex buffer for a shader is set in [DXBufferSet()](../DXBufferSet/DXBufferSet.md).

The DXVertexLayout structure is a version of the [D3D11\_INPUT\_ELEMENT\_DESC](https://docs.microsoft.com/en-us/windows/win32/api/d3d11/ns-d3d11-d3d11_input_element_desc) MSDN structure.
