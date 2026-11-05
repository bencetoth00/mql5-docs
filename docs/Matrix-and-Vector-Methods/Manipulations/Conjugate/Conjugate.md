# Conjugate

Conjugate

Changing the sign of the imaginary part of a complex number, return the modified matrix or vector.

|  |
| --- |
| matrixc matrixc::Conjugate();     vectorc vectorc::Conjugate(); |

Return Value

Complex conjugated matrix or vector.

Note

Conjugate can be applied to real (non-complex) matrix or vector. In this case matrix or vector just copied on return.

 

Simple algorithm of conjugation - method explanation

|  |
| --- |
| //--- Complex vector conjugation  vectorc VectorConjugate(const vectorc& vector\_a)    {     //--- create a new vector\_c     vectorc vector\_c(vector\_a.Size());        //--- go through all values of the new vector     for(ulong i=0; i<vector\_c.Size(); i++)       {        //--- transfer the real part of the element        vector\_c[i].real = vector\_a[i].real;        //--- transfer the imaginary part of the element by changing the sign (conjugation)        vector\_c[i].imag = -vector\_a[i].imag;       }         //--- return the conjugated vector      return(vector\_c);    } |
