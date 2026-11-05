# Percentile

Percentile

Return the specified percentile of values of matrix/vector elements or elements along the specified axis.

|  |
| --- |
| double vector::Percentile(    const int  percent      //      );     double matrix::Percentile(    const int  percent      //      );     vector matrix::Percentile(    const int  percent,     //     const int  axis         // axis     ); |

Parameters

percent

[in]  Percentiles to compute, which must be between 0 and 100 inclusive.

axis

[in]  Axis. 0 — horizontal axis, 1 — vertical axis.

Return Value

Percentile: scalar or vector.

Note

Valid values of the 'percent' parameter are in the range [0, 100]. A linear algorithm is used to calculate percentiles. The correct calculation of percentiles requires the sequence to be sorted.

 

Example

|  |
| --- |
| matrixf matrix\_a={{1,2,3},{4,5,6},{7,8,9},{10,11,12}};     Print("matrix\_a\n",matrix\_a);        vectorf cols\_percentile=matrix\_a.Percentile(50,0);     vectorf rows\_percentile=matrix\_a.Percentile(50,1);     float matrix\_percentile=matrix\_a.Percentile(50);        Print("cols\_percentile ",cols\_percentile);     Print("rows\_percentile ",rows\_percentile);     Print("percentile value  ",matrix\_percentile);           /\*     matrix\_a     [[1,2,3]      [4,5,6]      [7,8,9]      [10,11,12]]     cols\_percentile [5.5,6.5,7.5]     rows\_percentile [2,5,8,11]     percentile value  6.5     \*/ |
