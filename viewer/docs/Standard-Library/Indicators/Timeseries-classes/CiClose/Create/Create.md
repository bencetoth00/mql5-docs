# Create


# Creates a timeseries with the specified parameters for access to the closing prices of the bars in the history.

```cpp
bool  Create(
   string           symbol,     // symbol
   ENUM_TIMEFRAMES  period      // period
   )
```

Parameters

symbol

[in]  Timeseries symbol.

period

[in]  Timeseries timeframe ([ENUM\_TIMEFRAMES](../../../../../Constants,-Enumerations-and-Structures/Chart-Constants/Chart-Timeframes/Chart-Timeframes.md) enumeration value).

Return Value

true - successful, false - cannot create the timeseries.