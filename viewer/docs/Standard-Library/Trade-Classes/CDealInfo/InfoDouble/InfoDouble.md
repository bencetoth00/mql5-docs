# InfoDouble


Gets the value of specified double type property.

```cpp
bool  InfoDouble(
   ENUM_DEAL_PROPERTY_DOUBLE  prop_id,     // property ID
   double&                    var          // reference to variable
   ) const
```

Parameters

prop\_id

[in]  ID of double type property from [ENUM\_DEAL\_PROPERTY\_DOUBLE](../../../../Constants,-Enumerations-and-Structures/Trade-Constants/Deal-Properties/Deal-Properties.md#enum_deal_property_double) enumeration.

var

[out]  Reference to [double](../../../../Language-Basics/Data-Types/Real-Types-(double,-float)/Real-Types-(double,-float).md) type variable to place result.

Return Value

true – success, false – unable to get property value.

Note

The deal should be selected using the [Ticket](../Ticket/Ticket.md) (by ticket) or [SelectByIndex](../SelectByIndex/SelectByIndex.md) (by index) methods.