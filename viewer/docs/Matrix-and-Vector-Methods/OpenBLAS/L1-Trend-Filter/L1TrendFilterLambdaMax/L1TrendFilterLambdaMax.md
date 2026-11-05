# L1TrendFilterLambdaMax


Method for calculating the maximum value of the regularization parameter λmax for a data vector.

Calculations for vector<double> type

```cpp
bool vector::L1TrendFilterLambdaMax(
   double   lambda              // maximum value of the regularization parameter lambda
   );
```

Calculations for vector<float> type

```cpp
bool vectorf::L1TrendFilterLambdaMax(
   float    lambda              // maximum value of the regularization parameter lambda
   );
```

Parameters

lambda

[out]  The maximum value of the regularization parameter λmax, or -1 in case of an error.

Return Value

Returns true on success, otherwise false if [error](../../../../Constants,-Enumerations-and-Structures/Codes-of-Errors-and-Warnings/Runtime-Errors/Runtime-Errors.md) occurs.

Note

Memory consumption grows linearly with the size of the vector. The vector must contain at least 3 elements. The computed λmax can be used to select an appropriate λ parameter in the L1TrendFilter method [L1TrendFilter](../L1TrendFilter/L1TrendFilter.md) method.