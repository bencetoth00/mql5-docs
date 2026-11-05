# HistoryOrderGetTicket

HistoryOrderGetTicket

Return the ticket of a corresponding order in the history. Prior to calling HistoryOrderGetTicket(), first it is necessary to receive the history of deals and orders using the [HistorySelect()](../HistorySelect/HistorySelect.md) or [HistorySelectByPosition()](../HistorySelectByPosition/HistorySelectByPosition.md) function.

|  |
| --- |
| ulong  HistoryOrderGetTicket(     int  index      // Number in the list of orders     ); |

Parameters

index

[in]  Number of the order in the list of orders.

Return Value

Value of the [ulong](../../Language-Basics/Data-Types/Integer-Types/Char,-Short,-Int-and-Long-Types/Char,-Short,-Int-and-Long-Types.md) type. If the function fails, 0 is returned.

Note

Do not confuse orders of a trading history with current [pending orders](../OrdersTotal/OrdersTotal.md) that appear on the "Trade" tab of the "Toolbox" bar. The list of [orders](../../Constants,-Enumerations-and-Structures/Trade-Constants/Order-Properties/Order-Properties.md) that were canceled or have led to a transaction, can be viewed in the "History" tab of "Toolbox" of the client terminal.

Example:

|  |
| --- |
| void OnStart()    {     datetime from=0;     datetime to=TimeCurrent();  //--- request the entire history     HistorySelect(from,to);  //--- variables for returning values from order properties     ulong    ticket;     double   open\_price;     double   initial\_volume;     datetime time\_setup;     datetime time\_done;     string   symbol;     string   type;     long     order\_magic;     long     positionID;  //--- number of current pending orders     uint     total=HistoryOrdersTotal();  //--- go through orders in a loop     for(uint i=0;i<total;i++)       {        //--- return order ticket by its position in the list        if((ticket=HistoryOrderGetTicket(i))>0)          {           //--- return order properties           open\_price    =HistoryOrderGetDouble(ticket,ORDER\_PRICE\_OPEN);           time\_setup    =(datetime)HistoryOrderGetInteger(ticket,ORDER\_TIME\_SETUP);           time\_done     =(datetime)HistoryOrderGetInteger(ticket,ORDER\_TIME\_DONE);           symbol        =HistoryOrderGetString(ticket,ORDER\_SYMBOL);           order\_magic   =HistoryOrderGetInteger(ticket,ORDER\_MAGIC);           positionID    =HistoryOrderGetInteger(ticket,ORDER\_POSITION\_ID);           initial\_volume=HistoryOrderGetDouble(ticket,ORDER\_VOLUME\_INITIAL);           type          =GetOrderType(HistoryOrderGetInteger(ticket,ORDER\_TYPE));           //--- prepare and show information about the order           printf("#ticket %d %s %G %s at %G was set up at %s => done at %s, pos ID=%d",                  ticket,                  // order ticket                  type,                    // type                  initial\_volume,          // placed volume                  symbol,                  // symbol                  open\_price,              // specified open price                  TimeToString(time\_setup),// time of order placing                  TimeToString(time\_done), // time of order execution or deletion                  positionID               // ID of a position , to which the deal of the order is included                  );          }       }  //---    }  //+------------------------------------------------------------------+  //| Returns the string name of the order type                        |  //+------------------------------------------------------------------+  string GetOrderType(long type)    {     string str\_type="unknown operation";     switch(type)       {        case (ORDER\_TYPE\_BUY):            return("buy");        case (ORDER\_TYPE\_SELL):           return("sell");        case (ORDER\_TYPE\_BUY\_LIMIT):      return("buy limit");        case (ORDER\_TYPE\_SELL\_LIMIT):     return("sell limit");        case (ORDER\_TYPE\_BUY\_STOP):       return("buy stop");        case (ORDER\_TYPE\_SELL\_STOP):      return("sell stop");        case (ORDER\_TYPE\_BUY\_STOP\_LIMIT): return("buy stop limit");        case (ORDER\_TYPE\_SELL\_STOP\_LIMIT):return("sell stop limit");       }     return(str\_type);    } |

See also

[HistorySelect()](../HistorySelect/HistorySelect.md), [HistoryOrdersTotal()](../HistoryOrdersTotal/HistoryOrdersTotal.md), [HistoryOrderSelect()](../HistoryOrderSelect/HistoryOrderSelect.md), [Order Properties](../../Constants,-Enumerations-and-Structures/Trade-Constants/Order-Properties/Order-Properties.md)
