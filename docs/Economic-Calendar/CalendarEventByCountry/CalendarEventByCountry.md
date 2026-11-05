# CalendarEventByCountry

CalendarEventByCountry

Get the array of descriptions of all events available in the Calendar by a specified country code.

|  |
| --- |
| int  CalendarEventByCountry(     string               country\_code,     // country code name (ISO 3166-1 alpha-2)     MqlCalendarEvent&    events[]          // variable for receiving the description array     ); |

Parameters

country\_code

[in]  Country code name (ISO 3166-1 alpha-2)

events[]

[out] [MqlCalendarEvent](../../Constants,-Enumerations-and-Structures/Data-Structures/Economic-alendar-structures/Economic-alendar-structures.md#mqlcalendarevent) type array for receiving descriptions of all events for a specified country.

Return Value

Number of received descriptions. To get information about an error, call the [GetLastError()](../../Checkup/GetLastError/GetLastError.md) function. Possible errors:

- 4001 – ERR\_INTERNAL\_ERROR  (general runtime error),
- 4004 – ERR\_NOT\_ENOUGH\_MEMORY (not enough memory for executing a request),
- 5401 – ERR\_CALENDAR\_TIMEOUT (request time limit exceeded),
- errors of failed execution of [ArrayResize()](../../Array-Functions/ArrayResize/ArrayResize.md)

Example:

|  |
| --- |
| //+------------------------------------------------------------------+  //| Script program start function                                    |  //+------------------------------------------------------------------+  void OnStart()    {  //--- country code for EU (ISO 3166-1 Alpha-2)     string EU\_code="EU";  //--- get EU events     MqlCalendarEvent events[];     int events\_count=CalendarEventByCountry(EU\_code,events);  //--- display EU events in the Journal     if(events\_count>0)       {        PrintFormat("EU events: %d",events\_count);        ArrayPrint(events);       }  //---    }  /\*    Result:    EU events: 56               [id] [type]  [country\_id] [unit] [importance] [multiplier] [digits] [event\_code]                                          [ 0] 999010001      0          999      0            2            0        0  "ECB Non-monetary Policy Meeting"        [ 1] 999010002      0          999      0            2            0        0  "ECB Monetary Policy Meeting Account     [ 2] 999010003      0          999      0            3            0        0  "ECB Monetary Policy Press Conferenc     [ 3] 999010004      0          999      0            3            0        0  "ECB President Draghi Speech"            [ 4] 999010005      0          999      0            2            0        0  "ECB Vice President Constancio Speec     [ 5] 999010006      1          999      1            3            0        2  "ECB Deposit Facility Rate Decision"     [ 6] 999010007      1          999      1            3            0        2  "ECB Interest Rate Decision"             [ 7] 999010008      0          999      0            2            0        0  "ECB Economic Bulletin"                  [ 8] 999010009      1          999      2            2            3        3  "ECB Targeted LTRO"                      [ 9] 999010010      0          999      0            2            0        0  "ECB Executive Board Member Praet Sp     [10] 999010011      0          999      0            2            0        0  "ECB Executive Board Member Mersch S        ...     \*/ |

See also

[CalendarCountries](../CalendarCountries/CalendarCountries.md), [CalendarCountryById](../CalendarCountryById/CalendarCountryById.md)
