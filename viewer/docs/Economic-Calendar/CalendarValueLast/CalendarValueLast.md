# CalendarValueLast


Get the array of values for all events with the ability to sort by country and/or currency since the calendar database status with a specified change\_id.

```cpp
int  CalendarValueLast(
   ulong&               change_id,             // change ID
   MqlCalendarValue&    values[],              // array for value descriptions
   const string         country_code=NULL,     // country code name (ISO 3166-1 alpha-2)
   const string         currency=NULL          // country currency code name
   );
```

Parameters

change\_id

[in][out]  Change ID.

values[]

[out] [MqlCalendarValue](../../Constants,-Enumerations-and-Structures/Data-Structures/Economic-alendar-structures/Economic-alendar-structures.md#mqlcalendarvalue) type array for receiving event values. See the [example of handling calendar events](../../Constants,-Enumerations-and-Structures/Data-Structures/Economic-alendar-structures/Economic-alendar-structures.md#mqlcalendarvalue_sample).

country\_code=NULL

[in]  Country code name (ISO 3166-1 alpha-2)

currency=NULL

[in]  Country currency code name.

Return Value

Number of received event values. To get information about an error, call the [GetLastError()](../../Checkup/GetLastError/GetLastError.md) function. Possible errors:

- 4001 – ERR\_INTERNAL\_ERROR  (general runtime error),

- 4004 – ERR\_NOT\_ENOUGH\_MEMORY (not enough memory for executing a request),
- 5401 – ERR\_CALENDAR\_TIMEOUT (request time limit exceeded),

- 5400 – ERR\_CALENDAR\_MORE\_DATA (array size is insufficient for receiving descriptions of all values, only the ones that managed to fit in were received),

- errors of failed execution of [ArrayResize()](../../Array-Functions/ArrayResize/ArrayResize.md)

Note

All functions for working with the economic calendar use the trade server time ([TimeTradeServer](../../Date-and-Time/TimeTradeServer/TimeTradeServer.md)). This means that the time in the [MqlCalendarValue](../../Constants,-Enumerations-and-Structures/Data-Structures/Economic-alendar-structures/Economic-alendar-structures.md#mqlcalendarvalue) structure and the time inputs in the [CalendarValueHistoryByEvent](../CalendarValueHistoryByEvent/CalendarValueHistoryByEvent.md)/[CalendarValueHistory](../CalendarValueHistory/CalendarValueHistory.md) functions are set in a trade server timezone, rather than a user's local time.

If the events[] array of fixed length was passed to the function and there was not enough space to save the entire result, the ERR\_CALENDAR\_MORE\_DATA (5400) error is activated.

If change\_id = 0 is passed to the function, you will get the current change\_id of the calendar database to that parameter; and the function returns 0

For the country\_code and currency filters, NULL and "" values are equivalent and mean the absence of the filter.

For country\_code, the code field of the [MqlCalendarCountry](../../Constants,-Enumerations-and-Structures/Data-Structures/Economic-alendar-structures/Economic-alendar-structures.md#mqlcalendarcountry) structure, for example "US", "RU" or "EU", should be used.

For currency, the currency field of the [MqlCalendarCountry](../../Constants,-Enumerations-and-Structures/Data-Structures/Economic-alendar-structures/Economic-alendar-structures.md#mqlcalendarcountry) structure, for example "USD", "RUB" or "EUR", should be used.

The filters are applied by conjunction, i.e. [logical 'AND'](../../Language-Basics/Operations-and-Expressions/Boolean-Operations/Boolean-Operations.md) is used to select only the values of events both conditions (country and currency) are simultaneously met for

The function returns the array for a specified news and a new change\_id that can be used for subsequent calls of the function to receive the new values of the news. Thus, it is possible to update values for a specified news by calling this function with the last known change\_id.

The MqlCalendarValue structure provides methods for checking and setting values from the actual\_value, forecast\_value, prev\_value and revised\_prev\_value fields. If no value is specified, the field stores LONG\_MIN (-9223372036854775808).

Please note that the values stored in these field are multiplied by one million. It means that when you receive values in MqlCalendarValue using functions [CalendarValueById](../CalendarCountryById/CalendarCountryById.md), [CalendarValueHistoryByEvent](../CalendarValueHistoryByEvent/CalendarValueHistoryByEvent.md), [CalendarValueHistory](../CalendarValueHistory/CalendarValueHistory.md), [CalendarValueLastByEvent](../CalendarValueLastByEvent/CalendarValueLastByEvent.md) and [CalendarValueLast](CalendarValueLast.md), you should check if the field values are equal to LONG\_MIN; if a value is specified in a field, then you should divide the value by 1,000,000 in order to get the value. Another method to get the values is to check and to get values using the functions of the MqlCalendarValue structure.

The sample EA listening for the economic calendar events:

```cpp
#property description "Example of using the CalendarValueLast function"
#property description " to develop the economic calendar events listener."
#property description "To achieve this, get the current change ID"
#property description " of the Calendar database. Then, use this ID to receive"
#property description " only new events via the timer survey"
//+------------------------------------------------------------------+
//| Expert initialization function                                   |
//+------------------------------------------------------------------+
int OnInit()
  {
//--- create timer
   EventSetTimer(60);
//---
   return(INIT_SUCCEEDED);
  }
//+------------------------------------------------------------------+
//| Expert deinitialization function                                 |
//+------------------------------------------------------------------+
void OnDeinit(const int reason)
  {
//--- destroy timer
   EventKillTimer();
  }
//+------------------------------------------------------------------+
//| Expert tick function                                             |
//+------------------------------------------------------------------+
void OnTick()
  {
//---
  }
//+------------------------------------------------------------------+
//| Timer function                                                   |
//+------------------------------------------------------------------+
void OnTimer()
  {
//--- Calendar database change ID
   static ulong calendar_change_id=0;
//--- first launch attribute
   static bool first=true;
//--- event value array
   MqlCalendarValue values[];
//--- perform initialization - get the current calendar_change_id
   if(first)
     {
      //--- get the Calendar database change ID
      if(CalendarValueLast(calendar_change_id,values)>0)
        {
         //--- this code block cannot be executed during the first launch but let's add it anyway
         PrintFormat("%s: Received the Calendar database current ID: change_id=%d",
                     __FUNCTION__,calendar_change_id);
         //--- set the flag and exit before the timer's next event
         first=false;
         return;
        }
      else
        {
         //--- data are not received (this is normal for the first launch), check for an error
         int error_code=GetLastError();
         if(error_code==0)
           {
            PrintFormat("%s: Received the Calendar database current ID: change_id=%d",
                        __FUNCTION__,calendar_change_id);
            //--- set the flag and exit before the timer's next event
            first=false;
            //--- now we have the calendar_change_id value
            return;
           }
         else
           {
            //--- and this is really an error
            PrintFormat("%s: Failed to get events in CalendarValueLast. Error code: %d",
                        __FUNCTION__,error_code);
            //--- operation completed in a failure, re-initialize during the next call of the timer
            return;
           }
        }
     }
//--- we have the last known value of the Calendar change ID (change_id)
   ulong old_change_id=calendar_change_id;
//--- check if there are new Calendar events
   if(CalendarValueLast(calendar_change_id,values)>0)
     {
      PrintFormat("%s: Received new Calendar events: %d",
                  __FUNCTION__,ArraySize(values));
      //--- display data from the 'values' array in the Journal
      ArrayPrint(values);
      //--- display the values of the previous and new Calendar IDs in the Journal
      PrintFormat("%s: Previous change_id=%d, new change_id=%d",
                  __FUNCTION__,old_change_id,calendar_change_id);
      //--- display new events in the Journal
      ArrayPrint(values);
      /*
     write your code that is to handle occurrence of events here
      */
     }
//---
  }
/*
  Example of the listener operation:
  OnTimer: Received the Calendar database current ID: change_id=33281792
  OnTimer: Received new events for the Calendar: 1
        [id] [event_id]              [time]            [period] [revision] [actual_value] [prev_value] [revised_prev_value] [forecast_value] [impact_type] [reserved]
   [0] 91040   76020013 2019.03.20 15:30:00 1970.01.01 00:00:00          0       -5077000     -1913000 -9223372036854775808         -4077000             2          0
  OnTimer: Previous change_id=33281792, new change_id=33282048
        [id] [event_id]              [time]            [period] [revision] [actual_value] [prev_value] [revised_prev_value] [forecast_value] [impact_type] [reserved]
   [0] 91040   76020013 2019.03.20 15:30:00 1970.01.01 00:00:00          0       -5077000     -1913000 -9223372036854775808         -4077000             2          0
  OnTimer: Received new events for the Calendar: 1
        [id] [event_id]              [time]            [period] [revision]       [actual_value] [prev_value] [revised_prev_value] [forecast_value] [impact_type] [reserved]
   [0] 91041   76020013 2019.03.27 15:30:00 1970.01.01 00:00:00          0 -9223372036854775808     -5077000 -9223372036854775808         -7292000             0          0
  OnTimer: Previous change_id=33282048, new change_id=33282560
        [id] [event_id]              [time]            [period] [revision]       [actual_value] [prev_value] [revised_prev_value] [forecast_value] [impact_type] [reserved]
   [0] 91041   76020013 2019.03.27 15:30:00 1970.01.01 00:00:00          0 -9223372036854775808     -5077000 -9223372036854775808         -7292000             0          0
*/
```

 

See also

[CalendarValueLast](CalendarValueLast.md), [CalendarValueHistory](../CalendarValueHistory/CalendarValueHistory.md), [CalendarValueHistoryByEvent](../CalendarValueHistoryByEvent/CalendarValueHistoryByEvent.md), [CalendarValueById](../CalendarValueById/CalendarValueById.md)