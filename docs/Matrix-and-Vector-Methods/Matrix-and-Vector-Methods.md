# Matrix and Vector Methods

Matrices and vectors

A matrix is a two-dimensional array of double, float, or complex numbers.

A vector is a one-dimensional array of double, float, or complex numbers. The vector has no indication of whether it is vertical or horizontal. It is determined from the use context. For example, the vector operation Dot assumes that the left vector is horizontal and the right one is vertical. If the type indication is required, one-row or one-column matrices can be used. However, this is generally not necessary.

Matrices and vectors allocate memory for data dynamically. In fact, matrices and vectors are objects that have certain properties, such as the type of data they contain and dimensions. Matrix and vector properties can be obtained using methods such as vector\_a.Size(), matrix\_b.Rows(), vector\_c.Norm(), matrix\_d.Cond() and others. Any dimension can be changed.

When creating and initializing matrices, so-called static methods are used (these are like static methods of a class). For example: matrix::Eye(), matrix::Identity(), matrix::Ones(), vector::Ones(), matrix: :Zeros(), vector::Zeros(), matrix::Full(), vector::Full(), matrix::Tri().

At the moment, matrix and vector operations do not imply the use of the complex data type, as this development direction has not yet been completed.

MQL5 supports passing of matrices and vectors to DLLs. This enables the import of functions utilizing the relevant types, from external variables.

Matrices and vectors are passed to a DLL as a pointer to a buffer. For example, to pass a matrix of type float, the corresponding parameter of the function exported from the DLL must take a float-type buffer pointer.

MQL5

|  |
| --- |
| #import "mmlib.dll"  bool sgemm(uint flags, matrix<float> &C, const matrix<float> &A, const matrix<float> &B, ulong M, ulong N, ulong K, float alpha, float beta);  #import |

C++

|  |
| --- |
| extern "C" \_\_declspec(dllexport) bool sgemm(UINT flags, float \*C, const float \*A, const float \*B, UINT64 M, UINT64 N, UINT64 K, float alpha, float beta) |

In addition to buffers, you should pass matrix and vector sizes for correct processing.

All matrix and vector methods are listed below in alphabetical order.

