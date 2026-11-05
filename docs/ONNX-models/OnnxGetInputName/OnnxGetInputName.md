# OnnxGetInputName

OnnxGetInputName

Get the name of a model's input by index.

|  |
| --- |
| string  OnnxGetInputName(     long   onnx\_handle,  // ONNX session handle     long   index         // parameter index     ); |

Parameters

onnx\_handle

[in]  ONNX session object handle created via [OnnxCreate](../OnnxCreate/OnnxCreate.md) or [OnnxCreateFromBuffer](../OnnxCreateFromBuffer/OnnxCreateFromBuffer.md).

index

[in]  Index of the input parameter, starting with 0.

Return Value

Returns the name of the input parameter on success; otherwise returns NULL. To get the [error](../../Constants,-Enumerations-and-Structures/Codes-of-Errors-and-Warnings/Runtime-Errors/Runtime-Errors.md) code, call the [GetLastError](../../Checkup/GetLastError/GetLastError.md) function.
