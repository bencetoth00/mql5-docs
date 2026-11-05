# Mathematical operations

Mathematical operations

Mathematical operations, including addition, subtraction, multiplication and division, can be performed on matrices and vectors element-wise.

Both matrices or both vectors must be of the same type and must have the same dimensions. Each element of the matrix operates on the corresponding element of the second matrix.

You can also use a scalar of the appropriate type (double, float or complex) as the second term (multiplier, subtrahend or divisor). In this case, each member of the matrix or vector will operate on the specified scalar.

|  |
| --- |
| matrix matrix\_a={{0.1,0.2,0.3},{0.4,0.5,0.6}};    matrix matrix\_b={{1,2,3},{4,5,6}};       matrix matrix\_c1=matrix\_a+matrix\_b;    matrix matrix\_c2=matrix\_b-matrix\_a;    matrix matrix\_c3=matrix\_a\*matrix\_b;   // Hadamard product, not to be confused with matrix product! There is a special MatMul function for this    matrix matrix\_c4=matrix\_b/matrix\_a;       matrix\_c1=matrix\_a+1;    matrix\_c2=matrix\_b-double\_value;    matrix\_c3=matrix\_a\*M\_PI;    matrix\_c4=matrix\_b/0.1;     //--- operations in place are possible    matrix\_a+=matrix\_b;    matrix\_a/=2; |

The same operations are available for vectors.
