# CalendarValueHistory

CalendarValueHistory

Get the array of values for all events in a specified time range with the ability to sort by country and/or currency.

|  |
| --- |
| int  CalendarValueHistory(     MqlCalendarValue&  values[],              // array for value descriptions      datetime           datetime\_from,         // left border of a time range     datetime           datetime\_to=0          // right border of a time range     const string       country\_code=NULL,     // country code name (ISO 3166-1 alpha-2)     const string       currency=NULL          // country currency code name      ); |

Parameters

values[]

[out] [MqlCalendarValue](../../Constants,-Enumerations-and-Structures/Data-Structures/Economic-alendar-structures/Economic-alendar-structures.md#mqlcalendarvalue) type array for receiving event values. See the [example of handling calendar events](../../Constants,-Enumerations-and-Structures/Data-Structures/Economic-alendar-structures/Economic-alendar-structures.md#mqlcalendarvalue_sample).

datetime\_from

[in]  Initial date of a time range events are selected from by a specified ID, while datetime\_from < datetime\_to.

datetime\_to=0

[in]  End date of a time range events are selected from by a specified ID. If the datetime\_to is not set (or is 0), all event values beginning from the specified datetime\_from date in the Calendar database are returned (including the values of future events).

country\_code=NULL

[in]  Country code name (ISO 3166-1 alpha-2)

currency=NULL

[in]  Country currency code name.

Return Value

If successful, return the number of available values in the 'values' array, otherwise -1. To get information about an error, call the [GetLastError()](../../Checkup/GetLastError/GetLastError.md) function. Possible errors:

- 4001 – ERR\_INTERNAL\_ERROR  (general runtime error),

- 4004 – ERR\_NOT\_ENOUGH\_MEMORY (not enough memory for executing a request),
- 5401 – ERR\_CALENDAR\_TIMEOUT (request time limit exceeded),

- 5400 – ERR\_CALENDAR\_MORE\_DATA (array size is insufficient for receiving descriptions of all values, only the ones that managed to fit in were received),

- errors of failed execution of [ArrayResize()](../../Array-Functions/ArrayResize/ArrayResize.md)

 

Note

All functions for working with the economic calendar use the trade server time ([TimeTradeServer](../../Date-and-Time/TimeTradeServer/TimeTradeServer.md)). This means that the time in the [MqlCalendarValue](../../Constants,-Enumerations-and-Structures/Data-Structures/Economic-alendar-structures/Economic-alendar-structures.md#mqlcalendarvalue) structure and the time inputs in the [CalendarValueHistoryByEvent](../CalendarValueHistoryByEvent/CalendarValueHistoryByEvent.md)/[CalendarValueHistory](CalendarValueHistory.md) functions are set in a trade server timezone, rather than a user's local time.

If the events[] array of fixed length was passed to the function and there was not enough space to save the entire result, the ERR\_CALENDAR\_MORE\_DATA (5400) error is activated.

If the datetime\_to is not set (or is 0), all event values beginning from the specified datetime\_from date in the Calendar database are returned (including the values of future events).

For the country\_code and currency filters, NULL and "" values are equivalent and mean the absence of the filter.

For country\_code, the code field of the [MqlCalendarCountry](../../Constants,-Enumerations-and-Structures/Data-Structures/Economic-alendar-structures/Economic-alendar-structures.md#mqlcalendarcountry) structure, for example "US", "RU" or "EU", should be used.

For currency, the currency field of the [MqlCalendarCountry](../../Constants,-Enumerations-and-Structures/Data-Structures/Economic-alendar-structures/Economic-alendar-structures.md#mqlcalendarcountry) structure, for example "USD", "RUB" or "EUR", should be used.

The filters are applied by conjunction, i.e. [logical 'AND'](../../Language-Basics/Operations-and-Expressions/Boolean-Operations/Boolean-Operations.md) is used to select only the values of events both conditions (country and currency) are simultaneously met for.

The MqlCalendarValue structure provides methods for checking and setting values from the actual\_value, forecast\_value, prev\_value and revised\_prev\_value fields. If no value is specified, the field stores LONG\_MIN (-9223372036854775808).

Please note that the values stored in these field are multiplied by one million. It means that when you receive values in MqlCalendarValue using functions [CalendarValueById](../CalendarCountryById/CalendarCountryById.md), [CalendarValueHistoryByEvent](../CalendarValueHistoryByEvent/CalendarValueHistoryByEvent.md), [CalendarValueHistory](CalendarValueHistory.md), [CalendarValueLastByEvent](../CalendarValueLastByEvent/CalendarValueLastByEvent.md) and [CalendarValueLast](../CalendarValueLast/CalendarValueLast.md), you should check if the field values are equal to LONG\_MIN; if a value is specified in a field, then you should divide the value by 1,000,000 in order to get the value. Another method to get the values is to check and to get values using the functions of the MqlCalendarValue structure.

Example:

|  |
| --- |
| //+------------------------------------------------------------------+  //| Script program start function                                    |  //+------------------------------------------------------------------+  void OnStart()    {  //--- country code for EU (ISO 3166-1 Alpha-2)     string EU\_code="EU";  //--- get all EU event values     MqlCalendarValue values[];  //--- set the boundaries of the interval we take the events from     datetime date\_from=D'01.01.2018';  // take all events from 2018     datetime date\_to=0;                // 0 means all known events, including the ones that have not occurred yet   //--- request EU event history since 2018 year     if(CalendarValueHistory(values,date\_from,date\_to,EU\_code))       {        PrintFormat("Received event values for country\_code=%s: %d",                    EU\_code,ArraySize(values));        //--- decrease the size of the array for outputting to the Journal        ArrayResize(values,10);  //--- display event values in the Journal        ArrayPrint(values);             }     else       {        PrintFormat("Error! Failed to receive events for country\_code=%s",EU\_code);        PrintFormat("Error code: %d",GetLastError());       }  //---    }  /\*    Result:    Received event values for country\_code=EU: 1384          [id] [event\_id]           [time]               [period] [revision]   [actual\_value] [prev\_value] [revised\_prev\_value] [forecast\_value] [impact\_type] [reserved]     [0] 54215  999500001 2018.01.02 09:00:00 2017.12.01 00:00:00          3       60600000     60600000 -9223372036854775808         60500000             1          0     [1] 54221  999500002 2018.01.04 09:00:00 2017.12.01 00:00:00          3       56600000     56500000 -9223372036854775808         56000000             1          0     [2] 54222  999500003 2018.01.04 09:00:00 2017.12.01 00:00:00          3       58100000     58000000 -9223372036854775808         58400000             2          0     [3] 45123  999030005 2018.01.05 10:00:00 2017.11.01 00:00:00          0         600000       400000 -9223372036854775808           100000             1          0     [4] 45124  999030006 2018.01.05 10:00:00 2017.11.01 00:00:00          0        2800000      2500000 -9223372036854775808          1500000             1          0     [5] 45125  999030012 2018.01.05 10:00:00 2017.12.01 00:00:00          1         900000       900000 -9223372036854775808          1000000             2          0     [6] 45126  999030013 2018.01.05 10:00:00 2017.12.01 00:00:00          1        1400000      1500000 -9223372036854775808          1500000             2          0     [7] 54953  999520001 2018.01.05 20:30:00 2018.01.02 00:00:00          0      127900000     92100000 -9223372036854775808         76400000             0          0     [8] 22230  999040003 2018.01.08 10:00:00 2017.12.01 00:00:00          0        9100000      8200000              8100000          7600000             1          0     [9] 22231  999040004 2018.01.08 10:00:00 2017.12.01 00:00:00          0       18400000     16300000             16400000         16800000             1          0     \*/ |

See also

[CalendarCountries](../CalendarCountries/CalendarCountries.md), [CalendarEventByCountry](../CalendarEventByCountry/CalendarEventByCountry.md), [CalendarValueHistoryByEvent](../CalendarValueHistoryByEvent/CalendarValueHistoryByEvent.md), [CalendarEventById](../CalendarEventById/CalendarEventById.md), [CalendarValueById](../CalendarValueById/CalendarValueById.md)
