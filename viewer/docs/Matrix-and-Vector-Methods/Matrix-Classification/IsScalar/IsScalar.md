# IsScalar


Check if a square matrix is scalar matrix.

```cpp
bool matrix::IsScalar();
```

Return Value

True if square matrix is scalar matrix.

Note

Scalar matrix is a diagonal matrix, where all diagonal elements are equal.

Zero matrix of n-by-n size is scalar matrix. Square [identity matrix](../../Initialization/Identity/Identity.md) is scalar matrix.

Scalar matrix

```cpp
   I  0  0  0  0  0
   0  I  0  0  0  0
   0  0  I  0  0  0
   0  0  0  I  0  0
   0  0  0  0  I  0
   0  0  0  0  0  I
```