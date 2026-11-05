# OnnxCreateFromBuffer

OnnxCreateFromBuffer

Create an ONNX session, loading a model from a data array.

|  |
| --- |
| long  OnnxCreateFromBuffer(     const uchar&  buffer[],   // array reference     ulong         flags       // model creation flags     ); |

Parameters

buffer

[in] Array with ONNX model data.

flags

[in] Flags from [ENUM\_ONNX\_FLAGS](../Data-structures/Data-structures.md#enum_onnx_flags), describing the model creation mode: ONNX\_COMMON\_FOLDER and ONNX\_DEBUG\_LOGS.

Return Value

The handle of the created session or INVALID\_HANDLE if error occurs. To obtain the [error](../../Constants,-Enumerations-and-Structures/Codes-of-Errors-and-Warnings/Runtime-Errors/Runtime-Errors.md) code, call the [GetLastError](../../Checkup/GetLastError/GetLastError.md) function.
