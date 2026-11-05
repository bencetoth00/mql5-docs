# Create

Create

Creates the indicator of the specified type with the specified parameters.

|  |
| --- |
| CIndicator\*  Create(     const string           symbol,     // symbol name     const ENUM\_TIMEFRAMES  period,     // period     const ENUM\_INDICATOR   type,       // type     const int              count,      // number of parameters     const MqlParam&        params      // parameters array     ) |

Parameters

symbol

[in]  Indicator symbol name.

period

[in]  Indicator timeframe ([ENUM\_TIMEFRAMES](../../../../../Constants,-Enumerations-and-Structures/Chart-Constants/Chart-Timeframes/Chart-Timeframes.md) enumeration value).

type

[in]  Indicator type ([ENUM\_INDICATOR](../../../../../Constants,-Enumerations-and-Structures/Indicator-Constants/Indicator-Types/Indicator-Types.md) enumeration value).

count

[in]  Number of parameters for the indicator.

params

[in]  Reference to the parameters array for the indicator.

Return Value

Reference to the created indicator - successful, [NULL](../../../../../Language-Basics/Data-Types/Void-Type-and-NULL-Constant/Void-Type-and-NULL-Constant.md) - cannot create the indicator.
