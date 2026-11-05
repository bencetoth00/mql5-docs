# EnumToString


Converting an enumeration value of any type to a text form.

```cpp
string  EnumToString(
   any_enum  value      // any type enumeration value
   );
```

Parameters

value

[in]  Any type enumeration value.

Return Value

A string with a text representation of the enumeration. To get the error message call the [GetLastError()](../../Checkup/GetLastError/GetLastError.md) function.

Note

The function can set the following error values in the [\_LastError](../../Predefined-Variables/_LastError/_LastError.md) variable:

- ERR\_INTERNAL\_ERROR – error of the execution environment
- ERR\_NOT\_ENOUGH\_MEMORY – not enough memory to complete the operation
- ERR\_INVALID\_PARAMETER – can't allow the name of the enumeration value

 

Example:

```cpp
enum interval  // enumeration of named constants
  {
   month=1,     // one-month interval
   two_months,  // two months
   quarter,     // three months - a quarter
   halfyear=6,  // half a year
   year=12,     // a year - 12 months
  };
//+------------------------------------------------------------------+
//| Script program start function                                    |
//+------------------------------------------------------------------+
void OnStart()
  {
//--- set the time interval equal to one month
   interval period=month;
   Print(EnumToString(period)+"="+IntegerToString(period));
//--- set the time interval equal to a quarter (three months)
   period=quarter;
   Print(EnumToString(period)+"="+IntegerToString(period));
//--- set the time interval equal to one year (12 months)
   period=year;
   Print(EnumToString(period)+"="+IntegerToString(period));
//--- check how the order type is shown
   ENUM_ORDER_TYPE type=ORDER_TYPE_BUY;
   Print(EnumToString(type)+"="+IntegerToString(type));
//--- check how incorrect values are shown
   type=WRONG_VALUE;
   Print(EnumToString(type)+"="+IntegerToString(type));
// Result:
// month=1
// quarter=3
// year=12
// ORDER_TYPE_BUY=0
// ENUM_ORDER_TYPE::-1=-1
  }
```

See also

[Enumerations](../../Language-Basics/Data-Types/Integer-Types/Enumerations/Enumerations.md), [Input variables](../../Language-Basics/Variables/Input-Variables/Input-Variables.md)