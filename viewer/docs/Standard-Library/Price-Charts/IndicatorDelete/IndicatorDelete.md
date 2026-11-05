# IndicatorDelete


Removes an indicator with a specified name from the specified chart window.

```cpp
bool  IndicatorDelete(
   int            sub_win       // number of the subwindow
   const string   name          // short name of the indicator
   );
```

Parameters

sub\_win

[in]  Number of the chart subwindow. 0 denotes the main chart subwindow.

const name

[in]  The short name of the indicator which is set in the [INDICATOR\_SHORTNAME](../../../Constants,-Enumerations-and-Structures/Indicator-Constants/Custom-Indicator-Properties/Custom-Indicator-Properties.md#enum_customind_property_string) property with the [IndicatorSetString()](../../../Custom-Indicators/IndicatorSetString/IndicatorSetString.md) function. To get the short name of an indicator, use the [IndicatorName()](../IndicatorName/IndicatorName.md) function.

Return Value

Returns true in case of successful deletion of the indicator. Otherwise it returns false. To get [error](../../../Constants,-Enumerations-and-Structures/Codes-of-Errors-and-Warnings/Runtime-Errors/Runtime-Errors.md) details, use the [GetLastError()](../../../Checkup/GetLastError/GetLastError.md) function.

Note

If two indicators with identical short names exist in the chart subwindow, the first one in a row will be deleted.

If other indicators on this chart are based on the values of the indicator that is being deleted, such indicators will also be deleted.

Do not confuse the indicator short name and the file name that is specified when creating an indicator using functions [iCustom()](../../../Technical-Indicators/iCustom/iCustom.md) and [IndicatorCreate()](../../../Timeseries-and-Indicators-Access/IndicatorCreate/IndicatorCreate.md). If the short name of an indicator is not set explicitly, then the name of the file containing the source code of the indicator will be specified during compilation.

Deletion of an indicator from a chart does not mean that its calculation part will be deleted from the terminal memory. To release the indicator handle, use the [IndicatorRelease()](../../../Timeseries-and-Indicators-Access/IndicatorRelease/IndicatorRelease.md) function.

The indicator's short name should be formed correctly. It will be written to the [INDICATOR\_SHORTNAME](../../../Constants,-Enumerations-and-Structures/Indicator-Constants/Custom-Indicator-Properties/Custom-Indicator-Properties.md#enum_customind_property_string) property using the [IndicatorSetString()](../../../Custom-Indicators/IndicatorSetString/IndicatorSetString.md) function. It is recommended that the short name should contain values of all the input parameters of the indicator, because the indicator to be deleted from the chart by the [IndicatorDelete()](IndicatorDelete.md) function is identified by the short name.

See also

[IndicatorAdd()](../IndicatorAdd/IndicatorAdd.md), [IndicatorsTotal()](../IndicatorsTotal/IndicatorsTotal.md), [IndicatorName()](../IndicatorName/IndicatorName.md), [iCustom()](../../../Technical-Indicators/iCustom/iCustom.md), [IndicatorCreate()](../../../Timeseries-and-Indicators-Access/IndicatorCreate/IndicatorCreate.md), [IndicatorSetString()](../../../Custom-Indicators/IndicatorSetString/IndicatorSetString.md).