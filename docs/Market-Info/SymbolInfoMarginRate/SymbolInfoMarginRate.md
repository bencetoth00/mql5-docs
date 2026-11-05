# SymbolInfoMarginRate

SymbolInfoMarginRate

Returns the margin rates depending on the order type and direction.

|  |
| --- |
| bool  SymbolInfoMarginRate(     string             name,                     // symbol name     ENUM\_ORDER\_TYPE    order\_type,               // order type     double&            initial\_margin\_rate,      // initial margin rate     double&            maintenance\_margin\_rate   // maintenance margin rate     ); |

Parameters

name

[in] Symbol name.

order\_type

[in] Order type.

initial\_margin\_rate

[in] A [double](../../Language-Basics/Data-Types/Real-Types-(double,-float)/Real-Types-(double,-float).md) type variable for receiving an initial margin rate. Initial margin is a security deposit for 1 lot deal in the appropriate direction. Multiplying the rate by the initial margin, we receive the amount of funds to be reserved on the account when placing an order of the specified type.

maintenance\_margin\_rate

[out] A [double](../../Language-Basics/Data-Types/Real-Types-(double,-float)/Real-Types-(double,-float).md) type variable for receiving a maintenance margin rate. Maintenance margin is a minimum amount for maintaining an open position of 1 lot in the appropriate direction. Multiplying the rate by the maintenance margin, we receive the amount of funds to be reserved on the account after an order of the specified type is activated.

Return Value

Returns true if request for properties is successful, otherwise false.

Example:

|  |
| --- |
| #define SYMBOL\_NAME Symbol()     //+------------------------------------------------------------------+  //| Script program start function                                    |  //+------------------------------------------------------------------+  void OnStart()    {  //--- declare the variables the ratios are set into     double initial\_margin\_rate = 0;     // initial margin rate     double maintenance\_margin\_rate = 0; // maintenance margin rate       //--- get and send the SYMBOL\_NAME symbol ratios for the Buy market order to the journal     SymbolInfoMarginRatePrint(SYMBOL\_NAME, ORDER\_TYPE\_BUY, initial\_margin\_rate, maintenance\_margin\_rate);       //--- get and send the SYMBOL\_NAME symbol ratios for the Sell market order to the journal     SymbolInfoMarginRatePrint(SYMBOL\_NAME, ORDER\_TYPE\_SELL, initial\_margin\_rate, maintenance\_margin\_rate);        /\*     result:     Initial margin rate for symbol AFKS for the Buy market order: 0.225600     Maintenance margin rate for symbol AFKS for the Buy market order: 0.112800     Initial margin rate for symbol AFKS for the Sell market order: 0.254400     Maintenance margin rate for symbol AFKS for the Sell market order: 0.127200        \*/    }  //+------------------------------------------------------------------+  //| Send the margin ratios to the journal                            |  //+------------------------------------------------------------------+  void SymbolInfoMarginRatePrint(const string symbol, const ENUM\_ORDER\_TYPE order\_type, double &initial\_margin\_rate, double &maintenance\_margin\_rate)    {  //--- get the 'symbol' ratios for the order\_type market order     ResetLastError();     if(!SymbolInfoMarginRate(symbol, order\_type, initial\_margin\_rate, maintenance\_margin\_rate))       {        Print("SymbolInfoMarginRate() failed. Error ", GetLastError());        return;       }  //--- print the obtained ratio values     string type=(order\_type==ORDER\_TYPE\_BUY ? "Buy" : order\_type==ORDER\_TYPE\_SELL ? "Sell" : "Unknown");     PrintFormat("Initial margin rate for symbol %s for the %s market order: %f\n"+                 "Maintenance margin rate for symbol %s for the %s market order: %f",                 SYMBOL\_NAME, type, initial\_margin\_rate,                 SYMBOL\_NAME, type, maintenance\_margin\_rate);    } |
