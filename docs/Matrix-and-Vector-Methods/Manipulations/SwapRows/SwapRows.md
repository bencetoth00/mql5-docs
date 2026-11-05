# SwapRows

SwapRows

Swap rows in a matrix.

|  |
| --- |
| bool matrix::SwapRows(    const ulong  row1,     // index of first row    const ulong  row2      // index of second row     ); |

Parameters

row1

[in]  Index of the first row.

row2

[in]  Index of the second row.

Return Value

Returns true on success, false otherwise.

 

Example

|  |
| --- |
| matrix matrix\_a={{1,2,3,4},                      {5,6,7,8},                      {9,10,11,12},                      {13,14,15,16}};     matrix matrix\_i=matrix::Identity(4,4);     matrix matrix\_a1=matrix\_a;     matrix\_a1.SwapRows(0,3);     Print("matrix\_a1\n",matrix\_a1);        matrix matrix\_p=matrix\_i;     matrix\_p.SwapRows(0,3);     matrix matrix\_c1=matrix\_p.MatMul(matrix\_a);     Print("matrix\_c1\n",matrix\_c1);       /\*    matrix\_a1    [[13,14,15,16]     [5,6,7,8]     [9,10,11,12]     [1,2,3,4]]    matrix\_c1    [[13,14,15,16]     [5,6,7,8]     [9,10,11,12]     [1,2,3,4]]    \*/ |
