# Factored Calculations

Factored Calculations

This help section describes a set of functions for the numerical solution of linear algebra problems based on matrix factorizations and LAPACK library methods, wrapped in the matrix, matrixf, matrixc, and matrixcf classes.

These functions are focused on highly efficient and reliable calculations applicable to various types of matrices: real and complex, single- and double-precision. They cover key problems of applied linear algebra, including:

- Solving systems of linear equations (SLAEs);
- Estimating the condition number of a matrix;
- Inverse transformations and computing inverse matrices;
- Special SVD-based techniques for obtaining pseudoinverses and polar decompositions.

These functions work in conjunction with matrix prefactorizations such as Cholesky, LDL, PLU, and others, implemented in the corresponding modules. The algorithms used replicate the behavior of LAPACK and allow for efficient processing of both dense and specialized matrix structures (e.g., tridiagonal).

Below are all available functions, grouped by the factorization method used.

| Function | Action |
| --- | --- |
| [PLULinearEquationsSolution](PLULinearEquationsSolution/PLULinearEquationsSolution.md) | Solves a system of linear equations  A \* X = B,  A\*\*T \* X = B, or  A\*\*H \* X = B with an LU-factored square coefficient matrix AF computed by [FactorizationPLURaw](../Factorizations/FactorizationPLURaw/FactorizationPLURaw.md), with multiple right-hand sides. LAPACK function [GETRS](https://www.intel.com/content/www/us/en/docs/onemkl/developer-reference-fortran/2025-2/getrs.html). |
| [PLUInverse](PLUInverse/PLUInverse.md) | Computes the inverse of an LU-factored general matrix AF computed by [FactorizationPLURaw](../Factorizations/FactorizationPLURaw/FactorizationPLURaw.md). LAPACK function [GETRI](https://www.intel.com/content/www/us/en/docs/onemkl/developer-reference-fortran/2025-2/getri.html). |
| [PLUCondNumReciprocal](PLUCondNumReciprocal/PLUCondNumReciprocal.md) | Estimates the reciprocal of the condition number of a general matrix A in either the one-norm or infinity-norm, using the LU factorization computed by [FactorizationPLURaw](../Factorizations/FactorizationPLURaw/FactorizationPLURaw.md). LAPACK function [GECON](https://www.intel.com/content/www/us/en/docs/onemkl/developer-reference-fortran/2025-2/gecon.html). |
| [PLUQLinearEquationsSolution](PLUQLinearEquationsSolution/PLUQLinearEquationsSolution.md) | Solves a system of linear equations A \* X = scale \* RHS with a general N-by-N matrix A using the LU-factoization with complete pivoting computed by [FactorizationPLUQRaw](../Factorizations/FactorizationPLUQRaw/FactorizationPLUQRaw.md). LAPACK function [GESC2](https://www.intel.com/content/www/us/en/docs/onemkl/developer-reference-fortran/2025-2/gesc2.html). |
| [PLUGeTridLinearEquationsSolution](PLUGeTridLinearEquationsSolution/PLUGeTridLinearEquationsSolution.md) | Solves a system of linear equations A \* X = B,  A\*\*T \* X = B, or  A\*\*H \* X = B with a tridiagonal matrix A using the LU-factorization computed by [FactorizationPLUGeTridRaw](../Factorizations/FactorizationPLUGeTridRaw/FactorizationPLUGeTridRaw.md), with multiple right-hand sides. LAPACK function [GTTRS](https://www.intel.com/content/www/us/en/docs/onemkl/developer-reference-fortran/2025-2/gttrs.html). |
| [PLUGeTridCondNumReciprocal](PLUGeTridCondNumReciprocal/PLUGeTridCondNumReciprocal.md) | Estimates the reciprocal of the condition number of a general tridiagonal matrix A in either the one-norm or infinity-norm, using the LU factorization computed by [FactorizationPLUGeTridRaw](../Factorizations/FactorizationPLUGeTridRaw/FactorizationPLUGeTridRaw.md). LAPACK function [GTCON](https://www.intel.com/content/www/us/en/docs/onemkl/developer-reference-fortran/2025-2/gtcon.html). |
| [LDLLinearEquationsSolution](LDLLinearEquationsSolution/LDLLinearEquationsSolution.md) | Solves a system of linear equations  A \* X = B  with a real symmetric or complex Hermitian indefinite matrix using the factorization A = U\*\*T \* D \* U or A = L \* D \* L\*\*T computed by [FactorizationLDLRaw](../Factorizations/FactorizationLDLRaw/FactorizationLDLRaw.md), with multiple right-hand sides. LAPACK functions [SYTRS](https://www.intel.com/content/www/us/en/docs/onemkl/developer-reference-fortran/2025-2/sytrs.html), [HETRS](https://www.intel.com/content/www/us/en/docs/onemkl/developer-reference-fortran/2025-2/hetrs.html). |
| [LDLInverse](LDLInverse/LDLInverse.md) | Computes the inverse of a real symmetric or complex Hermitian indefinite matrix using the factorization A = U\*\*T \* D \* U or A = L \* D \* L\*\*T computed by [FactorizationLDLRaw](../Factorizations/FactorizationLDLRaw/FactorizationLDLRaw.md). LAPACK functions [SYTRI](https://www.intel.com/content/www/us/en/docs/onemkl/developer-reference-fortran/2025-2/sytri.html), [HETRI](https://www.intel.com/content/www/us/en/docs/onemkl/developer-reference-fortran/2025-2/hetri.html). |
| [LDLCondNumReciprocal](LDLCondNumReciprocal/LDLCondNumReciprocal.md) | Estimates the reciprocal of the condition number of a real symmetric or complex Hermitian indefinite matrix A, using the LDLT factorization computed by [FactorizationLDLRaw](../Factorizations/FactorizationLDLRaw/FactorizationLDLRaw.md). LAPACK functions [SYCON](https://www.intel.com/content/www/us/en/docs/onemkl/developer-reference-fortran/2025-2/sycon.html), [HECON](https://www.intel.com/content/www/us/en/docs/onemkl/developer-reference-fortran/2025-2/hecon.html). |
| [LDLComplexSyLinearEquationsSolution](LDLComplexSyLinearEquationsSolution/LDLComplexSyLinearEquationsSolution.md) | Solves a system of linear equations  A \* X = B  with a complex symmetric indefinite matrix using the factorization A = U\*\*T \* D \* U or A = L \* D \* L\*\*T computed by [FactorizationLDLComplexSyRaw](../Factorizations/FactorizationLDLComplexSyRaw/FactorizationLDLComplexSyRaw.md), with multiple right-hand sides. LAPACK function [SYTRS](https://www.intel.com/content/www/us/en/docs/onemkl/developer-reference-fortran/2025-2/sytrs.html). |
| [LDLComplexSyInverse](LDLComplexSyInverse/LDLComplexSyInverse.md) | Computes the inverse of a complex symmetric indefinite matrix using the factorization A = U\*\*T \* D \* U or A = L \* D \* L\*\*T computed by [FactorizationLDLComplexSyRaw](../Factorizations/FactorizationLDLComplexSyRaw/FactorizationLDLComplexSyRaw.md). LAPACK function [SYTRI](https://www.intel.com/content/www/us/en/docs/onemkl/developer-reference-fortran/2025-2/sytri.html). |
| [LDLComplexSyCondNumReciprocal](LDLComplexSyCondNumReciprocal/LDLComplexSyCondNumReciprocal.md) | Estimates the reciprocal of the condition number of a complex symmetric indefinite matrix A, using the LDLT factorization computed by [FactorizationLDLComplexSyRaw](../Factorizations/FactorizationLDLComplexSyRaw/FactorizationLDLComplexSyRaw.md). LAPACK function [SYCON](https://www.intel.com/content/www/us/en/docs/onemkl/developer-reference-fortran/2025-2/sycon.html). |
| [LDLSyTridPDLinearEquationsSolution](LDLSyTridPDLinearEquationsSolution/LDLSyTridPDLinearEquationsSolution.md) | Solves a system of linear equations  A \* X = B  with a real symmetric or complex Hermitian positive-definite tridiagonal matrix using the factorization A = L \* D \* L\*\*T computed by [FactorizationLDLSyTridPD](../Factorizations/FactorizationLDLSyTridPD/FactorizationLDLSyTridPD.md), with multiple right-hand sides. LAPACK function [PTTRS](https://www.intel.com/content/www/us/en/docs/onemkl/developer-reference-fortran/2025-2/pttrs.html). |
| [LDLSyTridPDCondNumReciprocal](LDLSyTridPDCondNumReciprocal/LDLSyTridPDCondNumReciprocal.md) | Estimates the reciprocal of the condition number of a real symmetric or complex Hermitian positive-definite tridiagonal matrix A using the LDLT factorization computed by [FactorizationLDLSyTridPD](../Factorizations/FactorizationLDLSyTridPD/FactorizationLDLSyTridPD.md). LAPACK function [PTCON](https://www.intel.com/content/www/us/en/docs/onemkl/developer-reference-fortran/2025-2/ptcon.html). |
| [CholeskyLinearEquationsSolution](CholeskyLinearEquationsSolution/CholeskyLinearEquationsSolution.md) | Solves a system of linear equations  A \* X = B  with a real symmetric or complex Hermitian positive-definite matrix using the factorization A = L \* L\*\*T computed by [FactorizationCholesky](../Factorizations/FactorizationCholesky/FactorizationCholesky.md), with multiple right-hand sides. LAPACK function [POTRS](https://www.intel.com/content/www/us/en/docs/onemkl/developer-reference-fortran/2025-2/potrs.html). |
| [CholeskyInverse](CholeskyInverse/CholeskyInverse.md) | Computes the inverse of a real symmetric or complex Hermitian positive-definite matrix using the LLT factorization computed by [FactorizationCholesky](../Factorizations/FactorizationCholesky/FactorizationCholesky.md). LAPACK function [POTRI](https://www.intel.com/content/www/us/en/docs/onemkl/developer-reference-fortran/2025-2/potri.html). |
| [CholeskyCondNumReciprocal](CholeskyCondNumReciprocal/CholeskyCondNumReciprocal.md) | Estimates the reciprocal of the condition number of a real symmetric or complex Hermitian positive-definite matrix A using the LDL factorization computed by [FactorizationCholesky](../Factorizations/FactorizationCholesky/FactorizationCholesky.md). LAPACK function [POCON](https://www.intel.com/content/www/us/en/docs/onemkl/developer-reference-fortran/2025-2/pocon.html). |
| [SylvesterEquationSchur](SylvesterEquationSchur/SylvesterEquationSchur.md) | Solves Sylvester equation for real quasi-triangular or complex triangular matrices: A\*X + X\*B = C where  A and B are both upper triangular. A is m-by-m and B is n-by-n; the right hand side C and the solution X are m-by-n. LAPACK function [TRSYL](https://www.intel.com/content/www/us/en/docs/onemkl/developer-reference-fortran/2025-2/trsyl.html). |
| [SylvesterEquationSchurBlocked](SylvesterEquationSchurBlocked/SylvesterEquationSchurBlocked.md) | Solves Sylvester equation for real quasi-triangular or complex triangular matrices: A\*X + X\*B = C where  A and B are both upper triangular. A is m-by-m and B is n-by-n; the right hand side C and the solution X are m-by-n. LAPACK function [TRSYL3](https://www.intel.com/content/www/us/en/docs/onemkl/developer-reference-fortran/2025-2/trsyl3.html). This is the block (BLAS level 3) version of [TRSYL](../Linear-Equations/SylvesterEquationTriangular/SylvesterEquationTriangular.md). Faster up to 5 times but not so accurate. |
| [Pseudo Inverse](Pseudo-Inverse/Pseudo-Inverse.md) | There is no special function in the OpenBLAS library to calculate the pseudo-inverse of a matrix. However, for this purpose can be used [singular value decomposition](../Singular-Value-Decomposition/Singular-Value-Decomposition.md) (SVD) |
| [Polar Decomposition](Polar-Decomposition/Polar-Decomposition.md) | There is no special function in the OpenBLAS library to calculate the polar decomposition of a matrix. However, for this purpose can be used [singular value decomposition](../Singular-Value-Decomposition/Singular-Value-Decomposition.md) (SVD) |

The functions provide support for various matrix types (real, complex, single-precision, and double-precision) and cover the following key tasks.

Condition Number Estimation

Unlike the true condition number, the estimate is approximate but much faster. Here, CondNumReciprocal denotes the inverse of the condition number (i.e., 1/cond\_number).

Functions of the \*CondNumReciprocal type are designed to estimate the reciprocal of the condition number of a matrix:

- [CholeskyCondNumReciprocal](CholeskyCondNumReciprocal/CholeskyCondNumReciprocal.md) — for positive-definite matrices with LLT factorization;
- [LDLCondNumReciprocal](LDLCondNumReciprocal/LDLCondNumReciprocal.md) — for indefinite symmetric or Hermitian matrices with LDL factorization;
- [LDLSyTridPDCondNumReciprocal](LDLSyTridPDCondNumReciprocal/LDLSyTridPDCondNumReciprocal.md) — for positive-definite symmetric tridiagonal matrices;
- [PLUCondNumReciprocal](PLUCondNumReciprocal/PLUCondNumReciprocal.md), [PLUGeTridCondNumReciprocal](PLUGeTridCondNumReciprocal/PLUGeTridCondNumReciprocal.md) —  for generalized and tridiagonal matrices with LU factorization.

Matrix Inverse

Functions of the \*Inverse type calculate the inverse matrix based on the corresponding factorization:

- [CholeskyInverse](CholeskyInverse/CholeskyInverse.md), [LDLInverse](LDLInverse/LDLInverse.md), [PLUInverse](PLUInverse/PLUInverse.md) — for various forms of factorization;
- use the ipiv index array if permutation information is required.

Linear System Solvers

\*LinearEquationsSolution functions solve linear equations of the form A \* X = B:

- Both matrix and vector right-hand sides are supported;
- The transposition (or Hermitian conjugation) of the coefficient matrix is taken into account via [ENUM\_EQUATIONS\_FORM](PLULinearEquationsSolution/PLULinearEquationsSolution.md#enum_equations_form);
- Separate functions are provided for tridiagonal and generalized matrices.

Поддержка расширенных LU-факторизаций

The [PLUQLinearEquationsSolution](PLUQLinearEquationsSolution/PLUQLinearEquationsSolution.md) function solves the system with scaling:

|  |
| --- |
| A \* X = scale \* B |

based on full LU factorization with row- and column-wise permutations.

Special Methods (based on SVD)

While the library functions do not directly implement polar decomposition or pseudoinverse matrices, this section contains implementation examples based on singular value decomposition:

- [PolarDecomposition](Polar-Decomposition/Polar-Decomposition.md) —  decomposition of A = Q \* P, where Q  is an orthogonal matrix and P is a symmetric positive-definite matrix;
- [PseudoInverse](Pseudo-Inverse/Pseudo-Inverse.md) — calculation of the pseudoinverse of a matrix A+ = V \* Σ⁺ \* Uᵀ.

 

Notes

- All functions return true on success and false on error.
- Prerequisites include previously performed factorizations (FactorizationCholesky, FactorizationLDLRaw, GETRF, etc.).
- Calculation results may be sensitive to numerical stability, especially for small values of rcond.
