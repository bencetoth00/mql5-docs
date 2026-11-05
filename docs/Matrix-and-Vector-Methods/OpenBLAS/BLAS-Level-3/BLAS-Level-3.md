# BLAS Level 3

BLAS Level 3

The "BLAS Level 3" section in MQL5 provides a set of high-performance functions for performing matrix-matrix operations — a fundamental class of linear algebra tasks optimized using the BLAS (Basic Linear Algebra Subprograms) Level 3 standards.

The functions in this section implement various types of matrix multiplication and update operations, including general, symmetric, Hermitian, and triangular cases. They support computations with data types float, double, complex, and complexf, offering a convenient object-oriented interface for the classes matrix, matrixf, matrixc, and matrixcf.

These methods fully correspond to the standard BLAS L3 subroutines (GEMM, SYMM, HEMM, SYRK, HERK, SYR2K, HER2K, TRMM), ensuring efficient utilization of modern processor instructions and multithreading.Thus, the BLAS Level 3 section is designed for solving linear algebra problems that require high accuracy and performance when working with large matrices, serving as a foundation for implementing numerical algorithms and data analysis in MQL5.

| Function | Action |
| --- | --- |
| [BlasL3GeMM](BlasL3GeMM/BlasL3GeMM.md) | Computes a matrix-matrix product with general matrices. C = alpha \* op(A) \* op(B) + beta \* C, where C is m-by-n matrix, op(A) is m-by-k matrix, op(B) is k-by-n matrix. BLAS function [GEMM](https://www.intel.com/content/www/us/en/docs/onemkl/developer-reference-fortran/2025-2/gemm-001.html). |
| [BlasL3SyMM](BlasL3SyMM/BlasL3SyMM.md) | Computes a matrix-matrix product where the input matrix A is symmetric. C = alpha\*A\*B + beta\*C  or C = alpha\*B\*A + beta\*C, where A is a symmetric matrix of m-by-m size if side='L', or n-by-n size otherwise; B and C are m-by-n matrices. BLAS function [SYMM](https://www.intel.com/content/www/us/en/docs/onemkl/developer-reference-fortran/2025-2/symm.html). |
| [BlasL3HeMM](BlasL3HeMM/BlasL3HeMM.md) | Computes a matrix-matrix product where the input matrix A is Hermitian. C = alpha\*A\*B + beta\*C  or C = alpha\*B\*A + beta\*C, where A is a Hermitian matrix of m-by-m size if side='L', or n-by-n size otherwise; B and C are m-by-n matrices. BLAS function [HEMM](https://www.intel.com/content/www/us/en/docs/onemkl/developer-reference-fortran/2025-2/hemm.html). |
| [BlasL3TrMM](BlasL3TrMM/BlasL3TrMM.md) | Computes a matrix-matrix product where the input matrix A is triangular. C = alpha\*op(A)  or C = alpha\*B\*op(A), where A is a triangular matrix of m-by-m size if side='L', or n-by-n size otherwise; B and C are m-by-n matrices. BLAS function [TRMM](https://www.intel.com/content/www/us/en/docs/onemkl/developer-reference-fortran/2025-2/trmm.html). |
| [BlasL3SyRK](BlasL3SyRK/BlasL3SyRK.md) | Performs a symmetric rank-k update. CU = alpha \* A \* A\*\*T + beta\*C  or CU = alpha \* A\*\*T \* A + beta\*C. BLAS function [SYRK](https://www.intel.com/content/www/us/en/docs/onemkl/developer-reference-fortran/2025-2/syrk.html). |
| [BlasL3HeRK](BlasL3HeRK/BlasL3HeRK.md) | Performs a Hermitian rank-k update. CU = alpha \* A \* A\*\*H + beta\*C  or CU = alpha \* A\*\*H \* A + beta\*C. BLAS function [HERK](https://www.intel.com/content/www/us/en/docs/onemkl/developer-reference-fortran/2025-2/herk.html). |
| [BlasL3SyR2K](BlasL3SyR2K/BlasL3SyR2K.md) | Performs a symmetric rank-2k update. CU = alpha \* A \* B\*\*T + alpha \* B \* A\*\*T + beta\*C  or CU = alpha \* A\*\*T \* B + alpha \* B\*\*T \* A + beta\*C. BLAS function [SYR2K](https://www.intel.com/content/www/us/en/docs/onemkl/developer-reference-fortran/2025-2/syr2k.html). |
| [BlasL3HeR2K](BlasL3HeR2K/BlasL3HeR2K.md) | Performs a Hermitian rank-2k update. CU = alpha \* A \* B\*\*H + alpha \* B \* A\*\*H + beta\*C  or CU = alpha \* A\*\*H \* B + alpha \* B\*\*H \* A + beta\*C. BLAS function [HER2K](https://www.intel.com/content/www/us/en/docs/onemkl/developer-reference-fortran/2025-2/her2k.html). |
