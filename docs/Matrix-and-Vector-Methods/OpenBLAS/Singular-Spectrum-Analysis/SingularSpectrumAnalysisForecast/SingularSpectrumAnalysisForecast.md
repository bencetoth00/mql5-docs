# SingularSpectrumAnalysisForecast

SingularSpectrumAnalysisForecast

A method function for calculating reconstructed and predicted data using spectral components of the input time series.

Calculations for vector<double> type

|  |
| --- |
| bool  vector::SingularSpectrumAnalysisForecast(     ulong    window\_length,         // window size for constructing the trajectory matrix     ulong    component\_count,       // number of components used for forecasting     ulong    forecast\_horizon,      // number of points to forecast     vector&  forecast               // vector consisting of reconstructed and predicted values     ); |

Calculations for vector<complex> type

|  |
| --- |
| bool  vector::SingularSpectrumAnalysisForecast(     ulong    window\_length,         // window size for constructing the trajectory matrix     ulong    component\_count,       // number of components used for forecasting     ulong    forecast\_horizon,      // number of points to forecast     vectorс& forecast               // vector consisting of reconstructed and predicted values     ); |

Parameters

window\_length

[in]  Window size for constructing the trajectory matrix, the number of components the input time series should be decomposed into.

component\_count

[in]  Number of components used for forecasting.

forecast\_horizon

[in]  Number of points to forecast.

forecast

[out]  Combining points reconstructed by component\_count plus forecast\_horizon points predicted using the first component\_count components. Thus, the forecast vector has the size of (T+forecast\_horizon), where T is the input series length.

Return Value

The function returns 'true' on success or 'false' if an [error](../../../../Constants,-Enumerations-and-Structures/Codes-of-Errors-and-Warnings/Runtime-Errors/Runtime-Errors.md) occurs.

Note

The window\_length parameter value should be less than the size of the input time series. To construct a full-fledged trajectory matrix, the optimal size is considered to be approximately equal to half the size of the input time series.
