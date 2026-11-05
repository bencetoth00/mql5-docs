# CholeskyLinearEquationsSolution

CholeskyLinearEquationsSolution

Solves a system of linear equations  A \* X = B  with a real symmetric or complex Hermitian positive-definite matrix using the factorization A = L \* L\*\*T computed by [FactorizationCholesky](../../Factorizations/FactorizationCholesky/FactorizationCholesky.md), with multiple right-hand sides. LAPACK function [POTRS](https://www.intel.com/content/www/us/en/docs/onemkl/developer-reference-fortran/2025-2/potrs.html).

Computing for type matrix<double>

|  |
| --- |
| bool  matrix::CholeskyLinearEquationsSolution(     matrix&             B,            // right hand side matrix B     matrix&             X             // solution matrix X     );     bool  matrix::CholeskyLinearEquationsSolution(     vector&             B,            // right hand side vector B     vector&             X             // solution vector X     ); |

Computing for type matrix<float>

|  |
| --- |
| bool  matrixf::CholeskyLinearEquationsSolution(     matrixf&            B,            // right hand side matrix B     matrixf&            X             // solution matrix X     );     bool  matrixf::CholeskyLinearEquationsSolution(     vectorf&            B,            // right hand side vector B     vectorf&            X             // solution vector X     ); |

Computing for type matrix<complex>

|  |
| --- |
| bool  matrixc::CholeskyLinearEquationsSolution(     matrixc&            B,            // right hand side matrix B     matrixc&            X             // solution matrix X     );     bool  matrixc::CholeskyLinearEquationsSolution(     vectorc&            B,            // right hand side vector B     vectorc&            X             // solution vector X     ); |

Computing for type matrix<complexf>

|  |
| --- |
| bool  matrixcf::CholeskyLinearEquationsSolution(     matrixcf&           B,            // right hand side matrix B     matrixcf&           X             // solution matrix X     );     bool  matrixcf::CholeskyLinearEquationsSolution(     vectorcf&           B,            // right hand side vector B     vectorcf&           X             // solution vector X     ); |

Parameters

B

[in]  Matrix B whose columns are the right-hand sides for the systems of equations. Vector B contains one column of right-hand side.

X

[out]  Matrix or vector X with solutions of linear equations system.

 

Return Value

Return true if successful, otherwise false in case of an [error](../../../../Constants,-Enumerations-and-Structures/Codes-of-Errors-and-Warnings/Runtime-Errors/Runtime-Errors.md).

Note

This method is applied to the matrix L obtained as result of [FactorizationCholesky](../../Factorizations/FactorizationCholesky/FactorizationCholesky.md) method.

Output matrix X has the same sizes as input matrix B. Output vector X has the same size as input vector B.
