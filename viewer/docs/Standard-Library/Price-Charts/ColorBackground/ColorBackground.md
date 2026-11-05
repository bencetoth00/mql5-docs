# ColorBackground

# ColorBackground (Get Method)

Gets the value of "ColorBackground" property (background color of the chart).

```cpp
color  ColorBackground() const
```

Return Value

Value of "ColorBackground" property of the chart assigned to the class instance. If there is no chart assigned, it returns [CLR\_NONE](../../../Constants,-Enumerations-and-Structures/Named-Constants/Other-Constants/Other-Constants.md).

# ColorBackground (Set Method)

Sets new value for "ColorBackground" property.

```cpp
bool  ColorBackground(
   color  new_color      // color
   )
```

Parameters

new\_color

[in]  New background color.

Return Value

true - successful, false - cannot change the color.