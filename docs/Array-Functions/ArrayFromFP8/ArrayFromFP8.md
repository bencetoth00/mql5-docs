# ArrayFromFP8

ArrayFromFP8

Copies an array of type [uchar](../../Language-Basics/Data-Types/Integer-Types/Char,-Short,-Int-and-Long-Types/Char,-Short,-Int-and-Long-Types.md#uchar) into an array of float or double type with the given format.

|  |
| --- |
| bool   ArrayFromFP8(     const float&         dst\_array[],        // copy to     const uchar&         src\_array[],        // copy from     ENUM\_FLOAT8\_FORMAT   fmt                 // format     ); |

Overloading for the double type

|  |
| --- |
| bool   ArrayFromFP8(     const double&        dst\_array[],        // copy to     const uchar&         src\_array[],        // copy from     ENUM\_FLOAT8\_FORMAT   fmt                 // format     ); |

Parameters

dst\_array[]

[out]  Receiver array of type float or double.

src\_array[]

[in]  Source array of type uchar.

fmt

[in]  Copying format from the [ENUM\_FLOAT8\_FORMAT](../../ONNX-models/Data-structures/Data-structures.md#enum_float8_format) enumeration.

 

Return Value

Returns true if successful or false otherwise.

 

Note

All kinds of FP8 format are defined in the [ENUM\_FLOAT8\_FORMAT](../../ONNX-models/Data-structures/Data-structures.md#enum_float8_format) enumeration and are used in MQL5 only for operations with [ONNX models](../../ONNX-models/ONNX-models.md).

If the output parameters obtained from the [OnnxRun](../../ONNX-models/OnnxRun/OnnxRun.md) function execution are of FP8 from the ENUM\_FLOAT8\_FORMAT enumeration, you can use this function to convert the result into float or double arrays.

FP8 (8-bit floating point) is one of the data types used to represent floating point numbers. In FP8, each number is represented by 8 data bits, typically divided into three components: sign, exponent and mantissa. This format offers a balance between accuracy and storage efficiency, making it attractive for applications that require memory and computational efficiency.

By employing compact number representation, FP8 reduces memory requirements and accelerates calculations. In addition, FP8 can be useful for implementing low-level operations such as arithmetic calculations and signal processing.

 

Example: function from the article [Working with ONNX models in float16 and float8 formats](https://www.mql5.com/ru/articles/14330 "Article \"Working with ONNX models in float16 and float8 formats\"")

|  |
| --- |
| //+------------------------------------------------------------------+  //| RunCastFloat8Float                                               |  //+------------------------------------------------------------------+  bool RunCastFloat8ToFloat(long model\_handle,const ENUM\_FLOAT8\_FORMAT fmt)    {     PrintFormat("TEST: %s(%s)",\_\_FUNCTION\_\_,EnumToString(fmt));  //---     float test\_data[15]   = {1,2,3,4,5,6,7,8,9,10,11,12,13,14,15};     uchar data\_float8[15] = {};     if(!ArrayToFP8(data\_float8,test\_data,fmt))       {        Print("error in ArrayToFP8. error code=",GetLastError());        OnnxRelease(model\_handle);        return(false);       }     U<uchar> input\_float8\_values[3\*5];     U<float> output\_float\_values[3\*5];     float    test\_data\_float[];  //--- convert float8 to float     if(!ArrayFromFP8(test\_data\_float,data\_float8,fmt))       {        Print("error in ArrayFromFP8. error code=",GetLastError());        OnnxRelease(model\_handle);        return(false);       }     for(uint i=0; i<data\_float8.Size(); i++)       {        input\_float8\_values[i].value=data\_float8[i];        PrintFormat("%d input value =%f  Hex float8 = %s  ushort value=%d",i,test\_data\_float[i],ArrayToHexString(input\_float8\_values[i].uc),input\_float8\_values[i].value);       }     Print("ONNX input array: ",ArrayToString(input\_float8\_values));  //--- execute model (convert float8 to float using ONNX)     if(!OnnxRun(model\_handle,ONNX\_NO\_CONVERSION,input\_float8\_values,output\_float\_values))       {        PrintFormat("error in OnnxRun. error code=%d",GetLastError());        OnnxRelease(model\_handle);        return(false);       }     Print("ONNX output array: ",ArrayToString(output\_float\_values));  //--- calculate error (compare ONNX and ArrayFromFP8 results)     double sum\_error=0.0;     for(uint i=0; i<test\_data.Size(); i++)       {        double delta=test\_data\_float[i]-(double)output\_float\_values[i].value;        sum\_error+=MathAbs(delta);        PrintFormat("%d output float %f = %s difference=%f",i,output\_float\_values[i].value,ArrayToHexString(output\_float\_values[i].uc),delta);       }  //---     PrintFormat("%s(%s): sum\_error=%f\n",\_\_FUNCTION\_\_,EnumToString(fmt),sum\_error);     return(true);    } |

 

See also

[ArrayToFP8](../ArrayToFP8/ArrayToFP8.md), [ArrayCopy](../ArrayCopy/ArrayCopy.md)
