# ChartIndicatorGet

ChartIndicatorGet

Returns the handle of the indicator with the specified short name in the specified chart window.

|  |
| --- |
| int  ChartIndicatorGet(     long           chart\_id,              // Chart ID     int            sub\_window             // The number of the subwindow     const string   indicator\_shortname    // Short name of the indicator     ); |

Parameters

chart\_id

[in]  Chart ID. 0 means the current chart.

sub\_window

[in]  The number of the chart subwindow. 0 means the main chart window.

const indicator\_shortname

[in]  The short name if the indicator, which is set in the [INDICATOR\_SHORTNAME](../../Constants,-Enumerations-and-Structures/Indicator-Constants/Custom-Indicator-Properties/Custom-Indicator-Properties.md#enum_customind_property_string) property using the [IndicatorSetString()](../../Custom-Indicators/IndicatorSetString/IndicatorSetString.md) function. To get the short name of an indicator, use the [ChartIndicatorName()](../ChartIndicatorName/ChartIndicatorName.md) function.

Return Value

Returns an indicator handle if successful, otherwise returns [INVALID\_HANDLE](../../Constants,-Enumerations-and-Structures/Named-Constants/Other-Constants/Other-Constants.md). To get information about [the error](../../Constants,-Enumerations-and-Structures/Codes-of-Errors-and-Warnings/Runtime-Errors/Runtime-Errors.md), call the [GetLastError()](../../Checkup/GetLastError/GetLastError.md) function.

Note

The indicator handle obtained using the ChartIndicatorGet() function increases the internal indicator usage counter. The terminal runtime system keeps all indicators, whose counter is greater than zero, loaded. Therefore, the indicator handle that is no longer needed should be immediately and explicitly released using [IndicatorRelease()](../../Timeseries-and-Indicators-Access/IndicatorRelease/IndicatorRelease.md) in the same program that received it, as shown in the example below. Otherwise, it will be impossible to find the “abandoned” handle and release it from another program correctly.

When creating an indicator, be careful forming its short name, which is written in the [INDICATOR\_SHORTNAME](../../Constants,-Enumerations-and-Structures/Indicator-Constants/Custom-Indicator-Properties/Custom-Indicator-Properties.md#enum_customind_property_string) property using the [IndicatorSetString()](../../Custom-Indicators/IndicatorSetString/IndicatorSetString.md) function. It is recommended that a short name should contain the values of input parameters of the indicator, since the indicator is identified in the [ChartIndicatorGet()](ChartIndicatorGet.md) function based on its short name.

Another way to identify the indicator is to get a list of its parameters for a given handle using the [IndicatorParameters()](../../Timeseries-and-Indicators-Access/IndicatorParameters/IndicatorParameters.md) function and then to analyze the obtained values.

Example:

|  |
| --- |
| //+------------------------------------------------------------------+  //| Script program start function                                    |  //+------------------------------------------------------------------+  void OnStart()    {     //--- The number of windows on the chart (at least one main window is always present)     int windows=(int)ChartGetInteger(0,CHART\_WINDOWS\_TOTAL);     //--- Check all windows     for(int w=0;w<windows;w++)       {        //--- the number of indicators in this window/subwindow        int total=ChartIndicatorsTotal(0,w);        //--- Go through all indicators in the window        for(int i=0;i<total;i++)          {           //--- get the short name of an indicator           string name=ChartIndicatorName(0,w,i);           //--- get the handle of an indicator           int handle=ChartIndicatorGet(0,w,name);           //--- Add to log           PrintFormat("Window=%d,  index=%d,  name=%s,  handle=%d",w,i,name,handle);           //--- You should obligatorily release the indicator handle when it is no longer needed           IndicatorRelease(handle);          }       }    } |

See also

[ChartIndicatorAdd()](../ChartIndicatorAdd/ChartIndicatorAdd.md), [ChartIndicatorName()](../ChartIndicatorName/ChartIndicatorName.md), [ChartIndicatorsTotal()](../ChartIndicatorsTotal/ChartIndicatorsTotal.md), [IndicatorParameters()](../../Timeseries-and-Indicators-Access/IndicatorParameters/IndicatorParameters.md)
