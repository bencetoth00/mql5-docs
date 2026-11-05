# ExpertRemove

ExpertRemove

The function stops an [Expert Advisor](../../index.md#expert) and unloads it from a chart.

|  |
| --- |
| void  ExpertRemove(); |

Return Value

No return value.

Note

The Expert Advisor is not stopped immediately as you call ExpertRemove(); just a flag to stop the EA operation is set. That is, any next event won't be processed, [OnDeinit()](../../Event-Handling/OnDeinit/OnDeinit.md) will be called and the Expert Advisor will be unloaded and removed from the chart.

Calling [ExpertRemove()](ExpertRemove.md) in the strategy tester inside the [OnInit()](../../Event-Handling/OnInit/OnInit.md) handler cancels testing on the current set of parameters. Such completion is considered an initialization error.

When calling [ExpertRemove()](ExpertRemove.md) in the strategy tester after [successful initialization](../../Event-Handling/OnInit/OnInit.md) of an EA, a test is completed normally with the call of [OnDeinit()](../../Event-Handling/OnDeinit/OnDeinit.md) and [OnTester()](../../Event-Handling/OnTester/OnTester.md). In this case, the entire trading statistics and an [optimization criterion](https://www.metatrader5.com/en/terminal/help/algotrading/optimization_types#criterion) value are obtained.

Example:

|  |
| --- |
| //+------------------------------------------------------------------+  //|                                            Test\_ExpertRemove.mq5 |  //|                        Copyright 2009, MetaQuotes Software Corp. |  //|                                             https://www.mql5.com |  //+------------------------------------------------------------------+  #property copyright "2009, MetaQuotes Software Corp."  #property link      "https://www.mql5.com"  #property version   "1.00"  input int ticks\_to\_close=20;// number of ticks before EA unload  //+------------------------------------------------------------------+  //| Expert deinitialization function                                 |  //+------------------------------------------------------------------+  void OnDeinit(const int reason)    {  //---      Print(TimeCurrent(),": " ,\_\_FUNCTION\_\_," reason code = ",reason);  //--- "clear" comment     Comment("");  //---    }  //+------------------------------------------------------------------+  //| Expert tick function                                             |  //+------------------------------------------------------------------+  void OnTick()    {     static int tick\_counter=0;  //---     tick\_counter++;     Comment("\nBefore unloading expert advisor ",\_\_FILE\_\_," left",             (ticks\_to\_close-tick\_counter)," ticks");  //--- before     if(tick\_counter>=ticks\_to\_close)       {        ExpertRemove();        Print(TimeCurrent(),": ",\_\_FUNCTION\_\_," expert advisor will be unloaded");       }     Print("tick\_counter =",tick\_counter);  //---    }  //+------------------------------------------------------------------+ |

See also

[Program running](../../MQL5-programs/Program-Running/Program-Running.md), [Client terminal events](../../MQL5-programs/Client-Terminal-Events/Client-Terminal-Events.md)
