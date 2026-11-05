# StringSetCharacter

StringSetCharacter

Returns copy of a string with a changed character in a specified position.

|  |
| --- |
| bool  StringSetCharacter(     string&   string\_var,       // string     int       pos,              // position     ushort    character         // character     ); |

Parameters

string\_var

[in][out]  String.

pos

[in]  Position of a character in a string. Can be from 0 to [StringLen](../StringLen/StringLen.md)(text).

character

[in]  Symbol code Unicode.

Return Value

In case of success returns true, otherwise false. In order to get an [error code](../../Constants,-Enumerations-and-Structures/Codes-of-Errors-and-Warnings/Runtime-Errors/Runtime-Errors.md), the [GetLastError()](../../Checkup/GetLastError/GetLastError.md) function should be called.

Note

If pos is less than [string length](../StringLen/StringLen.md) and the symbol code value = 0, the string is cut off (but the [buffer size](../StringBufferLen/StringBufferLen.md), distributed for the string remains unchanged). The string length becomes equal to pos.

If pos is equal to string length, the specified symbol is added at the string end, and the length is enlarged by one.

Example:

|  |
| --- |
| void OnStart()    {     string str="0123456789";     Print("before: str = ",str,",StringBufferLen(str) = ",           StringBufferLen(str),"  StringLen(str) = ",StringLen(str));  //--- add zero value in the middle     StringSetCharacter(str,6,0);     Print("after: str = ",str,",StringBufferLen(str) = ",           StringBufferLen(str),"  StringLen(str) = ",StringLen(str));  //--- add symbol at the end     int size=StringLen(str);     StringSetCharacter(str,size,'+');     Print("addition: str = ",str,",StringBufferLen(str) = ",           StringBufferLen(str),"  StringLen(str) = ",StringLen(str));    }  /\* Result     before: str = 0123456789 ,StringBufferLen(str) = 0   StringLen(str) = 10     after:  str = 012345 ,StringBufferLen(str) = 16   StringLen(str) = 6     addition: str = 012345+ ,StringBufferLen(str) = 16   StringLen(str) = 7  \*/ |

See also

[StringBufferLen](../StringBufferLen/StringBufferLen.md), [StringLen](../StringLen/StringLen.md), [StringFill](../StringFill/StringFill.md), [StringInit](../StringInit/StringInit.md), [CharToString](../../Conversion-Functions/CharToString/CharToString.md), [ShortToString](../../Conversion-Functions/ShortToString/ShortToString.md), [CharArrayToString](../../Conversion-Functions/CharArrayToString/CharArrayToString.md), [ShortArrayToString](../../Conversion-Functions/ShortArrayToString/ShortArrayToString.md)
