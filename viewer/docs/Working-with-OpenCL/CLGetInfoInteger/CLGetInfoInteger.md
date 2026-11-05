# CLGetInfoInteger


Returns the value of an integer property for an OpenCL object or device.

```cpp
long  CLGetInfoInteger(
   int  handle,                           // The handle of the OpenCL object or the number of the OpenCL device
   ENUM_OPENCL_PROPERTY_INTEGER  prop     // Requested property
   );
```

Parameters

handle

[in]  A handle to the OpenCL object or number of the OpenCL device. Numbering of OpenCL devices starts with zero.

prop

[in]  The type of a requested property from the [ENUM\_OPENCL\_PROPERTY\_INTEGER](CLGetInfoInteger.md#enum_opencl_property_integer) enumeration, the value of which you want to obtain.

Return Value

The value of the property if successful or -1 in case of an error. For information about the error, use the [GetLastError()](../../Checkup/GetLastError/GetLastError.md) function.

ENUM\_OPENCL\_PROPERTY\_INTEGER

| Identifier | Description | Type |
| --- | --- | --- |
| CL\_DEVICE\_COUNT | The number of devices with OpenCL support. This property does not require specification of the first parameter, i.e. you can pass a zero value for the handle parameter. | int |
| CL\_DEVICE\_TYPE | Type of device | [ENUM\_CL\_DEVICE\_TYPE](CLGetInfoInteger.md#enum_cl_device_type) |
| CL\_DEVICE\_VENDOR\_ID | Unique vendor identifier | uint |
| CL\_DEVICE\_MAX\_COMPUTE\_UNITS | Number of parallel calculated tasks in OpenCL device. One working group solves one computational task. The lowest value is 1 | uint |
| CL\_DEVICE\_MAX\_CLOCK\_FREQUENCY | Highest set frequency of the device in MHz. | uint |
| CL\_DEVICE\_GLOBAL\_MEM\_SIZE | Size of the global memory of the device in bytes | ulong |
| CL\_DEVICE\_LOCAL\_MEM\_SIZE | Size of the processed data (scene) local memory in bytes | uint |
| CL\_BUFFER\_SIZE | Actual size of the OpenCL buffer in bytes | ulong |
| CL\_DEVICE\_MAX\_WORK\_GROUP\_SIZE | The total number of the local working groups available for an OpenCL device. | ulong |
| CL\_KERNEL\_WORK\_GROUP\_SIZE | The total number of the local working groups available for an OpenCL program. | ulong |
| CL\_KERNEL\_LOCAL\_MEM\_SIZE | Size of the local memory (in bytes) used by an OpenCL program for solving all parallel tasks in a group. Use CL\_DEVICE\_LOCAL\_MEM\_SIZE to receive the maximum available value | ulong |
| CL\_KERNEL\_PRIVATE\_MEM\_SIZE | The minimum size of the private memory (in bytes) used by each task in the OpenCL program kernel. | ulong |
| CL\_LAST\_ERROR | The value of the last OpenCL error | int |

 

The ENUM\_CL\_DEVICE\_TYPE enumeration contains possible types of devices supporting OpenCL. You can receive the type of device by its number or the handle of the OpenCL object by calling CLGetInfoInteger(handle\_or\_deviceN, CL\_DEVICE\_TYPE).

ENUM\_CL\_DEVICE\_TYPE

| Identifier | Description |
| --- | --- |
| CL\_DEVICE\_ACCELERATOR | Dedicated OpenCL accelerators (for example, the IBM CELL Blade). These devices communicate with the host processor using a peripheral interconnect such as PCIe. |
| CL\_DEVICE\_CPU | An OpenCL device that is the host processor. The host processor runs the OpenCL implementations and is a single or multi-core CPU. |
| CL\_DEVICE\_GPU | An OpenCL device that is a GPU. |
| CL\_DEVICE\_DEFAULT | The default OpenCL device in the system. The default device cannot be a CL\_DEVICE\_TYPE\_CUSTOM device. |
| CL\_DEVICE\_CUSTOM | Dedicated accelerators that do not support programs written in OpenCL C. |

Example:

```cpp
void OnStart()
  {
   int cl_ctx;
//--- initialize OpenCL context
   if((cl_ctx=CLContextCreate(CL_USE_GPU_ONLY))==INVALID_HANDLE)
     {
      Print("OpenCL not found");
      return;
     }
//--- Display general information about OpenCL device
   Print("OpenCL type: ",EnumToString((ENUM_CL_DEVICE_TYPE)CLGetInfoInteger(cl_ctx,CL_DEVICE_TYPE)));
   Print("OpenCL vendor ID: ",CLGetInfoInteger(cl_ctx,CL_DEVICE_VENDOR_ID));
   Print("OpenCL units: ",CLGetInfoInteger(cl_ctx,CL_DEVICE_MAX_COMPUTE_UNITS));
   Print("OpenCL freq: ",CLGetInfoInteger(cl_ctx,CL_DEVICE_MAX_CLOCK_FREQUENCY)," MHz");
   Print("OpenCL global mem: ",CLGetInfoInteger(cl_ctx,CL_DEVICE_GLOBAL_MEM_SIZE)," bytes");
   Print("OpenCL local mem: ",CLGetInfoInteger(cl_ctx,CL_DEVICE_LOCAL_MEM_SIZE)," bytes");
//--- free OpenCL context
   CLContextFree(cl_ctx);
  }
```