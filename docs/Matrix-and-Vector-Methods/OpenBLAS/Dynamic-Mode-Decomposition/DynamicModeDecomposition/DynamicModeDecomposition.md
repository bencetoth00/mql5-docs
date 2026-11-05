# DynamicModeDecomposition

DynamicModeDecomposition

Compute the Dynamic Mode Decomposition(по-русски "разложение по динамическим модам") (DMD) for a pair of data snapshot matrices. LAPACK function GEDMD. For the input matrices X and Y such that Y = A\*X with an unaccessible matrix A, GEDMD computes a certain number of Ritz pairs of A using the standard Rayleigh-Ritz extraction from a subspace of  range(X) that is determined using the leading left singular vectors of X. Optionally, GEDMD returns the residuals of the computed Ritz pairs, the information needed for a refinement of the Ritz vectors, or the eigenvectors of the Exact DMD. Both matrices must be the same size.

Computing for type matrix<double>

|  |
| --- |
| bool  matrix::DynamicModeDecomposition(     matrix&               B,                       // second snapshot matrix in the pair     ENUM\_DMD\_SCALE        jobs,                    // determines whether the initial data snapshots are scaled by a diagonal matrix     ENUM\_DMD\_EIGV         jobz,                    // determines whether the eigenvectors (Koopman modes) will be computed     ENUM\_DMD\_RESIDUALS    jobr,                    // determines whether to compute the residuals     ENUM\_DMD\_REFINE       jobf,                    // specifies whether to store information needed for post-processing     ENUM\_SVD\_ALG          whtsvd,                  // allows for a selection of the SVD algorithm from the LAPACK library     long                  nrnk,                    // determines the mode how to compute the numerical rank     double                tol,                     // the tolerance for truncating small singular values     vectorc&              eigen\_values,            // vector of eigenvalues (Ritz values)     matrix&               left\_vectors,            // matrix of left singular vectors     matrix&               Z                        // matrix of Ritz vectors     vector&               residuals,               // residuals for the Ritz pairs     matrix&               res\_vectors,             // residual vectors for the Ritz pairs     matrix&               B,                       // computed vectors     matrix&               W,                       // eigenvectors of the matrix Rayleigh quotient     matrix&               S                        // computed vectors     ); |

Computing for type matrix<float>

|  |
| --- |
| bool  matrixf::DynamicModeDecomposition(     matrixf&              B,                       // second snapshot matrix in the pair     ENUM\_DMD\_SCALE        jobs,                    // determines whether the initial data snapshots are scaled by a diagonal matrix     ENUM\_DMD\_EIGV         jobz,                    // determines whether the eigenvectors (Koopman modes) will be computed     ENUM\_DMD\_RESIDUALS    jobr,                    // determines whether to compute the residuals     ENUM\_DMD\_REFINE       jobf,                    // specifies whether to store information needed for post-processing     ENUM\_SVD\_ALG          whtsvd,                  // allows for a selection of the SVD algorithm from the LAPACK library     long                  nrnk,                    // determines the mode how to compute the numerical rank     float                 tol,                     // the tolerance for truncating small singular values     vectorcf&             eigen\_values,            // vector of eigenvalues (Ritz values)     matrixf&              left\_vectors,            // matrix of left singular vectors     matrixf&              Z                        // matrix of Ritz vectors     vectorf&              residuals,               // residuals for the Ritz pairs     matrixf&              res\_vectors,             // residual vectors for the Ritz pairs     matrixf&              B,                       // computed vectors     matrixf&              W,                       // eigenvectors of the matrix Rayleigh quotient     matrixf&              S                        // computed vectors     ); |

Computing for type matrix<complex>

|  |
| --- |
| bool  matrixc::DynamicModeDecomposition(     matrixc&              B,                       // second snapshot matrix in the pair     ENUM\_DMD\_SCALE        jobs,                    // determines whether the initial data snapshots are scaled by a diagonal matrix     ENUM\_DMD\_EIGV         jobz,                    // determines whether the eigenvectors (Koopman modes) will be computed     ENUM\_DMD\_RESIDUALS    jobr,                    // determines whether to compute the residuals     ENUM\_DMD\_REFINE       jobf,                    // specifies whether to store information needed for post-processing     ENUM\_SVD\_ALG          whtsvd,                  // allows for a selection of the SVD algorithm from the LAPACK library     long                  nrnk,                    // determines the mode how to compute the numerical rank     double                tol,                     // the tolerance for truncating small singular values     vectorc&              eigen\_values,            // vector of eigenvalues (Ritz values)     matrixc&              left\_vectors,            // matrix of left singular vectors     matrixc&              Z                        // matrix of Ritz vectors     vector&               residuals,               // residuals for the Ritz pairs     matrixc&              res\_vectors,             // residual vectors for the Ritz pairs     matrixc&              B,                       // computed vectors     matrixc&              W,                       // eigenvectors of the matrix Rayleigh quotient     matrixc&              S                        // computed vectors     ); |

Computing for type matrix<complexf>

|  |
| --- |
| bool  matrixcf::DynamicModeDecomposition(     matrixcf&             B,                       // second snapshot matrix in the pair     ENUM\_DMD\_SCALE        jobs,                    // determines whether the initial data snapshots are scaled by a diagonal matrix     ENUM\_DMD\_EIGV         jobz,                    // determines whether the eigenvectors (Koopman modes) will be computed     ENUM\_DMD\_RESIDUALS    jobr,                    // determines whether to compute the residuals     ENUM\_DMD\_REFINE       jobf,                    // specifies whether to store information needed for post-processing     ENUM\_SVD\_ALG          whtsvd,                  // allows for a selection of the SVD algorithm from the LAPACK library     long                  nrnk,                    // determines the mode how to compute the numerical rank     float                 tol,                     // the tolerance for truncating small singular values     vectorcf&             eigen\_values,            // vector of eigenvalues (Ritz values)     matrixcf&             left\_vectors,            // matrix of left singular vectors     matrixcf&             Z                        // matrix of Ritz vectors     vectorf&              residuals,               // residuals for the Ritz pairs     matrixcf&             res\_vectors,             // residual vectors for the Ritz pairs     matrixcf&             B,                       // computed vectors     matrixcf&             W,                       // eigenvectors of the matrix Rayleigh quotient     matrixcf&             S                        // computed vectors     ); |

Parameters

Y

[in]  The second snapshot matrix in the pair.

jobs

[in]  Value from the [ENUM\_DMD\_SCALE](DynamicModeDecomposition.md#enum_dmd_scale) enumeration which determines whether the initial data snapshots are scaled by a diagonal matrix.

jobz

[in]   Value from the [ENUM\_DMD\_EIGV](DynamicModeDecomposition.md#enum_dmd_eigv) enumeration which determines whether the eigenvectors (Koopman modes) will be computed.

jobr

[in]   Value from the [ENUM\_DMD\_RESIDUALS](DynamicModeDecomposition.md#enum_dmd_residuals) enumeration which determines whether to compute the residuals.

jobf

[in]   Value from the [ENUM\_DMD\_REFINE](DynamicModeDecomposition.md#enum_dmd_refine) enumeration which specifies whether to store information needed for post-processing (e.g. computing refined Ritz vectors).

whtsvd

[in]   Value from the [ENUM\_SVD\_ALG](DynamicModeDecomposition.md#enum_svd_alg) enumeration which allows for a selection of the SVD algorithm from the LAPACK library.

nrnk

[in]   Value determines the mode how to compute the numerical rank, i.e. how to truncate small singular values of the input matrix X. If

       NRNK = -1 :: i-th singular value sigma(i) is truncated if sigma(i) <= TOL\*sigma(1). This option is recommended.

       NRNK = -2 :: i-th singular value sigma(i) is truncated if sigma(i) <= TOL\*sigma(i-1). This option is included for R&D purposes. It requires highly accurate SVD, which may not be feasible.

       The numerical rank can be enforced by using positive value of NRNK as follows: 0 < NRNK <= N :: at most NRNK largest singular values will be used. If the number of the computed nonzero singular values is less than NRNK, then only those nonzero values will be used and the actually used dimension is less than NRNK.

tol

[in]   The tolerance for truncating small singular values. 0 <= TOL < 1

eigen\_values

[out] Vector of eigenvalues of size K. The leading K (K<=N) entries of EIGS contain the computed eigenvalues (Ritz values).

left\_vectors

[out] Matrix of left singular vectors. The leading K columns contain a POD basis (POD - Proper Orthogonal Decomposition, правильная ортогональная декомпозиция), i.e. the leading K left singular vectors of the input data matrix X  All N columns of contain all left singular vectors of the input matrix X.

Z

[out] Matrix of Ritz vectors. If JOBZ =='V' then Z contains the  Ritz vectors.  Z(:,i) is an eigenvector of the i-th Ritz value; ||Z(:,i)||\_2=1. If JOBZ == 'F', then the Z(:,i)'s are given implicitly as the columns of X(:,1:K)\*W(1:K,1:K), i.e. X(:,1:K)\*W(:,i) is an eigenvector corresponding to EIGS(i). The columns of W(1:k,1:K) are the computed eigenvectors of the K-by-K Rayleigh quotient.

residuals

[out]  Residuals for the K computed Ritz pairs.

res\_vectors

[out]  Residual vectors for the K computed Ritz pairs.

B

[out]  M-by-K matrix (K<=N).

        If JOBF =='R', B(1:M,1:K) contains A\*U(:,1:K), and can be used for computing the refined vectors; see further details in the provided references.

        If JOBF == 'E', B(1:M,1:K) contains A\*U(:,1:K)\*W(1:K,1:K), which are the vectors from the Exact DMD, up to scaling by the inverse eigenvalues.

        If JOBF =='N', then B is not referenced.

W

[out]  K-by-K matrix (K<=N). Contains the K computed eigenvectors of the matrix Rayleigh quotient. The Ritz vectors (returned in Z) are the product of X (containing a POD basis for the input matrix X) and W.

S

[out]  K-by-K matrix (K<=N). The array S(1:K,1:K) is used for the matrix Rayleigh quotient. This content is overwritten during the eigenvalue decomposition by [GEEV](https://www.intel.com/content/www/us/en/docs/onemkl/developer-reference-fortran/2025-2/geev.html).

 

Return Value

The function returns 'true' on success or 'false' if an [error](../../../../Constants,-Enumerations-and-Structures/Codes-of-Errors-and-Warnings/Runtime-Errors/Runtime-Errors.md) occurs.

Note

The number of matrices rows (M) must not be less than the number of columns (N).

 

ENUM\_DMD\_SCALE

An enumeration that determines whether the initial data snapshots are scaled by a diagonal matrix.

| ID | Description |
| --- | --- |
| DMDSCALE\_S | 'S': The data snapshots matrices X and Y are multiplied with a diagonal matrix D so that X\*D has unit nonzero columns |
| DMDSCALE\_C | 'C': The snapshots are scaled as with the 'S' option.If it is found that an i-th column of X is zero vector and the corresponding i-th column of Y is non-zero, then the i-th column of Y is set to zero |
| DMDSCALE\_Y | 'Y': The data snapshots matrices X and Y are multiplied with a diagonal matrix D so that Y\*D has unit nonzero columns |
| DMDSCALE\_N | 'N': No data scaling |

 

ENUM\_DMD\_EIGV

An enumeration which determines whether the eigenvectors (Koopman modes) will be computed.

| ID | Description |
| --- | --- |
| DMDEIGV\_V | 'V': The eigenvectors (Koopman modes) will be computed |
| DMDEIGV\_F | 'F': The eigenvectors (Koopman modes) will be returned in factored form |
| DMDEIGV\_N | 'N': The eigenvectors are not computed |

 

ENUM\_DMD\_RESIDUALS

An enumeration which determines whether to compute the residuals.

| ID | Description |
| --- | --- |
| DMDRESIDUALS\_R | 'R': The residuals for the computed eigenpairs will be computed |
| DMDRESIDUALS\_N | 'N': The residuals are not computed |

 

ENUM\_DMD\_REFINE

An enumeration which specifies whether to store information needed for post-processing.

| ID | Description |
| --- | --- |
| DMDREFINE\_R | 'R': The matrix needed for the refinement of the Ritz vectors is computed and stored in the array B |
| DMDREFINE\_E | 'E': The unscaled eigenvectors of the Exact DMD are computed and returned in the array B |
| DMDREFINE\_N | 'N': No eigenvector refinement data is computed |

 

ENUM\_SVD\_ALG

An enumeration selecting the SVD algorythm.

| ID | Description |
| --- | --- |
| SVDALG\_1 | 1: [GESVD](https://www.intel.com/content/www/us/en/docs/onemkl/developer-reference-fortran/2025-2/gesvd.html) (the QR SVD algorithm) |
| SVDALG\_2 | 2: [GESDD](https://www.intel.com/content/www/us/en/docs/onemkl/developer-reference-fortran/2025-2/gesdd.html) (the Divide and Conquer algorithm) |
| SVDALG\_3 | 3: [GESVDQ](../../Singular-Value-Decomposition/SingularValueDecompositionQRPivot/SingularValueDecompositionQRPivot.md) (the preconditioned QR SVD; this and 4 are the most accurate options) |
| SVDALG\_4 | 4: [GEJSV](https://www.intel.com/content/www/us/en/docs/onemkl/developer-reference-fortran/2025-2/gejsv.html) (the preconditioned Jacobi SVD; this and 3 are the most accurate options) |
