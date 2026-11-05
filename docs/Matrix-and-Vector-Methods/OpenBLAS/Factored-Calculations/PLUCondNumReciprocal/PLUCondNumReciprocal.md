# PLUCondNumReciprocal

PLUCondNumReciprocal

Estimates the reciprocal of the condition number of a general matrix A in either the one-norm or infinity-norm, using the LU factorization computed by [FactorizationPLURaw](../../Factorizations/FactorizationPLURaw/FactorizationPLURaw.md). LAPACK function [GECON](https://www.intel.com/content/www/us/en/docs/onemkl/developer-reference-fortran/2025-2/gecon.html).

Computing for type matrix<double>

|  |
| --- |
| bool  matrix::PLUCondNumReciprocal(     ENUM\_BLAS\_NORM  norm,          // matrix norm     double          anorm,         // matrix norm value     double&         rcond          // condition number reciprocal     ); |

Computing for type matrix<float>

|  |
| --- |
| bool  matrixf::PLUCondNumReciprocal(     ENUM\_BLAS\_NORM  norm,          // matrix norm     float           anorm,         // matrix norm value     float&          rcond          // condition number reciprocal     ); |

Computing for type matrix<complex>

|  |
| --- |
| bool  matrixc::PLUCondNumReciprocal(     ENUM\_BLAS\_NORM  norm,          // matrix norm     double          anorm,         // matrix norm value     double&         rcond          // condition number reciprocal     ); |

Computing for type matrix<complexf>

|  |
| --- |
| bool  matrixcf::PLUCondNumReciprocal(     ENUM\_BLAS\_NORM  norm,          // matrix norm     float           anorm,         // matrix norm value     float&          rcond          // condition number reciprocal     ); |

Parameters

norm

[in]  Value from the [ENUM\_BLAS\_NORM](PLUCondNumReciprocal.md#enum_blas_norm) enumeration, which defines estimation the reciprocal of the condition number.

anorm

[in]  Matrix norm value. If norm = 'O', the one-norm of the original matrix A. If norm = 'I', the infinity-norm of the original matrix A. Norm value can be obtained with [MatrixNorm](../../Matrix-Norm/MatrixNorm/MatrixNorm.md) of the original matrix A.

rcond

[out] An estimate of the reciprocal of the condition number. The routine sets rcond=0 if the estimate underflows; in this case the matrix is singular (to working precision). However, anytime rcond is small compared to 1.0, for the working precision, the matrix may be poorly conditioned or even singular.

 

Return Value

Return true if successful, otherwise false in case of an [error](../../../../Constants,-Enumerations-and-Structures/Codes-of-Errors-and-Warnings/Runtime-Errors/Runtime-Errors.md).

Note

This method is applied to the matrix AF obtained as result of GETRF function.

The computed rcond is never less than r (the reciprocal of the true condition number) and in practice is nearly always less than 10r. A call to this routine involves solving a number of systems of linear equations A\*x = b; the number is usually 4 or 5 and never more than 11

 

ENUM\_BLAS\_NORM

An enumeration defining the matrix norm.

| ID | Description |
| --- | --- |
| BLASNORM\_O | 'O': One-norm |
| BLASNORM\_I | 'I': Infinity-norm |
