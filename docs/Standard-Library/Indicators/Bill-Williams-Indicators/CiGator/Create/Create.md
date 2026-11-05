# Create

Create

Creates the indicator with specified parameters. Use [Refresh()](../../../Base-classes/CIndicator/Refresh/Refresh.md) and [GetData()](../../../Base-classes/CIndicator/GetData/GetData.md) to update and get the indicator values.

|  |
| --- |
| bool  Create(     string           symbol,           // symbol     ENUM\_TIMEFRAMES  period,           // period     int              jaw\_period,       // jaws period     int              jaw\_shift,        // jaws shift     int              teeth\_period,     // teeth period     int              teeth\_shift,      // teeth shift     int              lips\_period,      // lips period     int              lips\_shift,       // lips shift     ENUM\_MA\_METHOD   ma\_method,        // averaging method     int              applied           // price type, handle     ) |

Parameters

symbol

[in]  Symbol.

period

[in]  Timeframe ([ENUM\_TIMEFRAMES](../../../../../Constants,-Enumerations-and-Structures/Chart-Constants/Chart-Timeframes/Chart-Timeframes.md) enumeration value).

jaw\_period

[in]  Jaws averaging period.

jaw\_shift

[in]  Jaws horizontal shift.

teeth\_period

[in]  Teeth averaging period.

teeth\_shift

[in]  Teeth horizontal shift.

lips\_period

[in]  Lips averaging period.

lips\_shift

[in]  Lips horizontal shift.

ma\_method

[in]  Averaging method ([ENUM\_MA\_METHOD](../../../../../Constants,-Enumerations-and-Structures/Indicator-Constants/Smoothing-Methods/Smoothing-Methods.md) enumeration value).

applied

[in]  Price type or handle to apply.

Return Value

true - successful, false - cannot create the indicator.
