# EigenVectorsTriangularZ

EigenVectorsTriangularZ

Computes eigenvectors of n real upper quasi-triangular or complex upper triangular matrix computed by [EigenHessenbergSchurQ](../EigenHessenbergSchurQ/EigenHessenbergSchurQ.md) or [EigenSolverSchur](../EigenSolverSchur/EigenSolverSchur.md).

A = Q \* T \* Q\*\*H, where T is an upper quasi-triangular matrix (the Schur form), and Q is the orthogonal matrix of Schur vectors.

LAPACK function [TREVC](https://www.intel.com/content/www/us/en/docs/onemkl/developer-reference-fortran/2025-2/trevc.html).

Computing for type matrix<double>

|  |
| --- |
| bool  matrix::EigenVectorsTriangularZ(     ENUM\_EIG\_VECTORS      side,                    // compute left and/or right eigenvectors     matrix&               schur\_z,                 // orthogonal matrix of Schur vectors     matrix&               left\_eigenvectors,       // matrix of computed left vectors     matrix&               right\_eigenvectors       // matrix of computed right vectors     ); |

Computing for type matrix<float>

|  |
| --- |
| bool  matrixf::EigenVectorsTriangularZ(     ENUM\_EIG\_VECTORS      side,                    // compute left and/or right eigenvectors     matrixf&              schur\_z,                 // orthogonal matrix of Schur vectors     matrixf&              left\_eigenvectors,       // matrix of computed left vectors     matrixf&              right\_eigenvectors       // matrix of computed right vectors     ); |

Computing for type matrix<complex>

|  |
| --- |
| bool  matrixc::EigenVectorsTriangularZ(     ENUM\_EIG\_VECTORS      side,                    // compute left and/or right eigenvectors     matrixc&              schur\_z,                 // orthogonal matrix of Schur vectors     matrixc&              left\_eigenvectors,       // matrix of computed left vectors     matrixc&              right\_eigenvectors       // matrix of computed right vectors     ); |

Computing for type matrix<complexf>

|  |
| --- |
| bool  matrixcf::EigenVectorsTriangularZ(     ENUM\_EIG\_VECTORS      side,                    // compute left and/or right eigenvectors     matrixcf&             schur\_z,                 // orthogonal matrix of Schur vectors     matrixcf&             left\_eigenvectors,       // matrix of computed left vectors     matrixcf&             right\_eigenvectors       // matrix of computed right vectors     ); |

Parameters

side

[in]  ENUM\_EIG\_VECTORS enumeration value which determines what the eigenvectors are computed left, right or both.

shur\_z

[in]  Orthogonal matrix of Schur vectors computed by [EigenHessenbergSchurQ](../EigenHessenbergSchurQ/EigenHessenbergSchurQ.md) or [EigenSolverSchur](../EigenSolverSchur/EigenSolverSchur.md). Can be of zero size. In this case no backtransformation is produced.

left\_eigenvectors

[out] Matrix of left eigenvectors.

right\_eigenvectors

[out] Matrix of right eigenvectors.

Return Value

Return true if successful, otherwise false in case of an [error](../../../../../Constants,-Enumerations-and-Structures/Codes-of-Errors-and-Warnings/Runtime-Errors/Runtime-Errors.md).

Note

The right eigenvector x and the left eigenvector y of T corresponding to an eigenvalue w are defined by:

   T\*x = w\*x,     (y\*\*H)\*T = w\*(y\*\*H)

where y\*\*H denotes the conjugate transpose of y.

The eigenvalues are not input to this routine, but are read directly from the diagonal blocks of T.

This routine returns the matrices X and/or Y of right and left eigenvectors of T, or the products Q\*X and/or Q\*Y, where Q is an input matrix.  If Q is the orthogonal factor that reduces a matrix A to Schur form T, then Q\*X and Q\*Y are the matrices of right and left eigenvectors of A.

ENUM\_EIG\_VECTORS

An enumeration that specifies whether to calculate eigenvectors.

| ID | Description |
| --- | --- |
| EIGVECTORS\_N | Cannot be used with this method |
| EIGVECTORS\_L | Only left eigenvectors are computed. |
| EIGVECTORS\_R | Only right eigenvectors are computed. |
| EIGVECTORS\_LR | Left and right eigenvectors are computed, eigenvalues are always computed. |
