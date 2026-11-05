# StringToColor


Converting "R,G,B" string or string with color name into color type value.

```cpp
color  StringToColor(
   string  color_string      // string representation of color
   );
```

Parameters

color\_string

[in]  String representation of a color of "R,G,B" type or name of one of predefined [Web-colors](../../Constants,-Enumerations-and-Structures/Objects-Constants/Web-Colors/Web-Colors.md).

Return Value

Color value.

 

Example:

```cpp
   color str_color=StringToColor("0,127,0");
   Print(str_color);
   Print((string)str_color);
//--- change color a little
   str_color=StringToColor("0,128,0");
   Print(str_color);
   Print((string)str_color);
```

See also

[ColorToString](../ColorToString/ColorToString.md), [ColorToARGB](../ColorToARGB/ColorToARGB.md)