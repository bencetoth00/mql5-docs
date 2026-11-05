# Date and Time


This is the group of functions for working with data of [datetime](../Language-Basics/Data-Types/Integer-Types/Datetime-Type/Datetime-Type.md) type (an integer that represents the number of seconds elapsed from 0 hours of January 1, 1970).

To arrange high-resolution counters and timers, use the [GetTickCount()](../Common-Functions/GetTickCount/GetTickCount.md) function, which produces values in milliseconds.

| Function | Action |
| --- | --- |
| [TimeCurrent](TimeCurrent/TimeCurrent.md) | Returns the last known server time (time of the last quote receipt) in the datetime format |
| [TimeTradeServer](TimeTradeServer/TimeTradeServer.md) | Returns the current calculation time of the trade server |
| [TimeLocal](TimeLocal/TimeLocal.md) | Returns the local computer time in datetime format |
| [TimeGMT](TimeGMT/TimeGMT.md) | Returns GMT in datetime format with the Daylight Saving Time by local time of the computer, where the client terminal is running |
| [TimeDaylightSavings](TimeDaylightSavings/TimeDaylightSavings.md) | Returns the sign of Daylight Saving Time switch |
| [TimeGMTOffset](TimeGMTOffset/TimeGMTOffset.md) | Returns the current difference between GMT time and the local computer time in seconds, taking into account DST switch |
| [TimeToStruct](TimeToStruct/TimeToStruct.md) | Converts a datetime value into a variable of MqlDateTime structure type |
| [StructToTime](StructToTime/StructToTime.md) | Converts a variable of MqlDateTime structure type into a datetime value |
