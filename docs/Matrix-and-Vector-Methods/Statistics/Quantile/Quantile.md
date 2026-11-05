# Quantile

Quantile

Return the specified quantile of values of matrix/vector elements or elements along the specified axis.

|  |
| --- |
| double vector::Quantile(    const double quantile      // quantile     );     double matrix::Quantile(    const double quantile      // quantile     );     vector matrix::Quantile(    const double quantile,     // quantile    const int    axis          // axis     ); |

Parameters

quantile

[in]  Quantile to compute, which must be between 0 and 1 inclusive.

axis

[in]  Axis. 0 — horizontal axis, 1 — vertical axis.

Return Value

Quantile: scalar or vector.

Note

The 'quantile' parameter takes values in the range [0, 1]. A linear algorithm is used to calculate quantiles. The correct calculation of quantiles requires the sequence to be sorted.

 

Example

|  |
| --- |
| matrixf matrix\_a={{1,2,3},{4,5,6},{7,8,9},{10,11,12}};     Print("matrix\_a\n",matrix\_a);        vectorf cols\_quantile=matrix\_a.Quantile(0.5,0);     vectorf rows\_quantile=matrix\_a.Quantile(0.5,1);     float matrix\_quantile=matrix\_a.Quantile(0.5);        Print("cols\_quantile ",cols\_quantile);     Print("rows\_quantile ",rows\_quantile);     Print("quantile value  ",matrix\_quantile);        /\*     matrix\_a     [[1,2,3]      [4,5,6]      [7,8,9]      [10,11,12]]     cols\_quantile [5.5,6.5,7.5]     rows\_quantile [2,5,8,11]     quantile value  6.5     \*/ |
