# Manipulations

Matrix and vector manipulations

These are methods for basic matrix operations: filling, copying, getting a part of a matrix, transposing, splitting and sorting.

There are also several methods for operations with matrix rows and columns.

| Function | Action |
| --- | --- |
| [HasNan](HasNan/HasNan.md) | Return the number of [NaN](../../Language-Basics/Data-Types/Real-Types-(double,-float)/Real-Types-(double,-float).md) values in a matrix/vector |
| [ReplaceNan](ReplaceNan/ReplaceNan.md) | Replace [NaN](../../Language-Basics/Data-Types/Real-Types-(double,-float)/Real-Types-(double,-float).md) values in a matrix/vector with the specified value and return the number of elements replaced |
| [ReplaceToZero](ReplaceToZero/ReplaceToZero.md) | Replace small values in a matrix/vector with the zero value and return the number of elements replaced |
| [NormalizeDouble](NormalizeDouble/NormalizeDouble.md) | Round matrix/vector elements to a specified accuracy |
| [Transpose](Transpose/Transpose.md) | Reverse or permute the axes of a matrix; returns the modified matrix |
| [TransposeConjugate](TransposeConjugate/TransposeConjugate.md) | Transposing a complex matrix with conjugation. Reverse or permute the axes of a matrix by changing a sign of an imaginary part of a complex number, return the modified matrix |
| [TriL](TriL/TriL.md) | Return a copy of a matrix with elements above the k-th diagonal zeroed. Lower triangular matrix |
| [TriU](TriU/TriU.md) | Return a copy of a matrix with elements below the k-th diagonal zeroed. Upper triangular matrix |
| [Diag](Diag/Diag.md) | Extract a diagonal or construct a diagonal matrix |
| [Row](Row/Row.md) | Return a row vector. Write a vector to the specified row |
| [Col](Col/Col.md) | Return a column vector. Write a vector to the specified column |
| [Copy](Copy/Copy.md) | Return a copy of the given matrix/vector |
| [Conjugate](Conjugate/Conjugate.md) | Changing the sign of the imaginary part of a complex number, return the modified matrix or vector |
| [Concat](Concat/Concat.md) | Concatenate 2 submatrices to one matrix. Concatenate 2 vectors to one vector |
| [Compare](Compare/Compare.md) | Compare the elements of two matrices/vectors with the specified precision |
| [CompareByDigits](CompareByDigits/CompareByDigits.md) | Compare the elements of two matrices/vectors up to significant digits |
| [CompareEqual](CompareEqual/CompareEqual.md) | Perform an absolute comparison of two matrices by unfolding successive rows into one-dimensional vectors |
| [Flat](Flat/Flat.md) | Allow addressing a matrix element through one index instead of two |
| [Clip](Clip/Clip.md) | Limit the elements of a matrix/vector to a specified range of valid values |
| [Reshape](Reshape/Reshape.md) | Change the shape of a matrix without changing its data |
| [Resize](Resize/Resize.md) | Return a new matrix with a changed shape and size |
| [Set](Set/Set.md) | Set the value for a vector element by the specified index |
| [SwapRows](SwapRows/SwapRows.md) | Swap rows in a matrix |
| [SwapCols](SwapCols/SwapCols.md) | Swap columns in a matrix |
| [Split](Split/Split.md) | Split a matrix into multiple submatrices |
| [Hsplit](Hsplit/Hsplit.md) | Split a matrix horizontally into multiple submatrices. Same as [Split](Split/Split.md) with axis=0 |
| [Vsplit](Vsplit/Vsplit.md) | Split a matrix vertically into multiple submatrices. Same as [Split](Split/Split.md) with axis=1 |
| [ArgSort](ArgSort/ArgSort.md) | Indirectly sort a matrix or vector. |
| [Sort](Sort/Sort.md) | Sort a matrix or vector in place. |
