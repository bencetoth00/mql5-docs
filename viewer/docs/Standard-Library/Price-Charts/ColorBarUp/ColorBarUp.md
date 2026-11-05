# ColorBarUp

# ColorBarUp (Get Method)

Gets the value of "ColorBarUp" property (color for bullish bars, their shadow, and candle body outlines).

```cpp
color  ColorBarUp() const
```

Return Value

Value of "ColorBarUp" property of the chart assigned to the class instance. If there is no chart assigned, it returns [CLR\_NONE](../../../Constants,-Enumerations-and-Structures/Named-Constants/Other-Constants/Other-Constants.md).

# ColorBarUp (Set Method)

Sets new value for "ColorBarUp" property.

```cpp
bool  ColorBarUp(
   color  new_color      // color
   )
```

Parameters

new\_color

[in]  New color for bullish bars, their shadow and candle body outlines.

Return Value

true - successful, false - cannot change the color.