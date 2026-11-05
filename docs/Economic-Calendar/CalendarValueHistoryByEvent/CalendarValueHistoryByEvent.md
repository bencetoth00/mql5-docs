# CalendarValueHistoryByEvent

CalendarValueHistoryByEvent

Get the array of values for all events in a specified time range by an event ID.

|  |
| --- |
| int  CalendarValueHistoryByEvent(     ulong              event\_id,          // event ID      MqlCalendarValue&  values[],          // array for value descriptions      datetime           datetime\_from,     // left border of a time range     datetime           datetime\_to=0      // right border of a time range     ); |

Parameters

event\_id

[in]  Event ID.

values[]

[out] [MqlCalendarValue](../../Constants,-Enumerations-and-Structures/Data-Structures/Economic-alendar-structures/Economic-alendar-structures.md#mqlcalendarvalue) type array for receiving event values. See the [example of handling calendar events](../../Constants,-Enumerations-and-Structures/Data-Structures/Economic-alendar-structures/Economic-alendar-structures.md#mqlcalendarvalue_sample).

datetime\_from

[in]  Initial date of a time range events are selected from by a specified ID, while datetime\_from < datetime\_to.

datetime\_to=0

[in]  End date of a time range events are selected from by a specified ID. If the datetime\_to is not set (or is 0), all event values beginning from the specified datetime\_from date in the Calendar database are returned (including the values of future events).

Return Value

If successful, return the number of available values in the 'values' array, otherwise -1. To get information about an error, call the [GetLastError()](../../Checkup/GetLastError/GetLastError.md) function. Possible errors:

- 4001 – ERR\_INTERNAL\_ERROR  (general runtime error),

- 4004 – ERR\_NOT\_ENOUGH\_MEMORY (not enough memory for executing a request),
- 5401 – ERR\_CALENDAR\_TIMEOUT (request time limit exceeded),

- 5400 – ERR\_CALENDAR\_MORE\_DATA (array size is insufficient for receiving descriptions of all values, only the ones that managed to fit in were received),

- errors of failed execution of [ArrayResize()](../../Array-Functions/ArrayResize/ArrayResize.md)

The MqlCalendarValue structure provides methods for checking and setting values from the actual\_value, forecast\_value, prev\_value and revised\_prev\_value fields. If no value is specified, the field stores LONG\_MIN (-9223372036854775808).

Please note that the values stored in these field are multiplied by one million. It means that when you receive values in MqlCalendarValue using functions [CalendarValueById](../CalendarCountryById/CalendarCountryById.md), [CalendarValueHistoryByEvent](CalendarValueHistoryByEvent.md), [CalendarValueHistory](../CalendarValueHistory/CalendarValueHistory.md), [CalendarValueLastByEvent](../CalendarValueLastByEvent/CalendarValueLastByEvent.md) and [CalendarValueLast](../CalendarValueLast/CalendarValueLast.md), you should check if the field values are equal to LONG\_MIN; if a value is specified in a field, then you should divide the value by 1,000,000 in order to get the value. Another method to get the values is to check and to get values using the functions of the MqlCalendarValue structure.

Note

All functions for working with the economic calendar use the trade server time ([TimeTradeServer](../../Date-and-Time/TimeTradeServer/TimeTradeServer.md)). This means that the time in the [MqlCalendarValue](../../Constants,-Enumerations-and-Structures/Data-Structures/Economic-alendar-structures/Economic-alendar-structures.md#mqlcalendarvalue) structure and the time inputs in the [CalendarValueHistoryByEvent](CalendarValueHistoryByEvent.md)/[CalendarValueHistory](../CalendarValueHistory/CalendarValueHistory.md) functions are set in a trade server timezone, rather than a user's local time.

Example:

|  |
| --- |
| //+------------------------------------------------------------------+  //| Script program start function                                    |  //+------------------------------------------------------------------+  void OnStart()    {  //--- country code for EU (ISO 3166-1 Alpha-2)     string EU\_code="EU";  //--- get EU events     MqlCalendarEvent events[];     int events\_count=CalendarEventByCountry(EU\_code,events);  //--- display EU events in the Journal     if(events\_count>0)       {        PrintFormat("EU events: %d",events\_count);        //--- reduce the event list, 10 events are sufficient for analysis        ArrayResize(events,10);        ArrayPrint(events);       }  //--- see that the "ECB Interest Rate Decision" event has event\_id=999010007     ulong event\_id=events[6].id;        // the event's ID may change in the Calendar, so be sure to verify     string event\_name=events[6].name;   // name of a Calendar event     PrintFormat("Get values for event\_name=%s event\_id=%d",event\_name,event\_id);  //--- get all values of the "ECB Interest Rate Decision" event     MqlCalendarValue values[];  //--- set the boundaries of the interval we take the events from     datetime date\_from=0;           // take all events from the beginning of the available history     datetime date\_to=D'01.01.2016'; // take events not older than 2016     if(CalendarValueHistoryByEvent(event\_id,values,date\_from,date\_to))       {        PrintFormat("Received values for %s: %d",                    event\_name,ArraySize(values));        //--- reduce the value list, 10 events are sufficient for analysis        ArrayResize(values,10);        ArrayPrint(values);       }     else       {        PrintFormat("Error! Failed to get values for event\_id=%d",event\_id);        PrintFormat("Error code: %d",GetLastError());       }    }  //---  /\*    Result:    EU events: 56              [id] [type] [sector] [frequency] [time\_mode] [country\_id] [unit] [importance] [multiplier] [digits]                                        [source\_url]                                 [event\_code]                                    [name] [reserv     [0] 999010001      0        5           0           0          999      0            2            0        0 "https://www.ecb.europa.eu/home/html/index.en.html" "ecb-non-monetary-policy-meeting"            "ECB Non-monetary Policy Meeting"                     [1] 999010002      0        5           0           0          999      0            2            0        0 "https://www.ecb.europa.eu/home/html/index.en.html" "ecb-monetary-policy-meeting-accounts"       "ECB Monetary Policy Meeting Accounts"                [2] 999010003      0        5           0           0          999      0            3            0        0 "https://www.ecb.europa.eu/home/html/index.en.html" "ecb-monetary-policy-press-conference"       "ECB Monetary Policy Press Conference"                [3] 999010004      0        5           0           0          999      0            3            0        0 "https://www.ecb.europa.eu/home/html/index.en.html" "ecb-president-draghi-speech"                "ECB President Draghi Speech"                         [4] 999010005      0        5           0           0          999      0            2            0        0 "https://www.ecb.europa.eu/home/html/index.en.html" "ecb-vice-president-vitor-constancio-speech" "ECB Vice President Constancio Speech"                [5] 999010006      1        5           0           0          999      1            3            0        2 "https://www.ecb.europa.eu/home/html/index.en.html" "ecb-deposit-rate-decision"                  "ECB Deposit Facility Rate Decision"                  [6] 999010007      1        5           0           0          999      1            3            0        2 "https://www.ecb.europa.eu/home/html/index.en.html" "ecb-interest-rate-decision"                 "ECB Interest Rate Decision"                          [7] 999010008      0        5           0           0          999      0            2            0        0 "https://www.ecb.europa.eu/home/html/index.en.html" "ecb-economic-bulletin"                      "ECB Economic Bulletin"                               [8] 999010009      1        5           0           0          999      2            2            3        3 "https://www.ecb.europa.eu/home/html/index.en.html" "targeted-ltro"                              "ECB Targeted LTRO"                                   [9] 999010010      0        5           0           0          999      0            2            0        0 "https://www.ecb.europa.eu/home/html/index.en.html" "ecb-executive-board-member-praet-speech"    "ECB Executive Board Member Praet Speech"            Get values for event\_name=ECB Interest Rate Decision event\_id=999010007    Received ECB Interest Rate Decision event values: 102         [id] [event\_id]              [time]            [period] [revision] [actual\_value] [prev\_value] [revised\_prev\_value]     [forecast\_value] [impact\_type] [reserved]     [0] 2776  999010007 2007.03.08 11:45:00 1970.01.01 00:00:00          0        3750000      4250000 -9223372036854775808 -9223372036854775808             0          0     [1] 2777  999010007 2007.05.10 11:45:00 1970.01.01 00:00:00          0        3750000      3750000 -9223372036854775808 -9223372036854775808             0          0     [2] 2778  999010007 2007.06.06 11:45:00 1970.01.01 00:00:00          0        4000000      3750000 -9223372036854775808 -9223372036854775808             0          0     [3] 2779  999010007 2007.07.05 11:45:00 1970.01.01 00:00:00          0        4000000      4000000 -9223372036854775808 -9223372036854775808             0          0     [4] 2780  999010007 2007.08.02 11:45:00 1970.01.01 00:00:00          0        4000000      4000000 -9223372036854775808 -9223372036854775808             0          0     [5] 2781  999010007 2007.09.06 11:45:00 1970.01.01 00:00:00          0        4000000      4000000 -9223372036854775808 -9223372036854775808             0          0     [6] 2782  999010007 2007.10.04 11:45:00 1970.01.01 00:00:00          0        4000000      4000000 -9223372036854775808 -9223372036854775808             0          0     [7] 2783  999010007 2007.11.08 12:45:00 1970.01.01 00:00:00          0        4000000      4000000 -9223372036854775808 -9223372036854775808             0          0     [8] 2784  999010007 2007.12.06 12:45:00 1970.01.01 00:00:00          0        4000000      4000000 -9223372036854775808 -9223372036854775808             0          0     [9] 2785  999010007 2008.01.10 12:45:00 1970.01.01 00:00:00          0        4000000      4000000 -9223372036854775808 -9223372036854775808             0          0  \*/ |

 

See also

[CalendarCountries](../CalendarCountries/CalendarCountries.md), [CalendarEventByCountry](../CalendarEventByCountry/CalendarEventByCountry.md), [CalendarValueHistory](../CalendarValueHistory/CalendarValueHistory.md), [CalendarEventById](../CalendarEventById/CalendarEventById.md), [CalendarValueById](../CalendarValueById/CalendarValueById.md)
