# IndicatorsTotal


Returns the number of all indicators applied to the specified chart window.

```cpp
int  IndicatorsTotal(
   long   chart_id,  // chart identifier
   int    sub_win    // number of the subwindow
   );
```

Parameters

chart\_id

[in]  Chart identifier. 0 denotes the main chart.

sub\_win

[in]  Number of the chart subwindow. 0 denotes the main chart window.

Return Value

The number of indicators in the specified chart window. To get [error](../../../Constants,-Enumerations-and-Structures/Codes-of-Errors-and-Warnings/Runtime-Errors/Runtime-Errors.md) details, use the [GetLastError()](../../../Checkup/GetLastError/GetLastError.md) function.

Note

The function allows going searching through all the indicators attached to the chart. The number of all the windows of the chart can be obtained from the [CHART\_WINDOWS\_TOTAL](../../../Constants,-Enumerations-and-Structures/Chart-Constants/Chart-Properties/Chart-Properties.md#enum_chart_property_integer) property using the [GetInteger()](../GetInteger/GetInteger.md) function.

See also

[IndicatorAdd()](../IndicatorAdd/IndicatorAdd.md), [IndicatorDelete()](../IndicatorDelete/IndicatorDelete.md), [IndicatorsTotal()](IndicatorsTotal.md), [iCustom()](../../../Technical-Indicators/iCustom/iCustom.md), [IndicatorCreate()](../../../Timeseries-and-Indicators-Access/IndicatorCreate/IndicatorCreate.md), [IndicatorSetString()](../../../Custom-Indicators/IndicatorSetString/IndicatorSetString.md).