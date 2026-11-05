# ArgMax

ArgMax

Return the index of the maximum value.

|  |
| --- |
| ulong vector::ArgMax();     ulong matrix::ArgMax();     vector matrix::ArgMax(    const int  axis      // axis     ); |

Parameters

axis

[in]  Axis. 0 — horizontal axis, 1 — vertical axis.

Return Value

Index of the maximum value.

 

Example

|  |
| --- |
| matrix matrix\_a={{10,3,2},{1,8,12},{6,5,4},{7,11,9}};     Print("matrix\_a\n",matrix\_a);        vector cols\_max=matrix\_a.ArgMax(0);     vector rows\_max=matrix\_a.ArgMax(1);     ulong  matrix\_max=matrix\_a.ArgMax();        Print("cols\_max=",cols\_max);     Print("rows\_max=",rows\_max);     Print("max index ",matrix\_max,"  max value ",matrix\_a.Flat(matrix\_max));        /\*     matrix\_a     [[10,3,2]      [1,8,12]      [6,5,4]      [7,11,9]]     cols\_max=[0,3,1]     rows\_max=[0,2,0,1]     max index 5  max value 12.0     \*/ |
