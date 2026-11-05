# PositionSelectByTicket

PositionSelectByTicket

Selects an open position to work with based on the ticket number specified in the position. If successful, returns true. Returns false if the function failed. Call [GetLastError()](../../Checkup/GetLastError/GetLastError.md) for error details.

|  |
| --- |
| bool  PositionSelectByTicket(     ulong   ticket     // Position ticket     ); |

Parameters

ticket

[in]  Position ticket.

Return Value

A value of the bool type.

Note

The PositionSelectByTicket() function copies position data to the program environment. Further calls of [PositionGetDouble()](../PositionGetDouble/PositionGetDouble.md), [PositionGetInteger()](../PositionGetInteger/PositionGetInteger.md) and [PositionGetString()](../PositionGetString/PositionGetString.md) return the previously copied data. Even if a position does not exist already (or its size, direction etc. has changed), the data may still be received sometimes. To make sure that you receive valid position data, it is recommended to call PositionSelectByTicket() before you access the data.

Example:

|  |
| --- |
| #define   EXPERT\_MAGIC  123456   // MagicNumber     //+------------------------------------------------------------------+  //| Script program start function                                    |  //+------------------------------------------------------------------+  void OnStart()    {  //--- declare and initialize the request and result structures     MqlTradeRequest request={};     MqlTradeResult  result ={};       //--- fill in trade request parameters to open a long position     request.action    = TRADE\_ACTION\_DEAL;                      // trading operation type     request.symbol    = Symbol();                               // symbol     request.volume    = 0.1;                                    // volume of 0.1 lot     request.type      = ORDER\_TYPE\_BUY;                         // order type     request.price     = SymbolInfoDouble(Symbol(), SYMBOL\_ASK); // open price     request.deviation = 5;                                      // allowed deviation from the price     request.magic     = EXPERT\_MAGIC;                           // order MagicNumber       //--- send a request. If failed to send a request, display the error code and complete operation     if(!OrderSend(request, result))       {        PrintFormat("OrderSend error ", GetLastError());        return;       }          //--- display operation data     PrintFormat("Trade request result: retcode: %u, deal: %I64u, order: %I64u", result.retcode, result.deal, result.order);       //--- get the position ticket from the trade operation result and select the position by ticket  //--- the ticket of a newly opened position corresponds to the ticket of the order that generated the deal     ulong ticket=result.order;     ResetLastError();     if(!PositionSelectByTicket(ticket))       {        PrintFormat("PositionSelectByTicket(%I64u) failed. Error %d", ticket, GetLastError());        return;       }     //--- display the data of a position, selected by ticket, in the journal     ENUM\_POSITION\_TYPE type  = (ENUM\_POSITION\_TYPE)PositionGetInteger(POSITION\_TYPE);     long               time  = PositionGetInteger(POSITION\_TIME\_MSC);     double             price = PositionGetDouble(POSITION\_PRICE\_OPEN);     double             volume= PositionGetDouble(POSITION\_VOLUME);     string             symbol= PositionGetString(POSITION\_SYMBOL);     int                digits= (int)SymbolInfoInteger(symbol, SYMBOL\_DIGITS);     PrintFormat("Current selected position: %s %.2f %s #%I64u at %.\*f, %s",                 symbol, volume, (type==POSITION\_TYPE\_BUY ? "Buy" : "Sell"), ticket, digits, price, TimeMscToString(time));     /\*     result:     Trade request result: retcode: 10009, deal: 2778100901, order: 2803905975     Current selected position: EURUSD 0.10 Buy #2803905975 at 1.10672, 2024.09.02 12:09:51.239     \*/    }  //+------------------------------------------------------------------+  //| Return time with milliseconds                                    |  //+------------------------------------------------------------------+  string TimeMscToString(const long time\_msc, int flags=TIME\_DATE|TIME\_MINUTES|TIME\_SECONDS)    {     return(TimeToString(time\_msc/1000, flags) + "." + IntegerToString(time\_msc %1000, 3, '0'));    } |

See also

[PositionGetSymbol()](../PositionGetSymbol/PositionGetSymbol.md), [PositionsTotal()](../PositionsTotal/PositionsTotal.md), [Position Properties](../../Constants,-Enumerations-and-Structures/Trade-Constants/Position-Properties/Position-Properties.md)
