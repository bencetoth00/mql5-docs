# SignalInfoSetDouble

SignalInfoSetDouble

Sets the value of [double](../../Language-Basics/Data-Types/Real-Types-(double,-float)/Real-Types-(double,-float).md) type property of signal copy settings.

|  |
| --- |
| bool  SignalInfoSetDouble(     ENUM\_SIGNAL\_INFO\_DOUBLE      property\_id,     // property identifier     double                       value            // new value     ); |

Parameters

property\_id

[in]  Signal copy settings property identifier. The value can be one of the values of the [ENUM\_SIGNAL\_INFO\_DOUBLE](../../Constants,-Enumerations-and-Structures/Trade-Constants/Signal-Properties/Signal-Properties.md#enum_signal_info_double) enumeration.

value

[in]  The value of signal copy settings property.

Return Value

Returns true if property has been changed, otherwise returns false. To read more about the [error](../../Constants,-Enumerations-and-Structures/Codes-of-Errors-and-Warnings/Runtime-Errors/Runtime-Errors.md) call [GetLastError()](../../Checkup/GetLastError/GetLastError.md).
