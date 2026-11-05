# LU

LU

LU factorization of a matrix as the product of a lower triangular matrix and an upper triangular matrix.

|  |
| --- |
| bool matrix::LU(    matrix&  L,     // lower triangular matrix    matrix&  U      // upper triangular matrix     ); |

Parameters

L key

[out]  Lower triangular matrix.

U

[out]  Upper triangular matrix.

Return Value

Returns true on success, false otherwise.

 

Example

|  |
| --- |
| matrix matrix\_a={{1,2,3,4},                      {5,2,6,7},                      {8,9,3,10},                      {11,12,14,4}};     matrix matrix\_l,matrix\_u;  //--- LU decomposition     matrix\_a.LU(matrix\_l,matrix\_u);     Print("matrix\_l\n",matrix\_l);     Print("matrix\_u\n",matrix\_u);  //--- check if A = L \* U     Print("check\n",matrix\_l.MatMul(matrix\_u));           /\*     matrix\_l     [[1,0,0,0]      [5,1,0,0]      [8,0.875,1,0]      [11,1.25,0.5904761904761905,1]]     matrix\_u     [[1,2,3,4]      [0,-8,-9,-13]      [0,0,-13.125,-10.625]      [0,0,0,-17.47619047619047]]     check     [[1,2,3,4]      [5,2,6,7]      [8,9,3,10]      [11,12,14,4]]     \*/ |
