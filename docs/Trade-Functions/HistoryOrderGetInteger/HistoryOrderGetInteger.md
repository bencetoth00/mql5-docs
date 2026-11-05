# HistoryOrderGetInteger

HistoryOrderGetInteger

Returns the requested property of an order. The order property must be of datetime, int type. There are 2 variants of the function.

1. Immediately returns the property value.

|  |
| --- |
| long  HistoryOrderGetInteger(     ulong                        ticket\_number,     // Ticket     ENUM\_ORDER\_PROPERTY\_INTEGER  property\_id        // Property identifier     ); |

2. Returns true or false, depending on the success of the function. If successful, the value of the property is placed into a target variable passed by reference by the last parameter.

|  |
| --- |
| bool  HistoryOrderGetInteger(     ulong                        ticket\_number,     // Ticket     ENUM\_ORDER\_PROPERTY\_INTEGER  property\_id,       // Property identifier     long&                        long\_var           // Here we accept the property value     ); |

Parameters

ticket\_number

[in]  Order ticket.

property\_id

[in]  Identifier of the order property. The value can be one of the values of the [ENUM\_ORDER\_PROPERTY\_INTEGER](../../Constants,-Enumerations-and-Structures/Trade-Constants/Order-Properties/Order-Properties.md#enum_order_property_integer) enumeration.

long\_var

[out]  Variable of the long type that accepts the value of the requested property.

Return Value

Value of the [long](../../Language-Basics/Data-Types/Integer-Types/Char,-Short,-Int-and-Long-Types/Char,-Short,-Int-and-Long-Types.md#long) type.

Note

Do not confuse orders of a trading history with current [pending orders](../OrdersTotal/OrdersTotal.md) that appear on the "Trade" tab of the "Toolbox" bar. The list of [orders](../../Constants,-Enumerations-and-Structures/Trade-Constants/Order-Properties/Order-Properties.md) that were canceled or have led to a transaction, can be viewed in the "History" tab of "Toolbox" of the client terminal.

Example:

|  |
| --- |
| //+------------------------------------------------------------------+  //| Trade function                                                   |  //+------------------------------------------------------------------+  void OnTrade()    {  //--- receive the last order's ticket from week's trading history     ulong last\_order=GetLastOrderTicket();     if(HistoryOrderSelect(last\_order))       {        //--- time of placing an order in milliseconds since 01.01.1970        long time\_setup\_msc=HistoryOrderGetInteger(last\_order,ORDER\_TIME\_SETUP\_MSC);        PrintFormat("Order #%d ORDER\_TIME\_SETUP\_MSC=%i64 => %s",                    last\_order,time\_setup\_msc,TimeToString(time\_setup\_msc/1000));        //--- order execution/cancellation time in milliseconds since 01.01.1970        long  time\_done\_msc=HistoryOrderGetInteger(last\_order,ORDER\_TIME\_DONE\_MSC);        PrintFormat("Order #%d ORDER\_TIME\_DONE\_MSC=%i64 => %s",                    last\_order,time\_done\_msc,TimeToString(time\_done\_msc/1000));       }     else // notify on failure        PrintFormat("HistoryOrderSelect() failed for #%d. Eror code=%d",                    last\_order,GetLastError());     //---    }  //+------------------------------------------------------------------+  //| Returns the last order ticket in history or -1                   |  //+------------------------------------------------------------------+  ulong GetLastOrderTicket()    {  //--- request history for the last 7 days     if(!GetTradeHistory(7))       {        //--- notify on unsuccessful call and return -1        Print(\_\_FUNCTION\_\_," HistorySelect() returned false");        return -1;       }  //---      ulong first\_order,last\_order,orders=HistoryOrdersTotal();  //--- work with orders if there are any     if(orders>0)       {        Print("Orders = ",orders);        first\_order=HistoryOrderGetTicket(0);        PrintFormat("first\_order = %d",first\_order);        if(orders>1)          {           last\_order=HistoryOrderGetTicket((int)orders-1);           PrintFormat("last\_order = %d",last\_order);           return last\_order;          }        return first\_order;       }  //--- no order found, return -1     return -1;    }  //+--------------------------------------------------------------------------+  //| Requests history for the last days and returns false in case of failure  |  //+--------------------------------------------------------------------------+  bool GetTradeHistory(int days)    {  //--- set a week period to request trade history     datetime to=TimeCurrent();     datetime from=to-days\*PeriodSeconds(PERIOD\_D1);     ResetLastError();  //--- make a request and check the result     if(!HistorySelect(from,to))       {        Print(\_\_FUNCTION\_\_," HistorySelect=false. Error code=",GetLastError());        return false;       }  //--- history received successfully     return true;    } |

See also

[HistorySelect()](../HistorySelect/HistorySelect.md), [HistoryOrdersTotal()](../HistoryOrdersTotal/HistoryOrdersTotal.md), [HistoryOrderSelect()](../HistoryOrderSelect/HistoryOrderSelect.md), [Order Properties](../../Constants,-Enumerations-and-Structures/Trade-Constants/Order-Properties/Order-Properties.md)
