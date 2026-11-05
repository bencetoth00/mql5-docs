# InfoDouble


Gets the value of specified double type property.

```cpp
bool  InfoDouble(
   ENUM_POSITION_PROPERTY_DOUBLE  prop_id,     // property ID
   double&                        var          // reference to variable
   ) const
```

Parameters

prop\_id

[in]  ID of double type property from [ENUM\_POSITION\_PROPERTY\_DOUBLE](../../../../Constants,-Enumerations-and-Structures/Trade-Constants/Position-Properties/Position-Properties.md#enum_position_property_double) enumeration.

var

[in]  Reference to [double](../../../../Language-Basics/Data-Types/Real-Types-(double,-float)/Real-Types-(double,-float).md) type variable to place result.

Return Value

true – success, false – unable to get property value.

Note

The position should be selected using the [Select](../Select/Select.md) (by ticket) or [SelectByIndex](../SelectByIndex/SelectByIndex.md) (by index) methods.