# Spread


Gets the element of the Spread timeseries by index.

```cpp
double  Spread(
   int    ind         // index
   )
```

Parameters

ind

[in]  Element index.

Return Value

If successful, it returns the numerical value of the Spread timeseries element with specified index, otherwise it returns EMPTY\_VALUE.

Note

The EMPTY\_VALUE is returned in two cases:

1. Timeseries is not used (the corresponding bit is not set).
2. Element index is out of range.