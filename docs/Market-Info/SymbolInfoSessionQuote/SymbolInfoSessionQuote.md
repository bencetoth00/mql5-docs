# SymbolInfoSessionQuote

SymbolInfoSessionQuote

Allows receiving time of beginning and end of the specified quoting sessions for a specified symbol and day of week.

|  |
| --- |
| bool  SymbolInfoSessionQuote(     string            name,                // symbol name     ENUM\_DAY\_OF\_WEEK  day\_of\_week,         // day of the week     uint              session\_index,       // session index     datetime&         from,                // time of the session beginning     datetime&         to                   // time of the session end     ); |

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

Return Value

If data for the specified session, symbol and day of the week are received, returns true, otherwise returns false.

Example:

|  |
| --- |
| #define SYMBOL\_NAME   Symbol()  #define SESSION\_INDEX 0     //+------------------------------------------------------------------+  //| Script program start function                                    |  //+------------------------------------------------------------------+  void OnStart()    {  //--- print the header with a symbol and SESSION\_INDEX and  //--- in a loop by day of the week from Mon to Fri, print the start and end times of the quote session in the journal     PrintFormat("Symbol %s, Quote session %d:", SYMBOL\_NAME, SESSION\_INDEX);     for(int i=MONDAY; i<SATURDAY; i++)        SymbolInfoSessionQuotePrint(SYMBOL\_NAME, (ENUM\_DAY\_OF\_WEEK)i, SESSION\_INDEX);     /\*     result:     Symbol RU000A103661, Quote session 0:     - Monday     06:45 - 00:00     - Tuesday    06:45 - 00:00     - Wednesday  06:45 - 00:00     - Thursday   06:45 - 00:00     - Friday     06:45 - 00:00     \*/    }  //+------------------------------------------------------------------+  //| Send the start and end times of the specified quote session      |  //| for the specified symbol and day of the week to the journal      |  //+------------------------------------------------------------------+  void SymbolInfoSessionQuotePrint(const string symbol, const ENUM\_DAY\_OF\_WEEK day\_of\_week, const uint session\_index)    {  //--- declare variables to record the beginning and end of the quote session     datetime date\_from;  // session start time     datetime date\_to;    // session end time       //--- get data from the quotation session by symbol and day of the week     if(!SymbolInfoSessionQuote(symbol, day\_of\_week, session\_index, date\_from, date\_to))       {        Print("SymbolInfoSessionQuote() failed. Error ", GetLastError());        return;       }         //--- create the week day name from the enumeration constant     string week\_day=EnumToString(day\_of\_week);     if(week\_day.Lower())        week\_day.SetChar(0, ushort(week\_day.GetChar(0)-32));     //--- send data for the specified quote session to the journal     PrintFormat("- %-10s %s - %s", week\_day, TimeToString(date\_from, TIME\_MINUTES), TimeToString(date\_to, TIME\_MINUTES));    } |

See also

[Symbol Properties](../../Constants,-Enumerations-and-Structures/Environment-State/Symbol-Properties/Symbol-Properties.md), [TimeToStruct](../../Date-and-Time/TimeToStruct/TimeToStruct.md), [Data Structures](../../Constants,-Enumerations-and-Structures/Data-Structures/Date-Type-Structure/Date-Type-Structure.md)
