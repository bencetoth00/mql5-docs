# CopyTicksRange

CopyTicksRange

Get ticks from an [MqlTick](../../../Constants,-Enumerations-and-Structures/Data-Structures/Price-Data-Structure/Price-Data-Structure.md) structure into a matrix or a vector within the specified date range. Elements are counted from the past to the present, which means that the tick with index 0 is the oldest one. To analyze a tick, check the [flags](CopyTicksRange.md#flags) field which shows what exactly has changed in the tick.

|  |
| --- |
| bool  matrix::CopyTicksRange(     string           symbol,                // symbol name     ulong            flags,                 // flag indicating the type of ticks to be received      ulong            from\_msc,              // time from which ticks are requested     ulong            to\_msc                 // time up to which ticks are requested     ); |

Vector Method

|  |
| --- |
| bool  vector::CopyTicksRange(     string           symbol,                // symbol name     ulong            flags,                 // flag indicating the type of ticks to be received      ulong            from\_msc,              // time from which ticks are requested     ulong            to\_msc                 // time up to which ticks are requested     ); |

Parameters

symbol

[in]  Symbol.

flags

[in]  A combination of flags from the [ENUM\_COPY\_TICKS](../CopyTicks/CopyTicks.md#enum_copy_ticks) enumeration indicating the contents of the requested data. When copying to a vector, you can specify only one value from the ENUM\_COPY\_TICKS enumeration, otherwise an error will occur.

from\_msc

[in]  Time starting from which ticks are requested. Time is specified in milliseconds since 01/01/1970. If the 'from\_msc' parameter is not specified, ticks from the beginning of the history are returned. Ticks with the time >= from\_msc will be returned.

to\_msc

[in]  Time up to which ticks are requested. Time is specified in milliseconds since 01/01/1970. Ticks with the time <= to\_msc are returned. If the to\_msc parameter is not specified, all ticks up to the history end are returned.

Return Value

Returns true on success or false if error occurs. [GetLastError()](../../../Checkup/GetLastError/GetLastError.md) can return the following errors:

- ERR\_HISTORY\_TIMEOUT — timeout for tick synchronization has expired, the function has returned all it had.
- ERR\_HISTORY\_SMALL\_BUFFER — static buffer is too small. Only the amount the array can store has been returned.
- ERR\_NOT\_ENOUGH\_MEMORY — not enough memory to receive historical data from the specified range into a dynamic tick array. Failed to allocate enough memory for the tick array.

 

Analyze the tick flags to find out which data has changed:

- TICK\_FLAG\_BID — the tick has changed the bid price
- TICK\_FLAG\_ASK — the tick has changed the ask price
- TICK\_FLAG\_LAST — the tick has changed the last deal price
- TICK\_FLAG\_VOLUME — the tick has changed the volume
- TICK\_FLAG\_BUY — the tick is a result of a buy deal
- TICK\_FLAG\_SELL — the tick is a result of a sell deal

 

Note

The CopyTicksRange() method is used to request ticks from exactly the specified range. For example, ticks for a specific day in history. CopyTicks() allows specifying only the start date, for example, to receive all ticks from the beginning of the month up to now.

 

See also

[Access to Timeseries and Indicators](../../../Timeseries-and-Indicators-Access/Timeseries-and-Indicators-Access.md), [CopyTicksRange](../../../Timeseries-and-Indicators-Access/CopyTicksRange/CopyTicksRange.md)
