# Matrix and Vector Types

Matrix and Vector Types

Matrix and vector are special data types in MQL5 which enable linear algebra operations. The following data types exist:

- matrix — a matrix containing double elements.
- matrixf — a matrix containing float elements.
- matrixc — a matrix containing complex elements.
- vector — a vector containing double elements.
- vectorf — a vector containing float elements.
- vectorc — a vector containing complex elements.

Template functions support notations like matrix<double>, matrix<float>, vector<double>, vector<float> instead of the corresponding types.

Matrix and vector initialization methods

| Function | Action |
| --- | --- |
| [Eye](../Initialization/Eye/Eye.md) | Return a matrix with ones on the diagonal and zeros elsewhere |
| [Identity](../Initialization/Identity/Identity.md) | Create an identity matrix of the specified size |
| [Ones](../Initialization/Ones/Ones.md) | Create and return a new matrix filled with ones |
| [Zeros](../Initialization/Zeros/Zeros.md) | Create and return a new matrix filled with zeros |
| [Full](../Initialization/Full/Full.md) | Create and return a new matrix filled with given value |
| [Tri](../Initialization/Tri/Tri.md) | Construct a matrix with ones at and below the given diagonal and zeros elsewhere |
| [Init](../Initialization/Init/Init.md) | Initialize a matrix or a vector |
| [Fill](../Initialization/Fill/Fill.md) | Fill an existing matrix or vector with the specified value |
