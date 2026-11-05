# Compare

Compare

Compare the elements of two matrices/vectors with the specified precision.

|  |
| --- |
| ulong vector::Compare(    const vector& vec,         // vector to compare    const double  epsilon       // precision     );     ulong matrix::Compare(    const matrix& mat,          // matrix to compare    const double  epsilon       // precision     ); |

Parameters

vec

[in]  Vector to compare.

mat

[in]  Matrix to compare.

epsilon

[in]  Precision.

Return Value

The number of mismatched elements of the matrices or vectors being compared: 0 if the matrices are equal, greater than 0 otherwise.

 

Note

The comparison operators == or != execute an exact element-wise comparison. It is known that the exact comparison of real numbers is of limited use, so the epsilon comparison method was added. It may happen that one matrix can contain elements in a range, for example from 1e-20 to 1e+20. Such matrices can be processed using element-wise comparison up to significant figures.

For complex matrices/vectors, the comparison involves estimating the distance between complex numbers. The distance is calculated as sqrt(pow(r1-r2, 2) + pow(i1-i2, 2) and is a real number that can already be compared with epsilon.

 

Example

|  |
| --- |
| matrix matrix\_a={{10,3,2},{1,8,12},{6,5,4}};     matrix matrix\_i=matrix::Identity(3,3);     matrix matrix\_c=matrix\_a.Inv();     matrix matrix\_check=matrix\_a.MatMul(matrix\_c);     Print("matrix\_check\n",matrix\_check);        ulong errors=matrix\_check.Compare(matrix::Identity(3,3),1e-15);     Print("errors=",errors);          /\*    matrix\_check    [[1,0,0]    [4.440892098500626e-16,1,8.881784197001252e-16]    [4.440892098500626e-16,2.220446049250313e-16,0.9999999999999996]]    errors=0       \*/ |
