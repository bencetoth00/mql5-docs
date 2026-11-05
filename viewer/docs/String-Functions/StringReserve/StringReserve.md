# StringReserve


Reserves the buffer of a specified size for a string in memory.

```cpp
bool  StringReserve(
   string&    string_var,       // string
   uint       new_capacity      // buffer size for storing a string
   );
```

Parameters

string\_var

[in][out]  String the buffer size should change the size for.

new\_capacity

[in]  Buffer size required for a string. If the new\_capacity size is less than the string length, the size of the current buffer does not change.

Return Value

In case of successful execution, returns true, otherwise - false. To receive an [error](../../Constants,-Enumerations-and-Structures/Codes-of-Errors-and-Warnings/Runtime-Errors/Runtime-Errors.md) code, the [GetLastError()](../../Checkup/GetLastError/GetLastError.md) function should be called.

Note

Generally, the string size is not equal to the size of the buffer meant for storing the string. When creating a string, the appropriate buffer is usually allocated with a margin. The StringReserve() function allows managing the buffer size and specify the optimal size for future operations.

Unlike [StringInit()](../StringInit/StringInit.md), the StringReserve() function does not change the string contents and does not fill it with characters.

Example:

```cpp
void OnStart()
  {
   string s;
//--- check the operation speed without using StringReserve
   ulong t0=GetMicrosecondCount();
   for(int i=0; i< 1024; i++)
      s+=" "+(string)i;
   ulong msc_no_reserve=GetMicrosecondCount()-t0;
   s=NULL;
//--- now, let's do the same using StringReserve
   StringReserve(s,1024 * 3);
   t0=GetMicrosecondCount();
   for(int i=0; i< 1024; i++)
      s+=" "+(string)i;
   ulong msc_reserve=GetMicrosecondCount()-t0;
//--- check the time
   Print("Test with StringReserve passed for "+(string)msc_reserve+" msc");
   Print("Test without StringReserve passed for "+(string)msc_no_reserve+" msc");
/* Result
     Test with StringReserve passed for 50 msc
     Test without StringReserve passed for 121 msc
*/
  }
```

See also

[StringBufferLen](../StringBufferLen/StringBufferLen.md), [StringSetLength](../StringSetLength/StringSetLength.md), [StringInit](../StringInit/StringInit.md), [StringSetCharacter](../StringSetCharacter/StringSetCharacter.md)