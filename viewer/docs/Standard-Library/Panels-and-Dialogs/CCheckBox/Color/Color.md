# Color

# Color (Get method)

Gets color of the label associated with the control.

```cpp
color  Color()  const
```

Return Value

Label color.

 

# Color (Set method)

Sets color of the label associated with the control.

```cpp
bool  Color(
   const color  value      // color
   )
```

Parameters

value

[in]  New label color.

Return Value

true - successful, otherwise - false.

Note

Label color is specified by setting [OBJPROP\_COLOR](../../../../Constants,-Enumerations-and-Structures/Objects-Constants/Object-Properties/Object-Properties.md#enum_object_property_integer) (color) of a chart object.