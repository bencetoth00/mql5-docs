# Fill

Fill

Fill an existing matrix or vector with the specified value.

|  |
| --- |
| void matrix::Fill(    const double  value      // value to fill     );     void vector::Fill(    const double  value      // value to fill     ); |

Parameters

value

[in]  Value to fill all the matrix elements.

Return Value

No return value. The matrix is filled in place with the specified value.

 

Example

|  |
| --- |
| matrix matrix\_a(2,2);     matrix\_a.Fill(10);     Print("matrix\_a\n",matrix\_a);     /\*    matrix\_a    [[10,10]     [10,10]]  \*/ |
