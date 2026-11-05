# CLGetDeviceInfo


The function receives device property from OpenCL driver.

```cpp
bool  CLGetDeviceInfo(
   int     handle,          // OpenCL device handle
   int     property_id,     // requested property ID
   uchar&  data[],          // array for receiving data
   uint&   size             // shift in the array elements, default value is 0
   );
```

Parameters

handle

[in]  OpenCL device index or OpenCL handle created by [CLContextCreate()](../CLContextCreate/CLContextCreate.md) function.

property\_id

[in]  ID of the OpenCL device property that should be received. The values can be of one of the predetermined ones listed in the [table below](CLGetDeviceInfo.md#openclpropertyids).

data[]

[out]  The array for receiving data on the requested property.

size

[out]  Size of the received data in the array data[].

Return Value

true if successful, otherwise false. For information about the error, use the [GetLastError()](../../Checkup/GetLastError/GetLastError.md) function.

Note

For one-dimensional arrays, the number of the element, from which data reading for OpenCL buffer starts, is calculated considering [AS\_SERIES](../../Array-Functions/ArrayGetAsSeries/ArrayGetAsSeries.md) flag.

The list of available IDs of OpenCL device properties

Exact description of the property and its functions can be found at [the official OpenCL web site](https://www.khronos.org/opencl/ "The official website of the OpenCL standard").

| Identifier | Value |
| --- | --- |
| CL\_DEVICE\_TYPE | 0x1000 |
| CL\_DEVICE\_VENDOR\_ID | 0x1001 |
| CL\_DEVICE\_MAX\_COMPUTE\_UNITS | 0x1002 |
| CL\_DEVICE\_MAX\_WORK\_ITEM\_DIMENSIONS | 0x1003 |
| CL\_DEVICE\_MAX\_WORK\_GROUP\_SIZE | 0x1004 |
| CL\_DEVICE\_MAX\_WORK\_ITEM\_SIZES | 0x1005 |
| CL\_DEVICE\_PREFERRED\_VECTOR\_WIDTH\_CHAR | 0x1006 |
| CL\_DEVICE\_PREFERRED\_VECTOR\_WIDTH\_SHORT | 0x1007 |
| CL\_DEVICE\_PREFERRED\_VECTOR\_WIDTH\_INT | 0x1008 |
| CL\_DEVICE\_PREFERRED\_VECTOR\_WIDTH\_LONG | 0x1009 |
| CL\_DEVICE\_PREFERRED\_VECTOR\_WIDTH\_FLOAT | 0x100A |
| CL\_DEVICE\_PREFERRED\_VECTOR\_WIDTH\_DOUBLE | 0x100B |
| CL\_DEVICE\_MAX\_CLOCK\_FREQUENCY | 0x100C |
| CL\_DEVICE\_ADDRESS\_BITS | 0x100D |
| CL\_DEVICE\_MAX\_READ\_IMAGE\_ARGS | 0x100E |
| CL\_DEVICE\_MAX\_WRITE\_IMAGE\_ARGS | 0x100F |
| CL\_DEVICE\_MAX\_MEM\_ALLOC\_SIZE | 0x1010 |
| CL\_DEVICE\_IMAGE2D\_MAX\_WIDTH | 0x1011 |
| CL\_DEVICE\_IMAGE2D\_MAX\_HEIGHT | 0x1012 |
| CL\_DEVICE\_IMAGE3D\_MAX\_WIDTH | 0x1013 |
| CL\_DEVICE\_IMAGE3D\_MAX\_HEIGHT | 0x1014 |
| CL\_DEVICE\_IMAGE3D\_MAX\_DEPTH | 0x1015 |
| CL\_DEVICE\_IMAGE\_SUPPORT | 0x1016 |
| CL\_DEVICE\_MAX\_PARAMETER\_SIZE | 0x1017 |
| CL\_DEVICE\_MAX\_SAMPLERS | 0x1018 |
| CL\_DEVICE\_MEM\_BASE\_ADDR\_ALIGN | 0x1019 |
| CL\_DEVICE\_MIN\_DATA\_TYPE\_ALIGN\_SIZE | 0x101A |
| CL\_DEVICE\_SINGLE\_FP\_CONFIG | 0x101B |
| CL\_DEVICE\_GLOBAL\_MEM\_CACHE\_TYPE | 0x101C |
| CL\_DEVICE\_GLOBAL\_MEM\_CACHELINE\_SIZE | 0x101D |
| CL\_DEVICE\_GLOBAL\_MEM\_CACHE\_SIZE | 0x101E |
| CL\_DEVICE\_GLOBAL\_MEM\_SIZE | 0x101F |
| CL\_DEVICE\_MAX\_CONSTANT\_BUFFER\_SIZE | 0x1020 |
| CL\_DEVICE\_MAX\_CONSTANT\_ARGS | 0x1021 |
| CL\_DEVICE\_LOCAL\_MEM\_TYPE | 0x1022 |
| CL\_DEVICE\_LOCAL\_MEM\_SIZE | 0x1023 |
| CL\_DEVICE\_ERROR\_CORRECTION\_SUPPORT | 0x1024 |
| CL\_DEVICE\_PROFILING\_TIMER\_RESOLUTION | 0x1025 |
| CL\_DEVICE\_ENDIAN\_LITTLE | 0x1026 |
| CL\_DEVICE\_AVAILABLE | 0x1027 |
| CL\_DEVICE\_COMPILER\_AVAILABLE | 0x1028 |
| CL\_DEVICE\_EXECUTION\_CAPABILITIES | 0x1029 |
| CL\_DEVICE\_QUEUE\_PROPERTIES | 0x102A |
| CL\_DEVICE\_NAME | 0x102B |
| CL\_DEVICE\_VENDOR | 0x102C |
| CL\_DRIVER\_VERSION | 0x102D |
| CL\_DEVICE\_PROFILE | 0x102E |
| CL\_DEVICE\_VERSION | 0x102F |
| CL\_DEVICE\_EXTENSIONS | 0x1030 |
| CL\_DEVICE\_PLATFORM | 0x1031 |
| CL\_DEVICE\_DOUBLE\_FP\_CONFIG | 0x1032 |
| CL\_DEVICE\_PREFERRED\_VECTOR\_WIDTH\_HALF | 0x1034 |
| CL\_DEVICE\_HOST\_UNIFIED\_MEMORY | 0x1035 |
| CL\_DEVICE\_NATIVE\_VECTOR\_WIDTH\_CHAR | 0x1036 |
| CL\_DEVICE\_NATIVE\_VECTOR\_WIDTH\_SHORT | 0x1037 |
| CL\_DEVICE\_NATIVE\_VECTOR\_WIDTH\_INT | 0x1038 |
| CL\_DEVICE\_NATIVE\_VECTOR\_WIDTH\_LONG | 0x1039 |
| CL\_DEVICE\_NATIVE\_VECTOR\_WIDTH\_FLOAT | 0x103A |
| CL\_DEVICE\_NATIVE\_VECTOR\_WIDTH\_DOUBLE | 0x103B |
| CL\_DEVICE\_NATIVE\_VECTOR\_WIDTH\_HALF | 0x103C |
| CL\_DEVICE\_OPENCL\_C\_VERSION | 0x103D |
| CL\_DEVICE\_LINKER\_AVAILABLE | 0x103E |
| CL\_DEVICE\_BUILT\_IN\_KERNELS | 0x103F |
| CL\_DEVICE\_IMAGE\_MAX\_BUFFER\_SIZE | 0x1040 |
| CL\_DEVICE\_IMAGE\_MAX\_ARRAY\_SIZE | 0x1041 |
| CL\_DEVICE\_PARENT\_DEVICE | 0x1042 |
| CL\_DEVICE\_PARTITION\_MAX\_SUB\_DEVICES | 0x1043 |
| CL\_DEVICE\_PARTITION\_PROPERTIES | 0x1044 |
| CL\_DEVICE\_PARTITION\_AFFINITY\_DOMAIN | 0x1045 |
| CL\_DEVICE\_PARTITION\_TYPE | 0x1046 |
| CL\_DEVICE\_REFERENCE\_COUNT | 0x1047 |
| CL\_DEVICE\_PREFERRED\_INTEROP\_USER\_SYNC | 0x1048 |
| CL\_DEVICE\_PRINTF\_BUFFER\_SIZE | 0x1049 |
| CL\_DEVICE\_IMAGE\_PITCH\_ALIGNMENT | 0x104A |
| CL\_DEVICE\_IMAGE\_BASE\_ADDRESS\_ALIGNMENT | 0x104B |

Example:

```cpp
void OnStart()
  {
//---
   int dCount= CLGetInfoInteger(0,CL_DEVICE_COUNT);
   for(int i = 0; i<dCount; i++)
     {
      int clCtx=CLContextCreate(i);
      if(clCtx == -1)
         Print("ERROR in CLContextCreate");
      string device;
      CLGetInfoString(clCtx,CL_DEVICE_NAME,device);
      Print(i,": ",device);
      uchar data[1024];
      uint size;
      CLGetDeviceInfo(clCtx,CL_DEVICE_VENDOR,data,size);
      Print("size = ",size);
      string str=CharArrayToString(data);
      Print(str);
     }
  }
//--- example of entries in Experts journal
//  2013.07.24 10:50:48     opencl (EURUSD,H1)      2: Advanced Micro Devices, Inc.
//  2013.07.24 10:50:48     opencl (EURUSD,H1)      size = 32
//  2013.07.24 10:50:48     opencl (EURUSD,H1)      Tahiti
//  2013.07.24 10:50:48     opencl (EURUSD,H1)      Intel(R) Corporation
//  2013.07.24 10:50:48     opencl (EURUSD,H1)      size = 21
//  2013.07.24 10:50:48     opencl (EURUSD,H1)      1:        Intel(R) Core(TM) i7-3770 CPU @ 3.40GHz
//  2013.07.24 10:50:48     opencl (EURUSD,H1)      NVIDIA Corporation
//  2013.07.24 10:50:48     opencl (EURUSD,H1)      size = 19
//  2013.07.24 10:50:48     opencl (EURUSD,H1)      0: GeForce GTX 580
```