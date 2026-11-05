# Create

Create

Creates the indicator with specified parameters. Use [Refresh()](../../../Base-classes/CIndicator/Refresh/Refresh.md) and [GetData()](../../../Base-classes/CIndicator/GetData/GetData.md) to update and get the indicator values.

|  |
| --- |
| bool  Create(     string           symbol,        // symbol     ENUM\_TIMEFRAMES  period,        // period     int              ma\_period,     // averaging period     int              ma\_shift,      // shift     ENUM\_MA\_METHOD   ma\_method,     // averaging method     int              applied        // price type, handle     ) |

Parameters

symbol

[in]  Symbol.

period

[in]  Timeframe ([ENUM\_TIMEFRAMES](../../../../../Constants,-Enumerations-and-Structures/Chart-Constants/Chart-Timeframes/Chart-Timeframes.md) enumeration value).

ma\_period

[in]  Averaging period.

ma\_shift

[in]  Horizontal shift.

ma\_method

[in]  Averaging method ([ENUM\_MA\_METHOD](../../../../../Constants,-Enumerations-and-Structures/Indicator-Constants/Smoothing-Methods/Smoothing-Methods.md) enumeration value).

applied

[in]  Price type or handle to apply.

Return Value

true - successful, false - cannot create the indicator.
