# EigenSolverSchur

EigenSolverSchur

Compute eigenvalues, upper triangular matrix in Schur form, and matrix of Schur vectors (LAPACK function [GEES](https://www.intel.com/content/www/us/en/docs/onemkl/developer-reference-fortran/2025-2/gees.html)). See also [Schur decomposition](https://en.wikipedia.org/wiki/Schur_decomposition).

Computing for type matrix<double>

|  |
| --- |
| bool  matrix::EigenSolverSchur(     ENUM\_EIG\_SCHUR        jobvs,                   // method to compute Schur vectors     vectorc&              eigen\_values,            // vector of computed eigenvalues     matrix&               schur\_matrix,            // matrix in Schur form     matrix&               schur\_vectors            // matrix of Schur vectors     ); |

Computing for type matrix<float>

|  |
| --- |
| bool  matrixf::EigenSolverSchur(     ENUM\_EIG\_SCHUR        jobvs,                   // method to compute Schur vectors     vectorcf&             eigen\_values,            // vector of computed eigenvalues     matrixf&              schur\_matrix,            // matrix in Schur form     matrixf&              schur\_vectors            // matrix of Schur vectors     ); |

Computing for type matrix<complex>

|  |
| --- |
| bool  matrixc::EigenSolverSchur(     ENUM\_EIG\_SCHUR        jobvs,                   // method to compute Schur vectors     vectorc&              eigen\_values,            // vector of computed eigenvalues     matrixc&              schur\_matrix,            // matrix in Schur form     matrixc&              schur\_vectors            // matrix of Schur vectors     ); |

Computing for type matrix<complexf>

|  |
| --- |
| bool  matrixcf::EigenSolverSchur(     ENUM\_EIG\_SCHUR        jobvs,                   // method to compute Schur vectors     vectorcf&             eigen\_values,            // vector of computed eigenvalues     matrixcf&             schur\_matrix,            // matrix in Schur form     matrixcf&             schur\_vectors            // matrix of Schur vectors     ); |

Parameters

jobvs

[in]  Value from the [ENUM\_EIG\_SCHUR](EigenSolverSchur.md#eigensolverschur) enumeration, which defines the method for computing Schur vectors.

eigen\_values

[out] Vector of eigenvalues.

schur\_matrix

[out]  Upper triangular Schur matrix (Schur form for the input matrix).

schur\_vectors

[out]  Matrix of Schur vectors; it is not computed if the jobvs parameter is set to N.

Return Value

Return true if successful, otherwise false in case of an [error](../../../../../Constants,-Enumerations-and-Structures/Codes-of-Errors-and-Warnings/Runtime-Errors/Runtime-Errors.md).

Note

Computation depends on the jobvs parameter values.

Real (non-complex) matrices can have a complex solution. Therefore, the input vector of eigenvalues must be complex. In case of a complex solution, the error code is set to [4019 (ERR\_MATH\_OVERFLOW)](../../../../../Constants,-Enumerations-and-Structures/Codes-of-Errors-and-Warnings/Runtime-Errors/Runtime-Errors.md). Otherwise, only the real parts of the complex values of the eigenvalue vector should be used.

 

ENUM\_EIG\_SCHUR

An enumeration defining the need to compute eigenvectors.

| ID | Description |
| --- | --- |
| EIGSCHUR\_N | Schur vectors are not computed |
| EIGSCHUR\_V | Schur vectors are computed |
