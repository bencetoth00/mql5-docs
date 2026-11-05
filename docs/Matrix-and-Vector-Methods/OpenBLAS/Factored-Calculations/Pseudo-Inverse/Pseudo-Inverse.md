# Pseudo Inverse

There is no special function in the OpenBLAS library to calculate the pseudo-inverse of a matrix. However, for this purpose can be used [singular value decomposition](../../Singular-Value-Decomposition/Singular-Value-Decomposition.md) (SVD):

1. Decompose matrix A into U \* Σ \* VT

2. Invert Σ (non-zero singular values ​​only)

3. Get the pseudo-inverse matrix using the formula

A+ = V \* Σ+ \* UT

Example

|  |
| --- |
| //+------------------------------------------------------------------+  //|  Тест функции PseudoInverse: проверка A \* A+ \* A ≈ A             |  //+------------------------------------------------------------------+  int TestPseudoInverse(ulong size\_m,ulong size\_n)    {     matrix matrix\_a=matrix::Random(size\_m,size\_n);     matrix matrix\_pi;     if(!PseudoInverse(matrix\_a,matrix\_pi))        return(1000);     //--- pseudo inverse test  A \* A+ \* A = A     matrix matrix\_a2=matrix\_a @ matrix\_pi @ matrix\_a;     int    errors=(int)matrix\_a.Compare(matrix\_a2,1e-11);        printf("Pseudo Inverse via SVD %s  matrix size %d x %d  errors=%d",errors==0?"passed":"failed",size\_m,size\_n,errors);        return(errors);    }  //+------------------------------------------------------------------+  //| Вычисляет псевдообратную матрицу с помощью сингулярного разлож.  |  //| A+ = V \* Σ⁻¹ \* Uᵀ                                                |  //+------------------------------------------------------------------+  bool PseudoInverse(matrix& matrix\_a,matrix& matrix\_pi)    {  //--- 1. SVD     matrix matrix\_u,matrix\_vt;     vector vector\_s;     if(!matrix\_a.SingularValueDecompositionDC(SVDZ\_S,vector\_s,matrix\_u,matrix\_vt))        return(false);     //--- 2. inverse diagonal matrix     ulong  diag=vector\_s.Size();     matrix matrix\_si=matrix::Zeros(diag,diag);     for(ulong i=0; i<diag; i++)       {        if(vector\_s[i]!=0.0)           matrix\_si[i][i]=1.0/vector\_s[i];       }     //--- 3. pseudo inverse  A+ = V \* Σ+ \* UT     matrix\_pi=matrix\_vt.Transpose() @ matrix\_si @ matrix\_u.Transpose();        return(true);    } |
