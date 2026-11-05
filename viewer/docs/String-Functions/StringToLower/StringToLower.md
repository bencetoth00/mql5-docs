# StringToLower


Transforms all symbols of a selected string into lowercase.

```cpp
bool  StringToLower(
   string&  string_var      // string to process
   );
```

Parameters

string\_var

[in][out]  String.

Return Value

In case of success returns true, otherwise - false. To get the [error code](../../Constants,-Enumerations-and-Structures/Codes-of-Errors-and-Warnings/Runtime-Errors/Runtime-Errors.md) call [GetLastError()](../../Checkup/GetLastError/GetLastError.md).

Example:

```cpp
void OnStart()
  {
//--- define the source string in uppercase
   string text=" - THIS STRING, WRITTEN IN UPPERCASE, MUST BE WRITTEN IN LOWERCASE";
//--- Display the source string in the log
   Print("Source line:\n", text);
//--- convert all string characters to lowercase and display the result in the log
   if(StringToLower(text))
      Print("The original string after using the StringToLower() function:\n", text);
   /*
   Result
   Source line:
    - THIS STRING, WRITTEN IN UPPERCASE, MUST BE WRITTEN IN LOWERCASE
   The original string after using the StringToLower() function:
    - this string, written in uppercase, must be written in lowercase
   */
  }
```

See also

[StringToUpper](../StringToUpper/StringToUpper.md), [StringTrimLeft](../StringTrimLeft/StringTrimLeft.md), [StringTrimRight](../StringTrimRight/StringTrimRight.md)