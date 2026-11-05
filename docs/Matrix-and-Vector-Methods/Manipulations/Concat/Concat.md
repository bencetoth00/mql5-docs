# Concat

Concat

Concatenate 2 submatrices to one matrix. Concatenate 2 vectors to one vector.

|  |
| --- |
| vector vector::Concat(    const vector&  second\_part      // second vector to concatenate     );     vector matrix::Concat(    const matrix&  second\_part      // second matrix to concatenate     );     matrix matrix::Split(    const matrix&  second\_part,     // second matrix to concatenate    const int      axis             // axis     ); |

Parameters

second\_part

[in] Second vector or matrix to concatenate. If matrices are concatenated along any of the axes, then the sizes of the matrices must be consistent according to the axis.

axis

[in]  Axis. 0 - horizontal axis, 1 - vertical axis.

Return Value

Returns vector if vectors or matrices concatenated without axis parameter, or matrix concatenated along horizontal or vertical axis.

 

Example

|  |
| --- |
| vector vector\_a={1,2,3,4};     vector vector\_b={5,6,7};     vector vector\_c=vector\_a.Concat(vector\_b);     Print("vector\_c=",vector\_c);        matrix matrix\_a={{1,2,3},{4,5,6}};     matrix matrix\_b={{7,8,9},{10,11,12}};     vector\_c=matrix\_a.Concat(matrix\_b);     Print("vector\_c=",vector\_c);        matrix matrix\_c0=matrix\_a.Concat(matrix\_b,0);     Print("matrix\_c0=\n",matrix\_c0);        matrix matrix\_c1=matrix\_a.Concat(matrix\_b,1);     Print("matrix\_c1=\n",matrix\_c1);       /\*    vector\_c=[1,2,3,4,5,6,7]    vector\_c=[1,2,3,4,5,6,7,8,9,10,11,12]    matrix\_c0=    [[1,2,3]     [4,5,6]     [7,8,9]     [10,11,12]]    matrix\_c1=    [[1,2,3,7,8,9]     [4,5,6,10,11,12]]    \*/ |
