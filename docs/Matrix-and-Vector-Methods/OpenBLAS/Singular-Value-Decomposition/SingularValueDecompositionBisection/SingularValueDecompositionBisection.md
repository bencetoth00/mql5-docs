# SingularValueDecompositionBisection

SingularValueDecompositionBisection

Singular Value Decomposition, bisection algorithm (LAPACK function [GESVDX](https://www.intel.com/content/www/us/en/docs/onemkl/developer-reference-fortran/2025-2/gesvdx.html)).

Computing for type matrix<double>

|  |
| --- |
| bool  matrix::SingularValueDecompositionBisection(     ENUM\_SVD\_VECTORS    jobv,     // compute left and right singular vectors     ENUM\_BLAS\_RANGE     range,    // subset of computable singular values     double              lower,    // lower limit of the subset     double              upper,    // upper limit of the subset     vector&             S,        // vector of computed singular values     matrix&             U,        // matrix of computed left vectors U     matrix&             VT        // transposed matrix of right vectors VT     ); |

Computing for type matrix<float>

|  |
| --- |
| bool  matrixf::SingularValueDecompositionBisection(     ENUM\_SVD\_VECTORS    jobv,     // compute left and right singular vectors     ENUM\_BLAS\_RANGE     range,    // subset of computable singular values     double              lower,    // lower limit of the subset     double              upper,    // upper limit of the subset     vectorf&            S,        // vector of computed singular values     matrixf&            U,        // matrix of computed left vectors U     matrixf&            VT        // ransposed matrix of right vectors VT     ); |

Computing for type matrix<complex>

|  |
| --- |
| bool  matrixc::SingularValueDecompositionBisection(     ENUM\_SVD\_VECTORS    jobv,     // compute left and right singular vectors     ENUM\_BLAS\_RANGE     range,    // subset of computable singular values     double              lower,    // lower limit of the subset     double              upper,    // upper limit of the subset     vector              S,        // vector of computed singular values     matrixc             U,        // matrix of computed left vectors U     matrixc             VT        // transposed matrix of right vectors VT     ); |

Computing for type matrix<complexf>

|  |
| --- |
| bool  matrixcf::SingularValueDecompositionBisection(     ENUM\_SVD\_VECTORS    jobv,     // compute left and right singular vectors     ENUM\_BLAS\_RANGE     range,    // subset of computable singular values     double              lower,    // lower limit of the subset     double              upper,    // upper limit of the subset     vectorf&            S,        // vector of computed singular values     matrixcf&           U,        // matrix of computed left vectors U     matrixcf&           VT        // transposed matrix of right vectors VT     ); |

Parameters

jobv

[in]  ENUM\_SVD\_VECTORS enumeration value which determines the method for computing left and right singular vectors.

range

[in]  ENUM\_BLAS\_RANGE enumeration value that defines a subset of computable singular values and vectors.

lower

[in]  The lower limit of singular values subset; specified depending on the value of the range parameter.

upper

[in]  The upper limit of singular values subset; specified depending on the value of the range parameter.

S

[out] Vector of singular values.

U

[out] Matrix of left singular vectors.

VT

[out] Matrix of right singular vectors.

Return Value

Return true if successful, otherwise false in case of an [error](../../../../Constants,-Enumerations-and-Structures/Codes-of-Errors-and-Warnings/Runtime-Errors/Runtime-Errors.md).

Note

Computation depends on the values of the jobuv and range parameters.

When BLASRANGE\_A is set, all singular values are computed, and the lower and upper parameters are ignored.

With the BLASRANGE\_V value, only those singular values (and their vectors) that fall within the range of real values specified by the 'lower' and 'upper' parameters are computed.

With the BLASRANGE\_I value, only those singular values (and their vectors) that fall within the range of integer indices specified by the 'lower' and 'upper' parameters are computed. For example, with lower=0 and upper=2, only the first three singular values are computed.

 

ENUM\_SVD\_VECTORS

An enumeration defining the way to compute left and right singular vectors.

| ID | Description |
| --- | --- |
| SVDVECTORS\_N | Only singular values are computed, without vectors. |
| SVDVECTORS\_U | Left singular vectors are computed. |
| SVDVECTORS\_V | Right singular vectors are computed. |
| SVDVECTORS\_UV | Left and right singular vectors are computed. |

ENUM\_BLAS\_RANGE

An enumeration defining a subset of computable singular values and vectors.

| ID | Description |
| --- | --- |
| BLASRANGE\_A | All singular or eigenvalues will be found. |
| BLASRANGE\_V | All singular or eigenvalues in the half-open interval (VL,VU] will be found. |
| BLASRANGE\_I | Singular or eigenvalues from IL to IU will be found |

 

See also

[SingularValueDecompositionDC](../SingularValueDecompositionDC/SingularValueDecompositionDC.md), [SingularValueDecompositionQR](../SingularValueDecompositionQR/SingularValueDecompositionQR.md), [SingularValueDecompositionQRPivot](../SingularValueDecompositionQRPivot/SingularValueDecompositionQRPivot.md)
