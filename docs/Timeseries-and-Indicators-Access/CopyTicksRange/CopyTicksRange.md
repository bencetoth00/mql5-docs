# CopyTicksRange

CopyTicksRange

The function receives ticks in the [MqlTick](../../Constants,-Enumerations-and-Structures/Data-Structures/Price-Data-Structure/Price-Data-Structure.md) format within the specified date range to ticks\_array. Indexing goes from the past to the present meaning that a tick with the index 0 is the oldest one in the array. For tick analysis, check the flags field, which shows what exactly has changed.

|  |
| --- |
| int  CopyTicksRange(     const string     symbol\_name,           // symbol name     MqlTick&         ticks\_array[],         // tick receiving array     uint             flags=COPY\_TICKS\_ALL,  // flag that defines the type of the ticks that are received     ulong            from\_msc=0,            // date, starting from which ticks are requested     ulong            to\_msc=0               // date, up to which ticks are requested     ); |

Parameters

symbol\_name

[in]  Symbol.

ticks\_array

[out] [MqlTick](../../Constants,-Enumerations-and-Structures/Data-Structures/Price-Data-Structure/Price-Data-Structure.md) static or dynamic array for receiving ticks. If the static array cannot hold all the ticks from the requested time interval, the maximum possible amount of ticks is received. In this case, the function generates the error [ERR\_HISTORY\_SMALL\_BUFFER](../../Constants,-Enumerations-and-Structures/Codes-of-Errors-and-Warnings/Runtime-Errors/Runtime-Errors.md) (4407) .

flags

[in]  A flag to define the type of the requested ticks. COPY\_TICKS\_INFO – ticks with Bid and/or Ask changes, COPY\_TICKS\_TRADE – ticks with changes in Last and Volume, COPY\_TICKS\_ALL – all ticks. For any type of request, the values of the previous tick are added to the remaining fields of the MqlTick structure.

from\_msc

[in]   The date, from which you want to request ticks. In milliseconds since 1970.01.01. If the from\_msc parameter is not specified, ticks from the beginning of the history are sent. Ticks with the time >= from\_msc are sent.

to\_msc

[in]   The date, up to which you want to request ticks. In milliseconds since 01.01.1970. Ticks with the time <= to\_msc are sent. If the to\_msc parameter is not specified, all ticks up to the end of the history are sent.

Return Value

The number of copied tick or -1 in case of an error. [GetLastError()](../../Checkup/GetLastError/GetLastError.md) is able to return the following errors:

- ERR\_HISTORY\_TIMEOUT – ticks synchronization waiting time is up, the function has sent all it had.
- ERR\_HISTORY\_SMALL\_BUFFER – static buffer is too small. Only the amount the array can store has been sent.
- ERR\_NOT\_ENOUGH\_MEMORY – insufficient memory for receiving a history from the specified range to the dynamic tick array. Failed to allocate enough memory for the tick array.

Note

The CopyTicksRange() function is used for requesting ticks strictly from a specified range, for example, from a certain day in history. At the same time, CopyTicks() allows specifying only a start date, for example – receive all ticks from the beginning of the month till the current moment.

See also

[SymbolInfoTick](../../Market-Info/SymbolInfoTick/SymbolInfoTick.md), [Structure for Current Prices](../../Constants,-Enumerations-and-Structures/Data-Structures/Price-Data-Structure/Price-Data-Structure.md), [OnTick](../../Event-Handling/OnTick/OnTick.md), [CopyTicks](../CopyTicks/CopyTicks.md)
