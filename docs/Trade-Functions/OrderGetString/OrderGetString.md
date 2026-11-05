# OrderGetString

OrderGetString

Returns the requested order property, pre-selected using [OrderGetTicket](../OrderGetTicket/OrderGetTicket.md) or [OrderSelect](../OrderSelect/OrderSelect.md). The order property must be of the string type. There are 2 variants of the function.

1. Immediately returns the property value.

|  |
| --- |
| string  OrderGetString(     ENUM\_ORDER\_PROPERTY\_STRING  property\_id        // Property identifier     ); |

2. Returns true or false, depending on the success of the function. If successful, the value of the property is placed into a target variable passed by reference by the last parameter.

|  |
| --- |
| bool  OrderGetString(     ENUM\_ORDER\_PROPERTY\_STRING  property\_id,       // Property identifier     string&                     string\_var         // Here we accept the property value     ); |

Parameters

property\_id

[in]  Identifier of the order property. The value can be one of the values of the [ENUM\_ORDER\_PROPERTY\_STRING](../../Constants,-Enumerations-and-Structures/Trade-Constants/Order-Properties/Order-Properties.md#enum_order_property_string) enumeration.

string\_var

[out]  Variable of the string type that accepts the value of the requested property.

Return Value

Value of the [string](../../Language-Basics/Data-Types/String-Type/String-Type.md) type.

Note

Do not confuse current [pending orders](../../Constants,-Enumerations-and-Structures/Trade-Constants/Order-Properties/Order-Properties.md) with positions, which are also displayed on the "Trade" tab of the "Toolbox" of the client terminal.

For the "netting" interpretation of positions ([ACCOUNT\_MARGIN\_MODE\_RETAIL\_NETTING](../../Constants,-Enumerations-and-Structures/Environment-State/Account-Properties/Account-Properties.md#enum_account_info_integer) and [ACCOUNT\_MARGIN\_MODE\_EXCHANGE](../../Constants,-Enumerations-and-Structures/Environment-State/Account-Properties/Account-Properties.md#enum_account_info_integer)), only one [position](../../Constants,-Enumerations-and-Structures/Trade-Constants/Position-Properties/Position-Properties.md) can exist for a [symbol](../../Checkup/Symbol/Symbol.md) at any moment of time. This position is a result of one or more [deals](../../Constants,-Enumerations-and-Structures/Trade-Constants/Deal-Properties/Deal-Properties.md). Do not confuse positions with valid [pending orders](../../Constants,-Enumerations-and-Structures/Trade-Constants/Order-Properties/Order-Properties.md), which are also displayed on the Trading tab of the Toolbox window.

If individual positions are allowed ([ACCOUNT\_MARGIN\_MODE\_RETAIL\_HEDGING](../../Constants,-Enumerations-and-Structures/Environment-State/Account-Properties/Account-Properties.md#enum_account_info_integer)), multiple positions can be open for one symbol.

To ensure receipt of fresh data about an order, it is recommended to call [OrderSelect()](../OrderSelect/OrderSelect.md) right before referring to them.

Example:

|  |
| --- |
| //+------------------------------------------------------------------+  //| Script program start function                                    |  //+------------------------------------------------------------------+  void OnStart()    {  //--- in a loop by the list of all account orders     int total=OrdersTotal();     for(int i=0; i<total; i++)       {        //--- get the order ticket in the list by the loop index        ulong ticket=OrderGetTicket(i);        if(ticket==0)           continue;                //--- get the order type and display the header for the list of string properties of the selected order        string type=OrderTypeDescription((ENUM\_ORDER\_TYPE)OrderGetInteger(ORDER\_TYPE));        PrintFormat("String properties of an active pending order %s #%I64u:", type, ticket);                //--- print all the string properties of the selected order under the header        OrderPropertiesStringPrint(13);       }     /\*     result:     String properties of an active pending order Sell Limit #2813781342:     Comment:     Test OrderGetString     Symbol:      EURUSD     External ID:      \*/    }  //+------------------------------------------------------------------+  //| Display string properties of the selected order in the journal   |  //+------------------------------------------------------------------+  void OrderPropertiesStringPrint(const uint header\_width=0)    {  //--- display the comment in the journal     OrderPropertyPrint("Comment:", header\_width, ORDER\_COMMENT);       //--- display a symbol the order has been placed for in the journal     OrderPropertyPrint("Symbol:", header\_width, ORDER\_SYMBOL);       //--- display the order ID in an external system in the journal      OrderPropertyPrint("External ID:", header\_width, ORDER\_EXTERNAL\_ID);    }  //+------------------------------------------------------------------+  //| Display the order string property value in the journal           |  //+------------------------------------------------------------------+  void OrderPropertyPrint(const string header, uint header\_width, ENUM\_ORDER\_PROPERTY\_STRING property)    {     string value="";     if(!OrderGetString(property, value))        PrintFormat("Cannot get property %s, error=%d", EnumToString(property), GetLastError());     else       {        //--- if the header width is passed to the function equal to zero, then the width will be the size of the header line + 1        uint w=(header\_width==0 ? header.Length()+1 : header\_width);        PrintFormat("%-\*s%-s", w, header, value);       }    }  //+------------------------------------------------------------------+  //| Return the order type description                                |  //+------------------------------------------------------------------+  string OrderTypeDescription(const ENUM\_ORDER\_TYPE type)    {     switch(type)       {        case ORDER\_TYPE\_BUY              :  return("Buy");        case ORDER\_TYPE\_SELL             :  return("Sell");        case ORDER\_TYPE\_BUY\_LIMIT        :  return("Buy Limit");        case ORDER\_TYPE\_SELL\_LIMIT       :  return("Sell Limit");        case ORDER\_TYPE\_BUY\_STOP         :  return("Buy Stop");        case ORDER\_TYPE\_SELL\_STOP        :  return("Sell Stop");        case ORDER\_TYPE\_BUY\_STOP\_LIMIT   :  return("Buy Stop Limit");        case ORDER\_TYPE\_SELL\_STOP\_LIMIT  :  return("Sell Stop Limit");        default                          :  return("Unknown order type: "+(string)type);       }    } |

See also

[OrdersTotal()](../OrdersTotal/OrdersTotal.md), [OrderGetTicket()](../OrderGetTicket/OrderGetTicket.md), [Order Properties](../../Constants,-Enumerations-and-Structures/Trade-Constants/Order-Properties/Order-Properties.md)
