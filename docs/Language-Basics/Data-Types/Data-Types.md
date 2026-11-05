# Data Types

Data Types

Any program operates with data. Data can be of different types depending on their purposes. For example, integer data are used to access to array components. Price data belong to those of double precision with floating point. This is related to the fact that no special data type for price data is provided in MQL5.

Data of different types are processed with different rates. Integer data are processed at the fastest. To process the double precision data, a special co-processor is used. However, because of complexity of internal representation of data with floating point, they are processed slower than the integer ones.

String data are processed at the longest because of dynamic computer memory allocation/reallocation.

The basic data types are:

- integers ([char](Integer-Types/Char,-Short,-Int-and-Long-Types/Char,-Short,-Int-and-Long-Types.md), [short](Integer-Types/Char,-Short,-Int-and-Long-Types/Char,-Short,-Int-and-Long-Types.md), [int](Integer-Types/Char,-Short,-Int-and-Long-Types/Char,-Short,-Int-and-Long-Types.md), [long](Integer-Types/Char,-Short,-Int-and-Long-Types/Char,-Short,-Int-and-Long-Types.md), [uchar](Integer-Types/Char,-Short,-Int-and-Long-Types/Char,-Short,-Int-and-Long-Types.md), [ushort](Integer-Types/Char,-Short,-Int-and-Long-Types/Char,-Short,-Int-and-Long-Types.md), [uint](Integer-Types/Char,-Short,-Int-and-Long-Types/Char,-Short,-Int-and-Long-Types.md), [ulong](Integer-Types/Char,-Short,-Int-and-Long-Types/Char,-Short,-Int-and-Long-Types.md));
- logical ([bool](Integer-Types/Bool-Type/Bool-Type.md));
- [literals](Integer-Types/Character-Constants/Character-Constants.md) (ushort);
- strings ([string](String-Type/String-Type.md));
- floating-point numbers ([double](Real-Types-(double,-float)/Real-Types-(double,-float).md), [float](Real-Types-(double,-float)/Real-Types-(double,-float).md));
- color ([color](Integer-Types/Color-Type/Color-Type.md));
- date and time ([datetime](Integer-Types/Datetime-Type/Datetime-Type.md));
- enumerations ([enum](Integer-Types/Enumerations/Enumerations.md)).

Complex data types are:

- [structures](Structures,-Classes-and-Interfaces/Structures,-Classes-and-Interfaces.md);
- [classes](Structures,-Classes-and-Interfaces/Structures,-Classes-and-Interfaces.md#class).

In terms of [OOP](../Object-Oriented-Programming/Object-Oriented-Programming.md) complex data types are called abstract data types.

The color and datetime types make sense only to facilitate visualization and input of parameters defined from outside - from the table of Expert Advisor or custom indicator properties (the [Inputs](../Variables/Input-Variables/Input-Variables.md) tab). Data of color and datetime types are represented as integers. Integer types and floating-point types are called arithmetic (numeric) types.

Only implicit [type casting](Typecasting/Typecasting.md) is used in [expressions](../Operations-and-Expressions/Expressions/Expressions.md), unless the explicit casting is specified.

See also

[Typecasting](Typecasting/Typecasting.md)
