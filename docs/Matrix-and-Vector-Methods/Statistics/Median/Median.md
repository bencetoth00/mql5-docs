# Median

Median

Compute the median of the matrix/vector elements.

|  |
| --- |
| double vector::Median();     double matrix::Median();     vector matrix::Median(    const int  axis      // axis     ); |

Parameters

axis

[in]  Axis. 0 — horizontal axis, 1 — vertical axis.

Return Value

Median: scalar or vector.

 

Note

The median is the middle value that separates the highest half of the array/vector elements from the lowest half of elements. Same as Quantile(0.5) and Percentile(50). The correct calculation of median requires the sequence to be sorted.

 

Example

|  |
| --- |
| matrixf matrix\_a={{1,2,3},{4,5,6},{7,8,9},{10,11,12}};     Print("matrix\_a\n",matrix\_a);        vectorf cols\_median=matrix\_a.Median(0);     vectorf rows\_median=matrix\_a.Median(1);     float matrix\_median=matrix\_a.Median();        Print("cols\_median ",cols\_median);     Print("rows\_median ",rows\_median);     Print("median value  ",matrix\_median);           /\*     matrix\_a     [[1,2,3]      [4,5,6]      [7,8,9]      [10,11,12]]     cols\_median [5.5,6.5,7.5]     rows\_median [2,5,8,11]     median value  6.5     \*/ |
