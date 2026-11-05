# EigenVectorsBackward


Forms the right or left eigenvectors of a real or complex general matrix by backward transformation on the computed eigenvectors of the balanced matrix output by [MatrixBalance](../MatrixBalance/MatrixBalance.md). LAPACK function [GEBAK](https://www.intel.com/content/www/us/en/docs/onemkl/developer-reference-fortran/2025-2/gebak.html).

Computing for type matrix<double>

```cpp
bool  matrix::EigenVectorsBackward(
   ENUM_EIG_BALANCE      job,                     // matrix balancing method
   ENUM_EIG_SIDE         side,                    // right or left eigenvectors
   long                  ilo,                     // subscript of balanced matrix
   long                  ihi,                     // superscript of balanced matrix
   vector&               scale,                   // details of permutations and scaling when balancing the input matrix
   matrix&               V                        // eigenvectors
   );
```

Computing for type matrix<float>

```cpp
bool  matrixf::EigenVectorsBackward(
   ENUM_EIG_BALANCE      job,                     // input matrix balancing method
   ENUM_EIG_SIDE         side,                    // right or left eigenvectors
   long                  ilo,                     // subscript of balanced matrix
   long                  ihi,                     // superscript of balanced matrix
   vectorf&              scale,                   // details of permutations and scaling when balancing the input matrix
   matrixf&              V                        // eigenvectors
   );
```

Computing for type matrix<complex>

```cpp
bool  matrixc::EigenVectorsBackward(
   ENUM_EIG_BALANCE      job,                     // input matrix balancing method
   ENUM_EIG_SIDE         side,                    // right or left eigenvectors
   long                  ilo,                     // subscript of balanced matrix
   long                  ihi,                     // superscript of balanced matrix
   vector&               scale,                   // details of permutations and scaling when balancing the input matrix
   matrixc&              V                        // eigenvectors
   );
```

Computing for type matrix<complexf>

```cpp
bool  matrixcf::EigenVectorsBackward(
   ENUM_EIG_BALANCE      job,                     // input matrix balancing method
   ENUM_EIG_SIDE         side,                    // right or left eigenvectors
   long                  ilo,                     // subscript of balanced matrix
   long                  ihi,                     // superscript of balanced matrix
   vectorf&              scale,                   // details of permutations and scaling when balancing the input matrix
   matrixcf&             V                        // eigenvectors
   );
```

Parameters

job

[in]  Value from the ENUM\_EIG\_BALANCE enumeration which determines the need and method for balancing the input matrix.

side

[in]  Value from the ENUM\_EIG\_SIDE enumeration defining the need to compute right or left eigenvectors.

ilo

[in]  Subscript of the balanced matrix. As returned by [MatrixBalance](../MatrixBalance/MatrixBalance.md).

ihi

[in]  Superscript of the balanced matrix. As returned by [MatrixBalance](../MatrixBalance/MatrixBalance.md).

scale

[in]  Vector of details of permutations and scaling when balancing the input matrix. As returned by [MatrixBalance](../MatrixBalance/MatrixBalance.md).

V

[out]  Right or left eigenvectors backtransformed from the input eigenvectors.

Return Value

Return true if successful, otherwise false in case of an [error](../../../../Constants,-Enumerations-and-Structures/Codes-of-Errors-and-Warnings/Runtime-Errors/Runtime-Errors.md).

Note

When computing eigenvalues and eigenvectors, matrix balancing (scaling of rows and columns) is often used to improve numerical stability. This balancing is performed by the GEBAL function, which transforms the matrix into a "nicer" form.

After balancing and computing the eigenvectors of the transformed matrix, the result does not correspond to the original matrix. In this case, [GEBAK](https://www.intel.com/content/www/us/en/docs/onemkl/developer-reference-fortran/2025-2/gebak.html) is called to transform the eigenvectors back into the space of the original (unbalanced) matrix.

This method is applied to the matrix of right or left eigenvectors of balanced matrix. They can be produced by some [eigen solver](../../Eigen-Values/General-Matrices/General-Matrices.md).

 

ENUM\_EIG\_BALANCE

An enumeration defining the need to compute eigenvectors.

| ID | Description |
| --- | --- |
| EIGBALANCE\_N | Do not diagonally scale or permute |
| EIGBALANCE\_P | Perform permutations to make the matrix more nearly upper triangular. Do not diagonally scale |
| EIGBALANCE\_S | Diagonally scale the matrix. Do not permute |
| EIGBALANCE\_B | Both diagonally scale and permute |

ENUM\_EIG\_SIDE

An enumeration defining the need to compute right or left eigenvectors.

| ID | Description |
| --- | --- |
| EIGSIDE\_R | 'R': right eigenvectors |
| EIGSIDE\_L | 'L': left eigenvectors |