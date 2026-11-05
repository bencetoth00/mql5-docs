# ColorStopLevels

ColorStopLevels (Get Method)

Gets the value of "ColorStopLevels" property (color of the SL and TP levels).

|  |
| --- |
| color  ColorStopLevels() const |

Return Value

Value of "ColorStopLevels" property of the chart assigned to the class instance. If there is no chart assigned, it returns [CLR\_NONE](../../../Constants,-Enumerations-and-Structures/Named-Constants/Other-Constants/Other-Constants.md).

ColorStopLevels (Set Method)

Sets new value for "ColorStopLevels" property.

|  |
| --- |
| bool  ColorStopLevels(     color  new\_color      // color     ) |

Parameters

new\_color

[in]  New color of the Stop Loss and Take Profit price levels.

Return Value

true - successful, false - cannot change the color.
