# iLowest

iLowest

Returns the index of the smallest value found on the corresponding chart (shift relative to the current bar).

|  |
| --- |
| int  iLowest(     const string        symbol,              // Symbol     ENUM\_TIMEFRAMES     timeframe,           // Period     ENUM\_SERIESMODE     type,                // Timeseries identifier     int                 count=WHOLE\_ARRAY,   // Number of elements     int                 start=0              // Index    ); |

Parameters

symbol

[in]  The symbol, on which the search will be performed. [NULL](../../Constants,-Enumerations-and-Structures/Named-Constants/Other-Constants/Other-Constants.md) means the current symbol.

timeframe

[in]  Period. It can be one of the values of the [ENUM\_TIMEFRAMES](../../Constants,-Enumerations-and-Structures/Chart-Constants/Chart-Timeframes/Chart-Timeframes.md) enumeration. 0 means the current chart period.

type

[in]  The identifier of the timeseries, in which the search will be performed. Can be equal to any value from [ENUM\_SERIESMODE](../../Constants,-Enumerations-and-Structures/Chart-Constants/Chart-Timeframes/Chart-Timeframes.md#enum_seriesmode).

count=WHOLE\_ARRAY

[in]  The number of elements in the timeseries (from the current bar towards index increasing direction), among which the search should be performed.

start=0

[in]  The index (shift relative to the current bar) of the initial bar, from which search for the lowest value begins. Negative values ​​are ignored and replaced with a zero value.

Return Value

The index of the lowest value found on the corresponding chart (shift relative to the current bar) or -1 in case of an error. For [error](../../Constants,-Enumerations-and-Structures/Codes-of-Errors-and-Warnings/Runtime-Errors/Runtime-Errors.md) details, call the [GetLastError()](../../Checkup/GetLastError/GetLastError.md) function.

Example:

|  |
| --- |
| double val;  //--- Search for a bar with the lowest value of the real volume among 15 consecutive bars  //--- From index 10 to index 24 inclusive, on the current timeframe     int val\_index=iLowest(NULL,0,MODE\_REAL\_VOLUME,15,10);     if(val\_index!=-1)         val=Low[val\_index];     else         PrintFormat("iLowest() call error. Error code=%d",GetLastError()); |
