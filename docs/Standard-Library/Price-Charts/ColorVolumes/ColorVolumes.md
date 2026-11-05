# ColorVolumes

ColorVolumes (Get Method)

Gets the value of "ColorVolumes" property (color for volumes and levels of opened positions).

|  |
| --- |
| color  ColorVolumes() const |

Return Value

Value of "ColorVolumes" property of the chart assigned to the class instance. If there is no chart assigned, it returns [CLR\_NONE](../../../Constants,-Enumerations-and-Structures/Named-Constants/Other-Constants/Other-Constants.md).

ColorVolumes (Set Method)

Sets new value for "ColorVolumes" property.

|  |
| --- |
| bool  ColorVolumes(     color  new\_color      // color     ) |

Parameters

new\_color

[in]  New color of the volumes and open position levels.

Return Value

true - successful, false - cannot change the color.
