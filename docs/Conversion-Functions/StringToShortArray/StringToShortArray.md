# StringToShortArray

StringToShortArray

The function symbol-wise copies a string into a specified place of an array of ushort type. It returns the number of copied elements.

|  |
| --- |
| int  StringToShortArray(     string  text\_string,     // source string     ushort& array[],         // array     int     start=0,         // starting position in the array     int     count=-1         // number of symbols     ); |

Parameters

text\_string

[in]  String to copy

array[]

[out]  Array of [ushort](../../Language-Basics/Data-Types/Integer-Types/Char,-Short,-Int-and-Long-Types/Char,-Short,-Int-and-Long-Types.md#ushort) type (analog of wchar\_t type).

start=0

[in]  Position, from which copying starts. Default - 0.

count=-1

[in]  Number of array elements to copy. Defines length of a resulting string. Default value is -1, which means copying up to the array end, or till terminal 0.Terminal 0 will also be copied to the recipient array, in this case the size of a dynamic array can be increased if necessary to the size of the string. If the size of the dynamic array exceeds the length of the string, the size of the array will not be reduced.

Return Value

Number of copied elements.

 

Example:

|  |
| --- |
| //+------------------------------------------------------------------+  //| Script program start function                                    |  //+------------------------------------------------------------------+  void OnStart()    {  //--- string with chars to convert     string text = "Chars: ❤♫☎✈✣☏☀✉☆☁♕♠®✧❆♣   ";     ushort short\_array[];  //--- find the position of the ":" character in the input string and extract the substring starting from the next character     int    pos=StringFind(text, ":");     string str=(pos<0 ? text : StringSubstr(text, pos+1));  //--- remove spaces, carriage movement and tabulation characters from the left and right of the resulting string     StringTrimLeft(str);     StringTrimRight(str);  //--- copy the resulting string into the ushort array and print the resulting array to the journal     int copied=StringToShortArray(str, short\_array);     PrintFormat("String of characters length: %u\n"                 "Number of characters copied (with terminal 0): %d\n"                 "Array of chars for the string '%s':",                 StringLen(str), copied, str);     ArrayPrint(short\_array, 0, " | ");     /\*     result:     String of characters length: 16     Number of characters copied (with terminal 0): 17     Array of chars for the string '❤♫☎✈✣☏☀✉☆☁♕♠®✧❆♣':     10084 |  9835 |  9742 |  9992 | 10019 |  9743 |  9728 |  9993 |  9734 |  9729 |  9813 |  9824 |   174 | 10023 | 10054 |  9827 |     0     \*/    } |

See also

[ShortArrayToString](../ShortArrayToString/ShortArrayToString.md), [StringToCharArray](../StringToCharArray/StringToCharArray.md), [Use of a Codepage](../../Constants,-Enumerations-and-Structures/Input-Output-Constants/Use-of-a-Codepage/Use-of-a-Codepage.md)
