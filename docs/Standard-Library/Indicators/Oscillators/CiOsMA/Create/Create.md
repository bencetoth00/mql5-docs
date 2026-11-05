# Create

Create

Creates the indicator with specified parameters. Use [Refresh()](../../../Base-classes/CIndicator/Refresh/Refresh.md) and [GetData()](../../../Base-classes/CIndicator/GetData/GetData.md) to update and get the indicator values.

|  |
| --- |
| bool  Create(     string           symbol,              // symbol     ENUM\_TIMEFRAMES  period,              // period     int              fast\_ema\_period,     // fast EMA period     int              slow\_ema\_period,     // slow EMA period     int              signal\_period,       // signal line period     int              applied              // price type, handle     ) |

Parameters

symbol

[in]  Symbol.

period

[in]  Timeframe ([ENUM\_TIMEFRAMES](../../../../../Constants,-Enumerations-and-Structures/Chart-Constants/Chart-Timeframes/Chart-Timeframes.md) enumeration value).

fast\_ema\_period

[in]  Fast EMA averaging period.

slow\_ema\_period

[in]  Slow EMA averaging period.

signal\_period

[in]  Signal line averaging period.

applied

[in]  Price type or handle to apply.

Return Value

true - successful, false - cannot create the indicator.
