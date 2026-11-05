# EigenSymmetricDC2s

EigenSymmetricDC2s

Compute all eigenvalues and, optionally, eigenvectors of a real symmetric or Hermitian (complex conjugated) matrix using the 2stage technique for the reduction to tridiagonal. If eigenvectors are desired, it uses a divide and conquer algorithm (LAPACK functions SYEVD\_2STAGE, HEEVD\_2STAGE).

Computing for type matrix<double>

|  |
| --- |
| bool  matrix::EigenSymmetricDC2s(     ENUM\_EIG\_VALUES       jobv,               // compute eigenvectors or not     vector&               eigen\_values,       // vector of computed eigenvalues     matrix&               eigen\_vectors       // matrix of computed eigenvectors     ); |

Computing for type matrix<float>

|  |
| --- |
| bool  matrixf::EigenSymmetricDC2s(     ENUM\_EIG\_VALUES       jobv,               // compute eigenvectors or not     vectorf&              eigen\_values,       // vector of computed eigenvalues     matrixf&              eigen\_vectors       // matrix of computed eigenvectors     ); |

Computing for type matrix<complex>

|  |
| --- |
| bool  matrixc::EigenSymmetricDC2s(     ENUM\_EIG\_VALUES       jobv,               // compute eigenvectors or not     vector&               eigen\_values,       // vector of computed eigenvalues     matrixc&              eigen\_vectors       // matrix of computed eigenvectors     ); |

Computing for type matrix<complexf>

|  |
| --- |
| bool  matrixcf::EigenSymmetricDC2s(     ENUM\_EIG\_VALUES       jobv,               // compute eigenvectors or not     vectorf&              eigen\_values,       // vector of computed eigenvalues     matrixcf&             eigen\_vectors       // matrix of computed eigenvectors     ); |

Parameters

jobv

[in] [ENUM\_EIG\_VALUES](../EigenSymmetricDC/EigenSymmetricDC.md#enum_eig_values) enumeration value which determines the method for computing eigenvectors. EIGVALUES\_V value cannot be used in the current release of OpenBLAS library.

eigen\_values

[out] Vector of eigenvalues.

eigen\_vectors

[out] Matrix of eigenvectors.

Return Value

Return true if successful, otherwise false in case of an [error](../../../../../Constants,-Enumerations-and-Structures/Codes-of-Errors-and-Warnings/Runtime-Errors/Runtime-Errors.md).

Note

Computation depends on the value of the jobv parameter.

When jobv = EIGVALUES\_V, eigenvectors and eigenvalues are calculated. In the current OpenBLAS implementation, this value is not supported. Attempting to use it will result in error 4003 (ERR\_INVALID\_PARAMETER).

If EIGVALUES\_N is set, eigenvectors are not calculated. Only eigenvalues are computed.

The input can be a symmetric (Hermitian), [upper triangular](../../../../Manipulations/TriU/TriU.md) or [lower triangular](../../../../Manipulations/TriL/TriL.md) matrix. Triangular matrices are assumed to be symmetric (Hermitian conjugated).

 

ENUM\_EIG\_VALUES

An enumeration that specifies whether to calculate eigenvectors.

| ID | Description |
| --- | --- |
| EIGVALUES\_V | Eigenvectors and eigenvalues are calculated. Not available in this release. |
| EIGVALUES\_N | Only eigenvalues are calculated, without vectors. |
