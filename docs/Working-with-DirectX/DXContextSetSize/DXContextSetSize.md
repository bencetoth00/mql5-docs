# DXContextSetSize

DXContextSetSize

Changes a frame size of a graphic context created in DXContextCreate().

|  |
| --- |
| bool  DXContextSetSize(     int    context,      // graphic context handle        uint&  width,        // width in pixels        uint&  height        // height in pixels        ); |

Parameters

context

[in]  Handle for a graphic context created in [DXContextCreate()](../DXContextCreate/DXContextCreate.md).

width

[in]  Frame width in pixels.

height

[in]  Frame height in pixels.

Return Value

In case of successful execution, returns true, otherwise - false. To receive an [error](../../Constants,-Enumerations-and-Structures/Codes-of-Errors-and-Warnings/Runtime-Errors/Runtime-Errors.md) code, the [GetLastError()](../../Checkup/GetLastError/GetLastError.md) function should be called.

Note

A frame size of a graphic context should be changed only between frame renderings.
