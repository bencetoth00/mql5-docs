# Create

Create

Creates the indicator with specified parameters. Use [Refresh()](../../../Base-classes/CIndicator/Refresh/Refresh.md) and [GetData()](../../../Base-classes/CIndicator/GetData/GetData.md) to update and get the indicator values.

|  |
| --- |
| bool  Create(     string           symbol,      // symbol     ENUM\_TIMEFRAMES  period,      // period     double           step,        // step     double           maximum      // coefficient     ) |

Parameters

symbol

[in]  Symbol.

period

[in]  Timeframe ([ENUM\_TIMEFRAMES](../../../../../Constants,-Enumerations-and-Structures/Chart-Constants/Chart-Timeframes/Chart-Timeframes.md) enumeration value).

step

[in]  Step for the velocity increasing.

maximum

[in]  Price following coefficient.

Return Value

true - successful, false - cannot change the indicator.
