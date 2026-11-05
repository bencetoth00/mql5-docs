# Create


Creates the indicator with specified parameters. Use [Refresh()](../../../Base-classes/CIndicator/Refresh/Refresh.md) and [GetData()](../../../Base-classes/CIndicator/GetData/GetData.md) to update and get the indicator values.

```cpp
bool  Create(
   string           symbol,         // symbol
   ENUM_TIMEFRAMES  period,         // period
   int              cmo_period,     // momentum period
   int              ema_period,     // averaging period
   int              ind_shift,      // shift
   int              applied         // price type, handle
   )
```

Parameters

symbol

[in]  Symbol.

period

[in]  Timeframe ([ENUM\_TIMEFRAMES](../../../../../Constants,-Enumerations-and-Structures/Chart-Constants/Chart-Timeframes/Chart-Timeframes.md) enumeration value).

cmo\_period

[in]  Momentum period.

ema\_period

[in]  Averaging period.

ind\_shift

[in]  Horizontal shift.

applied

[in]  Price type or handle to apply.

Return Value

true - successful, false - cannot create the indicator.