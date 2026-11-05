# Tridiagonal Matrices


 

Functions for computing eigenvalues and eigenvectors of symmetric tridiagonal matrices using various algorithms. Each function implements a specific solution method and supports matrix types [double](../../../../Language-Basics/Data-Types/Real-Types-(double,-float)/Real-Types-(double,-float).md) and [float](../../../../Language-Basics/Data-Types/Real-Types-(double,-float)/Real-Types-(double,-float).md).

Common Parameters:

- jobv — Determines whether to compute eigenvectors (EIGVALUES\_V) or only eigenvalues (EIGVALUES\_N).
- range — Specifies the range of computed eigenvalues (BLASRANGE\_A, BLASRANGE\_V, BLASRANGE\_I).
- lower and upper — Lower and upper bounds for computing a subset of the spectrum.
- abstol — Absolute error tolerance.

All functions operate on symmetric tridiagonal matrices and allow selecting the most suitable algorithm depending on performance and accuracy requirements.

| Function | Action |
| --- | --- |
| [EigenTridiagonalDC](EigenTridiagonalDC/EigenTridiagonalDC.md) | Compute eigenvalues and eigenvectors of a symmetric tridiagonal matrix using the divide-and-conquer algorithm (LAPACK function [STEVD](https://www.intel.com/content/www/us/en/docs/onemkl/developer-reference-fortran/2025-2/stevd.html)). |
| [EigenTridiagonalQR](EigenTridiagonalQR/EigenTridiagonalQR.md) | Compute eigenvalues and eigenvectors of a symmetric tridiagonal matrix using the QR algorithm (LAPACK function [STEV](https://www.intel.com/content/www/us/en/docs/onemkl/developer-reference-fortran/2025-2/stev.html)). |
| [EigenTridiagonalRobust](EigenTridiagonalRobust/EigenTridiagonalRobust.md) | Compute eigenvalues and eigenvectors of a symmetric tridiagonal matrix using the Multiple Relatively Robust Representations, MRRR algorithm (LAPACK function [STEVR](https://www.intel.com/content/www/us/en/docs/onemkl/developer-reference-fortran/2025-2/stevr.html)). |
| [EigenTridiagonalBisect](EigenTridiagonalBisect/EigenTridiagonalBisect.md) | Compute eigenvalues and eigenvectors of a symmetric tridiagonal matrix using the bisection algorithm (LAPACK function [STEVX](https://www.intel.com/content/www/us/en/docs/onemkl/developer-reference-fortran/2025-2/stevx.html)). |
| [EigenTridiagonalQL](EigenTridiagonalQL/EigenTridiagonalQL.md) | Compute all eigenvalues of a symmetric tridiagonal matrix using the Pal-Walker-Kahan variant of the QL or QR algorithm (LAPACK function [STERF](https://www.intel.com/content/www/us/en/docs/onemkl/developer-reference-fortran/2025-2/sterf.html)). |
| [EigenTridiagonalDCQ](EigenTridiagonalDCQ/EigenTridiagonalDCQ.md) | Compute eigenvalues and eigenvectors of a symmetric tridiagonal matrix using the divide-and-conquer algorithm (LAPACK function [STEDC](https://www.intel.com/content/www/us/en/docs/onemkl/developer-reference-fortran/2025-2/stedc.html)). |
| [EigenTridiagonalQRQ](EigenTridiagonalQRQ/EigenTridiagonalQRQ.md) | Compute eigenvalues and eigenvectors of a symmetric tridiagonal matrix using the QR algorithm (LAPACK function [STEQR](https://www.intel.com/content/www/us/en/docs/onemkl/developer-reference-fortran/2025-2/steqr.html)). |
| [EigenTridiagonalPosDefQ](EigenTridiagonalPosDefQ/EigenTridiagonalPosDefQ.md) | Compute eigenvalues and eigenvectors of a symmetric positive definite (положительно определённая) tridiagonal matrix using the QR algorithm (LAPACK function [PTEQR](https://www.intel.com/content/www/us/en/docs/onemkl/developer-reference-fortran/2025-2/pteqr.html)). |
