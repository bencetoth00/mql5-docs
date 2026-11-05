# ReflectHessenbergToQ

ReflectHessenbergToQ

Generates orthogonal matrix Q  which is defined as the product of n-1 elementary reflectors of order n, as returned by [ReduceToHessenberg](../ReduceToHessenberg/ReduceToHessenberg.md):

Q = H(1) H(2) . . . H(n-1).

LAPACK function [ORGHR](https://www.intel.com/content/www/us/en/docs/onemkl/developer-reference-fortran/2025-2/orghr.html).

As input is used transformed matrix reflect\_q with the same sizes n-by-n as in original matrix A.

Computing for type matrix<double>

|  |
| --- |
| bool  matrix::ReflectHessenbergToQ(     vector&         tau\_q,        // scalar factors of the elementary reflectors Q     matrix&         Q             // matrix Q     ); |

Computing for type matrix<float>

|  |
| --- |
| bool  matrix::ReflectHessenbergToQ(     vectorf&        tau\_q,        // scalar factors of the elementary reflectors Q     matrixf&        Q             // matrix Q     ); |

Computing for type matrix<complex>

|  |
| --- |
| bool  matrix::ReflectHessenbergToQ(     vectorc&        tau\_q,        // scalar factors of the elementary reflectors Q     matrixc&        Q             // matrix Q     ); |

Computing for type matrix<complexf>

|  |
| --- |
| bool  matrix::ReflectHessenbergToQ(     vectorcf&       tau\_q,        // scalar factors of the elementary reflectors Q     matrixcf&       Q             // matrix Q     ); |

Parameters

tau\_q

[in] Vector of the scalar factors of the elementary reflectors which represent the orthogonal matrix Q.

Q

[out]  Orthogonal matrix Q.

 

Return Value

Return true if successful, otherwise false in case of an [error](../../../../Constants,-Enumerations-and-Structures/Codes-of-Errors-and-Warnings/Runtime-Errors/Runtime-Errors.md).
