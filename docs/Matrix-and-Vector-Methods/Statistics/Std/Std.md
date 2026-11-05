# Std

Std

Return the standard deviation of values of matrix/vector elements or of elements along the given axis.

|  |
| --- |
| double vector::Std();     double vector::Std(    const int  ddof      // delta degrees of freedom  );     double matrix::Std();     vector matrix::Std(    const int  axis      // axis  );     vector matrix::Std(    const int  axis,     // axis    const int  ddof      // delta degrees of freedom  ); |

Parameters

axis

[in]  Axis. 0 — horizontal axis, 1 — vertical axis.

ddof

[in]  “Delta Degrees of Freedom”: the divisor used in the calculation is N - ddof, where N represents the number of elements. By default ddof is zero.

Return Value

Standard\_deviation: scalar or vector.

 

Note

The standard deviation is the square root of the average of the squared deviations from the mean, i. e., std = sqrt(mean(x)), where x = abs(a - a.mean())\*\*2.

The average squared deviation is typically calculated as x.sum() / (N - ddof), where N = len(x).

Expression with ddof=0 sometimes called the “population standard deviation”. If ddof>0 (most commonly used 1), the resulting quantity is sometimes called the “sample standard deviation”.

 

Example

|  |
| --- |
| matrixf matrix\_a={{10,3,2},{1,8,12},{6,5,4},{7,11,9}};     Print("matrix\_a\n",matrix\_a);        vectorf cols\_std=matrix\_a.Std(0);     vectorf rows\_std=matrix\_a.Std(1);     float matrix\_std=matrix\_a.Std();        Print("cols\_std ",cols\_std);     Print("rows\_std ",rows\_std);     Print("std value  ",matrix\_std);           /\*     matrix\_a     [[10,3,2]      [1,8,12]      [6,5,4]      [7,11,9]]     cols\_std [3.2403703,3.0310888,3.9607449]     rows\_std [3.5590262,4.5460606,0.81649661,1.6329932]     std value  3.452052593231201     \*/ |
