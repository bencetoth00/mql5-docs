# Running a model

Running a model

To run an ONNX model in MQL5, complete 3 steps:

1. Load the model from an \*.onnx file using the [OnnxCreate](../OnnxCreate/OnnxCreate.md) function or from an array using [OnnxCreateFromBuffer](../OnnxCreateFromBuffer/OnnxCreateFromBuffer.md).
2. Specify input and output data shapes using [OnnxSetInputShape](../OnnxSetInputShape/OnnxSetInputShape.md) and [OnnxSetOutputShape](../OnnxSetOutputShape/OnnxSetOutputShape.md) functions.
3. Run the model using the [OnnxRun](../OnnxRun/OnnxRun.md) function, passing to it the relevant input and output parameters.
4. When needed, you can terminate the model operation using the [OnnxRelease](../OnnxRelease/OnnxRelease.md) function.

 

When creating an ONNX model, you should consider the existing limits and restrictions, which are described at <https://github.com/microsoft/onnxruntime/blob/rel-1.14.0/docs/OperatorKernels.md>

Some of the examples of such restrictions are shown below:

| Operation | Supported data types |
| --- | --- |
| ReduceSum | tensor(double), tensor(float), tensor(int32), tensor(int64) |
| Mul | tensor(bfloat16), tensor(double), tensor(float), tensor(float16), tensor(int32), tensor(int64), tensor(uint32), tensor(uint64) |

 

