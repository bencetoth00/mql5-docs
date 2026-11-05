# EigenSolver

EigenSolver

Compute eigenvalues and eigenvectors of a regular square matrix using the classical algorithm (LAPACK function [GEEV](https://www.intel.com/content/www/us/en/docs/onemkl/developer-reference-fortran/2025-2/geev.html)).

Computing for type matrix<double>

|  |
| --- |
| bool  matrix::EigenSolver(     ENUM\_EIG\_VECTORS      jobv,                    // compute left and right eigenvectors     vectorc&              eigen\_values,            // vector of computed eigenvalues     matrix&               left\_eigenvectors,       // matrix of computed left vectors     matrix&               right\_eigenvectors       // matrix of computed right vectors     ); |

Computing for type matrix<float>

|  |
| --- |
| bool  matrixf::EigenSolver(     ENUM\_EIG\_VECTORS      jobv,                    // compute left and right eigenvectors     vectorcf&             eigen\_values,            // vector of computed eigenvalues     matrixf&              left\_eigenvectors,       // matrix of computed left vectors     matrixf&              right\_eigenvectors       // matrix of computed right vectors     ); |

Computing for type matrix<complex>

|  |
| --- |
| bool  matrixc::EigenSolver(     ENUM\_EIG\_VECTORS      jobv,                    // compute left and right vectors     vectorc&              eigen\_values,            // vector of computed eigenvalues     matrixc&              left\_eigenvectors,       // matrix of computed left vectors     matrixc&              right\_eigenvectors       // matrix of computed right vectors       ); |

Computing for type matrix<complexf>

|  |
| --- |
| bool  matrixcf::EigenSolver(     ENUM\_EIG\_VECTORS      jobv,                    // compute left and right vectors     vectorcf&             eigen\_values,            // vector of computed eigenvalues     matrixcf&             left\_eigenvectors,       // matrix of computed left vectors     matrixcf&             right\_eigenvectors       // matrix of computed right vectors       ); |

Parameters

jobv

[in] [ENUM\_EIG\_VECTORS](EigenSolver.md#enum_eig_vectors) enumeration value which determines the method for computing left and right eigenvectors.

EV

[out] Vector of eigenvalues.

left\_eigenvectors

[out] Matrix of left eigenvectors.

right\_eigenvectors

[out] Matrix of right eigenvectors.

Return Value

Return true if successful, otherwise false in case of an [error](../../../../../Constants,-Enumerations-and-Structures/Codes-of-Errors-and-Warnings/Runtime-Errors/Runtime-Errors.md).

Note

Computation depends on the value of the jobv parameter.

If EIGVECTORS\_N is set, the left and right vectors are not computed. Only eigenvalues are computed.

With EIGVECTORS\_L, only left eigenvectors are computed, right eigenvectors are not computed.

When EIGVECTORS\_R is set, only the right eigenvectors are computed, the left vectors are not computed.

With EIGVECTORS\_LR, the left and right eigenvectors are computed, Eigenvalues are always computed.

Real (non-complex) matrices can have a complex solution. Therefore, the vector of eigenvalues must be complex. In case of a complex solution, the error code is set to 4019 (ERR\_MATH\_OVERFLOW). Otherwise, only the real parts of the complex values of the eigenvalue vector should be used.

 

ENUM\_EIG\_VECTORS

An enumeration that specifies whether to calculate eigenvectors.

| ID | Description |
| --- | --- |
| EIGVECTORS\_N | Only eigenvalues are calculated, without vectors. |
| EIGVECTORS\_L | Only left eigenvectors are computed. |
| EIGVECTORS\_R | Only right eigenvectors are computed. |
| EIGVECTORS\_LR | Left and right eigenvectors are computed, eigenvalues are always computed. |
