# Polar Decomposition

There is no special function in the OpenBLAS library to calculate the polar decomposition of a matrix. However, for this purpose can be used [singular value decomposition](../../Singular-Value-Decomposition/Singular-Value-Decomposition.md) (SVD):

Polar decomposition formula: A = Q \* P, where:

Q - orthogonal (or unitary) matrix

P - symmetric (or Hermitian) positive-definite matrix.

How can be calculated polar decomposition using SVD.

SVD formula: A = U \* Σ \* VT ==> (U \* VT) \* (V \* Σ \* VT), ie Q = U \* VT and P = V \* Σ \* VT

Example

|  |
| --- |
| //+------------------------------------------------------------------+  //| Тест функции PolarDecomposition: проверка Q ортогональна и Q\*P=A |  //+------------------------------------------------------------------+  int TestPolarDecomposition(ulong size\_m,ulong size\_n)    {     matrix matrix\_a=matrix::Random(size\_m,size\_n);     matrix matrix\_q,matrix\_p;     if(!PolarDecomposition(matrix\_a,matrix\_q,matrix\_p))        return(1000);     //--- check orthogonality     matrix matrix\_qqt=(size\_m<=size\_n) ? matrix\_q@matrix\_q.Transpose() : matrix\_q.Transpose()@matrix\_q;     matrix matrix\_i=matrix::Identity(matrix\_qqt.Rows(),matrix\_qqt.Cols());     int    errors=(int)matrix\_i.Compare(matrix\_qqt,1e-11);     printf("matrix Q is %sorthogonal",errors==0?"":"not ");     //--- polar decomposition test  Q \* P = A     matrix matrix\_a2=matrix\_q @ matrix\_p;     errors+=(int)matrix\_a.Compare(matrix\_a2,1e-11);        printf("Polar Decomposition via SVD %s  matrix size %d x %d  errors=%d",errors==0?"passed":"failed",size\_m,size\_n,errors);        return(errors);    }  //+------------------------------------------------------------------+  //| Полярное разложение матрицы A = Q \* P через сингулярное разлож.  |  //| Q — ортогональная, P — положит. определённая симметричная матрица|  //+------------------------------------------------------------------+  bool PolarDecomposition(matrix& matrix\_a,matrix& matrix\_q,matrix& matrix\_p)    {  //--- SVD     matrix matrix\_u,matrix\_vt;     vector vector\_s;     if(!matrix\_a.SingularValueDecompositionDC(SVDZ\_S,vector\_s,matrix\_u,matrix\_vt))        return(false);     //--- get diagonal matrix     ulong  diag=vector\_s.Size();     matrix matrix\_s=matrix::Zeros(diag,diag);     matrix\_s.Diag(vector\_s);     //--- Q = U \* VT     matrix\_q=matrix\_u @ matrix\_vt;  //--- P = V \* Σ \* VT     matrix\_p=matrix\_vt.Transpose() @ matrix\_s @ matrix\_vt;        return(true);    } |
