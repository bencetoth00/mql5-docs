# InfoDouble


Gets the value of specified double type property.

```cpp
bool  InfoDouble(
   ENUM_ORDER_PROPERTY_DOUBLE  prop_id,     // property ID
   double&                     var          // reference to variable
   ) const
```

Parameters

prop\_id

[in]  ID of double type property from [ENUM\_ORDER\_PROPERTY\_DOUBLE](../../../../Constants,-Enumerations-and-Structures/Trade-Constants/Order-Properties/Order-Properties.md#enum_order_property_double) enumeration.

var

[out]  Reference to [double](../../../../Language-Basics/Data-Types/Real-Types-(double,-float)/Real-Types-(double,-float).md) type variable to place result.

Return Value

true – success, false – unable to get property value.

Note

The order should be selected using the [Select](../Select/Select.md) (by ticket) or [SelectByIndex](../SelectByIndex/SelectByIndex.md) (by index) methods.