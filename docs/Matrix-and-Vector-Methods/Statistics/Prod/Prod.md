# Prod

Prod

Return the product of the matrix/vector elements which can also be performed for the given axis.

|  |
| --- |
| double vector::Prod(    const double  initial=1      // initial multiplier     );     double matrix::Prod(    const double  initial=1      // initial multiplier     );     vector matrix::Prod(    const int     axis,          // axis    const double  initial=1      // initial multiplier     ); |

Parameters

axis

[in]  Axis. 0 — horizontal axis, 1 — vertical axis.

initial=1

[in]  Initial multiplier.

 

Example

|  |
| --- |
| matrix matrix\_a={{10,3,2},{1,8,12},{6,5,4},{7,11,9}};     Print("matrix\_a\n",matrix\_a);        vector cols\_prod=matrix\_a.Prod(0);     vector rows\_prod=matrix\_a.Prod(1);     double matrix\_prod=matrix\_a.Prod();        Print("cols\_prod=",cols\_prod);     cols\_prod=matrix\_a.Prod(0,0.1);     Print("cols\_prod=",cols\_prod);     Print("rows\_prod=",rows\_prod);     Print("prod value ",matrix\_prod);       /\*     matrix\_a     [[10,3,2]      [1,8,12]      [6,5,4]      [7,11,9]]     cols\_prod=[420,1320,864]     cols\_prod=[42,132,86.40000000000001]     rows\_prod=[60,96,120,693]     prod value 479001600.0    \*/ |
