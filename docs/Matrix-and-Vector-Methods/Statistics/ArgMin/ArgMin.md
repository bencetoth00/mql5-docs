# ArgMin

ArgMin

Return the index of the minimum value.

|  |
| --- |
| ulong vector::ArgMin();     ulong matrix::ArgMin();     vector matrix::ArgMin(    const int  axis      // axis     ); |

Parameters

axis

[in]  Axis. 0 — horizontal axis, 1 — vertical axis.

Return Value

Index of the minimum value.

 

Example

|  |
| --- |
| matrix matrix\_a={{10,3,2},{1,8,12},{6,5,4},{7,11,9}};     Print("matrix\_a\n",matrix\_a);        vector cols\_min=matrix\_a.ArgMin(0);     vector rows\_min=matrix\_a.ArgMin(1);     ulong  matrix\_min=matrix\_a.ArgMin();        Print("cols\_min=",cols\_min);     Print("rows\_min=",rows\_min);     Print("min index ",matrix\_min,"  min value ",matrix\_a.Flat(matrix\_min));        /\*     matrix\_a     [[10,3,2]      [1,8,12]      [6,5,4]      [7,11,9]]     cols\_min=[1,0,0]     rows\_min=[2,0,2,0]     min index 3  min value 1.0     \*/ |
