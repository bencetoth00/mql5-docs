# ChartIndicatorName

ChartIndicatorName

Returns the short name of the indicator by the number in the indicators list on the specified chart window.

|  |
| --- |
| string  ChartIndicatorName(     long  chart\_id,      // chart id     int   sub\_window     // number of the subwindow     int   index          // index of the indicator in the list of indicators added to the chart subwindow     ); |

Parameters

chart\_id

[in]  Chart ID. 0 denotes the current chart.

sub\_window

[in]  Number of the chart subwindow. 0 denotes the main chart subwindow.

index

[in]  the index of the indicator in the list of indicators. The numeration of indicators start with zero, i.e. the first indicator in the list has the 0 index. To obtain the number of indicators in the list use the [ChartIndicatorsTotal()](../ChartIndicatorsTotal/ChartIndicatorsTotal.md) function.

Return Value

The short name of the indicator which is set in the [INDICATOR\_SHORTNAME](../../Constants,-Enumerations-and-Structures/Indicator-Constants/Custom-Indicator-Properties/Custom-Indicator-Properties.md#enum_customind_property_string) property with the [IndicatorSetString()](../../Custom-Indicators/IndicatorSetString/IndicatorSetString.md) function. To get [error](../../Constants,-Enumerations-and-Structures/Codes-of-Errors-and-Warnings/Runtime-Errors/Runtime-Errors.md) details use the [GetLastError()](../../Checkup/GetLastError/GetLastError.md) function.

Note

Do not confuse the indicator short name and the file name that is specified when creating an indicator using functions [iCustom()](../../Technical-Indicators/iCustom/iCustom.md) and [IndicatorCreate()](../../Timeseries-and-Indicators-Access/IndicatorCreate/IndicatorCreate.md). If the short name of an indicator is not set explicitly, then the name of the file containing the source code of the indicator will be specified during compilation.

The indicator's short name should be formed correctly. It will be written to the [INDICATOR\_SHORTNAME](../../Constants,-Enumerations-and-Structures/Indicator-Constants/Custom-Indicator-Properties/Custom-Indicator-Properties.md#enum_customind_property_string) property using the [IndicatorSetString()](../../Custom-Indicators/IndicatorSetString/IndicatorSetString.md) function. It is recommended that the short name should contain values of all the input parameters of the indicator, because the indicator to be deleted from the chart by the [ChartIndicatorDelete()](../ChartIndicatorDelete/ChartIndicatorDelete.md) function is identified by the short name.

Example:

|  |
| --- |
| //+------------------------------------------------------------------+  //| Script program start function                                    |  //+------------------------------------------------------------------+  void OnStart()    {  //--- get the current chart ID and the number of its subwindows, including the main window     long chart\_id = ChartID();     int  wnd\_total= (int)ChartGetInteger(0,CHART\_WINDOWS\_TOTAL);       //--- iterate over all current chart windows in a loop     for(int w=0; w<wnd\_total; w++)       {        //--- get the number of indicators attached to the chart window specified by the loop index        int ind\_total=ChartIndicatorsTotal(chart\_id, w);                //--- print the header for the selected chart window        PrintFormat("Chart window %d indicators: ", w);                //--- get in the loop and write to the variable all the names of indicators attached to the selected window        string ind\_names="";        for(int i=0; i<ind\_total; i++)          {           ind\_names+="  "+ChartIndicatorName(chart\_id, w, i)+(i<ind\_total-1 ? "\n": "");          }        //--- print the obtained list of names of all indicators, attached to the specified chart window, in the journal        Print(ind\_names);       }     /\*     result:     Chart window 0 indicators:        AMA(9,2,30)       SAR(0.02,0.20)       Fractals     Chart window 1 indicators:        RSI(14)       AMA(9,2,30)     Chart window 2 indicators:        MFI(14)     \*/    } |

See also

[ChartIndicatorAdd()](../ChartIndicatorAdd/ChartIndicatorAdd.md), [ChartIndicatorDelete()](../ChartIndicatorDelete/ChartIndicatorDelete.md), [ChartIndicatorsTotal()](../ChartIndicatorsTotal/ChartIndicatorsTotal.md), [iCustom()](../../Technical-Indicators/iCustom/iCustom.md), [IndicatorCreate()](../../Timeseries-and-Indicators-Access/IndicatorCreate/IndicatorCreate.md), [IndicatorSetString()](../../Custom-Indicators/IndicatorSetString/IndicatorSetString.md)
