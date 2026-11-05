# ArrayToFP16

ArrayToFP16

Copies an array of type float or double into an array of type [ushort](../../Language-Basics/Data-Types/Integer-Types/Char,-Short,-Int-and-Long-Types/Char,-Short,-Int-and-Long-Types.md#ushort) with the given format.

|  |
| --- |
| bool   ArrayToFP16(     const ushort&        dst\_array[],        // copy to     const float&         src\_array[],        // copy from     ENUM\_FLOAT16\_FORMAT  fmt                 // format     ); |

Overloading for the double type

|  |
| --- |
| bool   ArrayToFP16(     const ushort&        dst\_array[],        // copy to     const double&        src\_array[],        // copy from     ENUM\_FLOAT16\_FORMAT  fmt                 // format     ); |

Parameters

dst\_array[]

[out]  Receiver array or type ushort.

src\_array[]

[in]  Source array of type float or double.

fmt

[in]  Copying format from the [ENUM\_FLOAT16\_FORMAT](../../ONNX-models/Data-structures/Data-structures.md#enum_float16_format) enumeration.

 

Return Value

Returns true if successful or false otherwise.

 

Note

Formats FLOAT16 and BFLOAT16 are defined in the [ENUM\_FLOAT16\_FORMAT](../../ONNX-models/Data-structures/Data-structures.md#enum_float16_format) enumeration and are used in MQL5 only for operations with [ONNX models](../../ONNX-models/ONNX-models.md).

The function converts input parameters of type float or double to type FLOAT16 and BFLOAT16. These input parameters are then used in the [OnnxRun](../../ONNX-models/OnnxRun/OnnxRun.md) function.

FLOAT16, also known as [half-precision float](https://en.wikipedia.org/wiki/Half-precision_floating-point_format), uses 16 bits to represent floating-point numbers. This format provides a balance between accuracy and computational efficiency. FLOAT16 is widely used in deep learning algorithms and neural networks, which require high-performance processing of large datasets. This format accelerates computations calculations by reducing the size of numbers, which is especially important when training deep neural networks on GPUs.

BFLOAT16 (or [Brain Floating Point 16](https://en.wikipedia.org/wiki/Bfloat16_floating-point_format)) also uses 16 bits but differs from FLOAT16 in the approach to format representation. In this format, 8 bits are allocated for representing the exponent, while the remaining 7 bits are used for representing the mantissa. This format was developed for use in deep learning and artificial intelligence, especially in Google's Tensor Processing Unit (TPU). BFLOAT16 demonstrates excellent performance in neural network training and can effectively accelerate computations.

 

Example: function from the article [Working with ONNX models in float16 and float8 formats](https://www.mql5.com/ru/articles/14330 "Article \"Working with ONNX models in float16 and float8 formats\"")

|  |
| --- |
| //+------------------------------------------------------------------+  //| RunCastFloat16ToDouble                                           |  //+------------------------------------------------------------------+  bool RunCastFloat16ToDouble(long model\_handle)    {     PrintFormat("test=%s",\_\_FUNCTION\_\_);     double test\_data[12]= {1,2,3,4,5,6,7,8,9,10,11,12};     ushort data\_uint16[12];     if(!ArrayToFP16(data\_uint16,test\_data,FLOAT\_FP16))       {        Print("error in ArrayToFP16. error code=",GetLastError());        return(false);       }     Print("test array:");     ArrayPrint(test\_data);     Print("ArrayToFP16:");     ArrayPrint(data\_uint16);     U<ushort> input\_float16\_values[3\*4];     U<double> output\_double\_values[3\*4];     float test\_data\_float[];     if(!ArrayFromFP16(test\_data\_float,data\_uint16,FLOAT\_FP16))       {        Print("error in ArrayFromFP16. error code=",GetLastError());        return(false);       }     for(int i=0; i<12; i++)       {        input\_float16\_values[i].value=data\_uint16[i];        PrintFormat("%d input value =%f  Hex float16 = %s  ushort value=%d",i,test\_data\_float[i],ArrayToString(input\_float16\_values[i].uc),input\_float16\_values[i].value);       }     Print("ONNX input array:");     ArrayPrint(input\_float16\_values);     bool res=OnnxRun(model\_handle,ONNX\_NO\_CONVERSION,input\_float16\_values,output\_double\_values);     if(!res)       {        PrintFormat("error in OnnxRun. error code=%d",GetLastError());        return(false);       }     Print("ONNX output array:");     ArrayPrint(output\_double\_values);  //---     double sum\_error=0.0;     for(int i=0; i<12; i++)       {        double delta=test\_data[i]-output\_double\_values[i].value;        sum\_error+=MathAbs(delta);        PrintFormat("%d output double %f = %s  difference=%f",i,output\_double\_values[i].value,ArrayToString(output\_double\_values[i].uc),delta);       }  //---     PrintFormat("test=%s   sum\_error=%f",\_\_FUNCTION\_\_,sum\_error);  //---     return(true);    } |

 

See also

[ArrayFromFP16](../ArrayFromFP16/ArrayFromFP16.md), [ArrayCopy](../ArrayCopy/ArrayCopy.md)
