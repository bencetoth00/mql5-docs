# LDLInverse


Computes the inverse of a real symmetric or complex Hermitian indefinite matrix using the factorization A = U\*\*T \* D \* U or A = L \* D \* L\*\*T computed by [FactorizationLDLRaw](../../Factorizations/FactorizationLDLRaw/FactorizationLDLRaw.md). LAPACK functions [SYTRI](https://www.intel.com/content/www/us/en/docs/onemkl/developer-reference-fortran/2025-2/sytri.html), [HETRI](https://www.intel.com/content/www/us/en/docs/onemkl/developer-reference-fortran/2025-2/hetri.html).

Computing for type matrix<double>

```cpp
bool  matrix::LDLInverse(
   long[]&         ipiv,          // pivot indices array
   matrix&         AI             // inverse of matrix A
   );
```

Computing for type matrix<float>

```cpp
bool  matrixf::LDLInverse(
   long[]&         ipiv,          // pivot indices array
   matrixf&        AI             // inverse of matrix A
   );
```

Computing for type matrix<complex>

```cpp
bool  matrixc::LDLInverse(
   long[]&         ipiv,          // pivot indices array
   matrixc&        AI             // inverse of matrix A
   );
```

Computing for type matrix<complexf>

```cpp
bool  matrixcf::LDLInverse(
   long[]&         ipiv,          // pivot indices array
   matrixcf&       AI             // inverse of matrix A
   );
```

Parameters

ipiv

[in]  Pivot indices array obtained as result of SYTRF or HETRF function.

AI

[out]  Inverted matrix.

 

Return Value

Return true if successful, otherwise false in case of an [error](../../../../Constants,-Enumerations-and-Structures/Codes-of-Errors-and-Warnings/Runtime-Errors/Runtime-Errors.md).

Note

This method is applied to the matrix AF obtained as result of SYTRF or HETRF function.