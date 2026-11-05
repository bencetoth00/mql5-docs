# OnnxSetOutputShape


Set the shape of a model's output data by index.

```cpp
bool  OnnxSetOutputShape(
   long          onnx_handle,   // ONNX session handle
   long          output_index,  // output parameter index
   const ulong&  shape[]        // array describing output data shape
   );
```

Parameters

onnx\_handle

[in]  ONNX session object handle created via [OnnxCreate](../OnnxCreate/OnnxCreate.md) or [OnnxCreateFromBuffer](../OnnxCreateFromBuffer/OnnxCreateFromBuffer.md).

output\_index

[in]  Index of the output parameter, starting from 0.

shape

[in]  Array describing model's output data shape.

Return Value

Returns the name of the input parameter on success; otherwise returns NULL. To get the [error](../../Constants,-Enumerations-and-Structures/Codes-of-Errors-and-Warnings/Runtime-Errors/Runtime-Errors.md) code, call the [GetLastError](../../Checkup/GetLastError/GetLastError.md) function.

 

Example:

```cpp
//---- describe the shapes of the model's input and output data
   const long  ExtOutputShape[] = {1,1};
   const long  ExtInputShape [] = {1,10,4};
//--- create the model
   long handle=OnnxCreateFromBuffer(model,ONNX_DEBUG_LOGS);
//--- specify the shape of the input data
   if(!OnnxSetInputShape(handle,0,ExtInputShape))
     {
      Print("failed, OnnxSetInputShape error ",GetLastError());
      OnnxRelease(handle);
      return(-1);
     }
//--- specify the shape of the output data
   if(!OnnxSetOutputShape(handle,0,ExtOutputShape))
     {
      Print("failed, OnnxSetOutputShape error ",GetLastError());
      OnnxRelease(handle);
      return(-1);
     }
```

See also

[OnnxSetInputShape](../OnnxSetInputShape/OnnxSetInputShape.md)