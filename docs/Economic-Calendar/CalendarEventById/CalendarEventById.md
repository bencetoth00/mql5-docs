# CalendarEventById

CalendarEventById

Get an event description by its ID.

|  |
| --- |
| bool  CalendarEventById(     ulong                event\_id,     // event ID     MqlCalendarEvent&    event         // variable for receiving an event description     ); |

Parameters

event\_id

[in]  Event ID.

event

[out] [MqlCalendarEvent](../../Constants,-Enumerations-and-Structures/Data-Structures/Economic-alendar-structures/Economic-alendar-structures.md#mqlcalendarevent) type variable for receiving an event description.

Return Value

Returns true if successful, otherwise - false. To get information about an error, call the [GetLastError()](../../Checkup/GetLastError/GetLastError.md) function. Possible errors:

- 4001 – ERR\_INTERNAL\_ERROR  (general runtime error),
- 5402 – ERR\_CALENDAR\_NO\_DATA (country is not found),
- 5401 – ERR\_CALENDAR\_TIMEOUT (request time limit exceeded).

Example:

|  |
| --- |
| //+------------------------------------------------------------------+  //| Script program start function                                    |  //+------------------------------------------------------------------+  void OnStart()    {  //--- country code for Germany (ISO 3166-1 Alpha-2)     string germany\_code="DE";  //--- get Germany events     MqlCalendarEvent events[];     int events\_count=CalendarEventByCountry(germany\_code,events);  //--- display Germany events in the Journal     if(events\_count>0)       {        PrintFormat("Germany events: %d",events\_count);        ArrayPrint(events);       }     else       {        PrintFormat("Failed to receive events for the country code %s, error %d",                    germany\_code,GetLastError());        //--- script early completion        return;       }  //--- get description of the last event from the events[] array     MqlCalendarEvent event;     ulong event\_id=events[events\_count-1].id;     if(CalendarEventById(event\_id,event))       {        MqlCalendarCountry country;         CalendarCountryById(event.country\_id,country);        PrintFormat("Event description with event\_id=%d received",event\_id);        PrintFormat("Country: %s (country code = %d)",country.name,event.country\_id);        PrintFormat("Event name: %s",event.name);        PrintFormat("Event code: %s",event.event\_code);        PrintFormat("Event importance: %s",EnumToString((ENUM\_CALENDAR\_EVENT\_IMPORTANCE)event.importance));        PrintFormat("Event type: %s",EnumToString((ENUM\_CALENDAR\_EVENT\_TYPE)event.type));        PrintFormat("Event sector: %s",EnumToString((ENUM\_CALENDAR\_EVENT\_SECTOR)event.sector));        PrintFormat("Event frequency: %s",EnumToString((ENUM\_CALENDAR\_EVENT\_FREQUENCY)event.frequency));        PrintFormat("Event release mode: %s",EnumToString((ENUM\_CALENDAR\_EVENT\_TIMEMODE)event.time\_mode));        PrintFormat("Event measurement unit: %s",EnumToString((ENUM\_CALENDAR\_EVENT\_UNIT)event.unit));        PrintFormat("Number of decimal places: %d",event.digits);        PrintFormat("Event multiplier: %s",EnumToString((ENUM\_CALENDAR\_EVENT\_MULTIPLIER)event.multiplier));        PrintFormat("Source URL: %s",event.source\_url);       }     else        PrintFormat("Failed to get event description for event\_d=%s, error %d",                    event\_id,GetLastError());    }  /\*    Result:    Germany events: 50               [id] [type] [sector] [frequency] [time\_mode] [country\_id] [unit] [importance] [multiplier] [digits]                                [source\_url]                       [event\_code]                             [name] [reserved]     [ 0] 276010001      1        6           2           0          276      1            1            0        1 "https://www.destatis.de/EN/Homepage.html"  "exports-mm"                       "Exports m/m"                               0     [ 1] 276010002      1        6           2           0          276      1            1            0        1 "https://www.destatis.de/EN/Homepage.html"  "imports-mm"                       "Imports m/m"                               0     [ 2] 276010003      1        4           2           0          276      1            1            0        1 "https://www.destatis.de/EN/Homepage.html"  "import-price-index-mm"            "Import Price Index m/m"                    0     [ 3] 276010004      1        4           2           0          276      1            1            0        1 "https://www.destatis.de/EN/Homepage.html"  "import-price-index-yy"            "Import Price Index y/y"                    0     ....     [47] 276500001      1        8           2           0          276      0            2            0        1 "https://www.markiteconomics.com"           "markit-manufacturing-pmi"         "Markit Manufacturing PMI"                  0     [48] 276500002      1        8           2           0          276      0            2            0        1 "https://www.markiteconomics.com"           "markit-services-pmi"              "Markit Services PMI"                       0     [49] 276500003      1        8           2           0          276      0            2            0        1 "https://www.markiteconomics.com"           "markit-composite-pmi"             "Markit Composite PMI"                      0    Event description with event\_id=276500003 received    Country: Germany (country code = 276)    Event name: Markit Composite PMI    Event code: markit-composite-pmi     Event importance: CALENDAR\_IMPORTANCE\_MODERATE     Event type: CALENDAR\_TYPE\_INDICATOR     Event sector: CALENDAR\_SECTOR\_BUSINESS     Event frequency: CALENDAR\_FREQUENCY\_MONTH     Event release mode: CALENDAR\_TIMEMODE\_DATETIME     Event measurement unit: CALENDAR\_UNIT\_NONE    Number of decimal places: 1     Value multiplier: CALENDAR\_MULTIPLIER\_NONE     Source URL: https://www.markiteconomics.com  \*/ |

See also

[CalendarEventByCountry](../CalendarEventByCountry/CalendarEventByCountry.md), [CalendarEventByCurrency](../CalendarEventByCurrency/CalendarEventByCurrency.md), [CalendarValueById](../CalendarValueById/CalendarValueById.md)
