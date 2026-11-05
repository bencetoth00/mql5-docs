# StringToDouble


The function converts string containing a symbol representation of number into number of double type.

```cpp
double  StringToDouble(
   string  value      // string
   );
```

Parameters

value

[in]  String containing a symbol representation of a number.

Return Value

Value of double type.

 

Example:

```cpp
//+------------------------------------------------------------------+
//| Script program start function                                    |
//+------------------------------------------------------------------+
void OnStart()
  {
//--- string to convert
   string str = "12345.54321";
//--- convert the input string as a real number into a double type variable
   double converted=StringToDouble(str);
//--- display the resulting number accurate to 8 decimal places in the journal
   PrintFormat("The string '%s' is converted to the real number %.8f", str, converted);
   /*
   result:
   The string '12345.54321' is converted to the real number 12345.54321000
   */
  }
```

See also

[NormalizeDouble](../NormalizeDouble/NormalizeDouble.md), [Real types (double, float)](../../Language-Basics/Data-Types/Real-Types-(double,-float)/Real-Types-(double,-float).md), [Typecasting](../../Language-Basics/Data-Types/Typecasting/Typecasting.md)