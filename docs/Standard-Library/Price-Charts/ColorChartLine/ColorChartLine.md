# ColorChartLine

ColorChartLine (Get Method)

Gets the value of "ColorChartLine" property (color for line chart and Doji candles).

|  |
| --- |
| color  ColorChartLine() const |

Return Value

Value of "ColorChartLine" property of the chart assigned to the class instance. If there is no chart assigned, it returns [CLR\_NONE](../../../Constants,-Enumerations-and-Structures/Named-Constants/Other-Constants/Other-Constants.md).

ColorChartLine (Set Method)

Sets new value for "ColorChartLine" property.

|  |
| --- |
| bool  ColorChartLine(     color  new\_color      // color     ) |

Parameters

new\_color

[in]  New color of the chart lines and Doji candles.

Return Value

true - successful, false - cannot change the color.
