# Create


Creates the indicator with specified parameters. Use [Refresh()](../../../Base-classes/CIndicator/Refresh/Refresh.md) and [GetData()](../../../Base-classes/CIndicator/GetData/GetData.md) to update and get the indicator values.

```cpp
bool  Create(
   string           string,              // symbol
   ENUM_TIMEFRAMES  period,              // period
   int              ma_period,           // averaging period
   int              fast_ema_period,     // fast EMA period
   int              slow_ema_period,     // slow EMA period
   int              ind_shift,           // shift
   int              applied              // price type, handle
   )
```

Parameters

string

[in]  Symbol.

period

[in]  Timeframe ([ENUM\_TIMEFRAMES](../../../../../Constants,-Enumerations-and-Structures/Chart-Constants/Chart-Timeframes/Chart-Timeframes.md) enumeration value).

ma\_period

[in]  Averaging period.

fast\_ema\_period

[in]  Fast EMA averaging period.

slow\_ema\_period

[in]  Slow EMA averaging period.

ind\_shift

[in]  Horizontal shift.

applied

[in]  Price type or handle to apply.

Return Value

true - successful, false - cannot create the indicator.