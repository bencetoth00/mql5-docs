# Initialization

Initialization

There are several ways to declare and initialize matrices and vectors.

| Function | Action |
| --- | --- |
| [Assign](Assign/Assign.md) | Copies a matrix, vector or array with auto cast |
| [CopyIndicatorBuffer](CopyIndicatorBuffer/CopyIndicatorBuffer.md) | Get the data of the specified [indicator](../../Technical-Indicators/Technical-Indicators.md) buffer in the specified quantity to a [vector](../../Language-Basics/Data-Types/Matrices-and-vectors/Matrices-and-vectors.md) |
| [CopyRates](CopyRates/CopyRates.md) | Gets the historical series of the [MqlRates](../../Constants,-Enumerations-and-Structures/Data-Structures/History-Data-Structure/History-Data-Structure.md) structure of the specified symbol-period in the specified amount into a matrix or vector |
| [CopyTicks](CopyTicks/CopyTicks.md) | Get ticks from an [MqlTick](../../Constants,-Enumerations-and-Structures/Data-Structures/Price-Data-Structure/Price-Data-Structure.md) structure into a matrix or a vector |
| [CopyTicksRange](CopyTicksRange/CopyTicksRange.md) | Get ticks from an [MqlTick](../../Constants,-Enumerations-and-Structures/Data-Structures/Price-Data-Structure/Price-Data-Structure.md) structure into a matrix or a vector within the specified date range |
| [Eye](Eye/Eye.md) | Return a matrix with ones on the diagonal and zeros elsewhere |
| [Identity](Identity/Identity.md) | Create an identity matrix of the specified size |
| [Ones](Ones/Ones.md) | Create and return a new matrix filled with ones |
| [Zeros](Zeros/Zeros.md) | Create and return a new matrix filled with zeros |
| [Full](Full/Full.md) | Create and return a new matrix filled with given value |
| [Tri](Tri/Tri.md) | Construct a matrix with ones at and below the given diagonal and zeros elsewhere |
| [Init](Init/Init.md) | Initialize a matrix or a vector |
| [Fill](Fill/Fill.md) | Fill an existing matrix or vector with the specified value |
| [Random](Random/Random.md) | Static function. Create and return a new matrix or vector filled with random values. Random values are generated uniformly within the specified range |

Declaration without specifying the size (no memory allocation for the data):

|  |
| --- |
| matrix         matrix\_a;   // double type matrix    matrix<double> matrix\_a1;  // another way to declare a double matrix; can be used in templates    matrixf        matrix\_a2;  // float matrix    matrix<float>  matrix\_a3;  // float matrix    vector         vector\_a;   // double vector    vector<double> vector\_a1;    vectorf        vector\_a2;  // float vector    vector<float>  vector\_a3; |

 

Declaration with the specified size (with memory allocation for the data, but without any initialization):

|  |
| --- |
| matrix         matrix\_a(128,128);           // the parameters can be either constants    matrix<double> matrix\_a1(InpRows,InpCols);  // or variables    matrixf        matrix\_a2(1,128);            // analog of a horizontal vector    matrix<float>  matrix\_a3(InpRows,1);        // analog of a vertical vector    vector         vector\_a(256);    vector<double> vector\_a1(InpSize);    vectorf        vector\_a2(SomeFunc());       // function SomeFunc returns a number of type ulong, which is used to set the vector size    vector<float>  vector\_a3(InpSize+16);       // expression can be used as a parameter |

 

Declaration with initialization (matrix and vector sizes are determined by the initializing sequence):

|  |
| --- |
| matrix         matrix\_a={{0.1,0.2,0.3},{0.4,0.5,0.6}};    matrix<double> matrix\_a1=matrix\_a;                      // must be matrices of the same type    matrixf        matrix\_a2={{1,0,0},{0,1,0},{0,0,1}};    matrix<float>  matrix\_a3={{1,2},{3,4}};    vector         vector\_a={-5,-4,-3,-2,-1,0,1,2,3,4,5};    vector<double> vector\_a1={1,5,2.4,3.3};    vectorf        vector\_a2={0,1,2,3};    vector<float>  vector\_a3=vector\_a2;                     // must be vectors of the same type |

 

Declaration with initialization:

|  |
| --- |
| template<typename T>  void MatrixArange(matrix<T> &mat,T value=0.0,T step=1.0)    {     for(ulong i=0; i<mat.Rows(); i++)       {        for(ulong j=0; j<mat.Cols(); j++,value+=step)           mat[i][j]=value;       }    }  template<typename T>  void VectorArange(vector<T> &vec,T value=0.0,T step=1.0)    {     for(ulong i=0; i<vec.Size(); i++,value+=step)        vec[i]=value;    }  ...       matrix  matrix\_a(size\_m,size\_k,MatrixArange,-M\_PI,0.1); // first an uninitialized matrix sized size\_m x size\_k is created, then function MatrixArange with the parameters specified at initialization is called    matrixf matrix\_a1(10,20,MatrixArange);                  // after creating the matrix, function MatrixArange with default parameters is called    vector  vector\_a(size,VectorArange,-10.0);              // after creating the vector, function VectorArange with one parameter is called while the second parameter is default    vectorf vector\_a1(128,VectorArange); |

 

Please note that the matrix or vector dimensions can be changed, since the memory for data is always dynamic.

Static methods

Static methods for creating matrices and vectors of the specified size, initialized in a certain way:

|  |
| --- |
| matrix         matrix\_a =matrix::Eye(4,5,1);    matrix<double> matrix\_a1=matrix::Full(3,4,M\_PI);    matrixf        matrix\_a2=matrixf::Identity(5,5);    matrixf<float> matrix\_a3=matrixf::Ones(5,5);    matrix         matrix\_a4=matrix::Tri(4,5,-1);    vector         vector\_a =vector::Ones(256);    vectorf        vector\_a1=vector<float>::Zeros(16);    vector<float>  vector\_a2=vectorf::Full(128,float\_value); |

 

Methods for initializing already created matrices and vectors:

|  |
| --- |
| matrix  matrix\_a;    matrix\_a.Init(size\_m,size\_k,MatrixArange,-M\_PI,0.1);    matrixf matrix\_a1(3,4);    matrix\_a1.Init(10,20,MatrixArange);    vector  vector\_a;    vector\_a.Init(128,VectorArange);    vectorf vector\_a1(10);    vector\_a1.Init(vector\_size,VectorArange,start\_value,step);       matrix\_a.Fill(double\_value);    vector\_a1.Fill(FLT\_MIN);    matrix\_a1.Identity(); |
