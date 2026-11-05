# Init

Init

Initializes the object.

|  |
| --- |
| bool  Init(     CSymbolInfo      symbol,   // symbol     ENUM\_TIMEFRAMES  period,   // timeframe     double           point     // point     ) |

Parameters

symbol

[in]  Pointer to the object of [CSymbolInfo](../../../../Trade-Classes/CSymbolInfo/CSymbolInfo.md) type for access to symbol information.

period

[in]  Timeframe ([ENUM\_TIMEFRAMES](../../../../../Constants,-Enumerations-and-Structures/Chart-Constants/Chart-Timeframes/Chart-Timeframes.md) enumeration).

point

[in]  The "weight" of 2/4-digit point.

Return Value

true - successful completion, otherwise - false.
