# ChartOpen

ChartOpen

Opens a new chart with the specified symbol and period.

|  |
| --- |
| long  ChartOpen(     string           symbol,     // Symbol name     ENUM\_TIMEFRAMES  period      // Period     ); |

Parameters

symbol

[in]  Chart symbol. [NULL](../../Language-Basics/Data-Types/Void-Type-and-NULL-Constant/Void-Type-and-NULL-Constant.md) means the symbol of the  current chart (the Expert Advisor is attached to).

period

[in]  Chart period (timeframe). Can be one of the [ENUM\_TIMEFRAMES](../../Constants,-Enumerations-and-Structures/Chart-Constants/Chart-Timeframes/Chart-Timeframes.md) values. 0 means the current chart period.

Return Value

If successful, it returns the opened chart ID. Otherwise returns 0.

Note

The maximum possible number of simultaneously open charts in the terminal can't exceed the [CHARTS\_MAX](../../Constants,-Enumerations-and-Structures/Named-Constants/Other-Constants/Other-Constants.md) value.

Example:

|  |
| --- |
| #define CHART\_SYMBOL  NULL  #define CHART\_PERIOD  PERIOD\_CURRENT     //+------------------------------------------------------------------+  //| Script program start function                                    |  //+------------------------------------------------------------------+  void OnStart()    {  //--- set a new chart symbol and timeframe     string symbol=CHART\_SYMBOL;     if(symbol==NULL)        symbol=Symbol();     ENUM\_TIMEFRAMES timeframe = (CHART\_PERIOD==PERIOD\_CURRENT ? Period() : CHART\_PERIOD);       //--- open a new chart with the specified symbol and period     long chart\_id=ChartOpen(symbol, timeframe);     if(chart\_id==0)       {        Print("ChartOpen() failed. Error ", GetLastError());        return;       }     //--- print open chart parameters in the journal     PrintFormat("A new chart of the %s symbol has been opened with a period of %s and ChartID %I64u",                 symbol, StringSubstr(EnumToString(timeframe), 7), chart\_id);     /\*     result:     A new chart of the GBPUSD symbol has been opened with a period of M1 and ChartID 133346697706632016     \*/    } |
