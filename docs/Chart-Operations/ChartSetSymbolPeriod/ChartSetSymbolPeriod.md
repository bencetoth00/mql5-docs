# ChartSetSymbolPeriod

ChartSetSymbolPeriod

Changes the symbol and period of the specified chart. The function is asynchronous, i.e. it sends the command and does not wait for its execution completion. The command is added to chart messages queue and will be executed after processing of all previous commands.

|  |
| --- |
| bool  ChartSetSymbolPeriod(     long             chart\_id,     // Chart ID     string           symbol,       // Symbol name     ENUM\_TIMEFRAMES  period        // Period     ); |

Parameters

chart\_id

[in]  Chart ID. 0 means the current chart.

symbol

[in]  Chart symbol. [NULL](../../Language-Basics/Data-Types/Void-Type-and-NULL-Constant/Void-Type-and-NULL-Constant.md) value means the current chart symbol (Expert Advisor is attached to)

period

[in]  Chart period (timeframe). Can be one of the [ENUM\_TIMEFRAMES](../../Constants,-Enumerations-and-Structures/Chart-Constants/Chart-Timeframes/Chart-Timeframes.md) values. 0 means the current chart period.

Return Value

Returns true if the command has been added to chart queue, otherwise false. To get an information about the [error](../../Constants,-Enumerations-and-Structures/Codes-of-Errors-and-Warnings/Runtime-Errors/Runtime-Errors.md), call the [GetLastError()](../../Checkup/GetLastError/GetLastError.md) function.

Note

The symbol/period change leads to the re-initialization of the Expert Advisor attached to a chart.

The call of ChartSetSymbolPeriod with the same symbol and timeframe can be used to update the chart (similar to the terminal's Refresh command). In its turn, the chart update triggers re-calculation of the indicators attached to it. Thus, you are able to calculate an indicator on the chart even if there are no ticks (e.g., on weekends).

Example:

|  |
| --- |
| #define   SYMBOL    "GBPUSD"  #define   PERIOD    PERIOD\_H1     //+------------------------------------------------------------------+  //| Script program start function                                    |  //+------------------------------------------------------------------+  void OnStart()    {  //--- get the current chart ID, symbol and period     long            chart\_id= ChartID();     string          symbol  = Symbol();     ENUM\_TIMEFRAMES period  = Period();     //--- report in the journal on replacing the current chart symbol and period with the ones set in SYMBOL and PERIOD     PrintFormat("Change the %s symbol and the %s period of the chart %I64u to %s %s",                 symbol, TimeframeDescrioption(period), chart\_id, SYMBOL, TimeframeDescrioption(PERIOD));                   //--- change the chart symbol and period     ChartSetSymbolPeriod(chart\_id, SYMBOL, PERIOD);     /\*     result:     Change the EURUSD symbol and the M1 period of the chart 133246248352168440 to GBPUSD H1     \*/    }  //+------------------------------------------------------------------+  //| Return the chart period description                              |  //+------------------------------------------------------------------+  string TimeframeDescrioption(const ENUM\_TIMEFRAMES timeframe)    {     return(StringSubstr(EnumToString(timeframe), 7));    } |

See also

[ChartSymbol](../ChartSymbol/ChartSymbol.md), [ChartPeriod](../ChartPeriod/ChartPeriod.md)
