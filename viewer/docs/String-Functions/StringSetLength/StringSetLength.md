# StringSetLength


Sets a specified length (in characters) for a string.

```cpp
bool  StringSetLength(
   string&    string_var,      // string
   uint       new_length       // new string length
   );
```

Parameters

string\_var

[in][out]  String, for which a new length in characters should be set.

new\_capacity

[in]  Required string length in characters. If new\_length is less than the current size, the excessive characters are discarded.

Return Value

In case of successful execution, returns true, otherwise - false. To receive an [error](../../Constants,-Enumerations-and-Structures/Codes-of-Errors-and-Warnings/Runtime-Errors/Runtime-Errors.md) code, the [GetLastError()](../../Checkup/GetLastError/GetLastError.md) function should be called.

Note

TheStringSetLength() function does not change the size of the buffer allocated for a string.

Example:

```cpp
void OnStart()
  {
//--- define the string
   string text="123456789012345";
//--- display a string and its length in the log
   PrintFormat("Before StringSetLength() the string '%s' has a size of %d characters", text, StringLen(text));
//--- reduce the string size to 10 characters
   StringSetLength(text, 10);
//--- display a string, changed due to StringSetLength() operation, and its new length to the log
   PrintFormat("After StringSetLength() the string is now '%s', and has a size of %d characters", text, StringLen(text));
   /*
   Result
   Before StringSetLength() the string '123456789012345' has a size of 15 characters
   After StringSetLength() the string is now '1234567890', and has a size of 10 characters
   */
  }
```

See also

[StringLen](../StringLen/StringLen.md), [StringBufferLen](../StringBufferLen/StringBufferLen.md), [StringReserve](../StringReserve/StringReserve.md) [StringInit](../StringInit/StringInit.md), [StringSetCharacter](../StringSetCharacter/StringSetCharacter.md)