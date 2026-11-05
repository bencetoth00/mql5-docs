# OnnxGetInputTypeInfo


Get the description of the input type from the model.

```cpp
bool  OnnxGetInputTypeInfo(
   long           onnx_handle,  // ONNX session handle
   long           index,        // parameter index
   OnnxTypeInfo&  typeinfo      // parameter type description
   );
```

Parameters

onnx\_handle

[in]  ONNX session object handle created via [OnnxCreate](../OnnxCreate/OnnxCreate.md) or [OnnxCreateFromBuffer](../OnnxCreateFromBuffer/OnnxCreateFromBuffer.md).

index

[in]  Index of the input parameter, starting with 0.

typeinfo

[out]  The [OnnxTypeInfo](../Data-structures/Data-structures.md#onnxtypeinfo) structure that describes the type of the input parameter.

Return Value

Returns true on success; otherwise returns false. To get the [error](../../Constants,-Enumerations-and-Structures/Codes-of-Errors-and-Warnings/Runtime-Errors/Runtime-Errors.md) code, call the [GetLastError](../../Checkup/GetLastError/GetLastError.md) function.