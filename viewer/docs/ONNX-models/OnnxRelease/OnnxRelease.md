# OnnxRelease


Close an ONNX session.

```cpp
bool  OnnxRelease(
   long   onnx_handle  // ONNX session handle
   );
```

Parameters

onnx\_handle

[in]  ONNX session object handle created via [OnnxCreate](../OnnxCreate/OnnxCreate.md) or [OnnxCreateFromBuffer](../OnnxCreateFromBuffer/OnnxCreateFromBuffer.md).

Return Value

Returns true on success; otherwise returns false. To get the [error](../../Constants,-Enumerations-and-Structures/Codes-of-Errors-and-Warnings/Runtime-Errors/Runtime-Errors.md) code, call the [GetLastError](../../Checkup/GetLastError/GetLastError.md) function.