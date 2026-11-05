# HistorySelect

HistorySelect

Retrieves the history of deals and orders for the specified period of server time.

|  |
| --- |
| bool  HistorySelect(     datetime  from\_date,     // From date     datetime  to\_date        // To date     ); |

Parameters

from\_date

[in]  Start date of the request.

to\_date

[in]  End date of the request.

Return Value

It returns true if successful, otherwise returns false.

Note

HistorySelect() creates a list of orders and a list of trades in a mql5-program, for further referring to the list elements using corresponding functions. The deals list size can be returned using the [HistoryDealsTotal()](../HistoryDealsTotal/HistoryDealsTotal.md) function; the size of the list of orders in the history can be obtained using [HistoryOrdersTotal()](../HistoryOrdersTotal/HistoryOrdersTotal.md). Selection in the list of orders should be better performed by [HistoryOrderGetTicket()](../HistoryOrderGetTicket/HistoryOrderGetTicket.md), for items in the list of deals [HistoryDealGetTicket()](../HistoryDealGetTicket/HistoryDealGetTicket.md) suits better.

After using [HistoryOrderSelect()](../HistoryOrderSelect/HistoryOrderSelect.md), the list of history orders available to the mql5 program is reset and filled again by the found order, if [the search of an order by the ticket](../HistoryOrderSelect/HistoryOrderSelect.md) has been completed successfully. The same applies to the list of deals available to the mql5 program - it is reset by [HistoryDealSelect()](../HistoryDealSelect/HistoryDealSelect.md) and filled again in case of a successful receipt of a deal by ticket number.

Example:

|  |
| --- |
| void OnStart()    {     color BuyColor =clrBlue;     color SellColor=clrRed;  //--- request trade history     HistorySelect(0,TimeCurrent());  //--- create objects     string   name;     uint     total=HistoryDealsTotal();     ulong    ticket=0;     double   price;     double   profit;     datetime time;     string   symbol;     long     type;     long     entry;  //--- for all deals     for(uint i=0;i<total;i++)       {        //--- try to get deals ticket        if((ticket=HistoryDealGetTicket(i))>0)          {           //--- get deals properties           price =HistoryDealGetDouble(ticket,DEAL\_PRICE);           time  =(datetime)HistoryDealGetInteger(ticket,DEAL\_TIME);           symbol=HistoryDealGetString(ticket,DEAL\_SYMBOL);           type  =HistoryDealGetInteger(ticket,DEAL\_TYPE);           entry =HistoryDealGetInteger(ticket,DEAL\_ENTRY);           profit=HistoryDealGetDouble(ticket,DEAL\_PROFIT);           //--- only for current symbol           if(price && time && symbol==Symbol())             {              //--- create price object              name="TradeHistory\_Deal\_"+string(ticket);              if(entry) ObjectCreate(0,name,OBJ\_ARROW\_RIGHT\_PRICE,0,time,price,0,0);              else      ObjectCreate(0,name,OBJ\_ARROW\_LEFT\_PRICE,0,time,price,0,0);              //--- set object properties              ObjectSetInteger(0,name,OBJPROP\_SELECTABLE,0);              ObjectSetInteger(0,name,OBJPROP\_BACK,0);              ObjectSetInteger(0,name,OBJPROP\_COLOR,type?BuyColor:SellColor);              if(profit!=0) ObjectSetString(0,name,OBJPROP\_TEXT,"Profit: "+string(profit));             }          }       }  //--- apply on chart     ChartRedraw();    } |

See also

[HistoryOrderSelect()](../HistoryOrderSelect/HistoryOrderSelect.md), [HistoryDealSelect()](../HistoryDealSelect/HistoryDealSelect.md)
