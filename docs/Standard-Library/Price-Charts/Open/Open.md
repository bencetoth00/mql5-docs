# Open

Open

Opens chart with specified parameters and assigns it to the class instance.

|  |
| --- |
| long  Open(     const string     symbol\_name,     // symbol     ENUM\_TIMEFRAMES  timeframe        // period     ) |

Parameters

symbol\_name

[in]  Chart symbol. [NULL](../../../Language-Basics/Data-Types/Void-Type-and-NULL-Constant/Void-Type-and-NULL-Constant.md) means the symbol of the current chart (to which an expert is attached).

timeframe

[in]  Chart timeframe (from [ENUM\_TIMEFRAMES](../../../Constants,-Enumerations-and-Structures/Chart-Constants/Chart-Timeframes/Chart-Timeframes.md) enumeration). 0 means the current timeframe.

Return Value

chart identifier.
