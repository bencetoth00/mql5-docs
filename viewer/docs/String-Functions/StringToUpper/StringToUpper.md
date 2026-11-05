# StringToUpper


Transforms all symbols of a selected string into capitals.

```cpp
bool  StringToUpper(
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
//--- define the source string in lowercase
   string text=" - this string, written in lowercase, must be written in uppercase";
//--- Display the source string in the log
   Print("Source line:\n", text);
//--- convert all string characters to uppercase and display the result in the log
   if(StringToUpper(text))
      Print("The original string after using the StringToUpper() function:\n", text);
   /*
   Result
   Source line:
    - this string, written in lowercase, must be written in uppercase
   The original string after using the StringToUpper() function:
    - THIS STRING, WRITTEN IN LOWERCASE, MUST BE WRITTEN IN UPPERCASE
   */
  }
```

See also

[StringToLower](../StringToLower/StringToLower.md), [StringTrimLeft](../StringTrimLeft/StringTrimLeft.md), [StringTrimRight](../StringTrimRight/StringTrimRight.md)