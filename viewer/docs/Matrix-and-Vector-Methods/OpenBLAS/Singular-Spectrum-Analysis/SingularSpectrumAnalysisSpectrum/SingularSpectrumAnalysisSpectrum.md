# SingularSpectrumAnalysisSpectrum


A method function for calculating the relative contributions of spectral components based on their eigenvalues.

Calculations for vector<double> type

```cpp
bool  vector::SingularSpectrumAnalysisSpectrum(
   ulong   window_length,      // window size for constructing the trajectory matrix
   vector& spectrum            // vector of component contributions to the input series (SSA spectrum)
   );
```

Calculations for vector<complex> type

```cpp
bool  vector::SingularSpectrumAnalysisSpectrum(
   ulong   window_length,      // window size for constructing the trajectory matrix
   vectorс& spectrum           // vector of component contributions to the input series (SSA spectrum)
   );
```

Parameters

window\_length

[in]  Window size for constructing the trajectory matrix, the number of components the input time series should be decomposed into.

spectrum

[out]  Vector of component contributions to the input series - eigenvalues of the covariance matrix of the input time series.

Return Value

The function returns 'true' on success or 'false' if an [error](../../../../Constants,-Enumerations-and-Structures/Codes-of-Errors-and-Warnings/Runtime-Errors/Runtime-Errors.md) occurs.

Note

The window\_length parameter value should be less than the size of the input time series. To construct a full-fledged trajectory matrix, the optimal size is considered to be approximately equal to half the size of the input time series.