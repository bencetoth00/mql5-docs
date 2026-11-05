# HistoryOrderGetString

HistoryOrderGetString

Returns the requested property of an order. The order property must be of the string type. There are 2 variants of the function.

1. Immediately returns the property value.

|  |
| --- |
| string  HistoryOrderGetString(     ulong                       ticket\_number,     // Ticket     ENUM\_ORDER\_PROPERTY\_STRING  property\_id        // Property identifier     ); |

2. Returns true or false, depending on the success of the function. If successful, the value of the property is placed into a target variable passed by reference by the last parameter.

|  |
| --- |
| bool  HistoryOrderGetString(     ulong                       ticket\_number,     // Ticket     ENUM\_ORDER\_PROPERTY\_STRING  property\_id,       // Property identifier     string&                     string\_var         // Here we accept the property value     ); |

Parameters

ticket\_number

[in]  Order ticket.

property\_id

[in]  Identifier of the order property. The value can be one of the values of the [ENUM\_ORDER\_PROPERTY\_STRING](../../Constants,-Enumerations-and-Structures/Trade-Constants/Order-Properties/Order-Properties.md#enum_order_property_string) enumeration.

string\_var

[out]  Variable of the string type.

Return Value

Value of the [string](../../Language-Basics/Data-Types/String-Type/String-Type.md) type.

Note

Do not confuse orders of a trading history with current [pending orders](../OrdersTotal/OrdersTotal.md) that appear on the "Trade" tab of the "Toolbox" bar. The list of [orders](../../Constants,-Enumerations-and-Structures/Trade-Constants/Order-Properties/Order-Properties.md) that were canceled or have led to a transaction, can be viewed in the "History" tab of "Toolbox" of the client terminal.

Example:

|  |
| --- |
| //+------------------------------------------------------------------+  //| Script program start function                                    |  //+------------------------------------------------------------------+  void OnStart()    {  //--- request deal and order history     if(!HistorySelect(0, TimeCurrent()))       {        Print("HistorySelect() failed. Error ", GetLastError());        return;       }         //--- in a loop by the list of all historical orders on the account     int total=HistoryOrdersTotal();     for(int i=0; i<total; i++)       {        //--- get the order ticket in the list by the loop index        ulong ticket=HistoryOrderGetTicket(i);        if(ticket==0)           continue;                //--- get the order type and display the header for the list of string properties of the selected order        string type=OrderTypeDescription((ENUM\_ORDER\_TYPE)HistoryOrderGetInteger(ticket, ORDER\_TYPE));        PrintFormat("String properties of an history order %s #%I64u:", type, ticket);                //--- print all the string properties of the selected order under the header        HistoryOrderPropertiesStringPrint(ticket, 16);       }     /\*     result:     String properties of an history order Buy #2646074112:     Comment:        [tp 1.09137]     Symbol:         EURUSD     External ID:         String properties of an history order Buy #2646131906:     Comment:             Symbol:         EURUSD     External ID:         \*/    }  //+------------------------------------------------------------------+  //| Display string properties of the                                 |  //| selected historical order in the journal                         |  //+------------------------------------------------------------------+  void HistoryOrderPropertiesStringPrint(const long ticket, const uint header\_width=0)    {     uint   w=0;     string header="";     string value="";       //--- define the header text and the width of the header field  //--- if the header width is passed to the function equal to zero, then the width will be the size of the header line + 1     header="Comment:";     w=(header\_width==0 ? header.Length()+1 : header\_width);  //--- get and display the comment with the specified header width in the journal     if(!HistoryOrderGetString(ticket, ORDER\_COMMENT, value))        return;     PrintFormat("%-\*s%-s", w, header, value);       //--- display a symbol the order has been placed for in the journal     header="Symbol:";     w=(header\_width==0 ? header.Length()+1 : header\_width);     if(!HistoryOrderGetString(ticket, ORDER\_SYMBOL, value))        return;     PrintFormat("%-\*s%-s", w, header, value);       //--- display the order ID in an external system in the journal      header="External ID:";     w=(header\_width==0 ? header.Length()+1 : header\_width);     if(!HistoryOrderGetString(ticket, ORDER\_EXTERNAL\_ID, value))        return;     PrintFormat("%-\*s%-s", w, header, value);    }  //+------------------------------------------------------------------+  //| Return the order type description                                |  //+------------------------------------------------------------------+  string OrderTypeDescription(const ENUM\_ORDER\_TYPE type)    {     switch(type)       {        case ORDER\_TYPE\_BUY              :  return("Buy");        case ORDER\_TYPE\_SELL             :  return("Sell");        case ORDER\_TYPE\_BUY\_LIMIT        :  return("Buy Limit");        case ORDER\_TYPE\_SELL\_LIMIT       :  return("Sell Limit");        case ORDER\_TYPE\_BUY\_STOP         :  return("Buy Stop");        case ORDER\_TYPE\_SELL\_STOP        :  return("Sell Stop");        case ORDER\_TYPE\_BUY\_STOP\_LIMIT   :  return("Buy Stop Limit");        case ORDER\_TYPE\_SELL\_STOP\_LIMIT  :  return("Sell Stop Limit");        default                          :  return("Unknown order type: "+(string)type);       }    } |

See also

[HistorySelect()](../HistorySelect/HistorySelect.md), [HistoryOrdersTotal()](../HistoryOrdersTotal/HistoryOrdersTotal.md), [HistoryOrderSelect()](../HistoryOrderSelect/HistoryOrderSelect.md), [Order Properties](../../Constants,-Enumerations-and-Structures/Trade-Constants/Order-Properties/Order-Properties.md)
