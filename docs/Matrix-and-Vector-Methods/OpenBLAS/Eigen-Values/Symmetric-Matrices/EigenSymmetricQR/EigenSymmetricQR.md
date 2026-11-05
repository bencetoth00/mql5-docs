# EigenSymmetricQR

EigenSymmetricQR

Compute eigenvalues and eigenvectors of a symmetric or Hermitian (complex conjugated) matrix using the QR algorithm (LAPACK functions [SYEV](https://www.intel.com/content/www/us/en/docs/onemkl/developer-reference-fortran/2025-2/syev.html), [HEEV](https://www.intel.com/content/www/us/en/docs/onemkl/developer-reference-fortran/2025-2/heev.html)).

Computing for type matrix<double>

|  |
| --- |
| bool  matrix::EigenSymmetricQR(     ENUM\_EIG\_VALUES       jobv,               // compute eigenvectors or not     vector&               eigen\_values,       // vector of computed eigenvalues     matrix&               eigen\_vectors       // matrix of computed eigenvectors     ); |

Computing for type matrix<float>

|  |
| --- |
| bool  matrixf::EigenSymmetricQR(     ENUM\_EIG\_VALUES       jobv,               // compute eigenvectors or not     vectorf&              eigen\_values,       // vector of computed eigenvalues     matrixf&              eigen\_vectors       // matrix of computed eigenvectors     ); |

Computing for type matrix<complex>

|  |
| --- |
| bool  matrixc::EigenSymmetricQR(     ENUM\_EIG\_VALUES       jobv,               // compute eigenvectors or not     vector&               eigen\_values,       // vector of computed eigenvalues     matrixc&              eigen\_vectors       // matrix of computed eigenvectors     ); |

Computing for type matrix<complexf>

|  |
| --- |
| bool  matrixcf::EigenSymmetricQR(     ENUM\_EIG\_VALUES       jobv,               // compute eigenvectors or not     vectorf&              eigen\_values,       // vector of computed eigenvalues     matrixcf&             eigen\_vectors       // matrix of computed eigenvectors     ); |

Parameters

jobv

[in] [ENUM\_EIG\_VALUES](../EigenSymmetricDC/EigenSymmetricDC.md#enum_eig_values) enumeration value which determines the method for computing eigenvectors.

eigen\_values

[out] Vector of eigenvalues.

eigen\_vectors

[out] Matrix of eigenvectors.

Return Value

Return true if successful, otherwise false in case of an [error](../../../../../Constants,-Enumerations-and-Structures/Codes-of-Errors-and-Warnings/Runtime-Errors/Runtime-Errors.md).

Note

Computation depends on the value of the jobv parameter.

When jobv = EIGVALUES\_V, eigenvectors and eigenvalues are calculated.

If EIGVALUES\_N is set, eigenvectors are not calculated. Only eigenvalues are computed.

The input can be a symmetric (Hermitian), [upper triangular](../../../../Manipulations/TriU/TriU.md) or [lower triangular](../../../../Manipulations/TriL/TriL.md) matrix. Triangular matrices are assumed to be symmetric (Hermitian conjugated).

 

ENUM\_EIG\_VALUES

An enumeration defining the need to compute eigenvectors.

| ID | Description |
| --- | --- |
| EIGVALUES\_V | Eigenvectors and eigenvalues are calculated. |
| EIGVALUES\_N | Only eigenvalues are computed, without vectors. |
