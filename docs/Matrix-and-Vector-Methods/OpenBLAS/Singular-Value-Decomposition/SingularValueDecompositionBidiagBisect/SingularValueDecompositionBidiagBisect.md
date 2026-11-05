# SingularValueDecompositionBidiagBisect

SingularValueDecompositionBidiagBisect

Singular Value Decomposition, bisection algorithm for bidiagonal matrices (LAPACK function [BDSVDX](https://www.intel.com/content/www/us/en/docs/onemkl/developer-reference-fortran/2025-2/bdsvdx.html)).

Computing for type matrix<double>

|  |
| --- |
| bool  matrix::SingularValueDecompositionBidiagBisect(     ENUM\_SVDBIDIAG\_Z    jobz,       // how to compute left vectors     ENUM\_BLAS\_RANGE     range,      // subset of computed singular values     double              lower,      // lower limit of the subset     double              upper,      // upper limit of the subset     vector&             S,          // vector of computed singular values     matrix&             U,          // U matrix of computed left vectors     matrix&             VT          // VT transposed matrix of right vectors     ); |

Computing for type matrix<float>

|  |
| --- |
| bool  matrixf::SingularValueDecompositionBidiagBisect(     ENUM\_SVDBIDIAG\_Z    jobz,       // how to compute left vectors     ENUM\_BLAS\_RANGE     range,      // subset of computed singular values     double              lower,      // lower limit of the subset     double              upper,      // upper limit of the subset     vectorf&            S,          // vector of computed singular values     matrixf&            U,          // U matrix of computed left vectors     matrixf&            VT          // VT transposed matrix of right vectors     ); |

Parameters

jobz

[in] [ENUM\_SVDBIDIAG\_Z](../SingularValueDecompositionBidiagDC/SingularValueDecompositionBidiagDC.md#enum_svdbidiag_z) enumeration value that determines how the left singular vectors should be computed.

range

[in] [ENUM\_BLAS\_RANGE](../SingularValueDecompositionBisection/SingularValueDecompositionBisection.md) enumeration value that defines a subset of computable singular values and vectors.

lower

[in]  The lower limit of singular values subset; specified depending on the value of the range parameter.

upper

[in]  The upper limit of singular values subset; specified depending on the value of the range parameter.

S

[out] Vector of singular values.

U

[out] Matrix of left singular vectors.

V

[out] Transposed matrix of right singular vectors.

Return Value

Return true if successful, otherwise false in case of an [error](../../../../Constants,-Enumerations-and-Structures/Codes-of-Errors-and-Warnings/Runtime-Errors/Runtime-Errors.md).

Note

When BLASRANGE\_A is set, all singular values are computed, and the lower and upper parameters are ignored.

With the BLASRANGE\_V value, only those singular values (and their vectors) that fall within the range of real values specified by the 'lower' and 'upper' parameters are computed.

With the BLASRANGE\_I value, only those singular values (and their vectors) that fall within the range of integer indices specified by the 'lower' and 'upper' parameters are computed. For example, with lower=0 and upper=2, only the first three singular values are computed.

A bidiagonal matrix is a square matrix with non-zero main diagonal and one of the sub-diagonals.

 

Upper bidiagonal matrix

|  |
| --- |
| [[x, x, 0, 0, 0],   [0, x, x, 0, 0],   [0, 0, x, x, 0],   [0, 0, 0, x, x],   [0, 0, 0, 0, x]] |

Lower bidiagonal matrix

|  |
| --- |
| [[x, 0, 0, 0, 0],   [x, x, 0, 0, 0],   [0, x, x, 0, 0],   [0, 0, x, x, 0],   [0, 0, 0, x, x]] |

 

ENUM\_SVDBIDIAG\_Z

An enumeration defining how left singular vectors should be computed.

| ID | Description |
| --- | --- |
| SVDJOBZ\_V | Compute singular values and singular vectors. |
| SVDJOBZ\_N | Compute singular values only. |

ENUM\_BLAS\_RANGE

An enumeration defining how right singular vectors should be computed.

| ID | Description |
| --- | --- |
| BLASRANGE\_A | All singular or eigenvalues will be found. |
| BLASRANGE\_V | All singular or eigenvalues in the half-open interval (VL,VU] will be found. |
| BLASRANGE\_I | The IL-th through IU-th singular or eigenvalues will be found. |

 

See also

[SingularValueDecompositionDC](../SingularValueDecompositionDC/SingularValueDecompositionDC.md), [SingularValueDecompositionQR](../SingularValueDecompositionQR/SingularValueDecompositionQR.md)
