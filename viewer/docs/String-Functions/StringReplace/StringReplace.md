# StringReplace


It replaces all the found substrings of a string by a set sequence of symbols.

```cpp
int  StringReplace(
   string&         str,              // the string in which substrings will be replaced
   const string    find,             // the searched substring
   const string    replacement       // the substring that will be inserted to the found positions
   );
```

Parameters

str

[in][out]  The string in which you are going to replace substrings.

find

[in]  The desired substring to replace.

replacement

[in]  The string that will be inserted instead of the found one.

Return Value

The function returns the number of replacements in case of success, otherwise -1. To get an [error](../../Constants,-Enumerations-and-Structures/Codes-of-Errors-and-Warnings/Runtime-Errors/Runtime-Errors.md) code call the [GetLastError()](../../Checkup/GetLastError/GetLastError.md) function.

Note

If the function has run successfully but no replacements have been made (the substring to replace was not found), it returns 0.

The error can result from incorrect str or find parameters (empty or non-initialized string, see [StringInit()](../StringInit/StringInit.md) ). Besides, the error occurs if there is not enough memory to complete the replacement.

Example:

```cpp
  string text="The quick brown fox jumped over the lazy dog.";
  int replaced=StringReplace(text,"quick","slow");
  replaced+=StringReplace(text,"brown","black");
  replaced+=StringReplace(text,"fox","bear");
  Print("Replaced: ", replaced,". Result=",text);
//  Result
//  Replaced: 3. Result=The slow black bear jumped over the lazy dog.
//
```

See also

[StringSetCharacter()](../StringSetCharacter/StringSetCharacter.md), [StringSubstr()](../StringSubstr/StringSubstr.md)