# EigVals

EigVals

Compute the eigenvalues of a general matrix.

|  |
| --- |
| bool matrix::EigVals(    vector&  eigen\_values      // vector of eigenvalues      ); |

Parameters

eigen\_values

[out]  Vector of right eigenvalues.

Return Value

Returns true on success, false otherwise.

 

Note

The only difference between EigVals and Eig is that EigVals does not calculate eigenvectors, while it only calculates eigenvalues.
