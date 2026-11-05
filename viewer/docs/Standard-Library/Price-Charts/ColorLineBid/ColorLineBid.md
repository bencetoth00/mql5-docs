# ColorLineBid

# ColorLineBid (Get Method)

Gets the value of "ColorLineBid" property (color of Bid line).

```cpp
color  ColorLineBid() const
```

Return Value

Value of "ColorLineBid" property of the chart assigned to the class instance. If there is no chart assigned, it returns [CLR\_NONE](../../../Constants,-Enumerations-and-Structures/Named-Constants/Other-Constants/Other-Constants.md).

# ColorLineBid (Set Method)

Sets new value for "ColorLineBid" property.

```cpp
bool  ColorLineBid(
   color  new_color      // color
   )
```

Parameters

new\_color

[in]  New color for Bid line.

Return Value

true - successful, false - cannot change the color.