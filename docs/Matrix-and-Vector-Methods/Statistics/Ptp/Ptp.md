# Ptp

Ptp

Return the range of values of a matrix/vector or of the given matrix axis, equivalent to Max() - Min(). Ptp - Peak to peak.

|  |
| --- |
| double vector::Ptp();     double matrix::Ptp();     vector matrix::Ptp(    const int  axis      // axis     ); |

Parameters

axis

[in]  Axis. 0 — horizontal axis, 1 — vertical axis.

Return Value

Vector with ranges of values (maximum - minimum) .

 

Example

|  |
| --- |
| matrix matrix\_a={{10,3,2},{1,8,12},{6,5,4},{7,11,9}};     Print("matrix\_a\n",matrix\_a);        vector cols\_ptp=matrix\_a.Ptp(0);     vector rows\_ptp=matrix\_a.Ptp(1);     double matrix\_ptp=matrix\_a.Ptp();        Print("cols\_ptp  ",cols\_ptp);     Print("rows\_ptp  ",rows\_ptp);     Print("ptp value  ",matrix\_ptp);        /\*     matrix\_a     [[10,3,2]      [1,8,12]      [6,5,4]      [7,11,9]]     cols\_ptp [9,8,10]     rows\_ptp [8,11,2,4]     ptp value  11.0     \*/ |
