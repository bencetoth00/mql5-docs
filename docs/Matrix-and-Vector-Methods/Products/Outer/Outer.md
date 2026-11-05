# Outer

Outer

Compute the outer product of two matrices or two vectors.

|  |
| --- |
| matrix matrix::Outer(    const matrix&  b      // second matrix     );     matrix vector::Outer(    const vector&  b      // second vector     ); |

Parameters

b

[in]  Matrix.

Return Value

Matrix.

 

Note

The outer product, like the Kronecker product, is also a block matrix (and vector) multiplication.

 

A simple algorithm for the outer product of two matrices in MQL5:

|  |
| --- |
| matrix MatrixOuter(const matrix& matrix\_a, const matrix& matrix\_b)    {  //--- size of the resulting matrix depends on the matrix sizes     ulong  rows=matrix\_a.Rows()\*matrix\_a.Cols();     ulong  cols=matrix\_b.Rows()\*matrix\_b.Cols();     matrix matrix\_c(rows,cols);     ulong  cols\_a=matrix\_a.Cols();     ulong  cols\_b=matrix\_b.Cols();  //---     for(ulong i=0; i<rows; i++)       {        ulong row\_a=i/cols\_a;        ulong col\_a=i%cols\_a;        for(ulong j=0; j<cols; j++)          {           ulong row\_b=j/cols\_b;           ulong col\_b=j%cols\_b;           matrix\_c[i][j]=matrix\_a[row\_a][col\_a] \* matrix\_b[row\_b][col\_b];          }       }  //---     return(matrix\_c);    } |

 

MQL5 example:

|  |
| --- |
| vector vector\_a={0,1,2,3,4,5};     vector vector\_b={0,1,2,3,4,5,6};     Print("vector\_a.Outer\n",vector\_a.Outer(vector\_b));     Print("vector\_a.Kron\n",vector\_a.Kron(vector\_b));        matrix matrix\_a={{0,1,2},{3,4,5}};     matrix matrix\_b={{0,1,2},{3,4,5},{6,7,8}};     Print("matrix\_a.Outer\n",matrix\_a.Outer(matrix\_b));     Print("matrix\_a.Kron\n",matrix\_a.Kron(matrix\_b));       /\*     vector\_a.Outer     [[0,0,0,0,0,0,0]      [0,1,2,3,4,5,6]      [0,2,4,6,8,10,12]      [0,3,6,9,12,15,18]      [0,4,8,12,16,20,24]      [0,5,10,15,20,25,30]]     vector\_a.Kron     [[0,0,0,0,0,0,0,0,1,2,3,4,5,6,0,2,4,6,8,10,12,0,3,6,9,12,15,18,0,4,8,12,16,20,24,0,5,10,15,20,25,30]]     matrix\_a.Outer     [[0,0,0,0,0,0,0,0,0]      [0,1,2,3,4,5,6,7,8]      [0,2,4,6,8,10,12,14,16]      [0,3,6,9,12,15,18,21,24]      [0,4,8,12,16,20,24,28,32]      [0,5,10,15,20,25,30,35,40]]     matrix\_a.Kron     [[0,0,0,0,1,2,0,2,4]      [0,0,0,3,4,5,6,8,10]      [0,0,0,6,7,8,12,14,16]      [0,3,6,0,4,8,0,5,10]      [9,12,15,12,16,20,15,20,25]      [18,21,24,24,28,32,30,35,40]]     \*/ |

 

Python example:

|  |
| --- |
| import numpy as np     A = np.arange(6)  B = np.arange(7)  print("np.outer")  print(np.outer(A, B))  print("np.kron")  print(np.kron(A, B))     A = np.arange(6).reshape(2, 3)  B = np.arange(9).reshape(3, 3)  print("np.outer")  print(np.outer(A, B))  print("np.kron")     np.outer  [[ 0  0  0  0  0  0  0]   [ 0  1  2  3  4  5  6]   [ 0  2  4  6  8 10 12]   [ 0  3  6  9 12 15 18]   [ 0  4  8 12 16 20 24]   [ 0  5 10 15 20 25 30]]  np.kron  [ 0  0  0  0  0  0  0  0  1  2  3  4  5  6  0  2  4  6  8 10 12  0  3  6    9 12 15 18  0  4  8 12 16 20 24  0  5 10 15 20 25 30]  np.outer  [[ 0  0  0  0  0  0  0  0  0]   [ 0  1  2  3  4  5  6  7  8]   [ 0  2  4  6  8 10 12 14 16]   [ 0  3  6  9 12 15 18 21 24]   [ 0  4  8 12 16 20 24 28 32]   [ 0  5 10 15 20 25 30 35 40]]  np.kron  [[ 0  0  0  0  1  2  0  2  4]   [ 0  0  0  3  4  5  6  8 10]   [ 0  0  0  6  7  8 12 14 16]   [ 0  3  6  0  4  8  0  5 10]   [ 9 12 15 12 16 20 15 20 25]   [18 21 24 24 28 32 30 35 40]] |
