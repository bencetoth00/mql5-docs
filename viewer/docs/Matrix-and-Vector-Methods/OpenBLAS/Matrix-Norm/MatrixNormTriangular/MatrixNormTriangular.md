# MatrixNormTriangular


Returns the value of the 1-norm, infinity-norm, Frobenius norm, or the largest absolute value of any element of a trapezoidal m-by-n or triangular matrix. LAPACK function [LANTR](https://www.intel.com/content/www/us/en/docs/onemkl/developer-reference-fortran/2025-2/lantr.html).

Computing for type matrix<double>

```cpp
bool  matrix::MatrixNormTriangular(
   ENUM_BLAS_NORMX norm,          // matrix norm
   double&         norm_value     // matrix norm value
   );
```

Computing for type matrix<float>

```cpp
bool  matrixf::MatrixNormTriangular(
   ENUM_BLAS_NORMX norm,          // matrix norm
   float&          norm_value     // matrix norm value
   );
```

Computing for type matrix<complex>

```cpp
bool  matrixc::MatrixNormTriangular(
   ENUM_BLAS_NORMX norm,          // matrix norm
   double&         norm_value     // matrix norm value
   );
```

Computing for type matrix<complexf>

```cpp
bool  matrixcf::MatrixNormTriangular(
   ENUM_BLAS_NORMX norm,          // matrix norm
   float&          norm_value     // matrix norm value
   );
```

Parameters

norm

[in]  Value from the ENUM\_BLAS\_NORMX enumeration, which specifies the value to be returned by the routine.

norm\_value

[out]  Calculated matrix norm value.

Return Value

Return true if successful, otherwise false in case of an [error](../../../../Constants,-Enumerations-and-Structures/Codes-of-Errors-and-Warnings/Runtime-Errors/Runtime-Errors.md).

Note

Matrix is triangular if m = n. It can be both upper or lower triangular.

If m < n then matrix must be upper trapezoidal, ie lower m-by-m triangular part must contain zeroes.

If m > n then matrix must be lower trapezoidal, ie upper n-by-n triangular part must contain zeroes.

 

ENUM\_BLAS\_NORMX

An enumeration defining which norm calculated.

| ID | Description |
| --- | --- |
| BLASNORMX\_O | 'O': One-norm |
| BLASNORMX\_I | 'I': Infinity-norm |
| BLASNORMX\_F | 'F': Frobenius-norm |
| BLASNORMX\_M | 'M': max(abs(A(i,j))) |