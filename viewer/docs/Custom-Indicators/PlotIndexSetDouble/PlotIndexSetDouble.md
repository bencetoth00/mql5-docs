# PlotIndexSetDouble


The function sets the value of the corresponding property of the corresponding indicator line. The indicator property must be of the double type.

```cpp
bool  PlotIndexSetDouble(
   int     plot_index,     // plotting style index
   int     prop_id,        // property identifier
   double  prop_value      // value to be set
   );
```

Parameters

plot\_index

[in]  Index of the [graphical plotting](../../Constants,-Enumerations-and-Structures/Indicator-Constants/Drawing-Styles/Drawing-Styles.md#enum_draw_type)

prop\_id

[in] The value can be one of the values of the [ENUM\_PLOT\_PROPERTY\_DOUBLE](../../Constants,-Enumerations-and-Structures/Indicator-Constants/Drawing-Styles/Drawing-Styles.md#enum_plot_property_double) enumeration.

prop\_value

[in]  The value of the property.

Return Value

If successful, returns [true](../../Language-Basics/Data-Types/Integer-Types/Bool-Type/Bool-Type.md), otherwise [false](../../Language-Basics/Data-Types/Integer-Types/Bool-Type/Bool-Type.md).