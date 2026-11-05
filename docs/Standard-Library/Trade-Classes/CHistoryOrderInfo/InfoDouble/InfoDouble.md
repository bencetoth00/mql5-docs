# InfoDouble

InfoDouble

Gets the value of specified double type property.

|  |
| --- |
| bool  InfoDouble(     ENUM\_ORDER\_PROPERTY\_DOUBLE  prop\_id,     // property ID     double&                     var          // reference to variable     ) const |

Parameters

prop\_id

[in]  ID of double type property from [ENUM\_ORDER\_PROPERTY\_DOUBLE](../../../../Constants,-Enumerations-and-Structures/Trade-Constants/Order-Properties/Order-Properties.md#enum_order_property_double) enumeration.

var

[out]  Reference to [double](../../../../Language-Basics/Data-Types/Real-Types-(double,-float)/Real-Types-(double,-float).md) type variable to place result.

Return Value

true – success, false – unable to get property value.

Note

The historical order should be selected using the [Ticket](../Ticket/Ticket.md) (by ticket) or [SelectByIndex](../SelectByIndex/SelectByIndex.md) (by index) methods.
