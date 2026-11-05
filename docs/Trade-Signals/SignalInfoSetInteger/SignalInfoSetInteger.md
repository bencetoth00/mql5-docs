# SignalInfoSetInteger

SignalInfoSetInteger

Sets the value of [integer](../../Language-Basics/Data-Types/Integer-Types/Integer-Types.md) type property of signal copy settings.

|  |
| --- |
| bool  SignalInfoSetInteger(     ENUM\_SIGNAL\_INFO\_INTEGER     property\_id,     // property identifier     long                         value            // new value     ); |

Parameters

property\_id

[in]  Signal copy settings property identifier. The value can be one of the values of the [ENUM\_SIGNAL\_INFO\_INTEGER](../../Constants,-Enumerations-and-Structures/Trade-Constants/Signal-Properties/Signal-Properties.md#enum_signal_info_integer) enumeration.

value

[in]  The value of signal copy settings property.

Return Value

Returns true if property has been changed, otherwise returns false. To read more about the [error](../../Constants,-Enumerations-and-Structures/Codes-of-Errors-and-Warnings/Runtime-Errors/Runtime-Errors.md) call [GetLastError()](../../Checkup/GetLastError/GetLastError.md).
