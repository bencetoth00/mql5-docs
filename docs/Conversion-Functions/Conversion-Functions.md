# Conversion Functions

Conversion Functions

This is a group of functions that provide conversion of data from one format into another.

The [NormalizeDouble()](NormalizeDouble/NormalizeDouble.md) function must be specially noted as it provides the necessary accuracy of the price presentation. In trading operations, no unnormalized prices may be used if their accuracy even a digit exceeds that required by the trade server.

| Function | Action |
| --- | --- |
| [CharToString](CharToString/CharToString.md) | Converting a symbol code into a one-character string |
| [DoubleToString](DoubleToString/DoubleToString.md) | Converting a numeric value to a text line with a specified accuracy |
| [EnumToString](EnumToString/EnumToString.md) | Converting an enumeration value of any type to string |
| [NormalizeDouble](NormalizeDouble/NormalizeDouble.md) | Rounding of a floating point number to a specified accuracy |
| [StringToDouble](StringToDouble/StringToDouble.md) | Converting a string containing a symbol representation of number into number of double type |
| [StringToInteger](StringToInteger/StringToInteger.md) | Converting a string containing a symbol representation of number into number of long type |
| [StringToTime](StringToTime/StringToTime.md) | Converting a string containing time or date in "yyyy.mm.dd [hh:mi]" format into datetime type |
| [TimeToString](TimeToString/TimeToString.md) | Converting a value containing time in seconds elapsed since 01.01.1970 into a string of "yyyy.mm.dd hh:mi" format |
| [IntegerToString](IntegerToString/IntegerToString.md) | Converting int into a string of preset length |
| [ShortToString](ShortToString/ShortToString.md) | Converting symbol code (unicode) into one-symbol string |
| [ShortArrayToString](ShortArrayToString/ShortArrayToString.md) | Copying array part into a string |
| [StringToShortArray](StringToShortArray/StringToShortArray.md) | Symbol-wise copying a string to a selected part of array of ushort type |
| [CharArrayToString](CharArrayToString/CharArrayToString.md) | Converting symbol code (ansi) into one-symbol array |
| [StringToCharArray](StringToCharArray/StringToCharArray.md) | Symbol-wise copying a string converted from Unicode to ANSI, to a selected place of array of uchar type |
| [CharArrayToStruct](CharArrayToStruct/CharArrayToStruct.md) | Copy uchar type array to [POD structure](../Language-Basics/Data-Types/Structures,-Classes-and-Interfaces/Structures,-Classes-and-Interfaces.md#simple_structure) |
| [StructToCharArray](StructToCharArray/StructToCharArray.md) | Copy [POD structure](../Language-Basics/Data-Types/Structures,-Classes-and-Interfaces/Structures,-Classes-and-Interfaces.md#simple_structure) to uchar type array |
| [ColorToARGB](ColorToARGB/ColorToARGB.md) | Converting color type to uint type to receive ARGB representation of the color. |
| [ColorToPRGB](ColorToPRGB/ColorToPRGB.md) | Converts the type [color](../Language-Basics/Data-Types/Integer-Types/Color-Type/Color-Type.md) in type [uint](../Language-Basics/Data-Types/Integer-Types/Char,-Short,-Int-and-Long-Types/Char,-Short,-Int-and-Long-Types.md#uint) to get premultiplied ARGB representation of color - PRGB. |
| [ColorToString](ColorToString/ColorToString.md) | Converting color value into string as "R,G,B" |
| [StringToColor](StringToColor/StringToColor.md) | Converting "R,G,B" string or string with color name into color type value |
| [StringFormat](StringFormat/StringFormat.md) | Converting number into string according to preset format |

See also

[Use of a Codepage](../Constants,-Enumerations-and-Structures/Input-Output-Constants/Use-of-a-Codepage/Use-of-a-Codepage.md)
