# PlotIndexSetString

PlotIndexSetString

The function sets the value of the corresponding property of the corresponding indicator line. The indicator property must be of the string type.

|  |
| --- |
| bool  PlotIndexSetString(     int     plot\_index,     // plotting style index     int     prop\_id,        // property identifier     string  prop\_value      // value to be set     ); |

Parameters

plot\_index

[in]  Index of [graphical plot](../../Constants,-Enumerations-and-Structures/Indicator-Constants/Drawing-Styles/Drawing-Styles.md#enum_draw_type)

prop\_id

[in] The value can be one of the values of the [ENUM\_PLOT\_PROPERTY\_STRING](../../Constants,-Enumerations-and-Structures/Indicator-Constants/Drawing-Styles/Drawing-Styles.md#enum_plot_property_string) enumeration.

prop\_value

[in]  The value of the property.

Return Value

If successful, returns [true](../../Language-Basics/Data-Types/Integer-Types/Bool-Type/Bool-Type.md), otherwise [false](../../Language-Basics/Data-Types/Integer-Types/Bool-Type/Bool-Type.md).
