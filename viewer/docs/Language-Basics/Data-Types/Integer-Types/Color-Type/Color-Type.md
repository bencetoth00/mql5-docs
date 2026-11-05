# Color Type


The color type is intended for storing information about color and occupies 4 bytes in memory. The first byte is ignored, the remaining 3 bytes contain the RGB-components.

Color constants can be represented in three ways: literally, by integers, or by name (for named [Web-colors](../../../../Constants,-Enumerations-and-Structures/Objects-Constants/Web-Colors/Web-Colors.md) only).

Literal representation consists of three parts representing numerical rate values of the three main color components: red, green, blue. The constant starts with C and is enclosed in single quotes. Numerical rate values of a color component lie in the range from 0 to 255.

Integer-valued representation is written in a form of hexadecimal or a decimal number. A hexadecimal number looks like 0x00BBGGRR, where RR is the rate of the red color component, GG - of the green one, and BB - of the blue one. Decimal constants are not directly reflected in the RGB. They represent a decimal value of the hexadecimal integer representation.

Specific colors reflect the so-called [Web-colors](../../../../Constants,-Enumerations-and-Structures/Objects-Constants/Web-Colors/Web-Colors.md) set.

Examples:

```cpp
//--- Literals
C'128,128,128'    // Gray
C'0x00,0x00,0xFF' // Blue
//color names
clrRed               // Red
clrYellow            // Yellow
clrBlack             // Black
//--- Integral representations
0xFFFFFF          // White
16777215          // White
0x008000          // Green
32768             // Green
```

See also

[Web Colors](../../../../Constants,-Enumerations-and-Structures/Objects-Constants/Web-Colors/Web-Colors.md), [ColorToString](../../../../Conversion-Functions/ColorToString/ColorToString.md), [StringToColor](../../../../Conversion-Functions/StringToColor/StringToColor.md), [Typecasting](../../Typecasting/Typecasting.md)