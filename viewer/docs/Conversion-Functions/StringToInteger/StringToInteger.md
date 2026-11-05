# StringToInteger


The function converts string containing a symbol representation of number into number of long (integer) type.

```cpp
long  StringToInteger(
   string  value      // string
   );
```

Parameters

value

[in]  String containing a number.

Return Value

Value of long type.

 

Example:

```cpp
//+------------------------------------------------------------------+
//| Script program start function                                    |
//+------------------------------------------------------------------+
void OnStart()
  {
//--- string to convert
   string str = "12345.54321";
//--- convert the input string as a number into a long type variable
   long converted=StringToInteger(str);
//--- display the obtained number in the journal with the fractional part cut off
   PrintFormat("The string '%s' is converted to the integer number %I64d", str, converted);
   /*
   result:
   The string '12345.54321' is converted to the integer number 12345
   */
  }
```

See also

[IntegerToString](../IntegerToString/IntegerToString.md), [Real types (double, float)](../../Language-Basics/Data-Types/Real-Types-(double,-float)/Real-Types-(double,-float).md), [Typecasting](../../Language-Basics/Data-Types/Typecasting/Typecasting.md)