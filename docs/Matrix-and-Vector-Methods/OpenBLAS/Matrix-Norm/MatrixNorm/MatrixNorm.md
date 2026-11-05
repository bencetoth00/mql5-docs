# MatrixNorm

MatrixNorm

Returns the value of the 1-norm, infinity-norm, Frobenius norm, or the largest absolute value of any element of a general rectangular matrix. LAPACK function [LANGE](https://www.intel.com/content/www/us/en/docs/onemkl/developer-reference-fortran/2025-2/lange.html).

Computing for type matrix<double>

|  |
| --- |
| bool  matrix::MatrixNorm(     ENUM\_BLAS\_NORMX norm,          // matrix norm     double&         norm\_value     // matrix norm value     ); |

Computing for type matrix<float>

|  |
| --- |
| bool  matrixf::MatrixNorm(     ENUM\_BLAS\_NORMX norm,          // matrix norm     float&          norm\_value     // matrix norm value     ); |

Computing for type matrix<complex>

|  |
| --- |
| bool  matrixc::MatrixNorm(     ENUM\_BLAS\_NORMX norm,          // matrix norm     double&         norm\_value     // matrix norm value     ); |

Computing for type matrix<complexf>

|  |
| --- |
| bool  matrixcf::MatrixNorm(     ENUM\_BLAS\_NORMX norm,          // matrix norm     float&          norm\_value     // matrix norm value     ); |

Parameters

norm

[in]  Value from the ENUM\_BLAS\_NORMX enumeration, which specifies the value to be returned by the routine.

norm\_value

[out]  Calculated matrix norm value.

Return Value

Return true if successful, otherwise false in case of an [error](../../../../Constants,-Enumerations-and-Structures/Codes-of-Errors-and-Warnings/Runtime-Errors/Runtime-Errors.md).

 

ENUM\_BLAS\_NORMX

An enumeration defining which norm calculated.

| ID | Description |
| --- | --- |
| BLASNORMX\_O | 'O': One-norm |
| BLASNORMX\_I | 'I': Infinity-norm |
| BLASNORMX\_F | 'F': Frobenius-norm |
| BLASNORMX\_M | 'M': max(abs(A(i,j))) |
