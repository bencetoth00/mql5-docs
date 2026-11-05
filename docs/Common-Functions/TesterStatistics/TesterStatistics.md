# TesterStatistics

TesterStatistics

The function returns the value of the specified statistical parameter calculated based on testing results.

|  |
| --- |
| double  TesterStatistics(     ENUM\_STATISTICS statistic\_id      // ID     ); |

Parameters

statistic\_id

[in]   The ID of the statistical parameter from the [ENUM\_STATISTICS](../../Constants,-Enumerations-and-Structures/Environment-State/Testing-Statistics/Testing-Statistics.md#enum_statistics) enumeration.

Return Value

The value of the statistical parameter from testing results.

Note

The function can be called inside [OnTester()](../../Event-Handling/OnTester/OnTester.md) or [OnDeinit()](../../Language-Basics/Functions/Event-Handling-Functions/Event-Handling-Functions.md) in the tester. In other cases the result is undefined.

 

Example:

|  |
| --- |
| // The EA based on standard "MACD Sample.mq5" file  // shows the result of TesterStatistics() in the Tester event handler  #define MACD\_MAGIC 1234502  //---  #include <Trade\Trade.mqh>  #include <Trade\SymbolInfo.mqh>  #include <Trade\PositionInfo.mqh>  #include <Trade\AccountInfo.mqh>  //---  input double InpLots          =0.1; // Lots  input int    InpTakeProfit    =50;  // Take Profit (in pips)  input int    InpTrailingStop  =30;  // Trailing Stop Level (in pips)  input int    InpMACDOpenLevel =3;   // MACD open level (in pips)  input int    InpMACDCloseLevel=2;   // MACD close level (in pips)  input int    InpMATrendPeriod =26;  // MA trend period  //+------------------------------------------------------------------+  //| Expert initialization function                                   |  //+------------------------------------------------------------------+  int OnInit(void)    {  //--- create all the necessary objects     if(!ExtExpert.Init())        return(INIT\_FAILED);  //--- successful initialization     return(INIT\_SUCCEEDED);    }  //+------------------------------------------------------------------+  //| Expert new tick handling function                                |  //+------------------------------------------------------------------+  void OnTick(void)    {     static datetime limit\_time=0; // last call time considering 'timeout'  //--- if the time exceeds the specified limit\_time value     if(TimeCurrent()>=limit\_time)       {        //--- check the data        if(Bars(Symbol(),Period())>2\*InpMATrendPeriod)          {           //--- if successful, increase limit\_time by 'timeout' seconds           if(ExtExpert.Processing())              limit\_time=TimeCurrent()+ExtTimeOut;          }       }    }  //+------------------------------------------------------------------+  //| Expert tester handling function                                  |  //+------------------------------------------------------------------+  double OnTester(void)    {     double ret=TesterStatistics(STAT\_PROFIT\_FACTOR);     double profit=TesterStatistics(STAT\_PROFIT);     int    trades\_total=(int)TesterStatistics(STAT\_TRADES);     int    profit\_total=(int)TesterStatistics(STAT\_PROFIT\_TRADES);     int    loss\_total=(int)TesterStatistics(STAT\_LOSS\_TRADES);     PrintFormat("%s: Profit = %.2f, trades total: %lu, profit trades total: %lu, loss trades total: %lu, profit factor: %.2f",\_\_FUNCTION\_\_,profit,trades\_total,profit\_total,loss\_total,ret);     return(ret);     /\*     Result:     OnTester: Profit = 209.84, trades total: 13, profit trades total: 11, loss trades total: 2, profit factor: 3.02     final balance 10209.84 USD     OnTester result 3.020606644198363     \*/    } |
