# StringToColor

StringToColor

Converting "R,G,B" string or string with color name into color type value.

|  |
| --- |
| color  StringToColor(     string  color\_string      // string representation of color     ); |

Parameters

color\_string

[in]  String representation of a color of "R,G,B" type or name of one of predefined [Web-colors](../../Constants,-Enumerations-and-Structures/Objects-Constants/Web-Colors/Web-Colors.md).

Return Value

Color value.

 

Example:

|  |
| --- |
| color str\_color=StringToColor("0,127,0");     Print(str\_color);     Print((string)str\_color);  //--- change color a little     str\_color=StringToColor("0,128,0");     Print(str\_color);     Print((string)str\_color); |

See also

[ColorToString](../ColorToString/ColorToString.md), [ColorToARGB](../ColorToARGB/ColorToARGB.md)
