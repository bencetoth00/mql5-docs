# StringAdd


The function adds a substring to the end of a string.

```cpp
bool  StringAdd(
   string&  string_var,        // string, to which we add
   string   add_substring      // string, which is added
   );
```

Parameters

string\_var

[in][out]  String, to which another one is added.

add\_substring

[in]  String that is added to the end of a  source string.

Return Value

In case of success returns true, otherwise false. In order to get an [error code](../../Constants,-Enumerations-and-Structures/Codes-of-Errors-and-Warnings/Runtime-Errors/Runtime-Errors.md), the [GetLastError()](../../Checkup/GetLastError/GetLastError.md) function should be called.

Example:

```cpp
void OnStart()
  {
   long length=1000000;
   string a="a",b="b",c;
//--- first method
   uint start=GetTickCount(),stop;
   long i;
   for(i=0;i<length;i++)
     {
      c=a+b;
     }
   stop=GetTickCount();
   Print("time for 'c = a + b' = ",(stop-start)," milliseconds, i = ",i);
//--- second method
   start=GetTickCount();
   for(i=0;i<length;i++)
     {
      StringAdd(a,b);
     }
   stop=GetTickCount();
   Print("time for 'StringAdd(a,b)' = ",(stop-start)," milliseconds, i = ",i);
//--- third method
   start=GetTickCount();
   a="a"; // re-initialize variable a
   for(i=0;i<length;i++)
     {
      StringConcatenate(c,a,b);
     }
   stop=GetTickCount();
   Print("time for 'StringConcatenate(c,a,b)' = ",(stop-start)," milliseconds, i = ",i);
  }
```

See also

[StringConcatenate](../StringConcatenate/StringConcatenate.md), [StringSplit](../StringSplit/StringSplit.md), [StringSubstr](../StringSubstr/StringSubstr.md)