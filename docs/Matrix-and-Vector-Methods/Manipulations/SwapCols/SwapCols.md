# SwapCols

SwapCols

Swap columns in a matrix.

|  |
| --- |
| bool matrix::SwapCols(    const ulong  row1,     // index of first column    const ulong  row2      // index of second column     ); |

Parameters

col1

[in]  Index of the first column.

col2

[in]  Index of the second column.

Return Value

Returns true on success, false otherwise.

 

Example

|  |
| --- |
| matrix matrix\_a={{1,2,3,4},                      {5,6,7,8},                      {9,10,11,12},                      {13,14,15,16}};     matrix matrix\_i=matrix::Identity(4,4);     matrix matrix\_a1=matrix\_a;     matrix\_a1.SwapCols(0,3);     Print("matrix\_a1\n",matrix\_a1);        matrix matrix\_p=matrix\_i;     matrix\_p.SwapCols(0,3);     matrix matrix\_c1=matrix\_a.MatMul(matrix\_p);     Print("matrix\_c1\n",matrix\_c1);       /\*    matrix\_a1    [[4,2,3,1]     [8,6,7,5]     [12,10,11,9]     [16,14,15,13]]    matrix\_c1    [[4,2,3,1]     [8,6,7,5]     [12,10,11,9]     [16,14,15,13]]    \*/ |
