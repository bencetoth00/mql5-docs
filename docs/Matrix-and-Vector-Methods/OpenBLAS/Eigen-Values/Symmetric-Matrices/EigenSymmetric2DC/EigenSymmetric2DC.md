# EigenSymmetric2DC

EigenSymmetric2DC

Compute all the eigenvalues, and optionally, the eigenvectors of a generalized symmetric-definite eigenproblem, of the form

A\*x=(lambda)\*B\*x,  A\*Bx=(lambda)\*x,  or B\*A\*x=(lambda)\*x.

Here A and B are assumed to be symmetric (Hermitian) and B is also positive definite. If eigenvectors are desired, it uses a divide-and-conquer algorithm (LAPACK functions [SYGVD](https://www.intel.com/content/www/us/en/docs/onemkl/developer-reference-fortran/2025-2/sygvd.html), [HEGVD](https://www.intel.com/content/www/us/en/docs/onemkl/developer-reference-fortran/2025-2/hegvd.html)).

Computing for type matrix<double>

|  |
| --- |
| bool  matrix::EigenSymmetric2DC(     ENUM\_EIGS2\_TYPE       itype,              // the problem type to be solved     ENUM\_EIG\_VALUES       jobv,               // compute eigenvectors or not     matrix&               B,                  // second matrix     vector&               eigen\_values,       // vector of computed eigenvalues     matrix&               eigen\_vectors,      // matrix of computed eigenvectors     matrix&               triangular\_factor   // triangular factor from the Cholesky factorization B     ); |

Computing for type matrix<float>

|  |
| --- |
| bool  matrixf::EigenSymmetric2DC(     ENUM\_EIGS2\_TYPE       itype,              // the problem type to be solved     ENUM\_EIG\_VALUES       jobv,               // compute eigenvectors or not     matrixf&              B,                  // second matrix     vectorf&              eigen\_values,       // vector of computed eigenvalues     matrixf&              eigen\_vectors,      // matrix of computed eigenvectors     matrixf&              triangular\_factor   // triangular factor from the Cholesky factorization B     ); |

Computing for type matrix<complex>

|  |
| --- |
| bool  matrixc::EigenSymmetric2DC(     ENUM\_EIGS2\_TYPE       itype,              // the problem type to be solved     ENUM\_EIG\_VALUES       jobv,               // compute eigenvectors or not     matrixc&              B,                  // second matrix     vector&               eigen\_values,       // vector of computed eigenvalues     matrixc&              eigen\_vectors,      // matrix of computed eigenvectors     matrixc&              triangular\_factor   // triangular factor from the Cholesky factorization B     ); |

Computing for type matrix<complexf>

|  |
| --- |
| bool  matrixcf::EigenSymmetric2DC(     ENUM\_EIGS2\_TYPE       itype,              // the problem type to be solved     ENUM\_EIG\_VALUES       jobv,               // compute eigenvectors or not     matrixcf&             B,                  // second matrix     vectorf&              eigen\_values,       // vector of computed eigenvalues     matrixcf&             eigen\_vectors,      // matrix of computed eigenvectors     matrixcf&             triangular\_factor   // triangular factor from the Cholesky factorization B     ); |

Parameters

itype

[in]  ENUM\_EIGS2\_TYPE enumeration value which specified the problem type to be solved : A\*x=(lambda)\*B\*x,  A\*Bx=(lambda)\*x,  or B\*A\*x=(lambda)\*x.

jobv

[in]  ENUM\_EIG\_VALUES enumeration value which determines the method for computing eigenvectors.

B

[in]  Second matrix B. Must be positive definite symmetric (or Hermitian conjugated) matrix.

eigen\_values

[out] Vector of eigenvalues.

eigen\_vectors

[out] Matrix of eigenvectors.

triangular\_factor

[out] The triangular factor U or L from the Cholesky factorization B = U\*\*T\*U or B = L\*L\*\*T.

Return Value

Return true if successful, otherwise false in case of an [error](../../../../../Constants,-Enumerations-and-Structures/Codes-of-Errors-and-Warnings/Runtime-Errors/Runtime-Errors.md).

Note

The input can be a symmetric (Hermitian), [upper triangular](../../../../Manipulations/TriU/TriU.md) or [lower triangular](../../../../Manipulations/TriL/TriL.md) matrix. Triangular matrices are assumed to be symmetric (Hermitian conjugated). Second matrix B must be positive definite symmetric. If the input matrix and second matrix B are triangular, then both must be the same triangular, upper or lower.

 

ENUM\_EIGS2\_TYPE

An enumeration that specifies  the problem type to be solved.

| ID | Description |
| --- | --- |
| EIGS2TYPE\_1 | 1:  A\*x = (lambda)\*B\*x |
| EIGS2TYPE\_2 | 2:  A\*B\*x = (lambda)\*x |
| EIGS2TYPE\_3 | 3:  B\*A\*x = (lambda)\*x |

ENUM\_EIG\_VALUES

An enumeration that specifies whether to calculate eigenvectors.

| ID | Description |
| --- | --- |
| EIGVALUES\_V | Eigenvectors and eigenvalues are calculated. |
| EIGVALUES\_N | Only eigenvalues are calculated, without vectors. |
