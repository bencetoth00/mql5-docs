# Sum

Sum

Return the sum of the matrix/vector elements which can also be performed for the given axis (axes).

|  |
| --- |
| double vector::Sum();     double matrix::Sum();     vector matrix::Sum(    const int  axis      // axis     ); |

Parameters

axis

[in]  Axis. 0 — horizontal axis, 1 — vertical axis.

Return Value

Sum of the matrix/vector elements which can also be performed for the given axis (axes).

 

Example

|  |
| --- |
| matrix matrix\_a={{10,3,2},{1,8,12},{6,5,4},{7,11,9}};     Print("matrix\_a\n",matrix\_a);        vector cols\_sum=matrix\_a.Sum(0);     vector rows\_sum=matrix\_a.Sum(1);     double matrix\_sum=matrix\_a.Sum();        Print("cols\_sum=",cols\_sum);     Print("rows\_sum=",rows\_sum);     Print("sum value ",matrix\_sum);        /\*     matrix\_a     [[10,3,2]      [1,8,12]      [6,5,4]      [7,11,9]]     cols\_sum=[24,27,27]     rows\_sum=[15,21,15,27]     sum value 78.0     \*/ |
