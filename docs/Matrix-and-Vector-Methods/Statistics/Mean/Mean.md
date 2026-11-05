# Mean

Mean

Compute the arithmetic mean of element values.

|  |
| --- |
| double vector::Mean();     double matrix::Mean();     vector matrix::Mean(    const int  axis      // axis     ); |

Parameters

axis

[in]  Axis. 0 — horizontal axis, 1 — vertical axis.

Return Value

Arithmetic mean of element values.

 

Example

|  |
| --- |
| matrixf matrix\_a={{10,3,2},{1,8,12},{6,5,4},{7,11,9}};     Print("matrix\_a\n",matrix\_a);        vectorf cols\_mean=matrix\_a.Mean(0);     vectorf rows\_mean=matrix\_a.Mean(1);     float matrix\_mean=matrix\_a.Mean();        Print("cols\_mean ",cols\_mean);     Print("rows\_mean ",rows\_mean);     Print("mean value  ",matrix\_mean);           /\*     matrix\_a     [[10,3,2]      [1,8,12]      [6,5,4]      [7,11,9]]     cols\_mean [6,6.75,6.75]     rows\_mean [5,7,5,9]     mean value  6.5     \*/ |
