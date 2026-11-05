# FactorizationCholesky


Computes the factorization of a real symmetric or complex Hermitian positive-definite matrix A. The factorization has the form:

   A = L \*  L\*\*T in case of lower triangular or symmetric matrix A

or

   A = U\*\*T  \* U in case of upper triangular matrix A

where L is lower triangular, U is upper triangular. LAPACK function [POTRF](https://www.intel.com/content/www/us/en/docs/onemkl/developer-reference-fortran/2025-2/potrf.html).

Computing for type matrix<double>

```cpp
bool  matrix::FactorizationCholesky(
   matrix&         L             // lower or upper triangular matrix
   );
```

Computing for type matrix<float>

```cpp
bool  matrix::FactorizationCholesky(
   matrixf&        L             // lower or upper triangular matrix
   );
```

Computing for type matrix<complex>

```cpp
bool  matrix::FactorizationCholesky(
   matrixc&        L             // lower or upper triangular matrix
   );
```

Computing for type matrix<complexf>

```cpp
bool  matrix::FactorizationCholesky(
   matrixcf&       L             // lower or upper triangular matrix
   );
```

Parameters

L

[out]  Lower or upper triangular matrix.

 

Return Value

Return true if successful, otherwise false in case of an [error](../../../../Constants,-Enumerations-and-Structures/Codes-of-Errors-and-Warnings/Runtime-Errors/Runtime-Errors.md).

Note

The input can be a symmetric (Hermitian), [upper triangular](../../../Manipulations/TriU/TriU.md) or [lower triangular](../../../Manipulations/TriL/TriL.md) matrix. Triangular matrices are assumed to be symmetric (Hermitian conjugated).

Matrices L and D can be used for further calculations with methods [LDLSyTridPDLinearEquationsSolution](../../Factored-Calculations/LDLSyTridPDLinearEquationsSolution/LDLSyTridPDLinearEquationsSolution.md) and [LDLSyTridPDCondNumReciprocal](../../Factored-Calculations/LDLSyTridPDCondNumReciprocal/LDLSyTridPDCondNumReciprocal.md).