| Function | Action | Category |
| --- | --- | --- |
| [Activation](Machine-learning/Activation/Activation.md) | Compute activation function values and write them to the passed vector/matrix | [Machine learning](Machine-learning/Machine-learning.md) |
| [ArgMax](Statistics/ArgMax/ArgMax.md) | Return the index of the maximum value | [Statistics](Statistics/Statistics.md) |
| [ArgMin](Statistics/ArgMin/ArgMin.md) | Return the index of the minimum value | [Statistics](Statistics/Statistics.md) |
| [ArgSort](Manipulations/ArgSort/ArgSort.md) | Return the sorted index | [Manipulations](Manipulations/Manipulations.md) |
| [Assign](Initialization/Assign/Assign.md) | Copies a matrix, vector or array with auto cast | [Initialization](Initialization/Initialization.md) |
| [Average](Statistics/Average/Average.md) | Compute the weighted average of matrix/vector values | [Statistics](Statistics/Statistics.md) |
| [Cholesky](Transformations/Cholesky/Cholesky.md) | Compute the Cholesky decomposition | [Transformations](Transformations/Transformations.md) |
| [Clip](Manipulations/Clip/Clip.md) | Limits the elements of a matrix/vector to a given range of valid values | [Manipulations](Manipulations/Manipulations.md) |
| [Col](Manipulations/Col/Col.md) | Return a column vector. Write a vector to the specified column. | [Manipulations](Manipulations/Manipulations.md) |
| [Cols](Features/Cols/Cols.md) | Return the number of columns in a matrix | [Features](Features/Features.md) |
| [Compare](Manipulations/Compare/Compare.md) | Compare the elements of two matrices/vectors with the specified precision | [Manipulations](Manipulations/Manipulations.md) |
| [CompareByDigits](Manipulations/CompareByDigits/CompareByDigits.md) | Compare the elements of two matrices/vectors with the significant figures precision | [Manipulations](Manipulations/Manipulations.md) |
| [Cond](Features/Cond/Cond.md) | Compute the condition number of a matrix | [Features](Features/Features.md) |
| [Convolve](Products/Convolve/Convolve.md) | Return the discrete, linear convolution of two vectors | [Products](Products/Products.md) |
| [Copy](Manipulations/Copy/Copy.md) | Return a copy of the given matrix/vector | [Manipulations](Manipulations/Manipulations.md) |
| [Concat](Manipulations/Concat/Concat.md) | Concatenate 2 submatrices to one matrix. Concatenate 2 vectors to one vector | [Manipulations](Manipulations/Manipulations.md) |
| [CopyIndicatorBuffer](Initialization/CopyIndicatorBuffer/CopyIndicatorBuffer.md) | Get the data of the specified [indicator](../Technical-Indicators/Technical-Indicators.md) buffer in the specified quantity to a [vector](../Language-Basics/Data-Types/Matrices-and-vectors/Matrices-and-vectors.md) | [Initialization](Initialization/Initialization.md) |
| [CopyRates](Initialization/CopyRates/CopyRates.md) | Gets the historical series of the [MqlRates](../Constants,-Enumerations-and-Structures/Data-Structures/History-Data-Structure/History-Data-Structure.md) structure of the specified symbol-period in the specified amount into a matrix or vector | [Initialization](Initialization/Initialization.md) |
| [CopyTicks](Initialization/CopyTicks/CopyTicks.md) | Get ticks from an [MqlTick](../Constants,-Enumerations-and-Structures/Data-Structures/Price-Data-Structure/Price-Data-Structure.md) structure into a matrix or a vector | [Initialization](Initialization/Initialization.md) |
| [CopyTicksRange](Initialization/CopyTicksRange/CopyTicksRange.md) | Get ticks from an [MqlTick](../Constants,-Enumerations-and-Structures/Data-Structures/Price-Data-Structure/Price-Data-Structure.md) structure into a matrix or a vector within the specified date range | [Initialization](Initialization/Initialization.md) |
| [CorrCoef](Products/CorrCoef/CorrCoef.md) | Compute the Pearson correlation coefficient (linear correlation coefficient) | [Products](Products/Products.md) |
| [Correlate](Products/Correlate/Correlate.md) | Compute the cross-correlation of two vectors | [Products](Products/Products.md) |
| [Cov](Products/Cov/Cov.md) | Compute the covariance matrix | [Products](Products/Products.md) |
| [CumProd](Statistics/CumProd/CumProd.md) | Return the cumulative product of matrix/vector elements, including those along the given axis | [Statistics](Statistics/Statistics.md) |
| [CumSum](Statistics/CumSum/CumSum.md) | Return the cumulative sum of matrix/vector elements, including those along the given axis | [Statistics](Statistics/Statistics.md) |
| [Derivative](Machine-learning/Derivative/Derivative.md) | Compute activation function derivative values and write them to the passed vector/matrix | [Machine learning](Machine-learning/Machine-learning.md) |
| [Det](Features/Det/Det.md) | Compute the determinant of a square invertible matrix | [Features](Features/Features.md) |
| [Diag](Manipulations/Diag/Diag.md) | Extract a diagonal or construct a diagonal matrix | [Manipulations](Manipulations/Manipulations.md) |
| [Dot](Products/Dot/Dot.md) | Dot product of two vectors | [Products](Products/Products.md) |
| [Eig](Transformations/Eig/Eig.md) | Computes the eigenvalues and right eigenvectors of a square matrix | [Transformations](Transformations/Transformations.md) |
| [EigVals](Transformations/EigVals/EigVals.md) | Computes the eigenvalues of a general matrix | [Transformations](Transformations/Transformations.md) |
| [Eye](Initialization/Eye/Eye.md) | Return a matrix with ones on the diagonal and zeros elsewhere | [Initialization](Initialization/Initialization.md) |
| [Fill](Initialization/Fill/Fill.md) | Fill an existing matrix or vector with the specified value | [Initialization](Initialization/Initialization.md) |
| [Flat](Manipulations/Flat/Flat.md) | Access a matrix element through one index instead of two | [Manipulations](Manipulations/Manipulations.md) |
| [Full](Initialization/Full/Full.md) | Create and return a new matrix filled with the given value | [Initialization](Initialization/Initialization.md) |
| [GeMM](Products/GeMM/GeMM.md) | The GeMM (General Matrix Multiply) method implements the general multiplication of two matrices | [Products](Products/Products.md) |
| [HasNan](Manipulations/HasNan/HasNan.md) | Return the number of [NaN](../Language-Basics/Data-Types/Real-Types-(double,-float)/Real-Types-(double,-float).md) values in a matrix/vector | [Manipulations](Manipulations/Manipulations.md) |
| [Hsplit](Manipulations/Hsplit/Hsplit.md) | Split a matrix horizontally into multiple submatrices. Same as Split with axis=0 | [Manipulations](Manipulations/Manipulations.md) |
| [Identity](Initialization/Identity/Identity.md) | Create an identity matrix of the specified size | [Initialization](Initialization/Initialization.md) |
| [Init](Initialization/Init/Init.md) | Matrix or vector initialization | [Initialization](Initialization/Initialization.md) |
| [Inner](Products/Inner/Inner.md) | Inner product of two matrices | [Products](Products/Products.md) |
| [Inv](Solutions/Inv/Inv.md) | Compute the multiplicative inverse of a square invertible matrix by the Jordan-Gauss method | [Solutions](Solutions/Solutions.md) |
| [Kron](Products/Kron/Kron.md) | Return Kronecker product of two matrices, matrix and vector, vector and matrix or two vectors | [Products](Products/Products.md) |
| [Loss](Machine-learning/Loss/Loss.md) | Compute loss function values and write them to the passed vector/matrix | [Machine learning](Machine-learning/Machine-learning.md) |
| [LstSq](Solutions/LstSq/LstSq.md) | Return the least-squares solution of linear algebraic equations (for non-square or degenerate matrices) | [Solutions](Solutions/Solutions.md) |
| [LU](Transformations/LU/LU.md) | Implement an LU decomposition of a matrix: the product of a lower triangular matrix and an upper triangular matrix | [Transformations](Transformations/Transformations.md) |
| [LUP](Transformations/LUP/LUP.md) | Implement an LUP factorization with partial permutation, which refers to LU decomposition with row permutations only: PA=LU | [Transformations](Transformations/Transformations.md) |
| [MatMul](Products/MatMul/MatMul.md) | Matrix product of two matrices | [Products](Products/Products.md) |
| [Max](Statistics/Max/Max.md) | Return the maximum value in a matrix/vector | [Statistics](Statistics/Statistics.md) |
| [Mean](Statistics/Mean/Mean.md) | Compute the arithmetic mean of element values | [Statistics](Statistics/Statistics.md) |
| [Median](Statistics/Median/Median.md) | Compute the median of the matrix/vector elements | [Statistics](Statistics/Statistics.md) |
| [Min](Statistics/Min/Min.md) | Return the minimum value in a matrix/vector | [Statistics](Statistics/Statistics.md) |
| [Norm](Features/Norm/Norm.md) | Return matrix or vector norm | [Features](Features/Features.md) |
| [Ones](Initialization/Ones/Ones.md) | Create and return a new matrix filled with ones | [Initialization](Initialization/Initialization.md) |
| [Outer](Products/Outer/Outer.md) | Compute the outer product of two matrices or two vectors | [Products](Products/Products.md) |
| [Percentile](Statistics/Percentile/Percentile.md) | Return the specified percentile of values of matrix/vector elements or elements along the specified axis | [Statistics](Statistics/Statistics.md) |
| [PInv](Solutions/PInv/PInv.md) | Compute the pseudo-inverse of a matrix by the Moore-Penrose method | [Solutions](Solutions/Solutions.md) |
| [Power](Products/Power/Power.md) | Raise a square matrix to an integer power | [Products](Products/Products.md) |
| [Prod](Statistics/Prod/Prod.md) | Return the product of matrix/vector elements, which can also be executed for the given axis | [Statistics](Statistics/Statistics.md) |
| [Ptp](Statistics/Ptp/Ptp.md) | Return the range of values of a matrix/vector or of the given matrix axis | [Statistics](Statistics/Statistics.md) |
| [QR](Transformations/QR/QR.md) | Compute the qr factorization of a matrix | [Transformations](Transformations/Transformations.md) |
| [Quantile](Statistics/Quantile/Quantile.md) | Return the specified quantile of values of matrix/vector elements or elements along the specified axis | [Statistics](Statistics/Statistics.md) |
| [Random](Initialization/Random/Random.md) | Static function. Create and return a new matrix or vector filled with random values. Random values are generated uniformly within the specified range | [Initialization](Initialization/Initialization.md) |
| [Rank](Features/Rank/Rank.md) | Return matrix rank using the Gaussian method | [Features](Features/Features.md) |
| [RegressionMetric](Machine-learning/RegressionMetric/RegressionMetric.md) | Compute the regression metric as the deviation error from the regression line constructed on the specified data array | [Statistics](Statistics/Statistics.md) |
| [Reshape](Manipulations/Reshape/Reshape.md) | Change the shape of a matrix without changing its data | [Manipulations](Manipulations/Manipulations.md) |
| [Resize](Manipulations/Resize/Resize.md) | Return a new matrix with a changed shape and size | [Manipulations](Manipulations/Manipulations.md) |
| [Row](Manipulations/Row/Row.md) | Return a row vector. Write the vector to the specified row | [Manipulations](Manipulations/Manipulations.md) |
| [Rows](Features/Rows/Rows.md) | Return the number of rows in a matrix | [Features](Features/Features.md) |
| [Set](Manipulations/Set/Set.md) | Sets the value for a vector element by the specified index | [Manipulations](Manipulations/Manipulations.md) |
| [Size](Features/Size/Size.md) | Return the size of vector | [Features](Features/Features.md) |
| [SLogDet](Features/SLogDet/SLogDet.md) | Compute the sign and logarithm of the determinant of an matrix | [Features](Features/Features.md) |
| [Solve](Solutions/Solve/Solve.md) | Solve a linear matrix equation or a system of linear algebraic equations | [Solutions](Solutions/Solutions.md) |
| [Sort](Manipulations/Sort/Sort.md) | Sort by place | [Manipulations](Manipulations/Manipulations.md) |
| [Spectrum](Features/Spectrum/Spectrum.md) | Compute spectrum of a matrix as the set of its eigenvalues from the product AT\*A | [Features](Features/Features.md) |
| [Split](Manipulations/Split/Split.md) | Split a matrix into multiple submatrices | [Manipulations](Manipulations/Manipulations.md) |
| [Std](Statistics/Std/Std.md) | Return the standard deviation of values of matrix/vector elements or elements along the specified axis | [Statistics](Statistics/Statistics.md) |
| [Sum](Statistics/Sum/Sum.md) | Return the sum of matrix/vector elements, which can also be executed for the given axis (axes) | [Statistics](Statistics/Statistics.md) |
| [SVD](Transformations/SVD/SVD.md) | Singular value decomposition | [Transformations](Transformations/Transformations.md) |
| [SwapCols](Manipulations/SwapCols/SwapCols.md) | Swap columns in a matrix | [Manipulations](Manipulations/Manipulations.md) |
| [SwapRows](Manipulations/SwapRows/SwapRows.md) | Swap rows in a matrix | [Manipulations](Manipulations/Manipulations.md) |
| [Trace](Features/Trace/Trace.md) | Return the sum along diagonals of the matrix | [Features](Features/Features.md) |
| [Transpose](Manipulations/Transpose/Transpose.md) | Transpose (swap the axes) and return the modified matrix | [Manipulations](Manipulations/Manipulations.md) |
| [Tri](Initialization/Tri/Tri.md) | Construct a matrix with ones on a specified diagonal and below, and zeros elsewhere | [Initialization](Initialization/Initialization.md) |
| [TriL](Manipulations/TriL/TriL.md) | Return a copy of a matrix with elements above the k-th diagonal zeroed. Lower triangular matrix | [Manipulations](Manipulations/Manipulations.md) |
| [TriU](Manipulations/TriU/TriU.md) | Return a copy of a matrix with the elements below the k-th diagonal zeroed. Upper triangular matrix | [Manipulations](Manipulations/Manipulations.md) |
| [Var](Statistics/Var/Var.md) | Compute the variance of values of matrix/vector elements | [Statistics](Statistics/Statistics.md) |
| [Vsplit](Manipulations/Vsplit/Vsplit.md) | Split a matrix vertically into multiple submatrices. Same as Split with axis=1 | [Manipulations](Manipulations/Manipulations.md) |
| [Zeros](Initialization/Zeros/Zeros.md) | Create and return a new matrix filled with zeros | [Initialization](Initialization/Initialization.md) |
