# String Type


The string type is used for storing text strings. A text string is a sequence of characters in the Unicode format with the final zero at the end of it. A string constant can be assigned to a string variable. A string constant is a sequence of Unicode characters enclosed in double quotes: "This is a string constant".

If you need to include a double quote (") into a string, the backslash character (\) must be put before it. Any special [character constants](../Integer-Types/Character-Constants/Character-Constants.md) can be written in a string, if the backslash character (\) is typed before them.

Examples:

```cpp
string svar="This is a character string";
string svar2=StringSubstr(svar,0,4);
Print("Copyright symbol\t\x00A9");
FileWrite(handle,"This string contains a new line symbols \n");
string MT5path="C:\\Program Files\\MetaTrader 5";
```

 

To make the source code readable, long constant strings can be split into parts without addition operation. During compilation, these parts will be combined into one long string:

```cpp
//--- Declare a long constant string
   string HTML_head="<!DOCTYPE html PUBLIC \"-//W3C//DTD XHTML 1.0 Transitional//EN\""
                    " \"http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd\">\n"
                    "<html xmlns=\"http://www.w3.org/1999/xhtml\">\n"
                    "<head>\n"
                    "<meta http-equiv=\"Content-Type\" content=\"text/html; charset=utf-8\" />\n"
                    "<title>Trade Operations Report</title>\n"
                    "</head>";
//--- Output the constant string into log
   Print(HTML_head);
  }
```

 

## Built-in string type methods

Strings can be handled by [string functions](../../../String-Functions/String-Functions.md), conversion functions and built-in methods of string type provided in the table:

| String method | Analog | Description |
| --- | --- | --- |
| Constructor string(const int len) |  | Constructs a string of a specified |
| string[] length both for reading and writing. The index should be within BufferSize() |  | Provides access to the string element by a specified index |
| static string string.Init(const int len, const ushort character); | [StringInit](../../../String-Functions/StringInit/StringInit.md) | Initializes a string using specified symbols with a specified size |
| void string.Fill(const ushort character); | [StringFill](../../../String-Functions/StringFill/StringFill.md) | Fills in the string with a specified symbol |
| int string.Len(); | [StringLen](../../../String-Functions/StringLen/StringLen.md) | Returns the number of characters in a string |
| int string.BufferSize(); | [StringBufferLen](../../../String-Functions/StringBufferLen/StringBufferLen.md) | Returns the size of a buffer distributed for a string |
| bool string.SetLen(const int new\_len); | [StringSetLength](../../../String-Functions/StringSetLength/StringSetLength.md) | Sets a specified length (in characters) for a string |
| bool string.Reserve(const int buffer\_len); | [StringReserve](../../../String-Functions/StringReserve/StringReserve.md) | Reserves the buffer of a specified size for a string in memory |
| bool string.Add(const string substring); | [StringAdd](../../../String-Functions/StringAdd/StringAdd.md) | Adds a specified substring to the end |
| int string.Concatenate(const scalar val1, const scalar val2...); | [StringConcatenate](../../../String-Functions/StringConcatenate/StringConcatenate.md) | Forms a string consisting of passed parameters |
| array string.Split(const ushort separator, const bool long\_separator); | [StringSplit](../../../String-Functions/StringSplit/StringSplit.md) | Returns a string array by a specified separator |
| int string.Compare(const string str, const bool case\_sensivity); | [StringCompare](../../../String-Functions/StringCompare/StringCompare.md) | Compares with a specified string and returns 1 if the first string exceeds the second one; 0 - if the strings are equal; -1 (minus one) - if the first string is less than the second one |
| string string.Substr(const int start\_pos, const int len); | [StringSubstr](../../../String-Functions/StringSubstr/StringSubstr.md) | Retrieves a substring from a specified position |
| int string.Find(const string substr, const int pos); | [StringFind](../../../String-Functions/StringFind/StringFind.md) | Returns an index of the position the necessary substring starts from |
| void string.ToLower(); | [StringToLower](../../../String-Functions/StringToLower/StringToLower.md) | Converts all characters to lower case |
| void string.ToUpper(); | [StringToUpper](../../../String-Functions/StringToUpper/StringToUpper.md) | Converts all characters to upper case |
| int string.TrimLeft(); | [StringTrimLeft](../../../String-Functions/StringTrimLeft/StringTrimLeft.md) | Deletes spaces, as well as carriage movement and tabulation characters to the left |
| int string.TrimRight() | [StringTrimRight](../../../String-Functions/StringTrimRight/StringTrimRight.md) | Deletes spaces, as well as carriage movement and tabulation characters to the right |
| void string.Double(const double var, const int digits=8); | [DoubleToString](../../../Conversion-Functions/DoubleToString/DoubleToString.md) | Converts a string to a [double](../Real-Types-(double,-float)/Real-Types-(double,-float).md) type number |
| void string.Enum(const enum value); | [EnumToString](../../../Conversion-Functions/EnumToString/EnumToString.md) | Converts the enumeration value of any type into a string |
| void string.Integer(const int value, const int str\_len=0, const ushort fill=' '); | [IntegerToString](../../../Conversion-Functions/IntegerToString/IntegerToString.md) | Converts a string to a [long](../Integer-Types/Char,-Short,-Int-and-Long-Types/Char,-Short,-Int-and-Long-Types.md#long) type number |
| void string.CharArray(const uchar array[], const int start\_pos=0, const int len=-1, const uint cp=CP\_ACP); | [CharArrayToString](../../../Conversion-Functions/CharArrayToString/CharArrayToString.md) | Converts part of the [uchar](../Integer-Types/Char,-Short,-Int-and-Long-Types/Char,-Short,-Int-and-Long-Types.md#uchar) type array to a string |
| void string.ShortArray(const ushort array[], const int start\_pos=0, const int len=-1); | [ShortArrayToString](../../../Conversion-Functions/ShortArrayToString/ShortArrayToString.md) | Copies part of the [ushort](../Integer-Types/Char,-Short,-Int-and-Long-Types/Char,-Short,-Int-and-Long-Types.md#ushort) type array to a string |
| void string.Time(const datetime dt,const int mode=TIME\_DATE|TIME\_MINUTES); | [TimeToString](../../../Conversion-Functions/TimeToString/TimeToString.md) | Converts [datetime](../Integer-Types/Datetime-Type/Datetime-Type.md) to the "yyyy.mm.dd hh:mi" format string. |
| void string.Format(const string format\_str); | [StringFormat](../../../Conversion-Functions/StringFormat/StringFormat.md) | Formats the obtained parameters into a string |

 

See also

[Conversion Functions](../../../Conversion-Functions/Conversion-Functions.md), [String Functions](../../../String-Functions/String-Functions.md), [FileOpen](../../../File-Functions/FileOpen/FileOpen.md), [FileReadString](../../../File-Functions/FileReadString/FileReadString.md), [FileWriteString](../../../File-Functions/FileWriteString/FileWriteString.md)