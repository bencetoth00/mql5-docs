# Automatic data type conversion

# Autoconvert input and output values when running ONNX models

The current ONNX version in MQL5 supports only tensors for [input/output](https://onnxruntime.ai/docs/api/python/api_summary.html#data-inputs-and-outputs) values. Tensors are data arrays with the elements of the following data types:

| ONNX type | Corresponds to MQL5 type |
| --- | --- |
| ONNX\_DATA\_TYPE\_BOOL | [bool](../../Language-Basics/Data-Types/Integer-Types/Bool-Type/Bool-Type.md) |
| ONNX\_DATA\_TYPE\_FLOAT | [float](../../Language-Basics/Data-Types/Real-Types-(double,-float)/Real-Types-(double,-float).md) |
| ONNX\_DATA\_TYPE\_UINT8 | [uchar](../../Language-Basics/Data-Types/Integer-Types/Char,-Short,-Int-and-Long-Types/Char,-Short,-Int-and-Long-Types.md) |
| ONNX\_DATA\_TYPE\_INT8 | [char](../../Language-Basics/Data-Types/Integer-Types/Char,-Short,-Int-and-Long-Types/Char,-Short,-Int-and-Long-Types.md) |
| ONNX\_DATA\_TYPE\_UINT16 | [ushort](../../Language-Basics/Data-Types/Integer-Types/Char,-Short,-Int-and-Long-Types/Char,-Short,-Int-and-Long-Types.md) |
| ONNX\_DATA\_TYPE\_INT16 | [short](../../Language-Basics/Data-Types/Integer-Types/Char,-Short,-Int-and-Long-Types/Char,-Short,-Int-and-Long-Types.md) |
| ONNX\_DATA\_TYPE\_INT32 | [int](../../Language-Basics/Data-Types/Integer-Types/Char,-Short,-Int-and-Long-Types/Char,-Short,-Int-and-Long-Types.md) |
| ONNX\_DATA\_TYPE\_INT64 | [long](../../Language-Basics/Data-Types/Integer-Types/Char,-Short,-Int-and-Long-Types/Char,-Short,-Int-and-Long-Types.md) |
| ONNX\_DATA\_TYPE\_FLOAT16 | — |
| ONNX\_DATA\_TYPE\_DOUBLE | [double](../../Language-Basics/Data-Types/Real-Types-(double,-float)/Real-Types-(double,-float).md) |
| ONNX\_DATA\_TYPE\_UINT32 | [uint](../../Language-Basics/Data-Types/Integer-Types/Char,-Short,-Int-and-Long-Types/Char,-Short,-Int-and-Long-Types.md) |
| ONNX\_DATA\_TYPE\_UINT64 | [ulong](../../Language-Basics/Data-Types/Integer-Types/Char,-Short,-Int-and-Long-Types/Char,-Short,-Int-and-Long-Types.md) |
| ONNX\_DATA\_TYPE\_COMPLEX64 | — |
| ONNX\_DATA\_TYPE\_COMPLEX128 | [complex](../../Language-Basics/Data-Types/Complex-number-(complex)/Complex-number-(complex).md) |
| ONNX\_DATA\_TYPE\_BFLOAT16 | — |
| ONNX\_DATA\_TYPE\_STRING | — |

 

Only arrays, [vectors and matrices](../../Language-Basics/Data-Types/Matrices-and-vectors/Matrices-and-vectors.md) (we will refer to them as the Data) can be fed into ONNX models as input/output values.

If the parameter types does not match the ONNX model's parameter type, and the [OnnxRun](../OnnxRun/OnnxRun.md) is called without the [ONNX\_NO\_CONVERSION](../Data-structures/Data-structures.md#enum_onnx_flags) flag specified, automatic data conversion will be applied. Autoconversion implies that before running an ONNX model, user Data will be copied into ONNX tensors with the relevant conversion.

When an ONNX model is run without the autoconversion, the model will be calculated using the Data without any additional copying.

IMPORTANT! Autoconversion does not control overflow (truncate), therefore you should carefully monitor the data and the data types input into the ONNX model.

Autoconversion supports the following ONNX types:

- ONNX\_DATA\_TYPE\_BOOL
- ONNX\_DATA\_TYPE\_FLOAT
- ONNX\_DATA\_TYPE\_UINT8
- ONNX\_DATA\_TYPE\_INT8
- ONNX\_DATA\_TYPE\_UINT16
- ONNX\_DATA\_TYPE\_INT16
- ONNX\_DATA\_TYPE\_INT32
- ONNX\_DATA\_TYPE\_INT64
- ONNX\_DATA\_TYPE\_FLOAT16
- ONNX\_DATA\_TYPE\_DOUBLE
- ONNX\_DATA\_TYPE\_UINT32
- ONNX\_DATA\_TYPE\_UINT64
- ONNX\_DATA\_TYPE\_COMPLEX64
- ONNX\_DATA\_TYPE\_COMPLEX128

Unsupported types:

- ONNX\_DATA\_TYPE\_BFLOAT16
- ONNX\_DATA\_TYPE\_STRING

 

### Autoconversion Rules by Tensor Types

If the [MQL5 type](../../Language-Basics/Data-Types/Data-Types.md) is not included into the list of types supported by the model, running the ONNX model will return the ERR\_ONNX\_NOT\_SUPPORTED error (error code 5802).

Note: During autoconversion, the [color](../../Language-Basics/Data-Types/Integer-Types/Bool-Type/Bool-Type.md) type is processed as uint, while [datetime](../../Language-Basics/Data-Types/Integer-Types/Datetime-Type/Datetime-Type.md) is processed as long.

 

Autoconversion of input values

| ONNX type (tensor item type) | MQL5 type supported by autoconversion |
| --- | --- |
| ONNX\_DATA\_TYPE\_BOOL | bool, char, uchar, short, ushort, int, color, uint, datetime, long,  folat, double, complex     During conversion, Data elements are checked by a simple comparison against 0 |
| ONNX\_DATA\_TYPE\_FLOAT16 | float, double |
| ONNX\_DATA\_TYPE\_FLOAT | char, uchar, short, ushort, int, color, uint, datetime, long, ulong, float, double |
| ONNX\_DATA\_TYPE\_UINT8 | See ONNX\_DATA\_TYPE\_FLOAT |
| ONNX\_DATA\_TYPE\_INT8 | See ONNX\_DATA\_TYPE\_FLOAT |
| ONNX\_DATA\_TYPE\_UINT16 | See ONNX\_DATA\_TYPE\_FLOAT |
| ONNX\_DATA\_TYPE\_INT16 | See ONNX\_DATA\_TYPE\_FLOAT |
| ONNX\_DATA\_TYPE\_INT32 | See ONNX\_DATA\_TYPE\_FLOAT |
| ONNX\_DATA\_TYPE\_INT64 | See ONNX\_DATA\_TYPE\_FLOAT |
| ONNX\_DATA\_TYPE\_DOUBLE | See ONNX\_DATA\_TYPE\_FLOAT |
| ONNX\_DATA\_TYPE\_UINT32 | See ONNX\_DATA\_TYPE\_FLOAT |
| ONNX\_DATA\_TYPE\_UINT64 | See ONNX\_DATA\_TYPE\_FLOAT |
| ONNX\_DATA\_TYPE\_COMPLEX64 | complex |
| ONNX\_DATA\_TYPE\_COMPLEX128 | complex |

 

Autoconversion of output values

| ONNX type (tensor item type) | MQL5 type supported by autoconversion |
| --- | --- |
| ONNX\_DATA\_TYPE\_BOOL | bool, char, uchar, short, ushort, int, color, uint, datetime, long,  folat, double, complex     If the tensor element is zero, then the Data element is set to 0; otherwise, the value is 1 |
| ONNX\_DATA\_TYPE\_FLOAT16 | float, double |
| ONNX\_DATA\_TYPE\_FLOAT | char, uchar, short, ushort, int, color, uint, datetime, long, ulong, float, double |
| ONNX\_DATA\_TYPE\_UINT8 | See ONNX\_DATA\_TYPE\_FLOAT |
| ONNX\_DATA\_TYPE\_INT8 | See ONNX\_DATA\_TYPE\_FLOAT |
| ONNX\_DATA\_TYPE\_UINT16 | See ONNX\_DATA\_TYPE\_FLOAT |
| ONNX\_DATA\_TYPE\_INT16 | See ONNX\_DATA\_TYPE\_FLOAT |
| ONNX\_DATA\_TYPE\_INT32 | See ONNX\_DATA\_TYPE\_FLOAT |
| ONNX\_DATA\_TYPE\_INT64 | See ONNX\_DATA\_TYPE\_FLOAT |
| ONNX\_DATA\_TYPE\_DOUBLE | See ONNX\_DATA\_TYPE\_FLOAT |
| ONNX\_DATA\_TYPE\_UINT32 | See ONNX\_DATA\_TYPE\_FLOAT |
| ONNX\_DATA\_TYPE\_UINT64 | See ONNX\_DATA\_TYPE\_FLOAT |
| ONNX\_DATA\_TYPE\_COMPLEX64 | complex |
| ONNX\_DATA\_TYPE\_COMPLEX128 | complex |

 

See also

[Type Casting](../../Language-Basics/Data-Types/Typecasting/Typecasting.md)
