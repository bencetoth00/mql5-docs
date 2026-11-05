# ColorLineLast

# ColorLineLast (Get Method)

Gets the value of "ColorLineLast" property (color of the last deal price line).

```cpp
color  ColorLineLast() const
```

Return Value

Value of "ColorLineLast" property of the chart assigned to the class instance. If there is no chart assigned, it returns [CLR\_NONE](../../../Constants,-Enumerations-and-Structures/Named-Constants/Other-Constants/Other-Constants.md).

# ColorLineLast (Set Method)

Sets new value for "ColorLineLast" property.

```cpp
bool  ColorLineLast(
   color  new_color      // color
   )
```

Parameters

new\_color

[in]  New color of the last deal price line.

Return Value

true - successful, false - cannot change the color.