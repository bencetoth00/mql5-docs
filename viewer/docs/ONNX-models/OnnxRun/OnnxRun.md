# OnnxRun


Run an ONNX model.

```cpp
bool  OnnxRun(
   long    onnx_handle,  // ONNX session handle
   ulong   flags,        // flags describing the run mode
   ...                   // model's inputs and outputs
   );
```

Parameters

onnx\_handle

[in]  ONNX session object handle created via [OnnxCreate](../OnnxCreate/OnnxCreate.md) or [OnnxCreateFromBuffer](../OnnxCreateFromBuffer/OnnxCreateFromBuffer.md).

flags

[in] Flags from [ENUM\_ONNX\_FLAGS](../Data-structures/Data-structures.md#enum_onnx_flags) describing the run mode: ONNX\_DEBUG\_LOGS and ONNX\_NO\_CONVERSION.

...

[in] [out]  Model inputs and outputs.

Returns true on success or false otherwise. To obtain the [error](../../Constants,-Enumerations-and-Structures/Codes-of-Errors-and-Warnings/Runtime-Errors/Runtime-Errors.md) code, call the [GetLastError](../../Checkup/GetLastError/GetLastError.md) function.

 

ENUM\_ONNX\_FLAGS

| ID | Description |
| --- | --- |
| ONNX\_LOGLEVEL\_VERBOSE | Log all messages |
| ONNX\_LOGLEVEL\_INFO | Log info messages, warnings, and errors (this flag replaces ONNX\_DEBUG\_LOGS) |
| ONNX\_LOGLEVEL\_WARNING | Log warnings and errors (default) |
| ONNX\_LOGLEVEL\_ERROR | Log errors only |
| ONNX\_NO\_CONVERSION | Disable auto conversion, use user data as is |
| ONNX\_COMMON\_FOLDER | Load a model file from the Common\Files folder; the value is equal to the [FILE\_COMMON](../../Constants,-Enumerations-and-Structures/Input-Output-Constants/Input-Output-Constants.md) flag |
| ONNX\_USE\_CPU\_ONLY | Execute the ONNX model using CPU only |
| ONNX\_GPU\_DEVICE\_0 | CUDA device with index 0 (default) |
| ONNX\_GPU\_DEVICE\_1 | CUDA device with index 1 \* |
| ONNX\_GPU\_DEVICE\_2 | CUDA device with index 2 \* |
| ONNX\_GPU\_DEVICE\_3 | CUDA device with index 3  \* |
| ONNX\_GPU\_DEVICE\_4 | CUDA device with index 4  \* |
| ONNX\_GPU\_DEVICE\_5 | CUDA device with index 5  \* |
| ONNX\_GPU\_DEVICE\_6 | CUDA device with index 6  \* |
| ONNX\_GPU\_DEVICE\_7 | CUDA device with index 7  \* |
| ONNX\_ENABLE\_PROFILING | Enable ONNX model profiling |

\* Flags of the form ONNX\_GPU\_DEVICE\_N should be used on systems with two or more CUDA-capable GPUs. If multiple GPU selection flags are specified, the device with the lowest index will be used.

If a non-existent device index is specified, the GPU will be selected automatically.

 

Example:

```cpp
const long                             ExtOutputShape[] = {1,1};    // model output shape
const long                             ExtInputShape [] = {1,10,4}; // model input form
#resource "Python/model.onnx" as uchar ExtModel[]                   // model as resource
//+------------------------------------------------------------------+
//| Script program start function                                    |
//+------------------------------------------------------------------+
int OnStart(void)
  {
   matrix rates;
//--- get 10 bars
   if(!rates.CopyRates("EURUSD",PERIOD_H1,COPY_RATES_OHLC,2,10))
      return(-1);
//--- input a set of OHLC vectors
   matrix x_norm=rates.Transpose();
   vector m=x_norm.Mean(0);
   vector s=x_norm.Std(0);
   matrix mm(10,4);
   matrix ms(10,4);
//--- fill in the normalization matrices
   for(int i=0; i<10; i++)
     {
      mm.Row(m,i);
      ms.Row(s,i);
     }
//--- normalize the input data
   x_norm-=mm;
   x_norm/=ms;
//--- create the model
   long handle=OnnxCreateFromBuffer(ExtModel,ONNX_DEBUG_LOGS);
//--- specify the shape of the input data
   if(!OnnxSetInputShape(handle,0,ExtInputShape))
     {
      Print("OnnxSetInputShape failed, error ",GetLastError());
      OnnxRelease(handle);
      return(-1);
     }
//--- specify the shape of the output data
   if(!OnnxSetOutputShape(handle,0,ExtOutputShape))
     {
      Print("OnnxSetOutputShape failed, error ",GetLastError());
      OnnxRelease(handle);
      return(-1);
     }
//--- convert normalized input data to float type
   matrixf x_normf;
   x_normf.Assign(x_norm);
//--- get the output data of the model here, i.e. the price prediction
   vectorf y_norm(1);
//--- run the model
   if(!OnnxRun(handle,ONNX_DEBUG_LOGS | ONNX_NO_CONVERSION,x_normf,y_norm))
     {
      Print("OnnxRun failed, error ",GetLastError());
      OnnxRelease(handle);
      return(-1);
     }
//--- print the output value of the model to the log
   Print(y_norm);
//--- do the reverse transformation to get the predicted price
   double y_pred=y_norm[0]*s[3]+m[3];
   Print("price predicted:",y_pred);
//--- completed operation
   OnnxRelease(handle);
   return(0);
  };
```

See also

[OnnxSetInputShape](../OnnxSetInputShape/OnnxSetInputShape.md), [OnnxSetOutputShape](../OnnxSetOutputShape/OnnxSetOutputShape.md)