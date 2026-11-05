# CumSum

CumSum

Return the cumulative sum of matrix/vector elements, including those along the given axis.

|  |
| --- |
| vector vector::CumSum();     vector matrix::CumSum();     matrix matrix::CumSum(    const int  axis      // axis     ); |

Parameters

axis

[in]  Axis. 0 — horizontal axis, 1 — vertical axis.

Return Value

Cumulative sum of the elements along the given axis.

 

Example

|  |
| --- |
| matrix matrix\_a={{10,3,2},{1,8,12},{6,5,4},{7,11,9}};     Print("matrix\_a\n",matrix\_a);        matrix cols\_cumsum=matrix\_a.CumSum(0);     matrix rows\_cumsum=matrix\_a.CumSum(1);     vector cumsum\_values=matrix\_a.CumSum();        Print("cols\_cumsum\n",cols\_cumsum);     Print("rows\_cumsum\n",rows\_cumsum);     Print("cumsum values  ",cumsum\_values);        /\*     matrix\_a     [[10,3,2]      [1,8,12]      [6,5,4]      [7,11,9]]     cols\_cumsum     [[10,3,2]      [11,11,14]      [17,16,18]      [24,27,27]]     rows\_cumsum     [[10,13,15]      [1,9,21]      [6,11,15]      [7,18,27]]     cumsum values  [10,13,15,16,24,36,42,47,51,58,69,78]     \*/ |
