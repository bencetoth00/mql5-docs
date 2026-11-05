# CustomSymbolSetSessionTrade

CustomSymbolSetSessionTrade

Sets the start and end time of the specified trading session for the specified symbol and week day.

|  |
| --- |
| bool  CustomSymbolSetSessionTrade(     const string      symbol\_name,         // symbol name     ENUM\_DAY\_OF\_WEEK  day\_of\_week,         // week day     uint              session\_index,       // session index     datetime          from,                // session start time     datetime          to                   // session end time     ); |

Parameters

symbol\_name

[in]  Custom symbol name.

ENUM\_DAY\_OF\_WEEK

[in]  Week day, value from the [ENUM\_DAY\_OF\_WEEK](../../Constants,-Enumerations-and-Structures/Environment-State/Symbol-Properties/Symbol-Properties.md#enum_day_of_week) enumeration.

uint

[in]  Index of the session, for which start and end times are to be set. Session indexing starts from 0.

from

[in]  Session start time in seconds from 00:00, data value in the variable is ignored.

to

[in]  Session end time in seconds from 00:00, data value in the variable is ignored.

Return Value

true – success, otherwise – false. To get information about the error, call the [GetLastError()](../../Checkup/GetLastError/GetLastError.md) function.

Note

If the session with the specified session\_index already exists, the function simply edits the beginning and end of the session.

If zero start and end parameters have been passed for the session (from=0 and to=0), the appropriate session with the session\_index is deleted, while the session indexing is shifted downwards.

Sessions can be added only sequentially. In other words, you can add session\_index=1 only if the session with the index 0 already exists. If this rule is broken, a new session is not created, while the function itself returns 'false'.

 

Example:

|  |
| --- |
| //+------------------------------------------------------------------+  //|                                  CustomSymbolSetSessionTrade.mq5 |  //|                                  Copyright 2024, MetaQuotes Ltd. |  //|                                             https://www.mql5.com |  //+------------------------------------------------------------------+  #property copyright "Copyright 2024, MetaQuotes Ltd."  #property link      "https://www.mql5.com"  #property version   "1.00"     #define   CUSTOM\_SYMBOL\_NAME     Symbol()+".C"           // custom symbol name  #define   CUSTOM\_SYMBOL\_PATH     "Forex"                 // name of the group, in which a symbol is to be created  #define   CUSTOM\_SYMBOL\_ORIGIN   Symbol()                // name of a symbol a custom one is to be based on     #define   SESSION\_0\_FROM         D'1970.01.01 00:15:00'  // session 0 start time  #define   SESSION\_0\_TO           D'1970.01.01 11:59:00'  // session 0 end time  #define   SESSION\_1\_FROM         D'1970.01.01 12:15:00'  // session 1 start time  #define   SESSION\_1\_TO           D'1970.01.01 23:59:00'  // session 1 end time     //+------------------------------------------------------------------+  //| Script program start function                                    |  //+------------------------------------------------------------------+  void OnStart()    {  //--- get the error code when creating a custom symbol     int create=CreateCustomSymbol(CUSTOM\_SYMBOL\_NAME, CUSTOM\_SYMBOL\_PATH, CUSTOM\_SYMBOL\_ORIGIN);       //--- if the error code is not 0 (successful symbol creation) and not 5304 (symbol has already been created) - leave     if(create!=0 && create!=5304)        return;        //--- print the header with the base symbol and session index and   //--- in a loop by day of the week from Mon to Fri, print the start and end times of each trading session in the journal      for(int session=0; session<2; session++)       {        PrintFormat("Trade session %d of the '%s' symbol from which the custom '%s' was created", session, CUSTOM\_SYMBOL\_ORIGIN, CUSTOM\_SYMBOL\_NAME);         for(int day\_of\_week=MONDAY; day\_of\_week<SATURDAY; day\_of\_week++)            SymbolInfoSessionQuotePrint(CUSTOM\_SYMBOL\_ORIGIN, (ENUM\_DAY\_OF\_WEEK)day\_of\_week, session);             }         //--- in a loop by two sessions     bool res=true;     for(int session=0; session<2; session++)       {        datetime from = SESSION\_0\_FROM;        datetime to   = SESSION\_0\_TO;        if(session>0)          {           from = SESSION\_1\_FROM;           to   = SESSION\_1\_TO;          }        //--- set the quote sessions time for a custom symbol of each day of the week        ResetLastError();        for(int day\_of\_week=MONDAY; day\_of\_week<SATURDAY; day\_of\_week++)           res &=CustomSymbolSetSessionQuote(CUSTOM\_SYMBOL\_NAME, (ENUM\_DAY\_OF\_WEEK)day\_of\_week, session, from, to);       }     //--- if there was an error when setting any of the sessions, display an appropriate message in the journal     if(!res)        Print("CustomSymbolSetSessionTrade() failed. Error ", GetLastError());       //--- print the header with the custom symbol and session index and   //--- in a loop by day of the week from Mon to Fri, print the start and end times of each trading session in the journal      for(int session=0; session<2; session++)       {        PrintFormat("Trade session %d of a custom symbol '%s' based on '%s'", session, CUSTOM\_SYMBOL\_NAME, CUSTOM\_SYMBOL\_ORIGIN);         for(int day\_of\_week=MONDAY; day\_of\_week<SATURDAY; day\_of\_week++)            SymbolInfoSessionQuotePrint(CUSTOM\_SYMBOL\_NAME, (ENUM\_DAY\_OF\_WEEK)day\_of\_week, session);            }         //--- display a hint about the script termination keys on the chart comment     Comment(StringFormat("Press 'Esc' to exit or 'Del' to delete the '%s' symbol and exit", CUSTOM\_SYMBOL\_NAME));  //--- wait for pressing the Esc or Del keys to exit in an endless loop     while(!IsStopped() && TerminalInfoInteger(TERMINAL\_KEYSTATE\_ESCAPE)==0)       {        Sleep(16);        //--- when pressing Del, delete the created custom symbol        if(TerminalInfoInteger(TERMINAL\_KEYSTATE\_DELETE)<0)          {           if(DeleteCustomSymbol(CUSTOM\_SYMBOL\_NAME))              PrintFormat("Custom symbol '%s' deleted successfully", CUSTOM\_SYMBOL\_NAME);           break;          }       }  //--- clear the chart before exiting     Comment("");     /\*     result:     Trade session 0 of the 'EURUSD' symbol from which the custom 'EURUSD.C' was created     - Monday     00:15 - 23:55     - Tuesday    00:15 - 23:55     - Wednesday  00:15 - 23:55     - Thursday   00:15 - 23:55     - Friday     00:15 - 23:55     Trade session 1 of the 'EURUSD' symbol from which the custom 'EURUSD.C' was created     - Monday     Session not set     - Tuesday    Session not set     - Wednesday  Session not set     - Thursday   Session not set     - Friday     Session not set     Trade session 0 of a custom symbol 'EURUSD.C' based on 'EURUSD'     - Monday     00:15 - 11:59     - Tuesday    00:15 - 11:59     - Wednesday  00:15 - 11:59     - Thursday   00:15 - 11:59     - Friday     00:15 - 11:59     Trade session 1 of a custom symbol 'EURUSD.C' based on 'EURUSD'     - Monday     12:15 - 23:59     - Tuesday    12:15 - 23:59     - Wednesday  12:15 - 23:59     - Thursday   12:15 - 23:59     - Friday     12:15 - 23:59     \*/    }  //+------------------------------------------------------------------+  //| Create a custom symbol, return an error code                     |  //+------------------------------------------------------------------+  int CreateCustomSymbol(const string symbol\_name, const string symbol\_path, const string symbol\_origin=NULL)    {  //--- define the name of a symbol a custom one is to be based on     string origin=(symbol\_origin==NULL ? Symbol() : symbol\_origin);       //--- if failed to create a custom symbol and this is not error 5304, report this in the journal     ResetLastError();     int error=0;     if(!CustomSymbolCreate(symbol\_name, symbol\_path, origin))       {        error=GetLastError();        if(error!=5304)           PrintFormat("CustomSymbolCreate(%s, %s, %s) failed. Error %d", symbol\_name, symbol\_path, origin, error);       }  //--- successful     return(error);    }  //+------------------------------------------------------------------+  //| Remove a custom symbol                                           |  //+------------------------------------------------------------------+  bool DeleteCustomSymbol(const string symbol\_name)    {  //--- hide the symbol from the Market Watch window     ResetLastError();     if(!SymbolSelect(symbol\_name, false))       {        PrintFormat("SymbolSelect(%s, false) failed. Error %d", GetLastError());        return(false);       }          //--- if failed to delete a custom symbol, report this in the journal and return 'false'     ResetLastError();     if(!CustomSymbolDelete(symbol\_name))       {        PrintFormat("CustomSymbolDelete(%s) failed. Error %d", symbol\_name, GetLastError());        return(false);       }  //--- successful     return(true);    }  //+------------------------------------------------------------------+  //| Send the start and end times of the specified quote session      |   //| for the specified symbol and day of the week to the journal      |   //+------------------------------------------------------------------+   void SymbolInfoSessionTradePrint(const string symbol, const ENUM\_DAY\_OF\_WEEK day\_of\_week, const uint session\_index)     {   //--- declare variables to record the beginning and end of the quote session      datetime date\_from;  // session start time      datetime date\_to;    // session end time         //--- create the week day name from the enumeration constant      string week\_day=EnumToString(day\_of\_week);      if(week\_day.Lower())         week\_day.SetChar(0, ushort(week\_day.GetChar(0)-32));       //--- get data from the quotation session by symbol and day of the week      if(!SymbolInfoSessionTrade(symbol, day\_of\_week, session\_index, date\_from, date\_to))        {         int err=GetLastError();        string message=(err==4307 ? StringFormat("- %-10s Session not set", week\_day) :                         StringFormat("SymbolInfoSessionTrade(%s, %s, session %d) failed. Error %d", symbol, week\_day, session\_index, GetLastError()));        Print(message);         return;        }           //--- send data for the specified trading session to the journal      PrintFormat("- %-10s %s - %s", week\_day, TimeToString(date\_from, TIME\_MINUTES), TimeToString(date\_to, TIME\_MINUTES));     } |

 

See also

[SymbolInfoSessionTrade](../../Market-Info/SymbolInfoSessionTrade/SymbolInfoSessionTrade.md), [Symbol info](../../Constants,-Enumerations-and-Structures/Environment-State/Symbol-Properties/Symbol-Properties.md), [TimeToStruct](../../Date-and-Time/TimeToStruct/TimeToStruct.md), [Date structure](../../Constants,-Enumerations-and-Structures/Data-Structures/Date-Type-Structure/Date-Type-Structure.md)
