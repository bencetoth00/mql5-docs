# Min

Min

Return the minimum value in a matrix/vector.

|  |
| --- |
| double vector::Min();     double matrix::Min();     vector matrix::Min(    const int  axis      // axis     ); |

Parameters

axis

[in]  Axis. 0 — horizontal axis, 1 — vertical axis.

Return Value

Minimum value in a matrix/vector.

 

Example

|  |
| --- |
| matrix matrix\_a={{10,3,2},{1,8,12},{6,5,4},{7,11,9}};     Print("matrix\_a\n",matrix\_a);        vector cols\_min=matrix\_a.Min(0);     vector rows\_min=matrix\_a.Min(1);     double matrix\_min=matrix\_a.Min();        Print("cols\_min=",cols\_min);     Print("rows\_min=",rows\_min);     Print("min value ",matrix\_min);        /\*     matrix\_a     [[10,3,2]      [1,8,12]      [6,5,4]      [7,11,9]]     cols\_min=[1,3,2]     rows\_min=[2,1,4,7]     min value 1.0     \*/ |
