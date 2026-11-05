# OnnxCreate


Create an ONNX session, loading a model from an \*.onnx file.

```cpp
long  OnnxCreate(
   string  filename,  // file path
   uint    flags      // flags to create the model
   );
```

Parameters

filename

[in]  Path to the \*.onnx file of the model relative to the \MQL5\Files\ folder.

flags

[in] Flags from [ENUM\_ONNX\_FLAGS](../Data-structures/Data-structures.md#enum_onnx_flags), describing the model creation mode: ONNX\_COMMON\_FOLDER and ONNX\_DEBUG\_LOGS.

Return Value

The handle of the created session or INVALID\_HANDLE if error occurs. To obtain the [error](../../Constants,-Enumerations-and-Structures/Codes-of-Errors-and-Warnings/Runtime-Errors/Runtime-Errors.md) code, call the [GetLastError](../../Checkup/GetLastError/GetLastError.md) function.

Note

If the specified file is not found on disk, the system retries to open the file, appending the '.onnx' extension to the name.