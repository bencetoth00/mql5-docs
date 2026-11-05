# OnnxSetInputShape

OnnxSetInputShape

Set the shape of a model's input data by index.

|  |
| --- |
| bool  OnnxSetInputShape(     long          onnx\_handle,  // ONNX session handle     long          input\_index,  // input parameter index     const ulong&  shape[]       // array describing input data shape     ); |

Parameters

onnx\_handle

[in]  ONNX session object handle created via [OnnxCreate](../OnnxCreate/OnnxCreate.md) or [OnnxCreateFromBuffer](../OnnxCreateFromBuffer/OnnxCreateFromBuffer.md).

input\_index

[in]  Index of the input parameter, starting from 0.

shape

[in]  Array describing model's input data shape.

Return Value

Returns the name of the input parameter on success; otherwise returns NULL. To get the [error](../../Constants,-Enumerations-and-Structures/Codes-of-Errors-and-Warnings/Runtime-Errors/Runtime-Errors.md) code, call the [GetLastError](../../Checkup/GetLastError/GetLastError.md) function.

 

Example:

|  |
| --- |
| //---- describe the shapes of the model's input and output data     const long  ExtOutputShape[] = {1,1};     const long  ExtInputShape [] = {1,10,4};  //--- create the model     long handle=OnnxCreateFromBuffer(model,ONNX\_DEBUG\_LOGS);  //--- specify the shape of the input data     if(!OnnxSetInputShape(handle,0,ExtInputShape))       {        Print("failed, OnnxSetInputShape error ",GetLastError());        OnnxRelease(handle);        return(-1);       }  //--- specify the shape of the output data     if(!OnnxSetOutputShape(handle,0,ExtOutputShape))       {        Print("failed, OnnxSetOutputShape error ",GetLastError());        OnnxRelease(handle);        return(-1);       } |

See also

[OnnxSetOutputShape](../OnnxSetOutputShape/OnnxSetOutputShape.md)
