# HistoryOrderSelect

HistoryOrderSelect

Selects an order from the history for further calling it through appropriate functions. It returns true if the function has been successfully completed. Returns false if the function has failed. For more details on error call [GetLastError()](../../Checkup/GetLastError/GetLastError.md).

|  |
| --- |
| bool  HistoryOrderSelect(     ulong  ticket      // Order ticket     ); |

Parameters

ticket

[in]  Order ticket.

Return Value

Returns true if successful, otherwise false.

Note

Do not confuse orders of a trading history with current [pending orders](../OrdersTotal/OrdersTotal.md) that appear on the "Trade" tab of the "Toolbox" bar. The list of [orders](../../Constants,-Enumerations-and-Structures/Trade-Constants/Order-Properties/Order-Properties.md) that were canceled or have led to a transaction, can be viewed in the "History" tab of "Toolbox" of the client terminal.

HistoryOrderSelect() clears in a mql5-program the list of orders from a history, available for calls, and copies to it a single order, if the execution of HistoryOrderSelect () has been completed successfully. If you need to go through all orders selected by [HistorySelect()](../HistorySelect/HistorySelect.md), you should better use [HistoryOrderGetTicket()](../HistoryOrderGetTicket/HistoryOrderGetTicket.md).

Example:

|  |
| --- |
| #define   TICKET    1819621374   // ticket of any known order, for example, from the account history  //+------------------------------------------------------------------+  //| Script program start function                                    |  //+------------------------------------------------------------------+  void OnStart()    {  //--- select a historical order by the ticket specified in TICKET     if(!HistoryOrderSelect(TICKET))       {        PrintFormat("HistoryOrderSelect(%I64u) failed. Error %d", TICKET, GetLastError());        return;       }     //--- if an order is successfully selected, get its data and display the order description in the journal     ENUM\_ORDER\_TYPE   order\_type  = (ENUM\_ORDER\_TYPE)HistoryOrderGetInteger(TICKET, ORDER\_TYPE);     ENUM\_ORDER\_STATE  order\_state = (ENUM\_ORDER\_STATE)HistoryOrderGetInteger(TICKET, ORDER\_STATE);     ENUM\_ORDER\_REASON order\_reason= (ENUM\_ORDER\_REASON)HistoryOrderGetInteger(TICKET, ORDER\_REASON);     long              order\_time  = HistoryOrderGetInteger(TICKET, ORDER\_TIME\_SETUP\_MSC);     string            order\_symbol=HistoryOrderGetString(TICKET, ORDER\_SYMBOL);     double            order\_vol\_init=HistoryOrderGetDouble(TICKET, ORDER\_VOLUME\_INITIAL);     double            order\_vol\_curr=HistoryOrderGetDouble(TICKET, ORDER\_VOLUME\_CURRENT);     PrintFormat("%s Order %.2f/%s %s #%I64u %s by %s at %s",                 order\_symbol, order\_vol\_init, (order\_vol\_curr>0 ? DoubleToString(order\_vol\_curr,2) : "0"),                 OrderTypeDescription(order\_type), TICKET, OrderStateDescription(order\_state),                 OrderReasonDescription(order\_reason), TimeMscToString(order\_time));     /\*     result for various specified tickets:     EURUSD Order 0.50/0.50 Buy Limit #2812894647 Canceled by Client at 2024.09.04 19:02:31.793     EURUSD Order 0.10/0 Sell #1753011743 Filled by Take Profit at 2023.06.12 17:04:20.353     GBPUSD Order 0.10/0 Buy #1819621374 Filled by Client at 2023.07.24 06:16:25.746     \*/    }  //+------------------------------------------------------------------+  //| Return the order type description                                |  //+------------------------------------------------------------------+  string OrderTypeDescription(const ENUM\_ORDER\_TYPE type)    {     switch(type)       {        case ORDER\_TYPE\_BUY              :  return("Buy");        case ORDER\_TYPE\_SELL             :  return("Sell");        case ORDER\_TYPE\_BUY\_LIMIT        :  return("Buy Limit");        case ORDER\_TYPE\_SELL\_LIMIT       :  return("Sell Limit");        case ORDER\_TYPE\_BUY\_STOP         :  return("Buy Stop");        case ORDER\_TYPE\_SELL\_STOP        :  return("Sell Stop");        case ORDER\_TYPE\_BUY\_STOP\_LIMIT   :  return("Buy Stop Limit");        case ORDER\_TYPE\_SELL\_STOP\_LIMIT  :  return("Sell Stop Limit");        default                          :  return("Unknown order type: "+(string)type);       }    }  //+------------------------------------------------------------------+  //| Return the order status description                              |  //+------------------------------------------------------------------+  string OrderStateDescription(ENUM\_ORDER\_STATE state)    {     switch(state)       {        case ORDER\_STATE\_STARTED         :  return("Started");        case ORDER\_STATE\_PLACED          :  return("Placed");        case ORDER\_STATE\_CANCELED        :  return("Canceled");        case ORDER\_STATE\_PARTIAL         :  return("Partial");        case ORDER\_STATE\_FILLED          :  return("Filled");        case ORDER\_STATE\_REJECTED        :  return("Rejected");        case ORDER\_STATE\_EXPIRED         :  return("Expired");        case ORDER\_STATE\_REQUEST\_ADD     :  return("Request Add");        case ORDER\_STATE\_REQUEST\_MODIFY  :  return("Request Modify");        case ORDER\_STATE\_REQUEST\_CANCEL  :  return("Request Cancel");        default                          :  return("Unknown state: "+(string)state);       }    }  //+------------------------------------------------------------------+  //| Return the order placement reason description                    |  //+------------------------------------------------------------------+  string OrderReasonDescription(const ENUM\_ORDER\_REASON reason)    {     switch(reason)       {        case ORDER\_REASON\_CLIENT   :  return("Client");        case ORDER\_REASON\_MOBILE   :  return("Mobile");        case ORDER\_REASON\_WEB      :  return("Web");        case ORDER\_REASON\_EXPERT   :  return("Expert");        case ORDER\_REASON\_SL       :  return("Stop Loss");        case ORDER\_REASON\_TP       :  return("Take Profit");        case ORDER\_REASON\_SO       :  return("Stop Out");        default                    :  return("Unknown reason: "+(string)reason);       }    }  //+------------------------------------------------------------------+  //| Return time with milliseconds                                    |  //+------------------------------------------------------------------+  string TimeMscToString(const long time\_msc, int flags=TIME\_DATE|TIME\_MINUTES|TIME\_SECONDS)    {     return(TimeToString(time\_msc/1000, flags) + "." + IntegerToString(time\_msc %1000, 3, '0'));    } |

See also

[HistorySelect()](../HistorySelect/HistorySelect.md), [HistoryOrderGetTicket()](../HistoryOrderGetTicket/HistoryOrderGetTicket.md), [Order Properties](../../Constants,-Enumerations-and-Structures/Trade-Constants/Order-Properties/Order-Properties.md)
