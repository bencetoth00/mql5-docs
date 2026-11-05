# SingularValueDecompositionDC


Singular Value Decomposition, "divide-and-conquer" algorithm. This algorithm is considered the fastest among other SVD algorithms (LAPACK function [GESDD](https://www.intel.com/content/www/us/en/docs/onemkl/developer-reference-fortran/2025-2/gesdd.html)).

Computing for type matrix<double>

```cpp
bool  matrix::SingularValueDecompositionDC(
   ENUM_SVD_Z      jobz,     // how to computed
   vector&         S,        // vector of computed singular values
   matrix&         U,        // matrix of computed left vectors U
   matrix&         VT        // transposed matrix of right vectors VT
   );
```

Computing for type matrix<float>

```cpp
bool  matrixf::SingularValueDecompositionDC(
   ENUM_SVD_Z      jobz,     // how to computed
   vectorf&        S,        // vector of computed singular values
   matrixf&        U,        // matrix of computed left vectors U
   matrixf&        VT        // transposed matrix of right vectors VT
   );
```

Computing for type matrix<complex>

```cpp
bool  matrixc::SingularValueDecompositionDC(
   ENUM_SVD_Z      jobz,     // how to computed
   vector&         S,        // vector of computed singular values
   matrixc&        U,        // matrix of computed left vectors U
   matrixc&        VT        // transposed matrix of right vectors VT
   );
```

Computing for type matrix<complexf>

```cpp
bool  matrixcf::SingularValueDecompositionDC(
   ENUM_SVD_Z      jobz,                   // how to computed
   vectorf&        singular_values,        // vector of computed singular values
   matrixcf&       U,                      // matrix of computed left vectors U
   matrixcf&       VT                      // transposed matrix of right vectors VT
   );
```

Parameters

jobz

[in] [ENUM\_SVD\_Z](SingularValueDecompositionDC.md#enum_svd_z) enumeration value which determines the method for computing left and singular eigenvectors.

S

[out] Vector of singular values.

U

[out] Matrix of left singular vectors.

VT

[out] Matrix of right singular vectors.

Return Value

Return true if successful, otherwise false in case of an [error](../../../../Constants,-Enumerations-and-Structures/Codes-of-Errors-and-Warnings/Runtime-Errors/Runtime-Errors.md).

Note

Computation depends on the value of the jobz parameter.

When jobv is set to SVDZ\_N, the left and right vectors are not computed. Only singular values are computed.

When jobv is set to SVDZ\_A, the full matrices of the U and VT vectors are computed.

When the value is SVDZ\_S, truncated matrices of vectors U and VT are computed.

 

ENUM\_SVD\_Z

An enumeration defining the way to compute left and right singular vectors.

| ID | Description |
| --- | --- |
| SVDZ\_N | Columns U or rows VT are not computed |
| SVDZ\_A | All M columns of U or all N columns of VT are returned in arrays U and VT |
| SVDZ\_S | The first min(M,N) columns of U or the first min(M,N) columns of VT are returned in arrays U and VT |

 

See also

[SingularValueDecompositionQR](../SingularValueDecompositionQR/SingularValueDecompositionQR.md), [SingularValueDecompositionQRPivot](../SingularValueDecompositionQRPivot/SingularValueDecompositionQRPivot.md)