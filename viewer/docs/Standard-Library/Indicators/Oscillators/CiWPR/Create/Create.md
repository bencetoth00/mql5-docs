# Create


Creates the indicator with specified parameters. Use [Refresh()](../../../Base-classes/CIndicator/Refresh/Refresh.md) and [GetData()](../../../Base-classes/CIndicator/GetData/GetData.md) to update and get the indicator values.

```cpp
bool  Create(
   string           symbol,          // symbol
   ENUM_TIMEFRAMES  period,          // period
   int              calc_period      // calculation period
   )
```

Parameters

symbol

[in]  Symbol.

period

[in]  Timeframe ([ENUM\_TIMEFRAMES](../../../../../Constants,-Enumerations-and-Structures/Chart-Constants/Chart-Timeframes/Chart-Timeframes.md) enumeration value).

calc\_period

[in]  Period for calculation.

Return Value

true - successful, false - cannot create the indicator.