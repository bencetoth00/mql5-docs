# CLGetInfoString


Returns string value of a property for OpenCL object or device.

```cpp
bool  CLGetInfoString(
   int  handle,                           // OpenCL object handle or OpenCL device number
   ENUM_OPENCL_PROPERTY_STRING  prop,     // requested property
   string&  value                         // referenced string
   );
```

Parameters

handle

[in]  OpenCL object handle or OpenCL device number. The numbering of OpenCL devices starts with zero.

prop

[in]  Type of requested property from [ENUM\_OPENCL\_PROPERTY\_STRING](CLGetInfoString.md#enum_opencl_property_string) enumeration, the value of which should be obtained.

value

[out]  String for receiving the property value.

Return Value

true if successful, otherwise false. For information about the error, use the [GetLastError()](../../Checkup/GetLastError/GetLastError.md) function.

ENUM\_OPENCL\_PROPERTY\_STRING

| Identifier | Description |
| --- | --- |
| CL\_PLATFORM\_PROFILE | CL\_PLATFORM\_PROFILE - OpenCL Profile.  Profile name may be one of the following values:   - FULL\_PROFILE - implementation supports OpenCL (functionality is defined as the part of the kernel specification without requiring additional extensions for OpenCL support); - EMBEDDED\_PROFILE - implementation supports OpenCL as a supplement. Amended profile is defined as a subset for each OpenCL version. |
| CL\_PLATFORM\_VERSION | OpenCL version |
| CL\_PLATFORM\_VENDOR | Platform vendor name |
| CL\_PLATFORM\_EXTENSIONS | List of extensions supported by the platform. Extension names should be supported by all devices related to this platform |
| CL\_DEVICE\_NAME | Device name |
| CL\_DEVICE\_VENDOR | Vendor name |
| CL\_DRIVER\_VERSION | OpenCL driver version in major\_number.minor\_number format |
| CL\_DEVICE\_PROFILE | OpenCL device profile. Profile name may be one of the following values:   - FULL\_PROFILE - implementation supports OpenCL (functionality is defined as the part of the kernel specification without requiring additional extensions for OpenCL support); - EMBEDDED\_PROFILE - implementation supports OpenCL as a supplement. Amended profile is defined as a subset for each OpenCL version. |
| CL\_DEVICE\_VERSION | OpenCL version in "OpenCL<space><major\_version.minor\_version><space><vendor-specific information>" format |
| CL\_DEVICE\_EXTENSIONS | List of extensions supported by the device. The list may contain extensions supported by the vendor, as well as one or more approved names:     cl\_khr\_int64\_base\_atomics     cl\_khr\_int64\_extended\_atomics     cl\_khr\_fp16     cl\_khr\_gl\_sharing     cl\_khr\_gl\_event     cl\_khr\_d3d10\_sharing     cl\_khr\_dx9\_media\_sharing     cl\_khr\_d3d11\_sharing |
| CL\_DEVICE\_BUILT\_IN\_KERNELS | The list of supported kernels separated by ";". |
| CL\_DEVICE\_OPENCL\_C\_VERSION | The maximum version supported by the compiler for this device. Version format:  "OpenCL<space>C<space><major\_version.minor\_version><space><vendor-specific information> " |
| CL\_ERROR\_DESCRIPTION | Text description of an OpenCL error |

Example:

```cpp
void OnStart()
  {
   int cl_ctx;
   string str;
//--- initialize OpenCL context
   if((cl_ctx=CLContextCreate(CL_USE_GPU_ONLY))==INVALID_HANDLE)
     {
      Print("OpenCL not found");
      return;
     }
//--- Display information about the platform
   if(CLGetInfoString(cl_ctx,CL_PLATFORM_NAME,str))
      Print("OpenCL platform name: ",str);
   if(CLGetInfoString(cl_ctx,CL_PLATFORM_VENDOR,str))
      Print("OpenCL platform vendor: ",str);
   if(CLGetInfoString(cl_ctx,CL_PLATFORM_VERSION,str))
      Print("OpenCL platform ver: ",str);
   if(CLGetInfoString(cl_ctx,CL_PLATFORM_PROFILE,str))
      Print("OpenCL platform profile: ",str);
   if(CLGetInfoString(cl_ctx,CL_PLATFORM_EXTENSIONS,str))
      Print("OpenCL platform ext: ",str);
//--- Display information about the device
   if(CLGetInfoString(cl_ctx,CL_DEVICE_NAME,str))
      Print("OpenCL device name: ",str);
   if(CLGetInfoString(cl_ctx,CL_DEVICE_PROFILE,str))
      Print("OpenCL device profile: ",str);
   if(CLGetInfoString(cl_ctx,CL_DEVICE_BUILT_IN_KERNELS,str))
      Print("OpenCL device kernels: ",str);
   if(CLGetInfoString(cl_ctx,CL_DEVICE_EXTENSIONS,str))
      Print("OpenCL device ext: ",str);
   if(CLGetInfoString(cl_ctx,CL_DEVICE_VENDOR,str))
      Print("OpenCL device vendor: ",str);
   if(CLGetInfoString(cl_ctx,CL_DEVICE_VERSION,str))
      Print("OpenCL device ver: ",str);
   if(CLGetInfoString(cl_ctx,CL_DEVICE_OPENCL_C_VERSION,str))
      Print("OpenCL open c ver: ",str);
//--- Display general information about the OpenCL device
   Print("OpenCL type: ",EnumToString((ENUM_CL_DEVICE_TYPE)CLGetInfoInteger(cl_ctx,CL_DEVICE_TYPE)));
   Print("OpenCL vendor ID: ",CLGetInfoInteger(cl_ctx,CL_DEVICE_VENDOR_ID));
   Print("OpenCL units: ",CLGetInfoInteger(cl_ctx,CL_DEVICE_MAX_COMPUTE_UNITS));
   Print("OpenCL freq: ",CLGetInfoInteger(cl_ctx,CL_DEVICE_MAX_CLOCK_FREQUENCY));
   Print("OpenCL global mem: ",CLGetInfoInteger(cl_ctx,CL_DEVICE_GLOBAL_MEM_SIZE));
   Print("OpenCL local mem: ",CLGetInfoInteger(cl_ctx,CL_DEVICE_LOCAL_MEM_SIZE));
//--- free OpenCL context
   CLContextFree(cl_ctx);
  }
```