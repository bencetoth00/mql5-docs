# CopyTime


The function gets to time\_array history data of bar opening time for the specified symbol-period pair in the specified quantity. It should be noted that elements ordering is from present to past, i.e., starting position of 0 means the current bar.

![CopyTime](../../assets/copytime.png)

When copying the yet unknown amount of data, it is recommended to use [dynamic array](../../Language-Basics/Data-Types/Dynamic-Array-Object/Dynamic-Array-Object.md) as a target array, because if the requested data count is less (or more) than the length of the target array, function tries to reallocate the memory so that the requested data fit entirely.

If you know the amount of data you need to copy, it should better be done to a [statically allocated buffer](../../Language-Basics/Data-Types/Dynamic-Array-Object/Dynamic-Array-Object.md#static_array), in order to prevent the allocation of excessive memory.

No matter what is the property of the target array - as\_series=true or as\_series=false. Data will be copied so that the oldest element will be located at the start of the physical memory allocated for the array. There are 3 variants of function calls.

Call by the first position and the number of required elements

```cpp
int  CopyTime(
   string           symbol_name,     // symbol name
   ENUM_TIMEFRAMES  timeframe,       // period
   int              start_pos,       // start position
   int              count,           // data count to copy
   datetime         time_array[]     // target array to copy open times
   );
```

Call by the start date and the number of required elements

```cpp
int  CopyTime(
   string           symbol_name,     // symbol name
   ENUM_TIMEFRAMES  timeframe,       // period
   datetime         start_time,      // start date and time
   int              count,           // data count to copy
   datetime         time_array[]     // target array to copy  open times
   );
```

Call by the start and end dates of a required time interval

```cpp
int  CopyTime(
   string           symbol_name,     // symbol name
   ENUM_TIMEFRAMES  timeframe,       // period
   datetime         start_time,      // start date and time
   datetime         stop_time,       // stop date and time
   datetime         time_array[]     // target array to copy open times
   );
```

Parameters

symbol\_name

[in]  Symbol name.

timeframe

[in]  Period.

start\_pos

[in]  The start position for the first element to copy.

count

[in]  Data count to copy.

start\_time

[in]  The start time for the first element to copy.

stop\_time

[in]  Bar time corresponding to the last element to copy.

time\_array[]

[out]  Array of [datetime](../../Language-Basics/Data-Types/Integer-Types/Datetime-Type/Datetime-Type.md) type.

Return Value

Returns the copied data count or -1 in case of an [error](../../Constants,-Enumerations-and-Structures/Codes-of-Errors-and-Warnings/Runtime-Errors/Runtime-Errors.md).

Note

If the whole interval of requested data is out of the available data on the server, the function returns -1. If data outside [TERMINAL\_MAXBARS](../../Constants,-Enumerations-and-Structures/Environment-State/Client-Terminal-Properties/Client-Terminal-Properties.md) (maximal number of bars on the chart) is requested, the function will also return -1.

When requesting data from the indicator, if requested timeseries are not yet built or they need to be downloaded from the server, the function will immediately return -1, but the process of downloading/building will be initiated.

When requesting data from an Expert Advisor or script, [downloading from the server](../Organizing-Data-Access/Organizing-Data-Access.md#synchronized) will be initiated, if  the terminal does not have these data locally, or building of a required timeseries will start, if data can be built from the local history but they are not ready yet. The function will return the amount of data that will be ready by the moment of timeout expiration, but history downloading will continue, and at the next similar request the function will return more data.

When requesting data by the start date and the number of required elements, only data whose date is less than (earlier) or equal to the date specified will be returned. It means, the open time of any bar, for which value is returned (volume, spread, value on the indicator buffer, prices Open, High, Low, Close or open time Time) is always less or equal to the specified one.

When requesting data in a specified range of dates, only data from this interval will be returned. The interval is set and counted up to seconds. It means, the open time of any bar, for which value is returned (volume, spread, value on the indicator buffer, prices Open, High, Low, Close or open time Time) is always within the requested interval.

Thus, if the current day is Saturday, at the attempt to copy data on a week timeframe specifying start\_time=Last\_Tuesday and stop\_time=Last\_Friday the function will return 0, because the open time on a week timeframe is always Sunday, but one week bar does not fall into the specified interval.

If you need to return value corresponding to the current uncompleted bar, you can use the first form of call specifying start\_pos=0 and count=1.

See a detailed example of requesting history data in section [Methods of Object Binding](../../Constants,-Enumerations-and-Structures/Objects-Constants/Methods-of-Object-Binding/Methods-of-Object-Binding.md). The script available in that section shows how to get the values of indicator [iFractals](../../Technical-Indicators/iFractals/iFractals.md) on the last 1000 bars and how to display the last 10 up and 10 down fractals on the chart. A similar technique can be used for all indicators that have missing data and that are usually drawn using the following [styles](../../Custom-Indicators/Indicator-Styles-in-Examples/Indicator-Styles-in-Examples.md):

- [DRAW\_SECTION](../../Custom-Indicators/Indicator-Styles-in-Examples/DRAW_SECTION/DRAW_SECTION.md),
- [DRAW\_ARROW](../../Custom-Indicators/Indicator-Styles-in-Examples/DRAW_ARROW/DRAW_ARROW.md),
- [DRAW\_ZIGZAG](../../Custom-Indicators/Indicator-Styles-in-Examples/DRAW_ZIGZAG/DRAW_ZIGZAG.md),
- [DRAW\_COLOR\_SECTION](../../Custom-Indicators/Indicator-Styles-in-Examples/DRAW_COLOR_SECTION/DRAW_COLOR_SECTION.md),
- [DRAW\_COLOR\_ARROW](../../Custom-Indicators/Indicator-Styles-in-Examples/DRAW_COLOR_ARROW/DRAW_COLOR_ARROW.md),
- [DRAW\_COLOR\_ZIGZAG](../../Custom-Indicators/Indicator-Styles-in-Examples/DRAW_COLOR_ZIGZAG/DRAW_COLOR_ZIGZAG.md).