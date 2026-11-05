# InfoInteger

InfoInteger

Gets the value of specified integer type property.

|  |
| --- |
| bool  InfoInteger(     ENUM\_ORDER\_PROPERTY\_INTEGER  prop\_id,     // property ID     long&                        var          // reference to variable     ) const |

Parameters

prop\_id

[in]  ID of integer type property from [ENUM\_ORDER\_PROPERTY\_INTEGER](../../../../Constants,-Enumerations-and-Structures/Trade-Constants/Order-Properties/Order-Properties.md#enum_order_property_integer) enumeration.

var

[out]  Reference to [long](../../../../Language-Basics/Data-Types/Integer-Types/Char,-Short,-Int-and-Long-Types/Char,-Short,-Int-and-Long-Types.md) type variable to place result.

Return Value

true – success, false – unable to get property value.

Note

The order should be selected using the [Select](../Select/Select.md) (by ticket) or [SelectByIndex](../SelectByIndex/SelectByIndex.md) (by index) methods.
