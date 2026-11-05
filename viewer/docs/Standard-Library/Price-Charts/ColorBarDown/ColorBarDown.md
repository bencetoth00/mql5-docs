# ColorBarDown

# ColorBarDown (Get Method)

Gets the value of "ColorBarDown" property (color for bearish bars, their shadow, and candle body outlines).

```cpp
color  ColorBarDown() const
```

Return Value

Value of "ColorBarDown" property of the chart assigned to the class instance. If there is no chart assigned, it returns [CLR\_NONE](../../../Constants,-Enumerations-and-Structures/Named-Constants/Other-Constants/Other-Constants.md).

# ColorBarDown (Set Method)

Sets new value for "ColorBarDown" property.

```cpp
bool  ColorBarDown(
   color  new_color      // color
   )
```

Parameters

new\_color

[in]  New color for bearish bars, their shadow, and candle body outlines.

Return Value

true - successful, false - cannot change the color.