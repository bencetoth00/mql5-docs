# EigenSolverX

EigenSolverX

Compute eigenvalues and eigenvectors of a regular square matrix in Expert mode, i.e. with the ability to influence the computation algorithm and the ability to obtain accompanying computation data (LAPACK function [GEEVX](https://www.intel.com/content/www/us/en/docs/onemkl/developer-reference-fortran/2025-2/geevx.html)).

Computing for type matrix<double>

|  |
| --- |
| bool  matrix::EigenSolverX(     ENUM\_EIG\_BALANCE      balance,                 // input matrix balancing method     ENUM\_EIG\_VECTORS      jobv,                    // determines computation of right and left eigenvectors     ENUM\_EIG\_SENSE        sense,                   // determines computation of reciprocal condition numbers     vectorc&              eigen\_values,            // vector of computed eigenvalues     matrix&               left\_eigenvectors,       // matrix of computed left vectors     matrix&               right\_eigenvectors       // matrix of computed right vectors     matrix&               schur\_matrix,            // balanced matrix in Schur form     long&                 ilo,                     // subscript of balanced matrix     long&                 ihi,                     // superscript of balanced matrix     vector&               scale,                   // details of permutations and scaling when balancing the input matrix     double&               ab\_norm,                 // 1-norm of balanced matrix     vector&               rconde,                  // vector of reciprocal condition numbers for each eigenvalue     vector&               rcondv                   // vector of reciprocal condition numbers for each eigenvector     ); |

Computing for type matrix<float>

|  |
| --- |
| bool  matrixf::EigenSolverX(     ENUM\_EIG\_BALANCE      balance,                 // input matrix balancing method     ENUM\_EIG\_VECTORS      jobv,                    // determines computation of right and left eigenvectors     ENUM\_EIG\_SENSE        sense,                   // determines computation of reciprocal condition numbers     vectorcf&             eigen\_values,            // vector of computed eigenvalues     matrixf&              left\_eigenvectors,       // matrix of computed left vectors     matrixf&              right\_eigenvectors       // matrix of computed right vectors     matrixf&              schur\_matrix,            // balanced matrix in Schur form     long&                 ilo,                     // subscript of balanced matrix     long&                 ihi,                     // superscript of balanced matrix     vectorf&              scale,                   // details of permutations and scaling when balancing the input matrix     float&                ab\_norm,                 // 1-norm of balanced matrix     vectorf&              rconde,                  // vector of reciprocal condition numbers for each eigenvalue     vectorf&              rcondv                   // vector of reciprocal condition numbers for each eigenvector     ); |

Computing for type matrix<complex>

|  |
| --- |
| bool  matrixc::EigenSolverX(     ENUM\_EIG\_BALANCE      balance,                 // input matrix balancing method     ENUM\_EIG\_VECTORS      jobv,                    // determines computation of right and left eigenvectors     ENUM\_EIG\_SENSE        sense,                   // determines computation of reciprocal condition numbers     vectorc&              eigen\_values,            // vector of computed eigenvalues     matrixc&              left\_eigenvectors,       // matrix of computed left vectors     matrixc&              right\_eigenvectors       // matrix of computed right vectors       matrixc&              schur\_matrix,            // balanced matrix in Schur form     long&                 ilo,                     // subscript of balanced matrix     long&                 ihi,                     // superscript of balanced matrix     vector&               scale,                   // details of permutations and scaling when balancing the input matrix     double&               ab\_norm,                 // 1-norm of balanced matrix     vector&               rconde,                  // vector of reciprocal condition numbers for each eigenvalue     vector&               rcondv                   // vector of reciprocal condition numbers for each eigenvector      ); |

Computing for type matrix<complexf>

|  |
| --- |
| bool  matrixcf::EigenSolverX(     ENUM\_EIG\_BALANCE      balance,                 // input matrix balancing method     ENUM\_EIG\_VECTORS      jobv,                    // determines computation of right and left eigenvectors     ENUM\_EIG\_SENSE        sense,                   // determines computation of reciprocal condition numbers     vectorcf&             eigen\_values,            // vector of computed eigenvalues     matrixcf&             left\_eigenvectors,       // matrix of computed left vectors     matrixcf&             right\_eigenvectors       // matrix of computed right vectors       matrixcf&             schur\_matrix,            // balanced matrix in Schur form     long&                 ilo,                     // subscript of balanced matrix     long&                 ihi,                     // superscript of balanced matrix     vectorf&              scale,                   // details of permutations and scaling when balancing the input matrix     float&                ab\_norm,                 // 1-norm of balanced matrix     vectorf&              rconde,                  // vector of reciprocal condition numbers for each eigenvalue     vectorf&              rcondv                   // vector of reciprocal condition numbers for each eigenvector      ); |

Parameters

balance

[in]  Value from the [ENUM\_EIG\_BALANCE](EigenSolverX.md#enum_eig_balance) enumeration which determines the need and method for balancing the input matrix; it is used to improve the conditioning of the eigenvalues and eigenvectors.

jobv

[in] [ENUM\_EIG\_VECTORS](../EigenSolver/EigenSolver.md#enum_eig_vectors) enumeration value which determines the method for computing left and right eigenvectors.

sense

[in]  Value from the [ENUM\_EIG\_SENSE](EigenSolverX.md#enum_eig_sense) enumeration determining the need to compute reciprocal condition numbers.

eigen\_values

[out] Vector of eigenvalues.

left\_eigenvectors

[out] Matrix of left eigenvectors.

right\_eigenvectors

[out] Matrix of right eigenvectors.

schur\_matrix

[out]  Balanced matrix in Schur form; the matrix is not filled if neither left nor right eigenvectors are computed.

ilo

[out]  Subscript of the balanced matrix; the matrix is not filled if no balancing is applied.

ihi

[out]  Superscript of the balanced matrix; the matrix is not filled if no balancing is applied.

scale

[out]  Vector of details of permutations and scaling when balancing the input matrix.

Details of the permutations and scaling factors applied when balancing A.

If P(j) is the index of the row and column interchanged with row and column j, and D(j) is the scaling factor applied to row and column j, then

scale(j) = P(j), for j = 1,...,ilo-1

= D(j), for j = ilo,...,ihi

= P(j) for j = ihi+1,..., n.

The order in which the interchanges are made is n to ihi+1, then 1 to ilo-1.

ab\_norm

[out]  1-norm of the balanced matrix (the maximum of the sum of absolute values of elements in any of the matrix columns).

rconde

[out]  Vector of reciprocal condition numbers for each eigenvalue; it is computed if the 'sense' parameter is set to 'E' or 'B'.

rcondv

[out]  Vector of reciprocal condition numbers for each eigenvector; it is computed if the 'sense' parameter is set to 'V' or 'B.

Return Value

Return true if successful, otherwise false in case of an [error](../../../../../Constants,-Enumerations-and-Structures/Codes-of-Errors-and-Warnings/Runtime-Errors/Runtime-Errors.md).

Note

Input matrix balancing depends on the value of the 'balance' parameter.

 

 

ENUM\_EIG\_BALANCE

An enumeration defining the need to compute eigenvectors.

| ID | Description |
| --- | --- |
| EIGBALANCE\_N | Do not diagonally scale or permute |
| EIGBALANCE\_P | Perform permutations to make the matrix more nearly upper triangular. Do not diagonally scale |
| EIGBALANCE\_S | Diagonally scale the matrix. Do not permute |
| EIGBALANCE\_B | Both diagonally scale and permute |

 

ENUM\_EIG\_VECTORS

An enumeration defining the need to compute eigenvectors.

| ID | Description |
| --- | --- |
| EIGVECTORS\_N | Only eigenvalues are computed, without vectors. |
| EIGVECTORS\_L | Only left eigenvectors are computed. |
| EIGVECTORS\_R | Only right eigenvectors are computed. |
| EIGVECTORS\_LR | Left and right eigenvectors are computed, eigenvalues are always computed. |

 

ENUM\_EIG\_SENSE

An enumeration defining the need to compute eigenvectors.

| ID | Description |
| --- | --- |
| EIGSENSE\_N | None of reciprocal condition numbers are computed |
| EIGSENSE\_E | Computed for eigenvalues only |
| EIGSENSE\_V | Computed for right eigenvectors only |
| EIGSENSE\_B | Computed for eigenvalues and right eigenvectors |
