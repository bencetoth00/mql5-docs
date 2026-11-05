# ReduceSymmetricToTridiagonal

ReduceSymmetricToTridiagonal

Reduces a real symmetric or complex Hermitian matrix A to trdiagonal form B by an orthogonal similarity transformation: Q\*\*T \* A \* Q = B. LAPACK functions [SYTRD](https://www.intel.com/content/www/us/en/docs/onemkl/developer-reference-fortran/2025-2/sytrd.html), [HETRD](https://www.intel.com/content/www/us/en/docs/onemkl/developer-reference-fortran/2025-2/hetrd.html).

Computing for type matrix<double>

|  |
| --- |
| bool  matrix::ReduceSymmetricToTridiagonal(     matrix&         B,            // tridiagonal matrix     matrix&         reflect\_q,    // q-reflectors     vector&         tau\_q         // scalar factors of the elementary reflectors Q     ); |

Computing for type matrix<float>

|  |
| --- |
| bool  matrix::ReduceSymmetricToTridiagonal(     matrixf&        B,            // tridiagonal matrix     matrixf&        reflect\_q,    // q-reflectors     vectorf&        tau\_q         // scalar factors of the elementary reflectors Q     ); |

Computing for type matrix<complex>

|  |
| --- |
| bool  matrix::ReduceSymmetricToTridiagonal(     matrixc&        B,            // tridiagonal matrix     matrixc&        reflect\_q,    // q-reflectors     vectorc&        tau\_q         // scalar factors of the elementary reflectors Q     ); |

Computing for type matrix<complexf>

|  |
| --- |
| bool  matrix::ReduceSymmetricToTridiagonal(     matrixcf&       B,            // tridiagonal matrix     matrixcf&       reflect\_q,    // q and p-reflectors     vectorcf&       tau\_q         // scalar factors of the elementary reflectors Q     ); |

Parameters

B

[out]  Symmetric (or Hermitian) tridiagonal matrix.

reflect\_q

[out] Upper or lower triangular matrix, it depends on the input matrix A. In upper case the diagonal and first superdiagonal of A are overwritten by the corresponding elements of the tridiagonal matrix B, and the elements above the first superdiagonal, with the array tau\_q, represent the orthogonal matrix Q as a product of elementary reflectors; in lower case the diagonal and first subdiagonal of A are overwritten by the corresponding elements of the tridiagonal matrix B, and the elements below the first subdiagonal, with the array tau\_q, represent the orthogonal matrix Q as a product of elementary reflectors.

tau\_q

[out] Vector of the scalar factors of the elementary reflectors which represent the orthogonal matrix Q.

Return Value

Return true if successful, otherwise false in case of an [error](../../../../Constants,-Enumerations-and-Structures/Codes-of-Errors-and-Warnings/Runtime-Errors/Runtime-Errors.md).

Note

In upper case the matrix Q is represented as a product of elementary reflectors

    Q = H(n-1) . . . H(2) H(1)

Each H(i) has the form

    H(i) = I - tau \* v \* v\*\*T

where tau is a scalar, and v is a vector with v(i+1:n) = 0 and v(i) = 1; v(1:i-1) is stored on exit in A(1:i-1,i+1), and tau in tau\_q(i).

In lower case the matrix Q is represented as a product of elementary reflectors

    Q = H(1) H(2) . . . H(n-1)

Each H(i) has the form

    H(i) = I - tau \* v \* v\*\*T

where tau is a scalar, and v is a vector with v(1:i) = 0 and v(i+1) = 1; v(i+2:n) is stored on exit in A(i+2:n,i), and tau in tau\_q(i). \*/

 

The contents of A on exit (output matrix reflect\_q) are illustrated by the following examples with n = 5:

|  |
| --- |
| upper case:                          lower case:       (  d   e   v2  v3  v4 )              (  d                  )    (      d   e   v3  v4 )              (  e   d              )    (          d   e   v4 )              (  v1  e   d          )    (              d   e  )              (  v1  v2  e   d      )    (                  d  )              (  v1  v2  v3  e   d  ) |

where d and e denote diagonal and off-diagonal elements of B and vi denotes an element of the vector defining H(i).

Matrix Q can be produced with [ReflectTridiagonalToQ](../ReflectBidiagonalToQP/ReflectBidiagonalToQP.md) method.

The input can be a symmetric, upper triangular or lower triangular matrix. Triangular matrices are assumed to be symmetric.
