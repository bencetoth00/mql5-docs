# EigenTridiagonalQR


Compute eigenvalues and eigenvectors of a symmetric tridiagonal matrix using the QR algorithm (LAPACK function [STEV](https://www.intel.com/content/www/us/en/docs/onemkl/developer-reference-fortran/2025-2/stev.html)).

Computing for type matrix<double>

```cpp
bool  matrix::EigenTridiagonalQR(
   ENUM_EIG_VALUES       jobv,               // compute eigenvectors or not
   vector&               eigen_values,       // vector of computed eigenvalues
   matrix&               eigen_vectors       // matrix of computed eigenvectors
   );
```

Computing for type matrix<float>

```cpp
bool  matrixf::EigenTridiagonalQR(
   ENUM_EIG_VALUES       jobv,               // compute eigenvectors or not
   vectorf&              eigen_values,       // vector of computed eigenvalues
   matrixf&              eigen_vectors       // matrix of computed eigenvectors
   );
```

Parameters

jobv

[in]  ENUM\_EIG\_VALUES enumeration value which determines the method for computing eigenvectors.

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

The input must be a symmetric matrix in the tridiagonal form.

 

ENUM\_EIG\_VALUES

An enumeration that specifies whether to calculate eigenvectors.

| ID | Description |
| --- | --- |
| EIGVALUES\_V | Eigenvectors and eigenvalues are calculated. |
| EIGVALUES\_N | Only eigenvalues are calculated, without vectors. |