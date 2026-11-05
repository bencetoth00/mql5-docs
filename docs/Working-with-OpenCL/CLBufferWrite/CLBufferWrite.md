# CLBufferWrite

CLBufferWrite

Writes into the OpenCL buffer and returns the number of written elements.

|  |
| --- |
| uint  CLBufferWrite(     int          buffer,                    // A handle to the OpenCL buffer     const void&  data[],                    // An array of values     uint         buffer\_offset=0,           // An offset in the OpenCL buffer in bytes, 0 by default     uint         data\_offset=0,             // An offset in the array in elements, 0 by default     uint         data\_count=WHOLE\_ARRAY     // The number of values from the array for writing, the whole array by default     ); |

There are also versions for handling [matrices and vectors](../../Matrix-and-Vector-Methods/Matrix-and-Vector-Methods.md).

Writes the values from the matrix to the buffer and returns true if successful.

|  |
| --- |
| uint  CLBufferWrite(     int           buffer,                    // a handle to the OpenCL buffer     uint          buffer\_offset,             // an offset in the OpenCL buffer in bytes     matrix<T>     &mat                       // the values matrix for writing to the buffer     ); |

Writes the values from the vector to the buffer and returns true if successful.

|  |
| --- |
| uint  CLBufferWrite(     int           buffer,                    // a handle to the OpenCL buffer     uint          buffer\_offset,             // an offset in the OpenCL buffer in bytes     vector<T>     &vec                       // the values vector for writing to the buffer     ); |

Parameters

buffer

[in]  A handle of the OpenCL buffer.

data[]

[in]  An array of values that should be written in the OpenCL buffer. Passed by reference.

buffer\_offset

[in]  An offset in the OpenCL buffer in bytes, from which writing begins. By default, writing start with the very beginning of the buffer.

data\_offset

[in]  The index of the first array element, starting from which values from the array are written in the OpenCL buffer. By default, values from the very beginning of the array are taken.

data\_count

[in]  The number of values that should be written. All the values of the array, by default.

mat

[out]  The matrix for reading data from the buffer can be any of the three types — matrix, matrixf or matrixc.

vec

[out]  The vector for reading data from the buffer can be of any of the three types — vector, vectorf or vectorc.

Return Value

The number of written elements. 0 is returned in case of an error. For information about the error, use the [GetLastError()](../../Checkup/GetLastError/GetLastError.md) function.

true if a matrix or a vector is handled successfully, otherwise false.

Note

For one-dimensional arrays, the number of the element, with which reading of data for writing into an OpenCL buffer begins, is calculated taking into account the [AS\_SERIES](../../Array-Functions/ArrayGetAsSeries/ArrayGetAsSeries.md) flags.

An array of two or more dimensions is presented as one-dimensional. In this case, data\_offset is the number of elements that should be skipped in the presentation, not the number of elements in the first dimension.

 

Example of matrix multiplication using the [MatMul](../../Matrix-and-Vector-Methods/Products/MatMul/MatMul.md) method and parallel computing in OpenCL

|  |
| --- |
| #define M       3000      // the number of rows in the first matrix  #define K       2000      // the number of columns in the first matrix is equal to the number of rows in the second one   #define N       3000      // the number of columns in the second matrix     //+------------------------------------------------------------------+  const string clSrc=    "#define N     "+IntegerToString(N)+"                              \r\n"    "#define K     "+IntegerToString(K)+"                              \r\n"    "                                                                  \r\n"    "\_\_kernel void matricesMul( \_\_global float \*in1,                   \r\n"    "                           \_\_global float \*in2,                   \r\n"    "                           \_\_global float \*out  )                 \r\n"    "{                                                                 \r\n"    "  int m = get\_global\_id( 0 );                                     \r\n"    "  int n = get\_global\_id( 1 );                                     \r\n"    "  float sum = 0.0;                                                \r\n"    "  for( int k = 0; k < K; k ++ )                                   \r\n"    "     sum += in1[ m \* K + k ] \* in2[ k \* N + n ];                  \r\n"    "  out[ m \* N + n ] = sum;                                         \r\n"    "}                                                                 \r\n";  //+------------------------------------------------------------------+  //| Script program start function                                    |  //+------------------------------------------------------------------+  void OnStart()   {  //--- initialize the random number generator    MathSrand((int)TimeCurrent());  //--- fill in the matrices of a given size with random values    matrixf mat1(M, K, MatrixRandom) ;    // first matrix    matrixf mat2(K, N, MatrixRandom);     // second matrix     //--- calculate the product of matrices using naive method    uint start=GetTickCount();    matrixf matrix\_naive=matrixf::Zeros(M, N);// the result of multiplying two matrices is set here    for(int m=0; m<M; m++)      for(int k=0; k<K; k++)        for(int n=0; n<N; n++)          matrix\_naive[m][n]+=mat1[m][k]\*mat2[k][n];    uint time\_naive=GetTickCount()-start;            //--- calculate the product of matrices via MatMull    start=GetTickCount();    matrixf matrix\_matmul=mat1.MatMul(mat2);    uint time\_matmul=GetTickCount()-start;           //--- calculate the product of matrices in OpenCL    matrixf matrix\_opencl=matrixf::Zeros(M, N);    int cl\_ctx;             // context handle    if((cl\_ctx=CLContextCreate(CL\_USE\_GPU\_ONLY))==INVALID\_HANDLE)     {      Print("OpenCL not found, leaving");      return;     }    int cl\_prg;             // program handle     int cl\_krn;             // kernel handle    int cl\_mem\_in1;         // first (input) buffer handle    int cl\_mem\_in2;         // second (input) buffer handle    int cl\_mem\_out;         // third (output) buffer handle  //--- create the program and the kernel    cl\_prg = CLProgramCreate(cl\_ctx, clSrc);    cl\_krn = CLKernelCreate(cl\_prg, "matricesMul");  //--- create all three buffers for three matrices    cl\_mem\_in1=CLBufferCreate(cl\_ctx, M\*K\*sizeof(float), CL\_MEM\_READ\_WRITE);    cl\_mem\_in2=CLBufferCreate(cl\_ctx, K\*N\*sizeof(float), CL\_MEM\_READ\_WRITE);  //--- third matrix - output    cl\_mem\_out=CLBufferCreate(cl\_ctx, M\*N\*sizeof(float), CL\_MEM\_READ\_WRITE);  //--- set the kernel arguments    CLSetKernelArgMem(cl\_krn, 0, cl\_mem\_in1);    CLSetKernelArgMem(cl\_krn, 1, cl\_mem\_in2);    CLSetKernelArgMem(cl\_krn, 2, cl\_mem\_out);  //--- write matrices to the device buffers    CLBufferWrite(cl\_mem\_in1, 0, mat1);    CLBufferWrite(cl\_mem\_in2, 0, mat2);    CLBufferWrite(cl\_mem\_out, 0, matrix\_opencl);  //--- OpenCL code execution time start    start=GetTickCount();  //--- set the parameters of the task working area and execute the OpenCL program    uint  offs[2] = {0, 0};    uint works[2] = {M, N};    start=GetTickCount();      bool ex=CLExecute(cl\_krn, 2, offs, works);  //--- calculate the result to the matrix    if(CLBufferRead(cl\_mem\_out, 0, matrix\_opencl))      PrintFormat("[%d x %d] matrix read: ", matrix\_opencl.Rows(), matrix\_opencl.Cols());     else        Print("CLBufferRead(cl\_mem\_out, 0, matrix\_opencl failed. Error ",GetLastError());     uint time\_opencl=GetTickCount()-start;       Print("Compare calculation time using each method");    PrintFormat("Naive product time = %d ms",time\_naive);    PrintFormat("MatMul product time = %d ms",time\_matmul);    PrintFormat("OpenCl product time = %d ms",time\_opencl);    //--- release all OpenCL contexts    CLFreeAll(cl\_ctx, cl\_prg, cl\_krn, cl\_mem\_in1, cl\_mem\_in2, cl\_mem\_out);     //--- compare all obtained result matrices with each other    Print("How many discrepancy errors are there between result matrices?");    ulong errors=matrix\_naive.Compare(matrix\_matmul,(float)1e-12);    Print("matrix\_direct.Compare(matrix\_matmul,1e-12)=",errors);    errors=matrix\_matmul.Compare(matrix\_opencl,float(1e-12));    Print("matrix\_matmul.Compare(matrix\_opencl,1e-12)=",errors);  /\*    Result:          [3000 x 3000] matrix read:     Compare the time of calculation with each method     Naive product time = 54750 ms     MatMul product time = 4578 ms     OpenCl product time = 922 ms     How many discrepancy errors are there between result matrices?     matrix\_direct.Compare(matrix\_matmul,1e-12)=0     matrix\_matmul.Compare(matrix\_opencl,1e-12)=0  \*/     }  //+------------------------------------------------------------------+  //| Fills the matrix with random values                              |  //+------------------------------------------------------------------+  void MatrixRandom(matrixf& m)   {    for(ulong r=0; r<m.Rows(); r++)     {      for(ulong c=0; c<m.Cols(); c++)       {        m[r][c]=(float)((MathRand()-16383.5)/32767.);       }     }   }  //+------------------------------------------------------------------+  //| Release all OpenCL contexts                                      |  //+------------------------------------------------------------------+  void CLFreeAll(int cl\_ctx, int cl\_prg, int cl\_krn,                 int cl\_mem\_in1, int cl\_mem\_in2, int cl\_mem\_out)   {  //--- delete all contexts created by OpenCL in reverse order    CLBufferFree(cl\_mem\_in1);    CLBufferFree(cl\_mem\_in2);    CLBufferFree(cl\_mem\_out);    CLKernelFree(cl\_krn);    CLProgramFree(cl\_prg);    CLContextFree(cl\_ctx);   } |
