# CopyTicks


Get ticks from an [MqlTick](../../../Constants,-Enumerations-and-Structures/Data-Structures/Price-Data-Structure/Price-Data-Structure.md) structure into a matrix or a vector. Elements are counted from the past to the present, which means that the tick with index 0 is the oldest one. To analyze a tick, check the [flags](CopyTicks.md#flags) field which shows what exactly has changed in the tick.

```cpp
bool  matrix::CopyTicks(
   string           symbol,                // symbol name
   ulong            flags,                 // flag indicating the type of ticks to be received
   ulong            from_msc,              // time from which ticks are requested
   ulong            count                  // number of ticks to be received
   );
```

Vector Method

```cpp
bool  vector::CopyTicks(
   string           symbol,                // symbol name
   ulong            flags,                 // flag indicating the type of ticks to be received
   ulong            from_msc,              // time from which ticks are requested
   ulong            count                  // number of ticks to be received
   );
```

Parameters

symbol

[in]  Symbol.

flags

[in]  A combination of flags from the [ENUM\_COPY\_TICKS](CopyTicks.md#enum_copy_ticks) enumeration indicating the contents of the requested data. When copying to a vector, you can specify only one value from the ENUM\_COPY\_TICKS enumeration, otherwise an error will occur.

from\_msc

[in]  Time starting from which ticks are requested. Time is specified in milliseconds since 01/01/1970. If from\_msc=0, the last number of ticks equal to 'count' are returned.

count

[in]  The number of requested ticks. If parameters 'from\_msc' and 'count' are not specified, all available ticks, but no more than 2000, will be written.

 

Return Value

Returns true on success or false if [error](../../../Constants,-Enumerations-and-Structures/Codes-of-Errors-and-Warnings/Runtime-Errors/Runtime-Errors.md) occurs.

Note

The first call of CopyTicks() initiates synchronization of the relevant symbol's tick database stored on the hard drive. If the local database does not provide all the requested ticks, then missing ticks will be automatically downloaded from the trade server. Ticks from from\_msc specified in CopyTicks() to the current moment will be synchronized. After that, all ticks arriving for this symbol will be added to the tick database thus keeping it in the synchronized state.

If from\_msc and count parameters are not specified, all available ticks, but no more than 2000, will be written to the matrix/vector.

In indicators, the CopyTicks() method returns the result immediately: When called from an indicator, CopyTick() immediately returns all available ticks of a symbol and launches synchronization of the tick database if available data is not enough. All indicators on the same symbol operate in one common thread, so the indicator cannot wait for the completion of synchronization. After synchronization, CopyTicks() will return all requested ticks during the next call. In indicators, the [OnCalculate()](../../../Event-Handling/OnCalculate/OnCalculate.md) function is called after the arrival of each tick.

In Expert Advisors and scripts, CopyTicks() can wait for the result for 45 seconds: as distinct from indicators, every Expert Advisor or script operates in a separate thread, and therefore can wait up to 45 seconds for the synchronization to complete. If the required amount of ticks fails to be synchronized during this time, CopyTicks() will return available ticks by timeout and will continue synchronization. [OnTick()](../../../Event-Handling/OnTick/OnTick.md) in Expert Advisors is not a handler of every tick, while it only notifies the Expert Advisor about changes in the market. This can be a batch of changes: the terminal can simultaneously receive multiple ticks, while OnTick() will be called only once, to notify the Expert Advisor about the latest market state.

Rate of data return: the terminal stores 4096 last ticks for each instrument in the fast access cache (65536 ticks for symbols with the Market Depth running). Requests concerning this data are executed the fastest. If requested ticks for the current trading session are beyond the cache, CopyTicks() calls the ticks stored in the terminal memory. These requests require more time to complete. The slowest requests are those requesting ticks for other days, since the data is read from the drive in this case.

 

ENUM\_COPY\_TICKS

The ENUM\_COPY\_TICKS enumeration contains the flags to specify the type of data to be passed to the matrix or array. The flag combination allows getting several series from the history in one request. The order of the rows in the matrix will correspond to the order of the values in the ENUM\_COPY\_TICKS enumeration. In other words, the row with High data will always be higher in the matrix than the row with Low data.

| ID | Value | Description |
| --- | --- | --- |
| COPY\_TICKS\_INFO | 1 | All ticks |
| COPY\_TICKS\_TRADE | 2 | Ticks containing Bid and/or Ask price changes |
| COPY\_TICKS\_ALL | 3 | Ticks containing Last and/or Volume price changes |
| COPY\_TICKS\_TIME\_MS | 1<<8 | Tick time in milliseconds |
| COPY\_TICKS\_BID | 1<<9 | Bid price |
| COPY\_TICKS\_ASK | 1<<10 | Ask price |
| COPY\_TICKS\_LAST | 1<<11 | Last price (last deal price) |
| COPY\_TICKS\_VOLUME | 1<<12 | Last price Volume |
| COPY\_TICKS\_FLAGS | 1<<13 | Tick Flags |
| Data arrangement |  |  |
| COPY\_TICKS\_VERTICAL | 1<<15 | Ticks are copied into the matrix along the vertical axis. The received ticks will be arranged vertically in the matrix, i.e., the oldest ticks will be in the first row, while the most recent ticks will be in the last matrix row.     With default copying, ticks are added into a matrix along the horizontal axis.     The flag is only applicable when copying to a matrix. |

Analyze the tick flags to find out which data has changed:

- TICK\_FLAG\_BID — the tick has changed the bid price
- TICK\_FLAG\_ASK — the tick has changed the ask price
- TICK\_FLAG\_LAST — the tick has changed the last deal price
- TICK\_FLAG\_VOLUME — the tick has changed the volume
- TICK\_FLAG\_BUY — the tick is a result of a buy deal
- TICK\_FLAG\_SELL — the tick is a result of a sell deal

 

See also

[Access to Timeseries and Indicators](../../../Timeseries-and-Indicators-Access/Timeseries-and-Indicators-Access.md), [CopyTicks](../../../Timeseries-and-Indicators-Access/CopyTicks/CopyTicks.md)