# Flat

Flat

Allows addressing a matrix element through one index instead of two.

|  |
| --- |
| bool matrix::Flat(    const ulong   index,     // index    const double  value      // value to set     );     double matrix::Flat(    const ulong   index,     // index     ); |

Parameters

index

[in]  Flat index

value

[in]  Value to set by given index.

Return Value

Value by given index.

 

Note

For the matrix mat(3,3), access can be written as follows:  

- reading: 'x=mat.Flat(4)', which is equivalent to 'x=mat[1][1]'
- writing: 'mat.Flat(5, 42)', equivalent to 'mat[1][2]=42'

 

Example

|  |
| --- |
| matrix matrix\_a={{10,3,2},{1,8,12},{6,5,4},{7,11,9}};     Print("matrix\_a\n",matrix\_a);     ulong arg\_max=matrix\_a.ArgMax();     Print("max\_value=",matrix\_a.Flat(arg\_max));     matrix\_a.Flat(arg\_max,0);     arg\_max=matrix\_a.ArgMax();     Print("max\_value=",matrix\_a.Flat(arg\_max));          /\*    matrix\_a    [[10,3,2]     [1,8,12]     [6,5,4]     [7,11,9]]    max\_value=12.0    max\_value=11.0    \*/ |
