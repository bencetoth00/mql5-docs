# Max

Max

Return the maximum value in a matrix/vector.

|  |
| --- |
| double vector::Max();     double matrix::Max();     vector matrix::Max(    const int  axis      // axis     ); |

Parameters

axis

[in]  Axis. 0 — horizontal axis, 1 — vertical axis.

Return Value

Maximum value in a matrix/vector.

 

Example

|  |
| --- |
| matrix matrix\_a={{10,3,2},{1,8,12},{6,5,4},{7,11,9}};     Print("matrix\_a\n",matrix\_a);        vector cols\_max=matrix\_a.Max(0);     vector rows\_max=matrix\_a.Max(1);     double matrix\_max=matrix\_a.Max();        Print("cols\_max=",cols\_max);     Print("rows\_max=",rows\_max);     Print("max value ",matrix\_max);        /\*     matrix\_a     [[10,3,2]      [1,8,12]      [6,5,4]      [7,11,9]]     cols\_max=[10,11,12]     rows\_max=[10,12,6,11]     max value 12.0     \*/ |
