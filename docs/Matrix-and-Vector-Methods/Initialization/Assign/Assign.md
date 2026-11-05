# Assign

Assign

Copies a matrix, vector or array with auto cast.

|  |
| --- |
| bool matrix::Assign(    const matrix<T>  &mat     // copied matrix     );  bool matrix::Assign(    const void       &array[] // copied array     );  bool vector::Assign(    const vector<T>  &vec     // copied vector     );  bool vector::Assign(    const void       &array[] // copied array     ); |

Parameters

m, v or array

[in]  The matrix, vector or array the values are copied from.

Return Value

Returns true if successful, otherwise — false.

Note

Unlike [Copy](../../Manipulations/Copy/Copy.md), the Assign method allows copying arrays as well. In this case, the auto cast takes place, while the resulting matrix or vector adjusts to the size of the copied array.

 

Example:

|  |
| --- |
| //--- copy the matrices    matrix a= {{2, 2}, {3, 3}, {4, 4}};    matrix b=a+2;    matrix c;    Print("matrix a \n", a);    Print("matrix b \n", b);    c.Assign(b);    Print("matrix c \n", a);     //--- copy the array to the matrix    matrix double\_matrix=matrix::Full(2,10,3.14);    Print("double\_matrix before Assign() \n", double\_matrix);    int int\_arr[5][5]= {{1, 2}, {3, 4}, {5, 6}};    Print("int\_arr: ");    ArrayPrint(int\_arr);    double\_matrix.Assign(int\_arr);    Print("double\_matrix after Assign(int\_arr) \n", double\_matrix);      /\*     matrix a     [[2,2]      [3,3]      [4,4]]     matrix b     [[4,4]      [5,5]      [6,6]]     matrix c     [[2,2]      [3,3]      [4,4]]        double\_matrix before Assign()      [[3.14,3.14,3.14,3.14,3.14,3.14,3.14,3.14,3.14,3.14]      [3.14,3.14,3.14,3.14,3.14,3.14,3.14,3.14,3.14,3.14]]           int\_arr:          [,0][,1][,2][,3][,4]     [0,]   1   2   0   0   0     [1,]   3   4   0   0   0     [2,]   5   6   0   0   0     [3,]   0   0   0   0   0     [4,]   0   0   0   0   0          double\_matrix after Assign(int\_arr)      [[1,2,0,0,0]      [3,4,0,0,0]      [5,6,0,0,0]      [0,0,0,0,0]      [0,0,0,0,0]]       \*/ |

See also

[Copy](../../Manipulations/Copy/Copy.md)
