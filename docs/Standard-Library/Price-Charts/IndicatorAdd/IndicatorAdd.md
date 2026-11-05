# IndicatorAdd

IndicatorAdd

Adds an indicator with the specified handle into a specified chart window.

|  |
| --- |
| bool  IndicatorAdd(     int   sub\_win         // number of the subwindow     int   handle          // handle of the indicator     ); |

Parameters

sub\_win

[in]  The number of the chart subwindow. 0 means the main chart window. if the number of a non-existing window is specified, a new window will be created.

handle

[in]  The handle of the indicator.

Return Value

The function returns true in case of success, otherwise it returns false. In order to obtain information about the [error](../../../Constants,-Enumerations-and-Structures/Codes-of-Errors-and-Warnings/Runtime-Errors/Runtime-Errors.md), call the [GetLastError()](../../../Checkup/GetLastError/GetLastError.md) function.

See also

[IndicatorDelete()](../IndicatorDelete/IndicatorDelete.md), [IndicatorsTotal()](../IndicatorsTotal/IndicatorsTotal.md), [IndicatorName()](../IndicatorName/IndicatorName.md).
