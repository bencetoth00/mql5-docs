# HistoryDealGetInteger

HistoryDealGetInteger

Returns the requested property of a deal. The deal property must be of the datetime, int type. There are 2 variants of the function.

1. Immediately returns the property value.

|  |
| --- |
| long  HistoryDealGetInteger(     ulong                       ticket\_number,     // Ticket     ENUM\_DEAL\_PROPERTY\_INTEGER  property\_id        // Property identifier     ); |

2. Returns true or false, depending on the success of the function. If successful, the value of the property is placed into a target variable passed by reference by the last parameter.

|  |
| --- |
| bool  HistoryDealGetInteger(     ulong                       ticket\_number,     // Ticket     ENUM\_DEAL\_PROPERTY\_INTEGER  property\_id,       // Property identifier     long&                       long\_var           // Here we accept the property value     ); |

Parameters

ticket\_number

[in]  Trade ticket.

property\_id

[in]  Identifier of the deal property. The value can be one of the values of the [ENUM\_DEAL\_PROPERTY\_INTEGER](../../Constants,-Enumerations-and-Structures/Trade-Constants/Deal-Properties/Deal-Properties.md#enum_deal_property_integer) enumeration.

long\_var

[out]  Variable of the long type that accepts the value of the requested property.

Return Value

Value of the [long](../../Language-Basics/Data-Types/Integer-Types/Char,-Short,-Int-and-Long-Types/Char,-Short,-Int-and-Long-Types.md#long) type.

Note

Do not confuse [orders](../../Constants,-Enumerations-and-Structures/Trade-Constants/Order-Properties/Order-Properties.md), [deals](../../Constants,-Enumerations-and-Structures/Trade-Constants/Deal-Properties/Deal-Properties.md) and [positions](../../Constants,-Enumerations-and-Structures/Trade-Constants/Position-Properties/Position-Properties.md). Each deal is the result of the execution of an order, each position is the summary result of one or more deals.

Example:

|  |
| --- |
| //+------------------------------------------------------------------+  //| Trade function                                                   |  //+------------------------------------------------------------------+  void OnTrade()    {  //--- receive the last deal's ticket from week's trading history     ulong last\_deal=GetLastDealTicket();     if(HistoryDealSelect(last\_deal))       {        //--- time of deal execution in milliseconds since 01.01.1970        long deal\_time\_msc=HistoryDealGetInteger(last\_deal,DEAL\_TIME\_MSC);        PrintFormat("Deal #%d DEAL\_TIME\_MSC=%i64 => %s",                    last\_deal,deal\_time\_msc,TimeToString(deal\_time\_msc/1000));       }     else        PrintFormat("HistoryDealSelect() failed for #%d. Eror code=%d",                    last\_deal,GetLastError());  //---    }  //+------------------------------------------------------------------+  //| Returns the last deal ticket in history or -1                    |  //+------------------------------------------------------------------+  ulong GetLastDealTicket()    {  //--- request history for the last 7 days     if(!GetTradeHistory(7))       {        //--- notify on unsuccessful call and return -1        Print(\_\_FUNCTION\_\_," HistorySelect() returned false");        return -1;       }  //---      ulong first\_deal,last\_deal,deals=HistoryDealsTotal();  //--- work with orders if there are any     if(deals>0)       {        Print("Deals = ",deals);        first\_deal=HistoryDealGetTicket(0);        PrintFormat("first\_deal = %d",first\_deal);        if(deals>1)          {           last\_deal=HistoryDealGetTicket((int)deals-1);           PrintFormat("last\_deal = %d",last\_deal);           return last\_deal;          }        return first\_deal;       }  //--- no deal found, return -1     return -1;    }  //+--------------------------------------------------------------------------+  //| Requests history for the last days and returns false in case of failure  |  //+--------------------------------------------------------------------------+  bool GetTradeHistory(int days)    {  //--- set a week period to request trade history     datetime to=TimeCurrent();     datetime from=to-days\*PeriodSeconds(PERIOD\_D1);     ResetLastError();  //--- make a request and check the result     if(!HistorySelect(from,to))       {        Print(\_\_FUNCTION\_\_," HistorySelect=false. Error code=",GetLastError());        return false;       }  //--- history received successfully     return true;    } |

See also

[HistoryDealsTotal()](../HistoryDealsTotal/HistoryDealsTotal.md), [HistorySelect()](../HistorySelect/HistorySelect.md), [HistoryDealGetTicket()](../HistoryDealGetTicket/HistoryDealGetTicket.md), [Deal Properties](../../Constants,-Enumerations-and-Structures/Trade-Constants/Deal-Properties/Deal-Properties.md)
