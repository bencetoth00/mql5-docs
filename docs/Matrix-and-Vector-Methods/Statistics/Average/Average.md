# Average

Average

Compute the weighted mean of matrix/vector values.

|  |
| --- |
| double vector::Average(    const vector& weigts      // weights vector     );     double matrix::Average(    const matrix& weigts      // weights matrix  );     vector matrix::Average(    const matrix& weigts,     // weights matrix    const int     axis        // axis     ); |

Parameters

axis

[in]  Axis. 0 — horizontal axis, 1 — vertical axis.

Return Value

Weighted mean: scalar or vector.

 

Note

The weight matrix/vector is associated with the main matrix/vector.

 

Example

|  |
| --- |
| matrixf matrix\_a={{10,3,2},{1,8,12},{6,5,4},{7,11,9}};     matrixf matrix\_w=matrixf::Ones(4,3);     Print("matrix\_a\n",matrix\_a);        vectorf cols\_average=matrix\_a.Average(matrix\_w,0);     vectorf rows\_average=matrix\_a.Average(matrix\_w,1);     float matrix\_average=matrix\_a.Average(matrix\_w);        Print("cols\_average ",cols\_average);     Print("rows\_average ",rows\_average);     Print("average value  ",matrix\_average);           /\*     matrix\_a     [[10,3,2]      [1,8,12]      [6,5,4]      [7,11,9]]     cols\_average [6,6.75,6.75]     rows\_average [5,7,5,9]     average value  6.5     \*/ value  6.5 |
