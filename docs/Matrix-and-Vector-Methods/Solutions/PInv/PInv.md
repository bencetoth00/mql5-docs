# PInv

PInv

Compute the pseudo-inverse of a matrix by the Moore-Penrose method.

|  |
| --- |
| matrix matrix::PInv() |

Return Value

The pseudo-inverse of matrix.

 

Example

|  |
| --- |
| int TestPseudoInverse(const int size\_m, const int size\_k)    {     matrix matrix\_a(size\_m,size\_k);     matrix matrix\_inverted(size\_k,size\_m);     matrix matrix\_temp;     matrix matrix\_a2;  //--- fill the matrix     MatrixTestFirst(matrix\_a);  //--- invert     matrix\_inverted=matrix\_a.PInv();  //--- check the correctness     int errors=0;  //--- A \* A+ \* A = A   (A+ is a pseudo-inverse of A)     matrix\_temp=matrix\_a.MatMul(matrix\_inverted);     matrix\_a2=matrix\_temp.MatMul(matrix\_a);     errors=(int)matrix\_a.CompareByDigits(matrix\_a2,10);        printf("PseudoInversion %s matrix\_size  %d x %d  errors=%d",errors==0?"passed":"failed",size\_m,size\_k,errors);  //---     return(errors);    } |
