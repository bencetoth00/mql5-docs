# OrderCalcProfit

OrderCalcProfit

The function calculates the profit for the current account, in the current market conditions, based on the parameters passed. The function is used for pre-evaluation of the result of a trade operation. The value is returned in the account currency.

|  |
| --- |
| bool  OrderCalcProfit(     ENUM\_ORDER\_TYPE       action,           // type of the order (ORDER\_TYPE\_BUY or ORDER\_TYPE\_SELL)     string                symbol,           // symbol name     double                volume,           // volume     double                price\_open,       // open price     double                price\_close,      // close price     double&               profit            // variable for obtaining the profit value     ); |

Parameters

action

[in]  Type of the order, can be one of the two values of the [ENUM\_ORDER\_TYPE](../../Constants,-Enumerations-and-Structures/Trade-Constants/Order-Properties/Order-Properties.md#enum_order_type) enumeration: ORDER\_TYPE\_BUY or ORDER\_TYPE\_SELL.

symbol

[in]  Symbol name.

volume

[in]  Volume of the trade operation.

price\_open

[in]  Open price.

price\_close

[in]  Close price.

profit

[out]  The variable, to which the calculated value of the profit will be written in case the function is successfully executed. The estimated profit value depends on many factors, and can differ in different market environments.

Return Value

The function returns true in case of success; otherwise it returns false. If an invalid order type is specified, the function will return false. In order to obtain information about the [error](../../Constants,-Enumerations-and-Structures/Codes-of-Errors-and-Warnings/Runtime-Errors/Runtime-Errors.md), call [GetLastError()](../../Checkup/GetLastError/GetLastError.md).

Example:

|  |
| --- |
| #define   VOLUME     1.0   // order volume  #define   DEVIATION  100   // number of points before the close price     //+------------------------------------------------------------------+  //| Script program start function                                    |  //+------------------------------------------------------------------+  void OnStart()    {     string currency\_profit=SymbolInfoString(\_Symbol,SYMBOL\_CURRENCY\_PROFIT);   // profit currency     double close\_price=ChartPriceOnDropped(); // the price coordinate, corresponding to the point where the script was dropped using the mouse, serves as the close price     //---     for(int i=0; i<=ORDER\_TYPE\_SELL; i++)       {        ENUM\_ORDER\_TYPE order\_type=(ENUM\_ORDER\_TYPE)i;                 // order type: 0 - Buy, 1 - Sell        double open\_price=PriceOpenByOrderType(\_Symbol, order\_type);   // open price: for Buy - Ask, for Sell - Bid               //--- if the open price is not received, continue the loop        if(open\_price==0)           continue;                //--- if the close price is zero (the script was not launched by dragging onto the chart), calculate the price        if(close\_price==0)           close\_price=(order\_type==ORDER\_TYPE\_BUY ? open\_price + DEVIATION \* \_Point : open\_price - DEVIATION \* \_Point);                //--- calculate the approximate profit size for the current account and market environment based on the passed parameters        double profit=0;        ResetLastError();        if(!OrderCalcProfit(order\_type, \_Symbol, VOLUME, open\_price, close\_price, profit))          {           Print("OrderCalcProfit() failed. Error ", GetLastError());           continue;          }                //--- print the received profit value in the journal        PrintFormat("Estimated profit for %.2f %s position on %s with opening price of %.\*f and closing price of %.\*f: %.2f %s",                    VOLUME, OrderTypeDescription(order\_type), \_Symbol, \_Digits, open\_price, \_Digits, close\_price, profit, currency\_profit);               }     /\*     result:     Estimated profit for 1.00 Buy position on EURUSD with opening price of 1.10757 and closing price of 1.10881: 124.00 USD     Estimated profit for 1.00 Sell position on EURUSD with opening price of 1.10753 and closing price of 1.10881: -128.00 USD     \*/    }  //+------------------------------------------------------------------+  //| Return open price by order type                                  |  //+------------------------------------------------------------------+  double PriceOpenByOrderType(const string symbol, const ENUM\_ORDER\_TYPE order\_type)    {     MqlTick tick={};     //--- get the last prices by symbol     if(!SymbolInfoTick(symbol, tick))       {        Print("SymbolInfoTick() failed. Error ", GetLastError());        return 0;       }         //--- return the price depending on the order type     switch(order\_type)       {        case ORDER\_TYPE\_BUY              :  return(tick.ask);        case ORDER\_TYPE\_SELL             :  return(tick.bid);        default                          :  return(0);       }    }  //+------------------------------------------------------------------+  //| Return the order type description                                |  //+------------------------------------------------------------------+  string OrderTypeDescription(const ENUM\_ORDER\_TYPE order\_type)    {     switch(order\_type)       {        case ORDER\_TYPE\_BUY              :  return("Buy");        case ORDER\_TYPE\_SELL             :  return("Sell");        default                          :  return("Unknown order type");       }    } |

See also

[OrderSend()](../OrderSend/OrderSend.md), [Order Properties](../../Constants,-Enumerations-and-Structures/Trade-Constants/Order-Properties/Order-Properties.md), [Trade Operation Types](../../Constants,-Enumerations-and-Structures/Trade-Constants/Trade-Operation-Types/Trade-Operation-Types.md)
