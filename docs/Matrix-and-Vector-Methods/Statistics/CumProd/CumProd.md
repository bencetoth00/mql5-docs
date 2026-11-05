# CumProd

CumProd

Return the cumulative product of matrix/vector elements, including those along the given axis.

|  |
| --- |
| vector vector::CumProd();     vector matrix::CumProd();     matrix matrix::CumProd(    const int  axis      // axis     ); |

Parameters

axis

[in]  Axis. 0 — horizontal axis for each column (i.e., over the rows), 1 — vertical axis for each row (i.e. over the columns)

Return Value

Cumulative product of the elements along the given axis.

 

Example

|  |
| --- |
| matrix matrix\_a={{10,3,2},{1,8,12},{6,5,4},{7,11,9}};     Print("matrix\_a\n",matrix\_a);        matrix cols\_cumprod=matrix\_a.CumProd(0);     matrix rows\_cumprod=matrix\_a.CumProd(1);     vector cumprod\_values=matrix\_a.CumProd();        Print("cols\_cumprod\n",cols\_cumprod);     Print("rows\_cumprod\n",rows\_cumprod);     Print("cumprod values  ",cumprod\_values);        /\*     matrix\_a     [[10,3,2]      [1,8,12]      [6,5,4]      [7,11,9]]     cols\_cumprod     [[10,3,2]      [10,24,24]      [60,120,96]      [420,1320,864]]     rows\_cumprod     [[10,30,60]      [1,8,96]      [6,30,120]      [7,77,693]]     cumprod values  [10,30,60,60,480,5760,34560,172800,691200,4838400,53222400,479001600]     \*/ |
