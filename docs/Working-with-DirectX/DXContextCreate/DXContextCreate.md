# DXContextCreate

DXContextCreate

Creates a graphic context for rendering frames of a specified size.

|  |
| --- |
| int  DXContextCreate(     uint  width,      // width in pixels     uint  height      // height in pixels     ); |

Parameters

width

[in]  Frame width in pixels.

height

[in]  Frame height in pixels.

Return Value

A handle for a created context or INVALID\_HANDLE in case of an error. To receive an [error](../../Constants,-Enumerations-and-Structures/Codes-of-Errors-and-Warnings/Runtime-Errors/Runtime-Errors.md) code, the [GetLastError()](../../Checkup/GetLastError/GetLastError.md) function should be called.

Note

All graphical objects created using the [DXBufferCreate](../DXBufferCreate/DXBufferCreate.md), [DXInputCreate](../DXInputCreate/DXInputCreate.md), [DXShaderCreate](../DXShaderCreate/DXShaderCreate.md) and [DXTextureCreate](../DXTextureCreate/DXTextureCreate.md) functions can be used only in a graphic context they were created in.

A frame size can subsequently be changed to [DXContextSetSize()](../DXContextSetSize/DXContextSetSize.md).

A created handle that is no longer in use should be explicitly released by the [DXRelease()](../DXRelease/DXRelease.md) function.
