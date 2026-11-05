# InfoInteger


Gets the value of specified integer type property.

```cpp
bool  InfoInteger(
   ENUM_DEAL_PROPERTY_INTEGER  prop_id,     // property ID
   long&                       var          // reference to variable
   ) const
```

Parameters

prop\_id

[in]  ID of integer type property from [ENUM\_DEAL\_PROPERTY\_INTEGER](../../../../Constants,-Enumerations-and-Structures/Trade-Constants/Deal-Properties/Deal-Properties.md#enum_deal_property_integer) enumeration.

var

[out]  Reference to [long](../../../../Language-Basics/Data-Types/Integer-Types/Char,-Short,-Int-and-Long-Types/Char,-Short,-Int-and-Long-Types.md) type variable to place result.

Return Value

true – success, false – unable to get property value.

Note

The deal should be selected using the [Ticket](../Ticket/Ticket.md) (by ticket) or [SelectByIndex](../SelectByIndex/SelectByIndex.md) (by index) methods.