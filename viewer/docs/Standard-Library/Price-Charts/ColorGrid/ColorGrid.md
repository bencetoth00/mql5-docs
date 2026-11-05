# ColorGrid

# ColorGrid (Get Method)

Gets the value of "ColorGrid" property (color of the grid).

```cpp
color  ColorGrid() const
```

Return Value

Value of "ColorGrid" property of the chart assigned to the class instance. If there is no chart assigned, it returns [CLR\_NONE](../../../Constants,-Enumerations-and-Structures/Named-Constants/Other-Constants/Other-Constants.md).

# ColorGrid (Set Method)

Sets new value for "ColorGrid" property.

```cpp
bool  ColorGrid(
   color  new_color      // color
   )
```

Parameters

new\_color

[in]  New grid color.

Return Value

true - successful, false - cannot change the color.