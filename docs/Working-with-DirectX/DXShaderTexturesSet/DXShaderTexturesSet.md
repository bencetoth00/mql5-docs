# DXShaderTexturesSet

DXShaderTexturesSet

Sets shader textures.

|  |
| --- |
| bool  DXShaderTexturesSet(     int          shader,         // shader handle     const  int&  textures[]      // array of structure handles     ); |

Parameters

shader

[in]  Handle of a shader created in [DXShaderCreate()](../DXShaderCreate/DXShaderCreate.md).

textures[]

[in]  Array of texture handles created using [DXTextureCreate()](../DXTextureCreate/DXTextureCreate.md).

Return Value

In case of successful execution, returns true, otherwise - false. To receive an [error](../../Constants,-Enumerations-and-Structures/Codes-of-Errors-and-Warnings/Runtime-Errors/Runtime-Errors.md) code, the [GetLastError()](../../Checkup/GetLastError/GetLastError.md) function should be called.

Note

The size of the texture array should be equal to the number of [Texture2D](https://docs.microsoft.com/en-us/windows/win32/direct3dhlsl/dx-graphics-hlsl-to-type) objects declared in the shader code.
