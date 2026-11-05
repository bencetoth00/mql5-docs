# CLHandleType

CLHandleType

Returns the type of an OpenCL handle as a value of the ENUM\_OPENCL\_HANDLE\_TYPE enumeration.

|  |
| --- |
| ENUM\_OPENCL\_HANDLE\_TYPE  CLHandleType(     int  handle     // Handle of an OpenCL object     ); |

Parameters

handle

[in]  A handle to an OpenCL object: a context, a kernel or an OpenCL program.

Return Value

The type of the OpenCL handle as a value of the [ENUM\_OPENCL\_HANDLE\_TYPE](CLHandleType.md#enum_opencl_handle_type) enumeration.

ENUM\_OPENCL\_HANDLE\_TYPE

| Identifier | Description |
| --- | --- |
| OPENCL\_INVALID | Incorrect handle |
| OPENCL\_CONTEXT | A handle of the OpenCL context |
| OPENCL\_PROGRAM | A handle of the OpenCL program |
| OPENCL\_KERNEL | A handle of the OpenCL kernel |
| OPENCL\_BUFFER | A handle of the OpenCL buffer |
