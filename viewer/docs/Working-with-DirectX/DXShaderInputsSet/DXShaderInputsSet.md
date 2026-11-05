# DXShaderInputsSet


Sets shader inputs.

```cpp
bool  DXShaderInputsSet(
   int         shader,       // shader handle
   const int&  inputs[]      // array of input handles
   );
```

Parameters

shader

[in]  Handle of a shader created in [DXShaderCreate()](../DXShaderCreate/DXShaderCreate.md).

inputs[]

[in]  Array of input handles created using [DXInputCreate()](../DXInputCreate/DXInputCreate.md).

Return Value

In case of successful execution, returns true, otherwise - false. To receive an [error](../../Constants,-Enumerations-and-Structures/Codes-of-Errors-and-Warnings/Runtime-Errors/Runtime-Errors.md) code, the [GetLastError()](../../Checkup/GetLastError/GetLastError.md) function should be called.

Note

The size of the input parameter should be equal to the number of [cbuffer](https://docs.microsoft.com/en-us/windows/win32/direct3dhlsl/dx-graphics-hlsl-constants) objects declared in the shader code.