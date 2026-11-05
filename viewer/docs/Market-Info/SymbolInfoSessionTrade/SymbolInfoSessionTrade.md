# SymbolInfoSessionTrade


Allows receiving time of beginning and end of the specified trading sessions for a specified symbol and day of week.

```cpp
bool  SymbolInfoSessionTrade(
   string            name,                // symbol name
   ENUM_DAY_OF_WEEK  day_of_week,         // day of the week
   uint              session_index,       // session index
   datetime&         from,                // session beginning time
   datetime&         to                   // session end time
   );
```

Parameters

name

[in]  Symbol name.

ENUM\_DAY\_OF\_WEEK

[in]  Day of the week, value of enumeration [ENUM\_DAY\_OF\_WEEK](../../Constants,-Enumerations-and-Structures/Environment-State/Symbol-Properties/Symbol-Properties.md#enum_day_of_week).

uint

[in]  Ordinal number of a session, whose beginning and end time we want to receive. Indexing of sessions starts with 0.

from

[out]  Session beginning time in seconds from 00 hours 00 minutes, in the returned value date should be ignored.

to

[out]  Session end time in seconds from 00 hours 00 minutes, in the returned value date should be ignored.

Return value

If data for the specified session, symbol and day of the week are received, returns true, otherwise returns false.

Example:

```cpp
#define SYMBOL_NAME   Symbol()
#define SESSION_INDEX 0
//+------------------------------------------------------------------+
//| Script program start function                                    |
//+------------------------------------------------------------------+
void OnStart()
  {
//--- print the header with a symbol and SESSION_INDEX and
//--- in a loop by day of the week from Mon to Fri, print the start and end times of the trading session in the journal
   PrintFormat("Symbol %s, Trade session %d:", SYMBOL_NAME, SESSION_INDEX);
   for(int i=MONDAY; i<SATURDAY; i++)
      SymbolInfoSessionTradePrint(SYMBOL_NAME, (ENUM_DAY_OF_WEEK)i, SESSION_INDEX);
   /*
   result:
   Symbol GBPUSD, Trade session 0:
   - Monday     00:15 - 23:55
   - Tuesday    00:15 - 23:55
   - Wednesday  00:15 - 23:55
   - Thursday   00:15 - 23:55
   - Friday     00:15 - 23:55
   */
  }
//+------------------------------------------------------------------+
//| Send the start and end times of the specified trade session      |
//| for the specified symbol and day of the week to the journal      |
//+------------------------------------------------------------------+
void SymbolInfoSessionTradePrint(const string symbol, const ENUM_DAY_OF_WEEK day_of_week, const uint session_index)
  {
//--- declare variables to record the beginning and end of the trading session
   datetime date_from;  // session start time
   datetime date_to;    // session end time
//--- get data from the trading session by symbol and day of the week
   if(!SymbolInfoSessionTrade(symbol, day_of_week, session_index, date_from, date_to))
     {
      Print("SymbolInfoSessionTrade() failed. Error ", GetLastError());
      return;
     }
//--- create the week day name from the enumeration constant
   string week_day=EnumToString(day_of_week);
   if(week_day.Lower())
      week_day.SetChar(0, ushort(week_day.GetChar(0)-32));
//--- send data for the specified trading session to the journal
   PrintFormat("- %-10s %s - %s", week_day, TimeToString(date_from, TIME_MINUTES), TimeToString(date_to, TIME_MINUTES));
  }
```

See also

[Symbol Properties](../../Constants,-Enumerations-and-Structures/Environment-State/Symbol-Properties/Symbol-Properties.md), [TimeToStruct](../../Date-and-Time/TimeToStruct/TimeToStruct.md), [Data Structures](../../Constants,-Enumerations-and-Structures/Data-Structures/Date-Type-Structure/Date-Type-Structure.md)