Below is an MQL5 code example from the public project [ONNX.Price.Prediction](../Creating-a-Model/Creating-a-Model.md#model_sample).

|  |
| --- |
| const long   ExtOutputShape[] = {1,1};    // model's output shape  const long   ExtInputShape [] = {1,10,4}; // model's input shape  #resource "Python/model.onnx" as uchar ExtModel[]// model as a resource  //+------------------------------------------------------------------+  //| Script program start function                                    |  //+------------------------------------------------------------------+  int OnStart(void)    {     matrix rates;  //--- get 10 bars     if(!rates.CopyRates("EURUSD",PERIOD\_H1,COPY\_RATES\_OHLC,2,10))        return(-1);  //--- input a set of OHLC vectors     matrix x\_norm=rates.Transpose();     vector m=x\_norm.Mean(0);                    vector s=x\_norm.Std(0);     matrix mm(10,4);     matrix ms(10,4);  //--- fill in the normalization matrices     for(int i=0; i<10; i++)       {        mm.Row(m,i);        ms.Row(s,i);       }  //--- normalize the input data     x\_norm-=mm;     x\_norm/=ms;  //--- create the model     long handle=OnnxCreateFromBuffer(ExtModel,ONNX\_DEBUG\_LOGS);  //--- specify the shape of the input data     if(!OnnxSetInputShape(handle,0,ExtInputShape))       {        Print("OnnxSetInputShape failed, error ",GetLastError());        OnnxRelease(handle);        return(-1);       }  //--- specify the shape of the output data     if(!OnnxSetOutputShape(handle,0,ExtOutputShape))       {        Print("OnnxSetOutputShape failed, error ",GetLastError());        OnnxRelease(handle);        return(-1);       }  //--- convert normalized input data to float type     matrixf x\_normf;     x\_normf.Assign(x\_norm);  //--- get the output data of the model here, i.e. the price prediction     vectorf y\_norm(1);  //--- run the model     if(!OnnxRun(handle,ONNX\_DEBUG\_LOGS | ONNX\_NO\_CONVERSION,x\_normf,y\_norm))       {        Print("OnnxRun failed, error ",GetLastError());        OnnxRelease(handle);        return(-1);       }  //--- print the output value of the model to the log     Print(y\_norm);  //--- do the reverse transformation to get the predicted price     double y\_pred=y\_norm[0]\*s[3]+m[3];     Print("price predicted:",y\_pred);  //--- complete operation     OnnxRelease(handle);     return(0);    } |

Script run example:

|  |
| --- |
| ONNX: Creating and using per session threadpools since use\_per\_session\_threads\_ is true  ONNX: Dynamic block base set to 0  ONNX: Initializing session.  ONNX: Adding default CPU execution provider.  ONNX: Total shared scalar initializer count: 0  ONNX: Total fused reshape node count: 0  ONNX: Total shared scalar initializer count: 0  ONNX: Total fused reshape node count: 0  ONNX: Use DeviceBasedPartition as default  ONNX: Saving initialized tensors.  ONNX: Done saving initialized tensors  ONNX: Session successfully initialized.  [0.28188983]  predicted 1.0559258806393044 |

The MetaTrader 5 terminal has selected the optimal executor for calculations — [ONNX Runtime Execution Provider](https://onnxruntime.ai/docs/execution-providers/). In this example, the model was executed on the CPU.

Let's modify the script to calculate the percentage of successful Close price predictions made based on the values of the preceding 10 bars.

|  |
| --- |
| #resource "Python/model.onnx" as uchar ExtModel[]// model as a resource     #define TESTS 10000  // number of test datasets  //+------------------------------------------------------------------+  //| Script program start function                                    |  //+------------------------------------------------------------------+  int OnStart()    {  //--- create the model     long session\_handle=OnnxCreateFromBuffer(ExtModel,ONNX\_DEBUG\_LOGS);     if(session\_handle==INVALID\_HANDLE)       {        Print("Cannot create model. Error ",GetLastError());        return(-1);       }     //--- since the input tensor size is not defined for the model, specify it explicitly  //--- first index is batch size, second index is series size, third index is number of series (OHLC)     const long input\_shape[]={1,10,4};     if(!OnnxSetInputShape(session\_handle,0,input\_shape))       {        Print("OnnxSetInputShape error ",GetLastError());        return(-2);       }     //--- since the output tensor size is not defined for the model, specify it explicitly  //--- first index is batch size, must match the batch size in the input tensor  //--- second index is number of predicted prices (only Close is predicted here)     const long output\_shape[]={1,1};     if(!OnnxSetOutputShape(session\_handle,0,output\_shape))       {        Print("OnnxSetOutputShape error ",GetLastError());        return(-3);       }  //--- run tests     vector closes(TESTS);      // vector to store validation prices     vector predicts(TESTS);    // vector to store obtained predictions     vector prev\_closes(TESTS); // vector to store preceding prices        matrix rates;              // matrix to get the OHLC series     matrix splitted[2];        // two submatrices to divide the series into test and validation     ulong  parts[]={10,1};     // sizes of divided submatrices     //--- start from the previous bar     for(int i=1; i<=TESTS; i++)       {        //--- get 11 bars        rates.CopyRates("EURUSD",PERIOD\_H1,COPY\_RATES\_OHLC,i,11);        //--- divide the matrix into test and validation        rates.Vsplit(parts,splitted);        //--- take the Close price from the validation matrix        closes[i-1]=splitted[1][3][0];        //--- last Close in the tested series        prev\_closes[i-1]=splitted[0][3][9];           //--- submit the test matrix of 10 bars to testing        predicts[i-1]=PricePredictionTest(session\_handle,splitted[0]);        //--- runtime error        if(predicts[i-1]<=0)          {           OnnxRelease(session\_handle);           return(-4);          }       }  //--- complete operation     OnnxRelease(session\_handle);  //--- evaluate if price movement was predicted correctly     int    right\_directions=0;     vector delta\_predicts=prev\_closes-predicts;     vector delta\_actuals=prev\_closes-closes;        for(int i=0; i<TESTS; i++)        if((delta\_predicts[i]>0 && delta\_actuals[i]>0) || (delta\_predicts[i]<0 && delta\_actuals[i]<0))           right\_directions++;     PrintFormat("right direction predictions = %.2f%%",(right\_directions\*100.0)/double(TESTS));  //---      return(0);    }  //+------------------------------------------------------------------+  //|  Prepare the data and run the model                              |  //+------------------------------------------------------------------+  double PricePredictionTest(const long session\_handle,matrix& rates)    {     static matrixf input\_data(10,4); // matrix for the transformed input     static vectorf output\_data(1);   // vector to receive the result     static matrix mm(10,4);          // matrix of horizontal vectors Mean     static matrix ms(10,4);          // matrix of horizontal vectors Std     //--- a set of OHLC vertical vectors must be input into the model     matrix x\_norm=rates.Transpose();  //--- normalize prices     vector m=x\_norm.Mean(0);     vector s=x\_norm.Std(0);     for(int i=0; i<10; i++)       {        mm.Row(m,i);        ms.Row(s,i);       }     x\_norm-=mm;     x\_norm/=ms;     //--- run the model     input\_data.Assign(x\_norm);     if(!OnnxRun(session\_handle,ONNX\_DEBUG\_LOGS,input\_data,output\_data))       {        Print("OnnxRun error ",GetLastError());        return(0);       }  //--- unnormalize the price from the output value     double y\_pred=output\_data[0]\*s[3]+m[3];        return(y\_pred);    } |

Run the script: the prediction accuracy is about 51%

|  |
| --- |
| ONNX: Creating and using per session threadpools since use\_per\_session\_threads\_ is true  ONNX: Dynamic block base set to 0  ONNX: Initializing session.  ONNX: Adding default CPU execution provider.  ONNX: Total shared scalar initializer count: 0  ONNX: Total fused reshape node count: 0  ONNX: Total shared scalar initializer count: 0  ONNX: Total fused reshape node count: 0  ONNX: Use DeviceBasedPartition as default  ONNX: Saving initialized tensors.  ONNX: Done saving initialized tensors  ONNX: Session successfully initialized.  right direction predictions = 51.34 % |
