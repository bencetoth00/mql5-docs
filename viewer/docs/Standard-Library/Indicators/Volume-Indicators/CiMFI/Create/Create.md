# Create


Creates the indicator with specified parameters. Use [Refresh()](../../../Base-classes/CIndicator/Refresh/Refresh.md) and [GetData()](../../../Base-classes/CIndicator/GetData/GetData.md) to update and get the indicator values.

```cpp
bool  Create(
   string               symbol,        // symbol
   ENUM_TIMEFRAMES      period,        // period
   int                  ma_period,     // averaging period
   ENUM_APPLIED_VOLUME  applied        // volume type
   )
```

Parameters

symbol

[in]  Symbol.

period

[in]  Timeframe ([ENUM\_TIMEFRAMES](../../../../../Constants,-Enumerations-and-Structures/Chart-Constants/Chart-Timeframes/Chart-Timeframes.md) enumeration value).

ma\_period

[in]  Averaging period.

applied

[in]  Volume type to apply ([ENUM\_APPLIED\_VOLUME](../../../../../Constants,-Enumerations-and-Structures/Indicator-Constants/Price-Constants/Price-Constants.md#enum_applied_volume_enum) enumeration value).

Return Value

true - successful, false - cannot create the indicator.