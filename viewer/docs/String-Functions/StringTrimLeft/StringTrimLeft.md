# StringTrimLeft


The function cuts line feed characters, spaces and tabs in the left part of the string till the first meaningful symbol. The string is modified at place.

```cpp
int  StringTrimLeft(
   string&  string_var      // string to cut
   );
```

Parameters

string\_var

[in][out]  String that will be cut from the left.

Return Value

Returns the number of cut symbols.

Example:

```cpp
void OnStart()
  {
//--- define the source string with six spaces on the left
   string text="      All spaces on the left will be removed from this string";
//--- Display the source string in the log
   PrintFormat("Source line:\n'%s'", text);
//--- remove all spaces on the left and display the number of removed characters and the resulting string in the log
   int num=StringTrimLeft(text);
   PrintFormat("The StringTrimLeft() function removed %d chars from the left side. Now the line looks like this:\n'%s'", num, text);
   /*
   Result
   Source line:
   '      All spaces on the left will be removed from this string'
   The StringTrimLeft() function removed 6 chars from the left side. Now the line looks like this:
   'All spaces on the left will be removed from this string'
   */
  }
```

See also

[StringTrimRight](../StringTrimRight/StringTrimRight.md), [StringToLower](../StringToLower/StringToLower.md), [StringToUpper](../StringToUpper/StringToUpper.md)