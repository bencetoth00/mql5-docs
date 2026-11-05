# Working with DirectX

Working with DirectX

DirectX 11 functions and shaders are designed for 3D visualization directly on a price chart.

Creating 3D graphics requires a graphic context ([DXContextCreate](DXContextCreate/DXContextCreate.md)) with the necessary image size. Besides, it is necessary to prepare vertex and index buffers ([DXBufferCreate](DXBufferCreate/DXBufferCreate.md)), as well as create vertex and pixel shaders ([DXShaderCreate](DXShaderCreate/DXShaderCreate.md)). This is enough to display graphics in color.

The next level of graphics requires the inputs ([DXInputSet](DXInputSet/DXInputSet.md)) for passing additional rendering parameters to shaders. This allows setting the camera and 3D object positions, describe light sources and implement mouse and keyboard control.

Thus, the built-in MQL5 functions enable you to create animated 3D charts directly in MetaTrader 5 with no need for third-party tools. A video card should support DX 11 and Shader Model 5.0 for the functions to work.

To start working with the library, simply read the article [How to create 3D graphics using DirectX in MetaTrader 5](https://www.mql5.com/en/articles/7708).

| Function | Action |
| --- | --- |
| [DXContextCreate](DXContextCreate/DXContextCreate.md) | Creates a graphic context for rendering frames of a specified size |
| [DXContextSetSize](DXContextSetSize/DXContextSetSize.md) | Changes a frame size of a graphic context created in DXContextCreate() |
| [DXContextSetSize](DXContextSetSize/DXContextSetSize.md) | Gets a frame size of a graphic context created in DXContextCreate() |
| [DXContextClearColors](DXContextClearColors/DXContextClearColors.md) | Sets a specified color to all pixels for the rendering buffer |
| [DXContextClearDepth](DXContextClearDepth/DXContextClearDepth.md) | Clears the depth buffer |
| [DXContextGetColors](DXContextGetColors/DXContextGetColors.md) | Gets an image of a specified size and offset from a graphic context |
| [DXContextGetDepth](DXContextGetDepth/DXContextGetDepth.md) | Gets the depth buffer of a rendered frame |
| [DXBufferCreate](DXBufferCreate/DXBufferCreate.md) | Creates a buffer of a specified type based on a data array |
| [DXTextureCreate](DXTextureCreate/DXTextureCreate.md) | Creates a 2D texture out of a rectangle of a specified size cut from a passed image |
| [DXInputCreate](DXInputCreate/DXInputCreate.md) | Creates shader inputs |
| [DXInputSet](DXInputSet/DXInputSet.md) | Sets shader inputs |
| [DXShaderCreate](DXShaderCreate/DXShaderCreate.md) | Creates a shader of a specified type |
| [DXShaderSetLayout](DXShaderSetLayout/DXShaderSetLayout.md) | Sets vertex layout for the vertex shader |
| [DXShaderInputsSet](DXShaderInputsSet/DXShaderInputsSet.md) | Sets shader inputs |
| [DXShaderTexturesSet](DXShaderTexturesSet/DXShaderTexturesSet.md) | Sets shader textures |
| [DXDraw](DXDraw/DXDraw.md) | Renders the vertices of the vertex buffer set in DXBufferSet() |
| [DXDrawIndexed](DXDrawIndexed/DXDrawIndexed.md) | Renders graphic primitives described by the index buffer from DXBufferSet() |
| [DXPrimiveTopologySet](DXPrimiveTopologySet/DXPrimiveTopologySet.md) | Sets the type of primitives for rendering using DXDrawIndexed() |
| [DXBufferSet](DXBufferSet/DXBufferSet.md) | Sets a buffer for the current rendering |
| [DXShaderSet](DXShaderSet/DXShaderSet.md) | Sets a shader for rendering |
| [DXHandleType](DXHandleType/DXHandleType.md) | Returns a handle type |
| [DXRelease](DXRelease/DXRelease.md) | Releases a handle |
