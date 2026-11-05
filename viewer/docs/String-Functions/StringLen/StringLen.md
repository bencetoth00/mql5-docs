# StringLen


Returns the number of symbols in a string.

```cpp
int  StringLen(
   string  string_value      // string
   );
```

Parameters

string\_value

[in]  String to calculate length.

Return Value

Number of symbols in a string without the ending zero.

Example:

```cpp
void OnStart()
  {
//--- define the test string
   string text="123456789012345";
//--- get the number of symbols in the string
   int str_len=StringLen(text);
//--- display the string and the number of symbols in it in the log
   PrintFormat("The StringLen() function returned the value of %d chars in string: '%s'", str_len, text);
   /*
   Result
   The StringLen() function returned the value of 15 chars in string: '123456789012345'
   */
  }
```

See also

[StringBufferLen](../StringBufferLen/StringBufferLen.md), [StringTrimLeft](../StringTrimLeft/StringTrimLeft.md), [StringTrimRight](../StringTrimRight/StringTrimRight.md), [StringToCharArray](../../Conversion-Functions/StringToCharArray/StringToCharArray.md), [StringToShortArray](../../Conversion-Functions/StringToShortArray/StringToShortArray.md)