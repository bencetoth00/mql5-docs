# MathClassify

MathClassify

Determines the type of a real number and returns a result as a value from the [ENUM\_FP\_CLASS](MathClassify.md#enum_fp_class) enumeration

|  |
| --- |
| ENUM\_FP\_CLASS  MathClassify(     double  value      // real number     ); |

Parameters

value

[in]  The real number to be checked

Return Value

A value from the ENUM\_FP\_CLASS enumeration

ENUM\_FP\_CLASS

| ID | Description |
| --- | --- |
| FP\_SUBNORMAL | A subnormal number which is closer to zero than the smallest representable normal number DBL\_MIN (2.2250738585072014e-308) |
| FP\_NORMAL | A normal number in the range between 2.2250738585072014e-308 and 1.7976931348623158e+308 |
| FP\_ZERO | A positive or a negative zero |
| FP\_INFINITE | A number which cannot be represented by the appropriate type, positive or negative infinity |
| FP\_NAN | Not a number. |

Example:

|  |
| --- |
| //+------------------------------------------------------------------+  //| Script program start function                                    |  //+------------------------------------------------------------------+  void OnStart()   {  //--- test NaN    double nan=double("nan");    PrintFormat("Test NaN: %G is %s, MathIsValidNumber(NaN)=%s",                nan,                EnumToString(MathClassify(nan)),                (string)MathIsValidNumber(nan));  //--- test infinity    double inf=double("inf");    PrintFormat("Test Inf: %G is %s, MathIsValidNumber(inf)=%s",                inf,                EnumToString(MathClassify(inf)),                (string)MathIsValidNumber(inf));  //--- test normal value    double normal=1.2345e6;    PrintFormat("Test Normal: %G is %s, MathIsValidNumber(normal)=%s",                normal,                EnumToString(MathClassify(normal)),                (string)MathIsValidNumber(normal));  //--- test subnormal value    double sub\_normal=DBL\_MIN/2.0;    PrintFormat("Test Subnormal: %G is %s, MathIsValidNumber(sub\_normal)=%s",                sub\_normal,                EnumToString(MathClassify(sub\_normal)),                (string)MathIsValidNumber(sub\_normal));  //--- test zero value    double zero=0.0/(-1);    PrintFormat("Test Zero: %G is %s, MathIsValidNumber(zero)=%s",                zero,                EnumToString(MathClassify(zero)),                (string)MathIsValidNumber(zero));   }    /\*   Result:     Test NaN: NAN is FP\_NAN, MathIsValidNumber(NaN)=false     Test Inf: INF is FP\_INFINITE, MathIsValidNumber(inf)=false     Test Normal: 1.2345E+06 is FP\_NORMAL, MathIsValidNumber(normal)=true     Test Subnormal: 1.11254E-308 is FP\_SUBNORMAL, MathIsValidNumber(sub\_normal)=true     Test Zero: -0 is FP\_ZERO, MathIsValidNumber(zero)=true  \*/   //+------------------------------------------------------------------+ |

See also

[Real types (double, float)](../../Language-Basics/Data-Types/Real-Types-(double,-float)/Real-Types-(double,-float).md), [MathIsValidNumber](../MathIsValidNumber/MathIsValidNumber.md)
