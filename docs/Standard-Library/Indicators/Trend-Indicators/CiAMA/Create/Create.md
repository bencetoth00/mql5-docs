# Create

Create

Creates the indicator with specified parameters. Use [Refresh()](../../../Base-classes/CIndicator/Refresh/Refresh.md) and [GetData()](../../../Base-classes/CIndicator/GetData/GetData.md) to update and get the indicator values.

|  |
| --- |
| bool  Create(     string           string,              // symbol     ENUM\_TIMEFRAMES  period,              // period     int              ma\_period,           // averaging period     int              fast\_ema\_period,     // fast EMA period     int              slow\_ema\_period,     // slow EMA period     int              ind\_shift,           // shift     int              applied              // price type, handle     ) |

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
