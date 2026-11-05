# EigenSolver2


Compute generalized eigenvalues and eigenvectors for a pair of ordinary square matrices (LAPACK function [GGEV](https://www.intel.com/content/www/us/en/docs/onemkl/developer-reference-fortran/2025-2/ggev.html)). Both matrices must be the same size.

Computing for type matrix<double>

```cpp
bool  matrix::EigenSolver2(
   matrix&               B,                       // second matrix in the pair
   ENUM_EIG_VECTORS      jobv,                    // method to compute right and left vectors
   vectorc&              alpha,                   // vector of computed eigenvalues
   vector&               beta,                    // vector of eigenvalue divisors
   matrix&               left_eigenvectors,       // matrix of computed left vectors
   matrix&               right_eigenvectors       // matrix of computed right vectors
   );
```

Computing for type matrix<float>

```cpp
bool  matrixf::EigenSolver2(
   matrix&               B,                       // second matrix in the pair
   ENUM_EIG_VECTORS      jobv,                    // method to compute right and left vectors
   vectorcf&             alpha,                   // vector of computed eigenvalues
   vectorf&              beta,                    // vector of eigenvalue divisors
   matrixf&              left_eigenvectors,       // matrix of computed left vectors
   matrixf&              right_eigenvectors       // matrix of computed right vectors
   );
```

Computing for type matrix<complex>

```cpp
bool  matrixc::EigenSolver2(
   matrixc&              B,                       // second matrix in the pair
   ENUM_EIG_VECTORS      jobv,                    // method to compute right and left vectors
   vectorc&              alpha,                   // vector of computed eigenvalues
   vectorc&              beta,                    // vector of eigenvalue divisors
   matrixc&              left_eigenvectors,       // matrix of computed left vectors
   matrixc&              right_eigenvectors       // matrix of computed right vectors
   );
```

Computing for type matrix<complexf>

```cpp
bool  matrixcf::EigenSolver2(
   matrixcf&             B,                       // second matrix in the pair
   ENUM_EIG_VECTORS      jobv,                    // method to compute right and left vectors
   vectorcf&             alpha,                   // vector of computed eigenvalues
   vectorcf&             beta,                    // vector of eigenvalue divisors
   matrixcf&             left_eigenvectors,       // matrix of computed left vectors
   matrixcf&             right_eigenvectors       // matrix of computed right vectors
   );
```

Parameters

B

[in]  The second matrix in the pair.

jobv

[in] [ENUM\_EIG\_VECTORS](../EigenSolver/EigenSolver.md#enum_eig_vectors) enumeration value which determines the method for computing left and right eigenvectors.

alpha

[out] Vector of eigenvalues.

beta

[out]  Vector of eigen value divisors.

left\_eigenvectors

[out] Matrix of left eigenvectors.

right\_eigenvectors

[out] Matrix of right eigenvectors.

Return Value

Return true if successful, otherwise false in case of an [error](../../../../../Constants,-Enumerations-and-Structures/Codes-of-Errors-and-Warnings/Runtime-Errors/Runtime-Errors.md).

Note

Computation depends on the value of the jobv parameter.

ENUM\_EIG\_VECTORS

An enumeration defining the need to compute eigenvectors.

| ID | Description |
| --- | --- |
| EIGVECTORS\_N | Only eigenvalues are computed, without vectors. |
| EIGVECTORS\_L | Only left eigenvectors are computed. |
| EIGVECTORS\_R | Only right eigenvectors are computed. |
| EIGVECTORS\_LR | Left and right eigenvectors are computed, eigenvalues are always computed. |

 

A generalized eigenvalue for a pair of matrices (A,B) is a scalar lambda or a ratio alpha/beta = lambda, such that A - lambda\*B is singular. It is usually represented as the pair (alpha,beta), as there is a reasonable interpretation for beta=0, and even for both being zero.

The right eigenvector v(j) corresponding to the eigenvalue lambda(j) of (A,B) satisfies

                 A \* v(j) = lambda(j) \* B \* v(j).

The left eigenvector u(j) corresponding to the eigenvalue lambda(j) of (A,B) satisfies

                 u(j)\*\*H \* A  = lambda(j) \* u(j)\*\*H \* B .

where u(j)\*\*H is the conjugate-transpose of u(j).

Real (non-complex) matrices can have a complex solution. Therefore, the input vector of eigenvalues must be complex. In case of a complex solution, the error code is set to [4019 (ERR\_MATH\_OVERFLOW)](../../../../../Constants,-Enumerations-and-Structures/Codes-of-Errors-and-Warnings/Runtime-Errors/Runtime-Errors.md). Otherwise, only the real parts of the complex values of the eigenvalue vector should be used.