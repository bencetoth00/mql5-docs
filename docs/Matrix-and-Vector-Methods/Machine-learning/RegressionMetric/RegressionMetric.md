# RegressionMetric

RegressionMetric

Compute the regression metric to evaluate the quality of the predicted data compared to the true data

|  |
| --- |
| double vector::RegressionMetric(     const vector&           vector\_true,   // vector of true values     ENUM\_REGRESSION\_METRIC  metric         // metric type     );     double matrix::RegressionMetric(     const matrix&           matrix\_true,   // matrix of true values     ENUM\_REGRESSION\_METRIC  metric         // metric type  );     vector matrix::RegressionMetric(     const matrix&           matrix\_true,   // matrix of true values     ENUM\_REGRESSION\_METRIC  metric,        // metric type     int                     axis           // axis     ); |

Parameters

vector\_true/matrix\_true

[in]  Vector or matrix of true values.

metric

[in]  Metric type from the [ENUM\_REGRESSION\_METRIC](../../Matrix-and-Vector-Types/Enumerations/Enumerations.md#enum_regression_metric) enumeration.

axis

[in]  Axis. 0 — horizontal axis, 1 — vertical axis.

Return Value

The calculated metric which evaluates the quality of the predicted data compared to the true data.

 

Note

- REGRESSION\_MAE — mean absolute error which represents the absolute differences between predicted values and corresponding true values
- REGRESSION\_MSE — mean square error which represents the squared differences between predicted values and corresponding true values
- REGRESSION\_RMSE — square root of MSE
- REGRESSION\_R2 - 1 — MSE(regression) / MSE(mean)
- REGRESSION\_MAPE — MAE as a percentage
- REGRESSION\_MSPE — MSE as a percentage
- REGRESSION\_RMSLE — RMSE computed on a logarithmic scale

 

Example:

|  |
| --- |
| vector y\_true = {3, -0.5, 2, 7};     vector y\_pred = {2.5, 0.0, 2, 8};  //---     double mse=y\_pred.RegressionMetric(y\_true,REGRESSION\_MSE);     Print("mse=",mse);  //---     double mae=y\_pred.RegressionMetric(y\_true,REGRESSION\_MAE);     Print("mae=",mae);  //---     double r2=y\_pred.RegressionMetric(y\_true,REGRESSION\_R2);     Print("r2=",r2);       /\* Result     mae=0.375     mse=0.5     r2=0.9486081370449679     \*/ |
