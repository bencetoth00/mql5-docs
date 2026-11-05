# InfoString

InfoString

Gets the value of specified string type property.

|  |
| --- |
| bool  InfoString(     ENUM\_DEAL\_PROPERTY\_STRING  prop\_id,     // property ID     string&                    var          // reference to variable     ) const |

Parameters

prop\_id

[in]  ID of text property from [ENUM\_DEAL\_PROPERTY\_STRING](../../../../Constants,-Enumerations-and-Structures/Trade-Constants/Deal-Properties/Deal-Properties.md#enum_deal_property_string) enumeration.

var

[out]  Reference to [string](../../../../Language-Basics/Data-Types/String-Type/String-Type.md) type variable to place result.

Return Value

true – success, false – unable to get property value.

Note

The deal should be selected using the [Ticket](../Ticket/Ticket.md) (by ticket) or [SelectByIndex](../SelectByIndex/SelectByIndex.md) (by index) methods.
