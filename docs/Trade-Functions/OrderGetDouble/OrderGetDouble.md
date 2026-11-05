# OrderGetDouble

OrderGetDouble

Returns the requested property of an order, pre-selected using [OrderGetTicket](../OrderGetTicket/OrderGetTicket.md) or [OrderSelect](../OrderSelect/OrderSelect.md). The order property must be of the double type. There are 2 variants of the function.

1. Immediately returns the property value.

|  |
| --- |
| double  OrderGetDouble(     ENUM\_ORDER\_PROPERTY\_DOUBLE  property\_id        // Property identifier     ); |

2. Returns true or false, depending on the success of a function. If successful, the value of the property is placed in a target variable passed by reference by the last parameter.

|  |
| --- |
| bool  OrderGetDouble(     [ENUM\_ORDER\_PROPERTY\_DOUBLE](../../Constants,-Enumerations-and-Structures/Trade-Constants/Order-Properties/Order-Properties.md#enum_order_property_double)  property\_id,       // Property identifier     double&                        double\_var         // Here we accept the property value     ); |

Parameters

property\_id

[in]  Identifier of the order property. The value can be one of the values of the [ENUM\_ORDER\_PROPERTY\_DOUBLE](../../Constants,-Enumerations-and-Structures/Trade-Constants/Order-Properties/Order-Properties.md#enum_order_property_double) enumeration.

double\_var

[out]  Variable of the double type that accepts the value of the requested property.

Return Value

Value of the [double](../../Language-Basics/Data-Types/Real-Types-(double,-float)/Real-Types-(double,-float).md) type. If the function fails, 0 is returned.

Note

Do not confuse current [pending orders](../../Constants,-Enumerations-and-Structures/Trade-Constants/Order-Properties/Order-Properties.md) with positions, which are also displayed on the "Trade" tab of the "Toolbox" of the client terminal.

For the "netting" interpretation of positions ([ACCOUNT\_MARGIN\_MODE\_RETAIL\_NETTING](../../Constants,-Enumerations-and-Structures/Environment-State/Account-Properties/Account-Properties.md#enum_account_info_integer) and [ACCOUNT\_MARGIN\_MODE\_EXCHANGE](../../Constants,-Enumerations-and-Structures/Environment-State/Account-Properties/Account-Properties.md#enum_account_info_integer)), only one [position](../../Constants,-Enumerations-and-Structures/Trade-Constants/Position-Properties/Position-Properties.md) can exist for a [symbol](../../Checkup/Symbol/Symbol.md) at any moment of time. This position is a result of one or more [deals](../../Constants,-Enumerations-and-Structures/Trade-Constants/Deal-Properties/Deal-Properties.md). Do not confuse positions with valid [pending orders](../../Constants,-Enumerations-and-Structures/Trade-Constants/Order-Properties/Order-Properties.md), which are also displayed on the Trading tab of the Toolbox window.

If individual positions are allowed ([ACCOUNT\_MARGIN\_MODE\_RETAIL\_HEDGING](../../Constants,-Enumerations-and-Structures/Environment-State/Account-Properties/Account-Properties.md#enum_account_info_integer)), multiple positions can be open for one symbol.

To ensure receipt of fresh data about an order, it is recommended to call [OrderSelect()](../OrderSelect/OrderSelect.md) right before referring to them.

Example:

|  |
| --- |
| //+------------------------------------------------------------------+  //| Script program start function                                    |  //+------------------------------------------------------------------+  void OnStart()    {  //--- in a loop by the list of all account orders     int total=OrdersTotal();     for(int i=0; i<total; i++)       {        //--- get the order ticket in the list by the loop index        ulong ticket=OrderGetTicket(i);        if(ticket==0)           continue;                //--- get the order type and display the header for the list of real properties of the selected order        string type=OrderTypeDescription((ENUM\_ORDER\_TYPE)OrderGetInteger(ORDER\_TYPE));        PrintFormat("Double properties of an active pending order %s #%I64u:", type, ticket);                //--- print all the real properties of the selected order under the header        OrderPropertiesDoublePrint(16);       }     /\*     result:     Double properties of an active pending order Sell Limit #2812000714:     Volume initial: 1.00     Volume current: 1.00     Price open:     145.282     StopLoss:       0.000     TakeProfit:     0.000     Price current:  145.044     StopLimit:      0.000     Double properties of an active pending order Buy Limit #2812001112:     Volume initial: 1.00     Volume current: 1.00     Price open:     144.836     StopLoss:       0.000     TakeProfit:     0.000     Price current:  145.051     StopLimit:      0.000     Double properties of an active pending order Buy Stop #2812001488:     Volume initial: 0.50     Volume current: 0.50     Price open:     1.10642     StopLoss:       0.00000     TakeProfit:     0.00000     Price current:  1.10530     StopLimit:      0.00000     Double properties of an active pending order Sell Stop #2812001712:     Volume initial: 0.50     Volume current: 0.50     Price open:     1.10374     StopLoss:       0.00000     TakeProfit:     0.00000     Price current:  1.10525     StopLimit:      0.00000     \*/    }  //+------------------------------------------------------------------+  //| Return the order type description                                |  //+------------------------------------------------------------------+  string OrderTypeDescription(const ENUM\_ORDER\_TYPE type)    {     switch(type)       {        case ORDER\_TYPE\_BUY              :  return("Buy");        case ORDER\_TYPE\_SELL             :  return("Sell");        case ORDER\_TYPE\_BUY\_LIMIT        :  return("Buy Limit");        case ORDER\_TYPE\_SELL\_LIMIT       :  return("Sell Limit");        case ORDER\_TYPE\_BUY\_STOP         :  return("Buy Stop");        case ORDER\_TYPE\_SELL\_STOP        :  return("Sell Stop");        case ORDER\_TYPE\_BUY\_STOP\_LIMIT   :  return("Buy Stop Limit");        case ORDER\_TYPE\_SELL\_STOP\_LIMIT  :  return("Sell Stop Limit");        default                          :  return("Unknown order type");       }    }  //+------------------------------------------------------------------+  //| Display real properties of the selected order in the journal     |  //+------------------------------------------------------------------+  void OrderPropertiesDoublePrint(const uint header\_width=0)    {  //--- get the order symbol and the number of decimal places for the symbol     string symbol = OrderGetString(ORDER\_SYMBOL);     int    digits = (int)SymbolInfoInteger(symbol, SYMBOL\_DIGITS);       //--- display the initial volume when placing an order with a header of the specified width in the journal     OrderPropertyPrint("Volume initial:",header\_width,2,ORDER\_VOLUME\_INITIAL);       //--- display the unfulfilled order volume in the journal     OrderPropertyPrint("Volume current:",header\_width,2,ORDER\_VOLUME\_CURRENT);       //--- display the price, specified in the order, in the journal     OrderPropertyPrint("Price open:",header\_width,digits,ORDER\_PRICE\_OPEN);       //--- display the StopLoss level in the journal     OrderPropertyPrint("StopLoss:",header\_width,digits,ORDER\_SL);     //--- display the TakeProfit level in the journal     OrderPropertyPrint("TakeProfit:",header\_width,digits,ORDER\_TP);     //--- display the current price by the order symbol in the journal     OrderPropertyPrint("Price current:",header\_width,digits,ORDER\_PRICE\_CURRENT);     //--- display the Limit order price, when StopLimit order is activated, in the journal     OrderPropertyPrint("StopLimit:",header\_width,digits,ORDER\_PRICE\_STOPLIMIT);    }  //+------------------------------------------------------------------+  //| Display the order real property value in the journal             |  //+------------------------------------------------------------------+  void OrderPropertyPrint(const string header, uint header\_width, int digits, ENUM\_ORDER\_PROPERTY\_DOUBLE property)    {     double value=0;     if(!OrderGetDouble(property, value))        PrintFormat("Cannot get property %s, error=%d", EnumToString(property), GetLastError());     else       {        //--- if the header width is passed to the function equal to zero, then the width will be the size of the header line + 1        uint w=(header\_width==0 ? header.Length()+1 : header\_width);        PrintFormat("%-\*s%-.\*f", w, header, digits, value);       }    } |

See also

[OrdersTotal()](../OrdersTotal/OrdersTotal.md), [OrderGetTicket()](../OrderGetTicket/OrderGetTicket.md), [Order Properties](../../Constants,-Enumerations-and-Structures/Trade-Constants/Order-Properties/Order-Properties.md)
