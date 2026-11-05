# Create

Create

Creates a timeseries with the specified parameters for access to the real volumes of the bars in the history.

|  |
| --- |
| bool  Create(     string           symbol,     // symbol     ENUM\_TIMEFRAMES  period      // period     ) |

Parameters

symbol

[in]  Timeseries symbol.

period

[in]  Timeseries timeframe ([ENUM\_TIMEFRAMES](../../../../../Constants,-Enumerations-and-Structures/Chart-Constants/Chart-Timeframes/Chart-Timeframes.md) enumeration value).

Return Value

true - successful, false - cannot create a timeseries.
