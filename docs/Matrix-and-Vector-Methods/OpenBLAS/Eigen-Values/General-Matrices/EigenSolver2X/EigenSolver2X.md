# EigenSolver2X

EigenSolver2X

Compute generalized eigenvalues and eigenvectors for a pair of regular square matrices in Expert mode, i.e. with the ability to influence the computation algorithm and the ability to obtain accompanying computation data (LAPACK function [GGEVX](https://www.intel.com/content/www/us/en/docs/onemkl/developer-reference-fortran/2025-2/ggevx.html)). Both matrices must be the same size.

Optionally, it also computes a balancing transformation to improve the conditioning of the eigenvalues and eigenvectors (ILO, IHI, LSCALE, RSCALE, ABNRM, and BBNRM), reciprocal condition numbers for the eigenvalues (RCONDE), and reciprocal condition numbers for the right eigenvectors (RCONDV).

Computing for type matrix<double>

|  |
| --- |
| bool  matrix::EigenSolver2X(     matrix&               B,                       // second matrix in the pair     ENUM\_EIG\_BALANCE      balance,                 // input matrix balancing method     ENUM\_EIG\_VECTORS      jobv,                    // determines computation of right and left eigenvectors     ENUM\_EIG\_SENSE        sense,                   // determines computation of reciprocal condition numbers     vectorc&              alpha,                   // vector of computed eigenvalues     vector&               beta,                    // vector of eigenvalue divisors     matrix&               left\_eigenvectors,       // matrix of computed left vectors     matrix&               right\_eigenvectors       // matrix of computed right vectors       matrix&               schur\_matrix1,           // the first part of the real Schur form of the "balanced" versions of the input A and B     matrix&               schur\_matrix2,           // the second part of the real Schur form of the "balanced" versions of the input A and B     long&                 ilo,                     // subscript of balanced matrix     long&                 ihi,                     // superscript of balanced matrix     vector&               lscale,                  // details of the permutations and scaling factors applied to the left side of A and B     vector&               rscale,                  // details of the permutations and scaling factors applied to the right side of A and B     double&               ab\_norm,                 // one-norm of balanced input matrix     double&               bb\_norm,                 // one-norm of balanced second matrix B     vector&               rconde,                  // vector of reciprocal condition numbers for each eigenvalue     vector&               rcondv                   // vector of reciprocal condition numbers for each eigenvector     ); |

Computing for type matrix<float>

|  |
| --- |
| bool  matrixf::EigenSolver2X(     matrixf&              B,                       // second matrix in the pair     ENUM\_EIG\_BALANCE      balance,                 // input matrix balancing method     ENUM\_EIG\_VECTORS      jobv,                    // determines computation of right and left eigenvectors     ENUM\_EIG\_SENSE        sense,                   // determines computation of reciprocal condition numbers     vectorcf&             alpha,                   // vector of computed eigenvalues     vectorf&              beta,                    // vector of eigenvalue divisors     matrixf&              left\_eigenvectors,       // matrix of computed left vectors     matrixf&              right\_eigenvectors       // matrix of computed right vectors       matrixf&              schur\_matrix1,           // the first part of the real Schur form of the "balanced" versions of the input A and B     matrixf&              schur\_matrix2,           // the second part of the real Schur form of the "balanced" versions of the input A and B     long&                 ilo,                     // subscript of balanced matrix     long&                 ihi,                     // superscript of balanced matrix     vectorf&              lscale,                  // details of the permutations and scaling factors applied to the left side of A and B     vectorf&              rscale,                  // details of the permutations and scaling factors applied to the right side of A and B     float&                ab\_norm,                 // one-norm of balanced input matrix     float&                bb\_norm,                 // one-norm of balanced second matrix B     vectorf&              rconde,                  // vector of reciprocal condition numbers for each eigenvalue     vectorf&              rcondv                   // vector of reciprocal condition numbers for each eigenvector     ); |

Computing for type matrix<complex>

|  |
| --- |
| bool  matrixc::EigenSolver2X(     matrixc&              B,                       // second matrix in the pair     ENUM\_EIG\_BALANCE      balance,                 // input matrix balancing method     ENUM\_EIG\_VECTORS      jobv,                    // determines computation of right and left eigenvectors     ENUM\_EIG\_SENSE        sense,                   // determines computation of reciprocal condition numbers     vectorc&              alpha,                   // vector of computed eigenvalues     vectorc&              beta,                    // vector of eigenvalue divisors     matrixc&              left\_eigenvectors,       // matrix of computed left vectors     matrixc&              right\_eigenvectors       // matrix of computed right vectors       matrixc&              schur\_matrix1,           // the first part of the real Schur form of the "balanced" versions of the input A and B     matrixc&              schur\_matrix2,           // the second part of the real Schur form of the "balanced" versions of the input A and B     long&                 ilo,                     // subscript of balanced matrix     long&                 ihi,                     // superscript of balanced matrix     vector&               lscale,                  // details of the permutations and scaling factors applied to the left side of A and B     vector&               rscale,                  // details of the permutations and scaling factors applied to the right side of A and B     double&               ab\_norm,                 // one-norm of balanced input matrix     double&               bb\_norm,                 // one-norm of balanced second matrix B     vector&               rconde,                  // vector of reciprocal condition numbers for each eigenvalue     vector&               rcondv                   // vector of reciprocal condition numbers for each eigenvector      ); |

Computing for type matrix<complexf>

|  |
| --- |
| bool  matrixcf::EigenSolver2X(     matrixcf&             B,                       // second matrix in the pair     ENUM\_EIG\_BALANCE      balance,                 // input matrix balancing method     ENUM\_EIG\_VECTORS      jobv,                    // determines computation of right and left eigenvectors     ENUM\_EIG\_SENSE        sense,                   // determines computation of reciprocal condition numbers     vectorcf&             alpha,                   // vector of computed eigenvalues     vectorf&              beta,                    // vector of eigenvalue divisors     matrixcf&             left\_eigenvectors,       // matrix of computed left vectors     matrixcf&             right\_eigenvectors       // matrix of computed right vectors       matrixcf&             schur\_matrix1,           // the first part of the real Schur form of the "balanced" versions of the input A and B     matrixcf&             schur\_matrix2,           // the second part of the real Schur form of the "balanced" versions of the input A and B     long&                 ilo,                     // subscript of balanced matrix     long&                 ihi,                     // superscript of balanced matrix     vectorf&              lscale,                  // details of the permutations and scaling factors applied to the left side of A and B     vectorf&              rscale,                  // details of the permutations and scaling factors applied to the right side of A and B     float&                ab\_norm,                 // one-norm of balanced input matrix     float&                bb\_norm,                 // one-norm of balanced second matrix B     vectorf&              rconde,                  // vector of reciprocal condition numbers for each eigenvalue     vectorf&              rcondv                   // vector of reciprocal condition numbers for each eigenvector      ); |

Parameters

B

[in]  The second matrix in the pair.

balance

[in]  Value from the [ENUM\_EIG\_BALANCE](EigenSolver2X.md#enum_eig_balance) enumeration which determines the need and method for balancing the input matrix; it is used to improve the conditioning of the eigenvalues and eigenvectors.

jobv

[in]   Value from the [ENUM\_EIG\_VECTORS](../EigenSolver/EigenSolver.md#enum_eig_vectors) enumeration which determines the method for computing left and right eigenvectors.

sense

[in]   Value from the [ENUM\_EIG\_SENSE](EigenSolver2X.md#enum_eig_sense) enumeration which determines the need to compute reciprocal condition numbers.

eigen\_values

[out] Vector of eigenvalues.

left\_eigenvectors

[out] Matrix of left eigenvectors.

right\_eigenvectors

[out] Matrix of right eigenvectors.

schur\_matrix1, schur\_matrix2

[out]  2 parts of balanced matrix in Schur form; the matrix is not filled if neither left nor right eigenvectors are computed.

ilo

[out]  Subscript of the balanced matrix; the matrix is not filled if no balancing is applied.

ihi

[out]  Superscript of the balanced matrix; the matrix is not filled if no balancing is applied.

lscale

[out]  Vector contains details of the permutations and scaling factors applied to the left side of A and B.

If PL(j) is the index of the row interchanged with row j, and DL(j) is the scaling factor applied to row j, then

lscale(j) = PL(j), for j = 1,..., ilo-1

= DL(j), for j = ilo,...,ihi

= PL(j) for j = ihi+1,..., n.

The order in which the interchanges are made is n to ihi+1, then 1 to ilo-1.

rscale

[out]  Vector contains details of the permutations and scaling factors applied to the right side of A and B.

If PR(j) is the index of the column interchanged with column j, and DR(j) is the scaling factor applied to column j, then

rscale(j) = PR(j), for j = 1,..., ilo-1

= DR(j), for j = ilo,...,ihi

= PR(j) for j = ihi+1,..., n.

The order in which the interchanges are made is n to ihi+1, then 1 to ilo-1.

ab\_norm

[out]  One-norm of the balanced input matrix (the maximum of the sum of absolute values of elements in any of the matrix columns).

bb\_norm

[out]  One-norm of balanced second matrix B.

rconde

[out]  Vector of reciprocal condition numbers for each eigenvalue; it is computed if the 'sense' parameter is set to 'E' or 'B'.

rcondv

[out]  Vector of reciprocal condition numbers for each eigenvector; it is computed if the 'sense' parameter is set to 'V' or 'B'.

Return Value

The function returns 'true' on success or 'false' if an [error](../../../../../Constants,-Enumerations-and-Structures/Codes-of-Errors-and-Warnings/Runtime-Errors/Runtime-Errors.md) occurs.

Note

Input matrices balancing depends on the value of the balance parameter.

ENUM\_EIG\_BALANCE

An enumeration that specifies whether the matrices should be balanced.

| ID | Description |
| --- | --- |
| EIGBALANCE\_N | Do not diagonally scale or permute. |
| EIGBALANCE\_P | Perform permutations to make the matrix more nearly upper triangular. Do not diagonally scale. |
| EIGBALANCE\_S | Diagonally scale the matrix. Do not permute. |
| EIGBALANCE\_B | Both diagonally scale and permute. |

 

ENUM\_EIG\_VECTORS

An enumeration defining the need to compute eigenvectors.

| ID | Description |
| --- | --- |
| EIGVECTORS\_N | Only eigenvalues are computed, without vectors. |
| EIGVECTORS\_L | Only left eigenvectors are computed. |
| EIGVECTORS\_R | Only right eigenvectors are computed. |
| EIGVECTORS\_LR | Left and right eigenvectors are computed, eigenvalues are always computed. |

 

ENUM\_EIG\_SENSE

An enumeration determining the need to compute reciprocal condition numbers.

| ID | Description |
| --- | --- |
| EIGSENSE\_N | None of reciprocal condition numbers are computed. |
| EIGSENSE\_E | Computed for eigenvalues only. |
| EIGSENSE\_V | Computed for right eigenvectors only. |
| EIGSENSE\_B | Computed for eigenvalues and right eigenvectors. |
