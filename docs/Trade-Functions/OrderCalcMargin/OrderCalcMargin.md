# OrderCalcMargin

OrderCalcMargin

The function calculates the margin required for the specified order type, on the current account, in the current market environment not taking into account current pending orders and open positions. It allows the evaluation of margin for the trade operation planned. The value is returned in the account currency.

|  |
| --- |
| bool  OrderCalcMargin(     ENUM\_ORDER\_TYPE       action,           // type of order     string                symbol,           // symbol name     double                volume,           // volume     double                price,            // open price     double&               margin            // variable for obtaining the margin value     ); |

Parameters

action

[in]  The order type, can be one of the values of the [ENUM\_ORDER\_TYPE](../../Constants,-Enumerations-and-Structures/Trade-Constants/Order-Properties/Order-Properties.md#enum_order_type) enumeration.

symbol

[in]  Symbol name.

volume

[in]  Volume of the trade operation.

price

[in]  Open price.

margin

[out]  The variable, to which the value of the required margin will be written in case the function is successfully executed. The calculation is performed as if there were no pending orders and open positions on the current account. The margin value depends on many factors, and can differ in different market environments.

Return Value

The function returns true in case of success; otherwise it returns false. In order to obtain information about the [error](../../Constants,-Enumerations-and-Structures/Codes-of-Errors-and-Warnings/Runtime-Errors/Runtime-Errors.md), call the [GetLastError()](../../Checkup/GetLastError/GetLastError.md) function.

Example:

|  |
| --- |
| #define   VOLUME     1.0   // order volume  #define   DEVIATION  100   // distance for setting a pending order  #define   STOP\_LIMIT 50    // order StopLimit distance     //+------------------------------------------------------------------+  //| Script program start function                                    |  //+------------------------------------------------------------------+  void OnStart()    {     string currency=AccountInfoString(ACCOUNT\_CURRENCY);     int array\_types[8]={ORDER\_TYPE\_BUY,                         ORDER\_TYPE\_SELL,                         ORDER\_TYPE\_BUY\_LIMIT,                         ORDER\_TYPE\_SELL\_LIMIT,                         ORDER\_TYPE\_BUY\_STOP,                         ORDER\_TYPE\_SELL\_STOP,                         ORDER\_TYPE\_BUY\_STOP\_LIMIT,                         ORDER\_TYPE\_SELL\_STOP\_LIMIT };                           //--- in a loop by the order type array     for(int i=0; i<(int)array\_types.Size(); i++)       {        //--- depending on the order type, get ORDER\_TYPE\_BUY or ORDER\_TYPE\_SELL type        ENUM\_ORDER\_TYPE type=MarketOrderByOrderType((ENUM\_ORDER\_TYPE)array\_types[i]);                //--- depending on the order type, get the price        double price=PriceByOrderType(\_Symbol, type);                //--- get the amount of margin required for the order type specified in 'action'         double margin=EMPTY\_VALUE;        ResetLastError();        if(!OrderCalcMargin(type, \_Symbol, VOLUME, price, margin))          {           Print("OrderCalcMargin() failed. Error ",GetLastError());           continue;          }        //--- print the result in the journal        PrintFormat("Margin required for %.2f %s order at price %.\*f on %s symbol: %.2f %s", VOLUME, OrderTypeDescription((ENUM\_ORDER\_TYPE)i), \_Digits, price, \_Symbol, margin, currency);       }     /\*     result:     Margin required for 1.00 Buy order at price 1.31668 on GBPUSD symbol: 1316.68 USD     Margin required for 1.00 Sell order at price 1.31661 on GBPUSD symbol: 1316.61 USD     Margin required for 1.00 Buy Limit order at price 1.31568 on GBPUSD symbol: 1315.68 USD     Margin required for 1.00 Sell Limit order at price 1.31761 on GBPUSD symbol: 1317.61 USD     Margin required for 1.00 Buy Stop order at price 1.31768 on GBPUSD symbol: 1317.68 USD     Margin required for 1.00 Sell Stop order at price 1.31561 on GBPUSD symbol: 1315.61 USD     Margin required for 1.00 Buy Stop Limit order at price 1.31718 on GBPUSD symbol: 1317.18 USD     Margin required for 1.00 Sell Stop Limit order at price 1.31611 on GBPUSD symbol: 1316.11 USD     \*/    }  //+------------------------------------------------------------------+  //| Return the Buy or Sell order type                                |  //+------------------------------------------------------------------+  ENUM\_ORDER\_TYPE MarketOrderByOrderType(ENUM\_ORDER\_TYPE type)    {     switch(type)       {        case ORDER\_TYPE\_BUY  : case ORDER\_TYPE\_BUY\_LIMIT  : case ORDER\_TYPE\_BUY\_STOP  : case ORDER\_TYPE\_BUY\_STOP\_LIMIT  :          return(ORDER\_TYPE\_BUY);        case ORDER\_TYPE\_SELL : case ORDER\_TYPE\_SELL\_LIMIT : case ORDER\_TYPE\_SELL\_STOP : case ORDER\_TYPE\_SELL\_STOP\_LIMIT :          return(ORDER\_TYPE\_SELL);       }     return(WRONG\_VALUE);    }  //+------------------------------------------------------------------+  //| Return open price by order type                                  |  //+------------------------------------------------------------------+  double PriceByOrderType(const string symbol, const ENUM\_ORDER\_TYPE order\_type)    {     int     digits=0;     double  point=0;     MqlTick tick={};     //--- get the symbol Point value     ResetLastError();     if(!SymbolInfoDouble(symbol, SYMBOL\_POINT, point))       {        Print("SymbolInfoDouble() failed. Error ", GetLastError());        return 0;       }         //--- get the symbol Digits value     long value=0;     if(!SymbolInfoInteger(symbol, SYMBOL\_DIGITS, value))       {        Print("SymbolInfoInteger() failed. Error ", GetLastError());        return 0;       }     digits=(int)value;       //--- get the last prices by symbol     if(!SymbolInfoTick(symbol, tick))       {        Print("SymbolInfoTick() failed. Error ", GetLastError());        return 0;       }         //--- return the price depending on the order type     switch(order\_type)       {        case ORDER\_TYPE\_BUY              :  return(tick.ask);        case ORDER\_TYPE\_SELL             :  return(tick.bid);        case ORDER\_TYPE\_BUY\_LIMIT        :  return(NormalizeDouble(tick.ask - DEVIATION \* point, digits));        case ORDER\_TYPE\_SELL\_LIMIT       :  return(NormalizeDouble(tick.bid + DEVIATION \* point, digits));        case ORDER\_TYPE\_BUY\_STOP         :  return(NormalizeDouble(tick.ask + DEVIATION \* point, digits));        case ORDER\_TYPE\_SELL\_STOP        :  return(NormalizeDouble(tick.bid - DEVIATION \* point, digits));        case ORDER\_TYPE\_BUY\_STOP\_LIMIT   :  return(NormalizeDouble(tick.ask + DEVIATION \* point - STOP\_LIMIT \* point, digits));        case ORDER\_TYPE\_SELL\_STOP\_LIMIT  :  return(NormalizeDouble(tick.bid - DEVIATION \* point + STOP\_LIMIT \* point, digits));        default                          :  return(0);       }    }  //+------------------------------------------------------------------+  //| Return the order type description                                |  //+------------------------------------------------------------------+  string OrderTypeDescription(const ENUM\_ORDER\_TYPE order\_type)    {     switch(order\_type)       {        case ORDER\_TYPE\_BUY              :  return("Buy");        case ORDER\_TYPE\_SELL             :  return("Sell");        case ORDER\_TYPE\_BUY\_LIMIT        :  return("Buy Limit");        case ORDER\_TYPE\_SELL\_LIMIT       :  return("Sell Limit");        case ORDER\_TYPE\_BUY\_STOP         :  return("Buy Stop");        case ORDER\_TYPE\_SELL\_STOP        :  return("Sell Stop");        case ORDER\_TYPE\_BUY\_STOP\_LIMIT   :  return("Buy Stop Limit");        case ORDER\_TYPE\_SELL\_STOP\_LIMIT  :  return("Sell Stop Limit");        case ORDER\_TYPE\_CLOSE\_BY         :  return("Close By");        default                          :  return("Unknown order type");       }    }  //+------------------------------------------------------------------+ |

See also

[OrderSend()](../OrderSend/OrderSend.md), [Order Properties](../../Constants,-Enumerations-and-Structures/Trade-Constants/Order-Properties/Order-Properties.md), [Trade Operation Types](../../Constants,-Enumerations-and-Structures/Trade-Constants/Trade-Operation-Types/Trade-Operation-Types.md)
