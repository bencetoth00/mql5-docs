# StringBufferLen


The function returns the size of buffer allocated for the string.

```cpp
int  StringBufferLen(
   string  string_var      // string
   )
```

Parameters

string\_var

[in]  String.

Return Value

The value 0 means that the string is constant and buffer size can't be changed. -1 means that the string belongs to the client terminal, and modification of the buffer contents can have indeterminate results.

Example:

```cpp
void OnStart()
  {
   long length=1000;
   string a="a",b="b";
//---
   long i;
   Print("before: StringBufferLen(a) = ",StringBufferLen(a),
         "  StringLen(a) = ",StringLen(a));
   for(i=0;i<length;i++)
     {
      StringAdd(a,b);
     }
   Print("after: StringBufferLen(a) = ",StringBufferLen(a),
         "  StringLen(a) = ",StringLen(a));
  }
```

See also

[StringAdd](../StringAdd/StringAdd.md), [StringInit](../StringInit/StringInit.md), [StringLen](../StringLen/StringLen.md), [StringFill](../StringFill/StringFill.md)