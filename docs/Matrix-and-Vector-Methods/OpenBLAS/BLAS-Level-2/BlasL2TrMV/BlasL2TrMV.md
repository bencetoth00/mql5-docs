# BlasL2TrMV

BlasL2TrMV

Computes a matrix-vector product using a triangular n-by-n matrix.

y = op(A) \* x

BLAS function [TRMV](https://www.intel.com/content/www/us/en/docs/onemkl/developer-reference-fortran/2025-2/trmv.html).

Computing for type matrix<double>

|  |
| --- |
| bool  matrix::BlasL2TrMV(     ENUM\_BLAS\_TRANS trans,         // specifies option op(A)     vector&         X,             // vector X     vector&         Y              // result vector Y     ); |

Computing for type matrix<float>

|  |
| --- |
| bool  matrixf::BlasL2TrMV(     ENUM\_BLAS\_TRANS trans,         // specifies option op(A)     vectorf&        X,             // vector X     vectorf&        Y              // result vector Y     ); |

Computing for type matrix<complex>

|  |
| --- |
| bool  matrixc::BlasL2TrMV(     ENUM\_BLAS\_TRANS trans,         // specifies option op(A)     vectorc&        X,             // vector X     vectorc&        Y              // result vector Y     ); |

Computing for type matrix<complexf>

|  |
| --- |
| bool  matrixcf::BlasL2TrMV(     ENUM\_BLAS\_TRANS trans,         // specifies option op(A)     vectorcf&       X,             // vector X     vectorcf&       Y              // result vector Y     ); |

Parameters

trans

[in]  Value from the ENUM\_BLAS\_TRANS enumeration, which specifies the operation:

if trans= 'N', then y = A \* x;

if trans= 'T', then y = A\*\*T \* x;

if trans= 'C', then y = A\*\*H \* x.

X

[in]  Vector x of size n.

Y

[out]  Result vector y of size n.

Return Value

Return true if successful, otherwise false in case of an [error](../../../../Constants,-Enumerations-and-Structures/Codes-of-Errors-and-Warnings/Runtime-Errors/Runtime-Errors.md).

Note

The input can be upper triangular or lower triangular matrix.

 

ENUM\_BLAS\_TRANS

An enumeration defining option op(A).

| ID | Description |
| --- | --- |
| BLASTRANS\_N | 'N': No transpose |
| BLASTRANS\_T | 'T': Transpose |
| BLASTRANS\_C | 'C': Conjugate transpose |
