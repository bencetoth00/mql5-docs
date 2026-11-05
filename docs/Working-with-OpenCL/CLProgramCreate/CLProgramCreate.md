# CLProgramCreate

CLProgramCreate

Creates an OpenCL program from a source code.

|  |
| --- |
| int  CLProgramCreate(     int           context,     // Handle to an OpenCL context     const string  source       // Source code     ); |

An overloaded function version creates an OpenCL program and writes compiler messages into the passed string.

|  |
| --- |
| int  CLProgramCreate(     int           context,     // Handle to an OpenCL context     const string  source,      // Source code     string       &build\_log    // A string for receiving the compilation log     ); |

Parameters

context

[in]  Handle of the OpenCL context.

source

[in]  String with the source code of the OpenCL program.

&build\_log

[in]  A string for receiving the OpenCL compiler messages.

Return Value

A handle to an OpenCL object if successful. In case of error -1 is returned. For information about the error, use the [GetLastError()](../../Checkup/GetLastError/GetLastError.md) function.

Note

At the moment, the following error codes are used:

- ERR\_OPENCL\_INVALID\_HANDLE – invalid handle to the context OpenCL.
- ERR\_INVALID\_PARAMETER – invalid string parameter.
- ERR\_NOT\_ENOUGH\_MEMORY – not enough memory to complete operation.
- ERR\_OPENCL\_PROGRAM\_CREATE – internal error of OpenCL or compilation error.

In some graphic cards working with the [double](../../Language-Basics/Data-Types/Real-Types-(double,-float)/Real-Types-(double,-float).md) type numbers is disabled by default. This can lead to compilation error 5105. To enable support for the double type numbers, please add the following directive to your OpenCL program: [#pragma OPENCL EXTENSION cl\_khr\_fp64 : enable](https://www.khronos.org/registry/OpenCL/sdk/1.0/docs/man/xhtml/cl_khr_fp64.html).  However if a graphic card doesn't support double, enabling this directive won't be of help.

Example:

|  |
| --- |
| //+------------------------------------------------------------------+  //| OpenCL kernel                                                    |  //+------------------------------------------------------------------+  const string  cl\_src=         //--- by default some GPU doesn't support doubles         //--- cl\_khr\_fp64 directive is used to enable work with doubles         "#pragma OPENCL EXTENSION cl\_khr\_fp64 : enable      \r\n"         //--- OpenCL kernel function         "\_\_kernel void Test\_GPU(\_\_global double \*data,      \r\n"         "                       const    int N,             \r\n"         "                       const    int total\_arrays)  \r\n"         "  {                                                \r\n"         "   uint kernel\_index=get\_global\_id(0);             \r\n"         "   if (kernel\_index>total\_arrays) return;          \r\n"         "   uint local\_start\_offset=kernel\_index\*N;         \r\n"         "   for(int i=0; i<N; i++)                          \r\n"         "     {                                             \r\n"         "       data[i+local\_start\_offset] \*= 2.0;          \r\n"         "     }                                             \r\n"         "  }                                                \r\n";  //+------------------------------------------------------------------+  //| Test\_CPU                                                         |  //+------------------------------------------------------------------+  bool Test\_CPU(double &data[],const int N,const int id,const int total\_arrays)    {  //--- check array size     if(ArraySize(data)==0) return(false);  //--- check array index     if(id>total\_arrays) return(false);  //--- calculate local offset for array with index id     int local\_start\_offset=id\*N;  //--- multiply elements by 2     for(int i=0; i<N; i++)       {        data[i+local\_start\_offset]\*=2.0;       }     return true;    }  //---  #define ARRAY\_SIZE   100  // size of the array  #define TOTAL\_ARRAYS 5    // total arrays  //--- OpenCL handles  int cl\_ctx;  // OpenCL context handle  int cl\_prg;  // OpenCL program handle  int cl\_krn;  // OpenCL kernel handle  int cl\_mem;  // OpenCL buffer handle  //---  double DataArray1[]; // data array for CPU calculation  double DataArray2[]; // data array for GPU calculation  //+------------------------------------------------------------------+  //| Script program start function                                    |  //+------------------------------------------------------------------+  int OnStart()    {  //--- initialize OpenCL objects  //--- create OpenCL context     if((cl\_ctx=CLContextCreate())==INVALID\_HANDLE)       {        Print("OpenCL not found. Error=",GetLastError());        return(1);       }  //--- create OpenCL program     if((cl\_prg=CLProgramCreate(cl\_ctx,cl\_src))==INVALID\_HANDLE)       {        CLContextFree(cl\_ctx);        Print("OpenCL program create failed. Error=",GetLastError());        return(1);       }  //--- create OpenCL kernel     if((cl\_krn=CLKernelCreate(cl\_prg,"Test\_GPU"))==INVALID\_HANDLE)       {        CLProgramFree(cl\_prg);        CLContextFree(cl\_ctx);        Print("OpenCL kernel create failed. Error=",GetLastError());        return(1);       }  //--- create OpenCL buffer     if((cl\_mem=CLBufferCreate(cl\_ctx,ARRAY\_SIZE\*TOTAL\_ARRAYS\*sizeof(double),CL\_MEM\_READ\_WRITE))==INVALID\_HANDLE)       {        CLKernelFree(cl\_krn);        CLProgramFree(cl\_prg);        CLContextFree(cl\_ctx);        Print("OpenCL buffer create failed. Error=",GetLastError());        return(1);       }  //--- set OpenCL kernel constant parameters     CLSetKernelArgMem(cl\_krn,0,cl\_mem);     CLSetKernelArg(cl\_krn,1,ARRAY\_SIZE);     CLSetKernelArg(cl\_krn,2,TOTAL\_ARRAYS);  //--- prepare data arrays     ArrayResize(DataArray1,ARRAY\_SIZE\*TOTAL\_ARRAYS);     ArrayResize(DataArray2,ARRAY\_SIZE\*TOTAL\_ARRAYS);  //--- fill arrays with data     for(int j=0; j<TOTAL\_ARRAYS; j++)       {        //--- calculate local start offset for jth array        uint local\_offset=j\*ARRAY\_SIZE;        //--- prepare array with index j        for(int i=0; i<ARRAY\_SIZE; i++)          {           //--- fill arrays with function MathCos(i+j);           DataArray1[i+local\_offset]=MathCos(i+j);           DataArray2[i+local\_offset]=MathCos(i+j);          }       };  //--- test CPU calculation     for(int j=0; j<TOTAL\_ARRAYS; j++)       {        //--- calculation of the array with index j        Test\_CPU(DataArray1,ARRAY\_SIZE,j,TOTAL\_ARRAYS);       }  //--- prepare CLExecute params     uint  offset[]={0};  //--- global work size     uint  work[]={TOTAL\_ARRAYS};  //--- write data to OpenCL buffer     CLBufferWrite(cl\_mem,DataArray2);  //--- execute OpenCL kernel     CLExecute(cl\_krn,1,offset,work);  //--- read data from OpenCL buffer     CLBufferRead(cl\_mem,DataArray2);  //--- total error     double total\_error=0;  //--- compare results and calculate error     for(int j=0; j<TOTAL\_ARRAYS; j++)       {        //--- calculate local offset for jth array        uint local\_offset=j\*ARRAY\_SIZE;        //--- compare the results        for(int i=0; i<ARRAY\_SIZE; i++)          {           double v1=DataArray1[i+local\_offset];           double v2=DataArray2[i+local\_offset];           double delta=MathAbs(v2-v1);           total\_error+=delta;           //--- show first and last arrays           if((j==0) || (j==TOTAL\_ARRAYS-1))              PrintFormat("array %d of %d, element [%d]:  %f, %f, [error]=%f",j+1,TOTAL\_ARRAYS,i,v1,v2,delta);          }       }     PrintFormat("Total error: %f",total\_error);  //--- delete OpenCL objects  //--- free OpenCL buffer     CLBufferFree(cl\_mem);  //--- free OpenCL kernel     CLKernelFree(cl\_krn);  //--- free OpenCL program     CLProgramFree(cl\_prg);  //--- free OpenCL context     CLContextFree(cl\_ctx);  //---     return(0);    } |
