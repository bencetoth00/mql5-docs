# ColorCandleBull

# ColorCandleBull (Get Method)

Gets the value of "ColorCandleBull" property (body color of the bullish candle).

```cpp
color  ColorCandleBull() const
```

Return Value

Value of "ColorCandleBull" property of the chart assigned to the class instance. If there is no chart assigned, it returns [CLR\_NONE](../../../Constants,-Enumerations-and-Structures/Named-Constants/Other-Constants/Other-Constants.md).

# ColorCandleBull (Set Method)

Sets new value for "ColorCandleBull" property.

```cpp
bool  ColorCandleBull(
   color  new_color      // color
   )
```

Parameters

new\_color

[in]  New color of the bullish candle body.

Return Value

true - successful, false - cannot change the color.