# ChartSymbol

ChartSymbol

Returns the symbol name for the specified chart.

|  |
| --- |
| string  ChartSymbol(     long  chart\_id=0      // Chart ID     ); |

Parameters

chart\_id=0

[in]  Chart ID. 0 means the current chart.

Return Value

If chart does not exist, the result will be an empty string.

Example:

|  |
| --- |
| //+------------------------------------------------------------------+  //| Script program start function                                    |  //+------------------------------------------------------------------+  void OnStart()    {  //--- get the current chart symbol and display the obtained value in the journal     string chart\_symbol = ChartSymbol();     Print("Current chart symbol: ", chart\_symbol);       //--- take the existing (in this case, the current) chart ID     long chart\_id=ChartID();     chart\_symbol=ChartSymbol(chart\_id);     PrintFormat("Chart symbol with ID %I64d: %s", chart\_id, chart\_symbol);     //--- set a random chart ID when receiving a symbol     chart\_symbol = ChartSymbol(1234567890);     if(chart\_symbol=="")        Print("The chart with ID 1234567890 does not exist");     else        Print("Chart symbol with ID 1234567890: ", chart\_symbol);     /\*     result:     Current chart symbol: GBPUSD     Chart symbol with ID 132966427583395104: GBPUSD     The chart with ID 1234567890 does not exist     \*/    } |

See also

[ChartSetSymbolPeriod](../ChartSetSymbolPeriod/ChartSetSymbolPeriod.md)
