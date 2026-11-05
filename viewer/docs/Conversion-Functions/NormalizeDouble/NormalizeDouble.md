# NormalizeDouble


Rounding floating point number to a specified accuracy.

```cpp
double  NormalizeDouble(
   double  value,      // normalized number
   int     digits      // number of digits after decimal point
   );
```

Parameters

value

[in] Value with a floating point.

digits

[in]  Accuracy format, number of digits after point (0-8).

Return Value

Value of double type with preset accuracy.

Note

Calculated values of StopLoss, TakeProfit, and values of open prices for pending orders must be normalized with the accuracy, the value of which can be obtained by [Digits()](../../Checkup/Digits/Digits.md).

Please note that when output to Journal using the Print() function, a normalized number may contain a greater number of decimal places than you expect. For example, for:

```cpp
   double a=76.671;             // A normalized number with three decimal places
   Print("Print(76.671)=",a);   // Output as is
   Print("DoubleToString(a,8)=",DoubleToString(a,8)); // Output with a preset accuracy
```

you will have the following in the terminal:

|  |
| --- |
| DoubleToString(a,8)=76.67100000   Print(76.671)=76.67100000000001 |

 

Example:

```cpp
   double pi=M_PI;
   Print("pi = ",DoubleToString(pi,16));
   double pi_3=NormalizeDouble(M_PI,3);
   Print("NormalizeDouble(pi,3) = ",DoubleToString(pi_3,16))
   ;
   double pi_8=NormalizeDouble(M_PI,8);
   Print("NormalizeDouble(pi,8) = ",DoubleToString(pi_8,16));
   double pi_0=NormalizeDouble(M_PI,0);
   Print("NormalizeDouble(pi,0) = ",DoubleToString(pi_0,16));
/*
   Result:
   pi= 3.1415926535897931
   NormalizeDouble(pi,3)= 3.1419999999999999
   NormalizeDouble(pi,8)= 3.1415926499999998
   NormalizeDouble(pi,0)= 3.0000000000000000
*/
```

See also

[DoubleToString](../DoubleToString/DoubleToString.md), [Real types (double, float)](../../Language-Basics/Data-Types/Real-Types-(double,-float)/Real-Types-(double,-float).md), [Typecasting](../../Language-Basics/Data-Types/Typecasting/Typecasting.md)