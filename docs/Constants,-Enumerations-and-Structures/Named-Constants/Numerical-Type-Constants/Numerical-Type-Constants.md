# Numerical Type Constants

Numerical Type Constants

Each simple numerical type is intended for a certain type of tasks and allows optimizing the operation of a mql5-program when used correctly. For a better code readability and correct handling of calculation results, there are constants which allow to receive information about restrictions set to a certain type of simple data.

| Constant | Description | Value |
| --- | --- | --- |
| CHAR\_MIN | Minimal value, which can be represented by char type | -128 |
| CHAR\_MAX | Maximal value, which can be represented by char type | 127 |
| UCHAR\_MAX | Maximal value, which can be represented by uchar type | 255 |
| SHORT\_MIN | Minimal value, which can be represented by short type | -32768 |
| SHORT\_MAX | Maximal value, which can be represented by short type | 32767 |
| USHORT\_MAX | Maximal value, which can be represented by ushort type | 65535 |
| INT\_MIN | Minimal value, which can be represented by int type | -2147483648 |
| INT\_MAX | Maximal value, which can be represented by int type | 2147483647 |
| UINT\_MAX | Maximal value, which can be represented by uint type | 4294967295 |
| LONG\_MIN | Minimal value, which can be represented by long type | -9223372036854775808 |
| LONG\_MAX | Maximal value, which can be represented by long type | 9223372036854775807 |
| ULONG\_MAX | Maximal value, which can be represented by ulong type | 18446744073709551615 |
| DBL\_MIN | Minimal positive value, which can be represented by double type | 2.2250738585072014e-308 |
| DBL\_MAX | Maximal value, which can be represented by double type | 1.7976931348623158e+308 |
| DBL\_EPSILON | Minimal value, which satisfies the condition:  1.0+DBL\_EPSILON != 1.0 (for double type) | 2.2204460492503131e-016 |
| DBL\_DIG | Number of significant decimal digits for double type | 15 |
| DBL\_MANT\_DIG | Number of bits in a mantissa for double type | 53 |
| DBL\_MAX\_10\_EXP | Maximal decimal value of exponent degree for double type | 308 |
| DBL\_MAX\_EXP | Maximal binary value of exponent degree for double type | 1024 |
| DBL\_MIN\_10\_EXP | Minimal decimal value of exponent degree for double type | (-307) |
| DBL\_MIN\_EXP | Minimal binary value of exponent degree for double type | (-1021) |
| FLT\_MIN | Minimal positive value, which can be represented by float type | 1.175494351e-38 |
| FLT\_MAX | Maximal value, which can be represented by float type | 3.402823466e+38 |
| FLT\_EPSILON | Minimal value, which satisfies the condition:  1.0+DBL\_EPSILON != 1.0 (for float type) | 1.192092896e–07 |
| FLT\_DIG | Number of significant decimal digits for float type | 6 |
| FLT\_MANT\_DIG | Number of bits in a mantissa for float type | 24 |
| FLT\_MAX\_10\_EXP | Maximal decimal value of exponent degree for float type | 38 |
| FLT\_MAX\_EXP | Maximal binary value of exponent degree for float type | 128 |
| FLT\_MIN\_10\_EXP | Minimal decimal value of exponent degree for float type | -37 |
| FLT\_MIN\_EXP | Minimal binary value of exponent degree for float type | (-125) |

Example:

|  |
| --- |
| void OnStart()    {  //--- print the constant values     printf("CHAR\_MIN = %d",CHAR\_MIN);     printf("CHAR\_MAX = %d",CHAR\_MAX);     printf("UCHAR\_MAX = %d",UCHAR\_MAX);     printf("SHORT\_MIN = %d",SHORT\_MIN);     printf("SHORT\_MAX = %d",SHORT\_MAX);     printf("USHORT\_MAX = %d",USHORT\_MAX);     printf("INT\_MIN = %d",INT\_MIN);     printf("INT\_MAX = %d",INT\_MAX);     printf("UINT\_MAX = %u",UINT\_MAX);     printf("LONG\_MIN = %I64d",LONG\_MIN);     printf("LONG\_MAX = %I64d",LONG\_MAX);     printf("ULONG\_MAX = %I64u",ULONG\_MAX);     printf("EMPTY\_VALUE = %.16e",EMPTY\_VALUE);     printf("DBL\_MIN = %.16e",DBL\_MIN);     printf("DBL\_MAX = %.16e",DBL\_MAX);     printf("DBL\_EPSILON = %.16e",DBL\_EPSILON);     printf("DBL\_DIG = %d",DBL\_DIG);     printf("DBL\_MANT\_DIG = %d",DBL\_MANT\_DIG);     printf("DBL\_MAX\_10\_EXP =  %d",DBL\_MAX\_10\_EXP);     printf("DBL\_MAX\_EXP = %d",DBL\_MAX\_EXP);     printf("DBL\_MIN\_10\_EXP = %d",DBL\_MIN\_10\_EXP);     printf("DBL\_MIN\_EXP = %d",DBL\_MIN\_EXP);     printf("FLT\_MIN = %.8e",FLT\_MIN);     printf("FLT\_MAX = %.8e",FLT\_MAX);     printf("FLT\_EPSILON = %.8e",FLT\_EPSILON);  /\*     CHAR\_MIN = -128     CHAR\_MAX = 127     UCHAR\_MAX = 255     SHORT\_MIN = -32768     SHORT\_MAX = 32767     USHORT\_MAX = 65535     INT\_MIN = -2147483648     INT\_MAX = 2147483647     UINT\_MAX = 4294967295     LONG\_MIN = -9223372036854775808     LONG\_MAX = 9223372036854775807     ULONG\_MAX = 18446744073709551615     EMPTY\_VALUE = 1.7976931348623157e+308     DBL\_MIN = 2.2250738585072014e-308     DBL\_MAX = 1.7976931348623157e+308     DBL\_EPSILON = 2.2204460492503131e-16     DBL\_DIG = 15     DBL\_MANT\_DIG = 53     DBL\_MAX\_10\_EXP =  308     DBL\_MAX\_EXP = 1024     DBL\_MIN\_10\_EXP = -307     DBL\_MIN\_EXP = -1021     FLT\_MIN = 1.17549435e-38     FLT\_MAX = 3.40282347e+38     FLT\_EPSILON = 1.19209290e-07  \*/     } |
