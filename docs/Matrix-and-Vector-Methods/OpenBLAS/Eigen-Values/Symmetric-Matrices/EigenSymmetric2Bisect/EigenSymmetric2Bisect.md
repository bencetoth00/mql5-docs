# EigenSymmetric2Bisect

EigenSymmetric2Bisect

Compute all the eigenvalues, and optionally, the eigenvectors of a generalized symmetric-definite eigenproblem, of the form

A\*x=(lambda)\*B\*x,  A\*Bx=(lambda)\*x,  or B\*A\*x=(lambda)\*x.

Here A and B are assumed to be symmetric (Hermitian) and B is also positive definite. Eigenvalues and eigenvectors can be selected by specifying either a range of values or a range of indices for the desired eigenvalues. This method uses bisection algorithm (LAPACK functions [SYGVX](https://www.intel.com/content/www/us/en/docs/onemkl/developer-reference-fortran/2025-2/sygvx.html), [HEGVX](https://www.intel.com/content/www/us/en/docs/onemkl/developer-reference-fortran/2025-2/hegvx.html)).

Computing for type matrix<double>

|  |
| --- |
| bool  matrix::EigenSymmetric2Bisect(     ENUM\_EIGS2\_TYPE       itype,              // the problem type to be solved     ENUM\_EIG\_VALUES       jobv,               // compute eigenvectors or not     ENUM\_BLAS\_RANGE       range,              // subset of eigenvalues to compute     double                lower,              // lower bound of the subset     double                upper,              // Upper bound of the subset     double                abstol,             // absolute error tolerance     matrix&               B,                  // second matrix     vector&               eigen\_values,       // vector of computed eigenvalues     matrix&               eigen\_vectors,      // matrix of computed eigenvectors     matrix&               triangular\_factor   // triangular factor from the Cholesky factorization B     ); |

Computing for type matrix<float>

|  |
| --- |
| bool  matrixf::EigenSymmetric2Bisect(     ENUM\_EIGS2\_TYPE       itype,              // the problem type to be solved     ENUM\_EIG\_VALUES       jobv,               // compute eigenvectors or not     ENUM\_BLAS\_RANGE       range,              // subset of eigenvalues to compute     float                 lower,              // lower bound of the subset     float                 upper,              // upper bound of the subset     float                 abstol,             // absolute error tolerance     matrixf&              B,                  // second matrix     vectorf&              eigen\_values,       // vector of computed eigenvalues     matrixf&              eigen\_vectors,      // matrix of computed eigenvectors     matrixf&              triangular\_factor   // triangular factor from the Cholesky factorization B     ); |

Computing for type matrix<complex>

|  |
| --- |
| bool  matrixc::EigenSymmetric2Bisect(     ENUM\_EIGS2\_TYPE       itype,              // the problem type to be solved     ENUM\_EIG\_VALUES       jobv,               // compute eigenvectors or not     ENUM\_BLAS\_RANGE       range,              // subset of eigenvalues to compute     double                lower,              // lower bound of the subset     double                upper,              // Upper bound of the subset     double                abstol,             // absolute error tolerance     matrixc&              B,                  // second matrix     vector&               eigen\_values,       // vector of computed eigenvalues     matrixc&              eigen\_vectors,      // matrix of computed eigenvectors     matrixc&              triangular\_factor   // triangular factor from the Cholesky factorization B     ); |

Computing for type matrix<complexf>

|  |
| --- |
| bool  matrixcf::EigenSymmetric2Bisect(     ENUM\_EIGS2\_TYPE       itype,              // the problem type to be solved     ENUM\_EIG\_VALUES       jobv,               // compute eigenvectors or not     ENUM\_BLAS\_RANGE       range,              // subset of eigenvalues to compute     float                 lower,              // lower bound of the subset     float                 upper,              // Upper bound of the subset     float                 abstol,             // absolute error tolerance     matrixcf&             B,                  // second matrix     vectorf&              eigen\_values,       // vector of computed eigenvalues     matrixcf&             eigen\_vectors,      // matrix of computed eigenvectors     matrixcf&             triangular\_factor   // triangular factor from the Cholesky factorization B     ); |

Parameters

itype

[in]  ENUM\_EIGS2\_TYPE enumeration value which specified the problem type to be solved : A\*x=(lambda)\*B\*x,  A\*Bx=(lambda)\*x,  or B\*A\*x=(lambda)\*x.

jobv

[in]  ENUM\_EIG\_VALUES enumeration value which determines the method for computing eigenvectors.

range

[in] [ENUM\_BLAS\_RANGE](../../../Singular-Value-Decomposition/SingularValueDecompositionBisection/SingularValueDecompositionBisection.md) enumeration value that defines a subset of computable eigenvalues and vectors.

lower

[in]  The lower bound of eigenvalues subset; it is specified depending on the value of the 'range' parameter.

upper

[in]  The upper bound of eigenvalues subset; it is specified depending on the value of the 'range' parameter.

abstol

[in]  Absolute error tolerance.

The absolute error tolerance to which each eigenvalue/eigenvector is required.

If jobv = 'V', the eigenvalues and eigenvectors output have residual norms bounded by abstol, and the dot products between different eigenvectors are bounded by abstol.

If abstol < n \*eps\*|T|, then n \*eps\*|T| is used instead, where eps is the machine precision, and |T| is the 1-norm of the matrix T. The eigenvalues are computed to an accuracy of eps\*|T| irrespective of abstol.

If high relative precision is important, 'abstol' should be set to a safe minimum value X such that 1.0/X does not overflow.

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

Computation depends on the values of the jobv and range parameters.

When BLASRANGE\_A is set, all eigenvalues are computed, and the lower and upper parameters are ignored.

With the BLASRANGE\_V value, only those eigenvalues (and their vectors) are computed, which fall within the range of real values specified by the 'lower' and 'upper' parameters.

With the BLASRANGE\_I value, only those eigenvalues (and their vectors) are computed, which fall within the range of integer indices specified by the 'lower' and 'upper' parameters. For example, with lower=0 and upper=2, only the first three eigenvalues are computed.

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

ENUM\_BLAS\_RANGE

An enumeration defining how right singular vectors should be computed.

| ID | Description |
| --- | --- |
| BLASRANGE\_A | All singular or eigenvalues will be found. |
| BLASRANGE\_V | All singular or eigenvalues in the half-open interval (VL,VU] will be found. |
| BLASRANGE\_I | The IL-th through IU-th singular or eigenvalues will be found. |
