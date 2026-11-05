# Economic ?alendar structures

# Economic Calendar structures

This section describes the structures for working with the [economic calendar](https://www.metatrader5.com/en/terminal/help/charts_analysis/fundamental) available directly in the MetaTrader platform. The economic calendar is a ready-made encyclopedia featuring descriptions of macroeconomic indicators, their release dates and degrees of importance. Relevant values of macroeconomic indicators are sent to the MetaTrader platform right at the moment of publication and are displayed on a chart as tags allowing you to visually track the required indicators by countries, currencies and importance.

[Economic calendar functions](../../../Economic-Calendar/Economic-Calendar.md) allow conducting the auto analysis of incoming events according to custom importance criteria from a perspective of necessary countries/currency pairs.

Country descriptions are set by the MqlCalendarCountry structure. It is used in the [CalendarCountryById()](../../../Economic-Calendar/CalendarCountryById/CalendarCountryById.md) and [CalendarCountries()](../../../Economic-Calendar/CalendarCountries/CalendarCountries.md) functions

```cpp
struct MqlCalendarCountry
  {
   ulong                               id;                    // country ID (ISO 3166-1)
   string                              name;                  // country text name (in the current terminal encoding)
   string                              code;                  // country code name (ISO 3166-1 alpha-2)
   string                              currency;              // country currency code
   string                              currency_symbol;       // country currency symbol
   string                              url_name;              // country name used in the mql5.com website URL
  };
```

 

Event descriptions are set by the MqlCalendarEvent structure. It is used in the [CalendarEventById()](../../../Economic-Calendar/CalendarEventById/CalendarEventById.md), [CalendarEventByCountry()](../../../Economic-Calendar/CalendarEventByCountry/CalendarEventByCountry.md) and [CalendarEventByCurrency()](../../../Economic-Calendar/CalendarEventByCurrency/CalendarEventByCurrency.md) functions

```cpp
struct MqlCalendarEvent
  {
   ulong                               id;                    // event ID
   ENUM_CALENDAR_EVENT_TYPE            type;                  // event type from the ENUM_CALENDAR_EVENT_TYPE enumeration
   ENUM_CALENDAR_EVENT_SECTOR          sector;                // sector an event is related to
   ENUM_CALENDAR_EVENT_FREQUENCY       frequency;             // event frequency
   ENUM_CALENDAR_EVENT_TIMEMODE        time_mode;             // event time mode
   ulong                               country_id;            // country ID
   ENUM_CALENDAR_EVENT_UNIT            unit;                  // economic indicator value's unit of measure
   ENUM_CALENDAR_EVENT_IMPORTANCE      importance;            // event importance
   ENUM_CALENDAR_EVENT_MULTIPLIER      multiplier;            // economic indicator value multiplier
   uint                                digits;                // number of decimal places
   string                              source_url;            // URL of a source where an event is published
   string                              event_code;            // event code
   string                              name;                  // event text name in the terminal language (in the current terminal encoding)
  };
```

 

Event values are set by the MqlCalendarValue structure. It is used in the [CalendarValueById()](../../../Economic-Calendar/CalendarValueById/CalendarValueById.md), [CalendarValueHistoryByEvent()](../../../Economic-Calendar/CalendarValueHistoryByEvent/CalendarValueHistoryByEvent.md), [CalendarValueHistory()](../../../Economic-Calendar/CalendarValueHistory/CalendarValueHistory.md), [CalendarValueLastByEvent()](../../../Economic-Calendar/CalendarValueLastByEvent/CalendarValueLastByEvent.md) and [CalendarValueLast()](../../../Economic-Calendar/CalendarValueLast/CalendarValueLast.md) functions

```cpp
struct MqlCalendarValue
  {
   ulong                               id;                    // value ID
   ulong                               event_id;              // event ID
   datetime                            time;                  // event date and time
   datetime                            period;                // event reporting period
   int                                 revision;              // revision of the published indicator relative to the reporting period
   long                                actual_value;          // actual value multiplied by 10^6 or LONG_MIN if the value is not set
   long                                prev_value;            // previous value multiplied by 10^6 or LONG_MIN if the value is not set
   long                                revised_prev_value;    // revised previous value multiplied by 10^6 or LONG_MIN if the value is not set
   long                                forecast_value;        // forecast value multiplied by 10^6 or LONG_MIN if the value is not set
   ENUM_CALENDAR_EVENT_IMPACT          impact_type;           // potential impact on the currency rate
  //--- functions checking the values
   bool                         HasActualValue(void) const;   // returns true if actual_value is set
   bool                         HasPreviousValue(void) const; // returns true if prev_value is set
   bool                         HasRevisedValue(void) const;  // returns true if revised_prev_value is set
   bool                         HasForecastValue(void) const; // returns true if forecast_value is set
  //--- functions receiving the values
   double                       GetActualValue(void) const;   // returns actual_value or nan if the value is no set
   double                       GetPreviousValue(void) const; // returns prev_value or nan if the value is no set
   double                       GetRevisedValue(void) const;  // returns revised_prev_value or nan if the value is no set
   double                       GetForecastValue(void) const; // returns forecast_value or nan if the value is no set
  };
```

The MqlCalendarValue structure provides methods for checking and setting values from the actual\_value, forecast\_value, prev\_value and revised\_prev\_value fields. If no value is specified, the field stores LONG\_MIN (-9223372036854775808).

Please note that the values stored in these field are multiplied by one million. It means that when you receive values in MqlCalendarValue using functions [CalendarValueById](../../../Economic-Calendar/CalendarCountryById/CalendarCountryById.md), [CalendarValueHistoryByEvent](../../../Economic-Calendar/CalendarValueHistoryByEvent/CalendarValueHistoryByEvent.md), [CalendarValueHistory](../../../Economic-Calendar/CalendarValueHistory/CalendarValueHistory.md), [CalendarValueLastByEvent](../../../Economic-Calendar/CalendarValueLastByEvent/CalendarValueLastByEvent.md) and [CalendarValueLast](../../../Economic-Calendar/CalendarValueLast/CalendarValueLast.md), you should check if the field values are equal to LONG\_MIN; if a value is specified in the field, then you should divide the value by 1,000,000 in order to get the desired value. Another method to get the values is to check and to get values using the functions of the MqlCalendarValue structure.

An example of handling calendar events:

```cpp
//--- Create a structure to store calendar events with real values instead of integers
struct AdjustedCalendarValue
  {
   ulong                               id;                    // value ID
   ulong                               event_id;              // event ID
   datetime                            time;                  // event date and time
   datetime                            period;                // event reporting period
   int                                 revision;              // revision of the published indicator relative to the reporting period
   double                              actual_value;          // actual value
   double                              prev_value;            // previous value
   double                              revised_prev_value;    // revised previous value
   double                              forecast_value;        // forecast value
   ENUM_CALENDAR_EVENT_IMPACT          impact_type;           // potential impact on the currency rate
  };
//+------------------------------------------------------------------+
//| Script program start function                                    |
//+------------------------------------------------------------------+
void OnStart()
  {
//---
//--- country code for EU (ISO 3166-1 Alpha-2)
   string EU_code="EU";
//--- get all EU event values
   MqlCalendarValue values[];
//--- set the boundaries of the interval we take the events from
   datetime date_from=D'01.01.2021';  // take all events from 2021
   datetime date_to=0;                // 0 means all known events, including the ones that have not occurred yet
//--- request EU event history since 2021
   if(!CalendarValueHistory(values, date_from, date_to, EU_code))
     {
      PrintFormat("Error! Failed to get events for country_code=%s", EU_code);
      PrintFormat("Error code: %d", GetLastError());
      return;
     }
   else
      PrintFormat("Received event values for country_code=%s: %d",
                  EU_code, ArraySize(values));
//--- reduce the size of the array for output to the Journal
   if(ArraySize(values)>5)
      ArrayResize(values, 5);
//--- output event values to the Journal as they are, without checking or converting to actual values
   Print("Output calendar values as they are");
   ArrayPrint(values);
//--- check the field values and convert to actual values
//--- option 1 to check and get the values
   AdjustedCalendarValue values_adjusted_1[];
   int total=ArraySize(values);
   ArrayResize(values_adjusted_1, total);
//--- copy the values with checks and adjustments
   for(int i=0; i<total; i++)
     {
      values_adjusted_1[i].id=values[i].id;
      values_adjusted_1[i].event_id=values[i].event_id;
      values_adjusted_1[i].time=values[i].time;
      values_adjusted_1[i].period=values[i].period;
      values_adjusted_1[i].revision=values[i].revision;
      values_adjusted_1[i].impact_type=values[i].impact_type;
      //--- check values and divide by 1,000,000
      if(values[i].actual_value==LONG_MIN)
         values_adjusted_1[i].actual_value=double("nan");
      else
         values_adjusted_1[i].actual_value=values[i].actual_value/1000000.;
      if(values[i].prev_value==LONG_MIN)
         values_adjusted_1[i].prev_value=double("nan");
      else
         values_adjusted_1[i].prev_value=values[i].prev_value/1000000.;
      if(values[i].revised_prev_value==LONG_MIN)
         values_adjusted_1[i].revised_prev_value=double("nan");
      else
         values_adjusted_1[i].revised_prev_value=values[i].revised_prev_value/1000000.;
      if(values[i].forecast_value==LONG_MIN)
         values_adjusted_1[i].forecast_value=double("nan");
      else
         values_adjusted_1[i].forecast_value=values[i].forecast_value/1000000.;
     }
   Print("The first method to check and get calendar values");
   ArrayPrint(values_adjusted_1);
//--- option 2 to check and get the values
   AdjustedCalendarValue values_adjusted_2[];
   ArrayResize(values_adjusted_2, total);
//--- copy the values with checks and adjustments
   for(int i=0; i<total; i++)
     {
      values_adjusted_2[i].id=values[i].id;
      values_adjusted_2[i].event_id=values[i].event_id;
      values_adjusted_2[i].time=values[i].time;
      values_adjusted_2[i].period=values[i].period;
      values_adjusted_2[i].revision=values[i].revision;
      values_adjusted_2[i].impact_type=values[i].impact_type;
      //--- check and get values
      if(values[i].HasActualValue())
         values_adjusted_2[i].actual_value=values[i].GetActualValue();
      else
         values_adjusted_2[i].actual_value=double("nan");
      if(values[i].HasPreviousValue())
         values_adjusted_2[i].prev_value=values[i].GetPreviousValue();
      else
         values_adjusted_2[i].prev_value=double("nan");
      if(values[i].HasRevisedValue())
         values_adjusted_2[i].revised_prev_value=values[i].GetRevisedValue();
      else
         values_adjusted_2[i].revised_prev_value=double("nan");
      if(values[i].HasForecastValue())
         values_adjusted_2[i].forecast_value=values[i].GetForecastValue();
      else
         values_adjusted_2[i].forecast_value=double("nan");
     }
   Print("The second method to check and get calendar values");
   ArrayPrint(values_adjusted_2);
//--- option 3 to get the values - without checks
   AdjustedCalendarValue values_adjusted_3[];
   ArrayResize(values_adjusted_3, total);
//--- copy the values with checks and adjustments
   for(int i=0; i<total; i++)
     {
      values_adjusted_3[i].id=values[i].id;
      values_adjusted_3[i].event_id=values[i].event_id;
      values_adjusted_3[i].time=values[i].time;
      values_adjusted_3[i].period=values[i].period;
      values_adjusted_3[i].revision=values[i].revision;
      values_adjusted_3[i].impact_type=values[i].impact_type;
      //--- get values without checks
      values_adjusted_3[i].actual_value=values[i].GetActualValue();
      values_adjusted_3[i].prev_value=values[i].GetPreviousValue();
      values_adjusted_3[i].revised_prev_value=values[i].GetRevisedValue();
      values_adjusted_3[i].forecast_value=values[i].GetForecastValue();
     }
   Print("The third method to get calendar values - without checks");
   ArrayPrint(values_adjusted_3);
  }
/*
   We have received event values for country_code=EU: 1051
  Output the calendar values as they are
         [id] [event_id]              [time]            [period] [revision]       [actual_value]         [prev_value] [revised_prev_value]     [forecast_value] [impact_type] [reserved]
   [0] 144520  999500001 2021.01.04 12:00:00 2020.12.01 00:00:00          3             55200000             55500000 -9223372036854775808             55500000             2        ...
   [1] 144338  999520001 2021.01.04 23:30:00 2020.12.29 00:00:00          0            143100000            143900000 -9223372036854775808 -9223372036854775808             0        ...
   [2] 147462  999010020 2021.01.04 23:45:00 1970.01.01 00:00:00          0 -9223372036854775808 -9223372036854775808 -9223372036854775808 -9223372036854775808             0        ...
   [3] 111618  999010018 2021.01.05 12:00:00 2020.11.01 00:00:00          0             11000000             10500000 -9223372036854775808             11000000             0        ...
   [4] 111619  999010019 2021.01.05 12:00:00 2020.11.01 00:00:00          0              3100000              3100000              3200000              3100000             0        ...
  The first method to check and get calendar values
         [id] [event_id]              [time]            [period] [revision] [actual_value] [prev_value] [revised_prev_value] [forecast_value] [impact_type]
   [0] 144520  999500001 2021.01.04 12:00:00 2020.12.01 00:00:00          3       55.20000     55.50000                  nan         55.50000             2
   [1] 144338  999520001 2021.01.04 23:30:00 2020.12.29 00:00:00          0      143.10000    143.90000                  nan              nan             0
   [2] 147462  999010020 2021.01.04 23:45:00 1970.01.01 00:00:00          0            nan          nan                  nan              nan             0
   [3] 111618  999010018 2021.01.05 12:00:00 2020.11.01 00:00:00          0       11.00000     10.50000                  nan         11.00000             0
   [4] 111619  999010019 2021.01.05 12:00:00 2020.11.01 00:00:00          0        3.10000      3.10000              3.20000          3.10000             0
  The second method to check and get calendar values
         [id] [event_id]              [time]            [period] [revision] [actual_value] [prev_value] [revised_prev_value] [forecast_value] [impact_type]
   [0] 144520  999500001 2021.01.04 12:00:00 2020.12.01 00:00:00          3       55.20000     55.50000                  nan         55.50000             2
   [1] 144338  999520001 2021.01.04 23:30:00 2020.12.29 00:00:00          0      143.10000    143.90000                  nan              nan             0
   [2] 147462  999010020 2021.01.04 23:45:00 1970.01.01 00:00:00          0            nan          nan                  nan              nan             0
   [3] 111618  999010018 2021.01.05 12:00:00 2020.11.01 00:00:00          0       11.00000     10.50000                  nan         11.00000             0
   [4] 111619  999010019 2021.01.05 12:00:00 2020.11.01 00:00:00          0        3.10000      3.10000              3.20000          3.10000             0
  The third method to get calendar values - without checks
         [id] [event_id]              [time]            [period] [revision] [actual_value] [prev_value] [revised_prev_value] [forecast_value] [impact_type]
   [0] 144520  999500001 2021.01.04 12:00:00 2020.12.01 00:00:00          3       55.20000     55.50000                  nan         55.50000             2
   [1] 144338  999520001 2021.01.04 23:30:00 2020.12.29 00:00:00          0      143.10000    143.90000                  nan              nan             0
   [2] 147462  999010020 2021.01.04 23:45:00 1970.01.01 00:00:00          0            nan          nan                  nan              nan             0
   [3] 111618  999010018 2021.01.05 12:00:00 2020.11.01 00:00:00          0       11.00000     10.50000                  nan         11.00000             0
   [4] 111619  999010019 2021.01.05 12:00:00 2020.11.01 00:00:00          0        3.10000      3.10000              3.20000          3.10000             0
*/
```

 

Event frequency is specified in the [MqlCalendarEvent](Economic-alendar-structures.md#mqlcalendarevent) structure. Possible values are set in the listing ENUM\_CALENDAR\_EVENT\_FREQUENCY

| ID | Description |
| --- | --- |
| CALENDAR\_FREQUENCY\_NONE | Release frequency is not set |
| CALENDAR\_FREQUENCY\_WEEK | Released once a week |
| CALENDAR\_FREQUENCY\_MONTH | Released once a month |
| CALENDAR\_FREQUENCY\_QUARTER | Released once a quarter |
| CALENDAR\_FREQUENCY\_YEAR | Released once a year |
| CALENDAR\_FREQUENCY\_DAY | Released once a day |

 

Event type is specified in the [MqlCalendarEvent](Economic-alendar-structures.md#mqlcalendarevent) structure. Possible values are set in the listing ENUM\_CALENDAR\_EVENT\_TYPE

| ID | Description |
| --- | --- |
| CALENDAR\_TYPE\_EVENT | Event (meeting, speech, etc.) |
| CALENDAR\_TYPE\_INDICATOR | Indicator |
| CALENDAR\_TYPE\_HOLIDAY | Holiday |

 

A sector of the economy an event is related to is specified in the [MqlCalendarEvent](Economic-alendar-structures.md#mqlcalendarevent) structure. Possible values are set in the listing ENUM\_CALENDAR\_EVENT\_SECTOR

| ID | Description |
| --- | --- |
| CALENDAR\_SECTOR\_NONE | Sector is not set |
| CALENDAR\_SECTOR\_MARKET | Market, exchange |
| CALENDAR\_SECTOR\_GDP | Gross Domestic Product (GDP) |
| CALENDAR\_SECTOR\_JOBS | Labor market |
| CALENDAR\_SECTOR\_PRICES | Prices |
| CALENDAR\_SECTOR\_MONEY | Money |
| CALENDAR\_SECTOR\_TRADE | Trading |
| CALENDAR\_SECTOR\_GOVERNMENT | Government |
| CALENDAR\_SECTOR\_BUSINESS | Business |
| CALENDAR\_SECTOR\_CONSUMER | Consumption |
| CALENDAR\_SECTOR\_HOUSING | Housing |
| CALENDAR\_SECTOR\_TAXES | Taxes |
| CALENDAR\_SECTOR\_HOLIDAYS | Holidays |

 

Event importance is specified in the [MqlCalendarEvent](Economic-alendar-structures.md#mqlcalendarevent) structure. Possible values are set in the listing ENUM\_CALENDAR\_EVENT\_IMPORTANCE

| ID | Description |
| --- | --- |
| CALENDAR\_IMPORTANCE\_NONE | Importance is not set |
| CALENDAR\_IMPORTANCE\_LOW | Low importance |
| CALENDAR\_IMPORTANCE\_MODERATE | Medium importance |
| CALENDAR\_IMPORTANCE\_HIGH | High importance |

 

Measurement unit type used in displaying event values is specified in the [MqlCalendarEvent](Economic-alendar-structures.md#mqlcalendarevent) structure. Possible values are set in the listing ENUM\_CALENDAR\_EVENT\_UNIT

| ID | Description |
| --- | --- |
| CALENDAR\_UNIT\_NONE | Measurement unit is not set |
| CALENDAR\_UNIT\_PERCENT | Percentage |
| CALENDAR\_UNIT\_CURRENCY | National currency |
| CALENDAR\_UNIT\_HOUR | Hours |
| CALENDAR\_UNIT\_JOB | Jobs |
| CALENDAR\_UNIT\_RIG | Drilling rigs |
| CALENDAR\_UNIT\_USD | USD |
| CALENDAR\_UNIT\_PEOPLE | People |
| CALENDAR\_UNIT\_MORTGAGE | Mortgage loans |
| CALENDAR\_UNIT\_VOTE | Votes |
| CALENDAR\_UNIT\_BARREL | Barrels |
| CALENDAR\_UNIT\_CUBICFEET | Cubic feet |
| CALENDAR\_UNIT\_POSITION | Non-commercial net positions |
| CALENDAR\_UNIT\_BUILDING | Buildings |

 

In some cases, economic parameter values require a multiplier set in the [MqlCalendarEvent](Economic-alendar-structures.md#mqlcalendarevent) structure. Possible multiplier values are set in the listing ENUM\_CALENDAR\_EVENT\_MULTIPLIER

| ID | Description |
| --- | --- |
| CALENDAR\_MULTIPLIER\_NONE | Multiplier is not set |
| CALENDAR\_MULTIPLIER\_THOUSANDS | Thousands |
| CALENDAR\_MULTIPLIER\_MILLIONS | Millions |
| CALENDAR\_MULTIPLIER\_BILLIONS | Billions |
| CALENDAR\_MULTIPLIER\_TRILLIONS | Trillions |

 

Event's potential impact on a national currency rate is indicated in the [MqlCalendarValue](Economic-alendar-structures.md#mqlcalendarvalue) structure. Possible values are set in the listing ENUM\_CALENDAR\_EVENT\_IMPACT

| ID | Description |
| --- | --- |
| CALENDAR\_IMPACT\_NA | Impact is not set |
| CALENDAR\_IMPACT\_POSITIVE | Positive impact |
| CALENDAR\_IMPACT\_NEGATIVE | Negative impact |

 

Event time is specified in the [MqlCalendarEvent](Economic-alendar-structures.md#mqlcalendarevent) structure. Possible values are set in the listing ENUM\_CALENDAR\_EVENT\_TIMEMODE

| ID | Description |
| --- | --- |
| CALENDAR\_TIMEMODE\_DATETIME | Source publishes an exact time of an event |
| CALENDAR\_TIMEMODE\_DATE | Event takes all day |
| CALENDAR\_TIMEMODE\_NOTIME | Source publishes no time of an event |
| CALENDAR\_TIMEMODE\_TENTATIVE | Source publishes a day of an event rather than its exact time. The time is specified upon the occurrence of the event. |

 

See also

[Economic Calendar](../../../Economic-Calendar/Economic-Calendar.md)