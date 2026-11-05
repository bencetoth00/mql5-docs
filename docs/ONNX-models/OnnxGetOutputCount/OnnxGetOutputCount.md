# OnnxGetOutputCount

OnnxGetOutputCount

Get the number of outputs in an ONNX model.

|  |
| --- |
| long  OnnxGetOutputCount(     long   onnx\_handle  // ONNX session handle     ); |

Parameters

onnx\_handle

[in]  ONNX session object handle created via [OnnxCreate](../OnnxCreate/OnnxCreate.md) or [OnnxCreateFromBuffer](../OnnxCreateFromBuffer/OnnxCreateFromBuffer.md).

Return Value

Returns the number of output parameters on success; otherwise returns -1. To get the [error](../../Constants,-Enumerations-and-Structures/Codes-of-Errors-and-Warnings/Runtime-Errors/Runtime-Errors.md) code, call the [GetLastError](../../Checkup/GetLastError/GetLastError.md) function.
