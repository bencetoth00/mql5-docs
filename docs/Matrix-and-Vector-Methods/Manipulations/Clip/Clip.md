# Clip

Clip

Limit the elements of a matrix/vector to a specified range of valid values.

|  |
| --- |
| bool matrix::Clip(    const double  min\_value,     // minimum value    const double  max\_value      // maximum value     );  bool vector::Clip(    const double  min\_value,     // minimum value    const double  max\_value      // maximum value     ); |

Parameters

min\_value

[in]  Minimum value.

max\_value

[in] Maximum value.

Return Value

Returns true on success, false otherwise.

 

Note

The matrix (or vector) is processed in place. No copies are created.

 

Example

|  |
| --- |
| matrix matrix\_a={{1,2,3},{4,5,6},{7,8,9},{10,11,12}};     bool res=matrix\_a.Clip(4,8);     Print("matrix\_a\n",matrix\_a);       /\*    matrix\_a    [[4,4,4]     [4,5,6]     [7,8,8]     [8,8,8]]    \*/ |
