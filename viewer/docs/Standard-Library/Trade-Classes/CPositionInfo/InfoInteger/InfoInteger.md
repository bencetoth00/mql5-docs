# InfoInteger


Gets the value of specified integer type property.

```cpp
bool  InfoInteger(
   ENUM_POSITION_PROPERTY_INTEGER  prop_id,     // property ID
   long&                           var          // reference to variable
   ) const
```

Parameters

prop\_id

[in]  ID of integer type property from [ENUM\_POSITION\_PROPERTY\_INTEGER](../../../../Constants,-Enumerations-and-Structures/Trade-Constants/Position-Properties/Position-Properties.md#enum_position_property_integer) enumeration.

var

[out]  Reference to [long](../../../../Language-Basics/Data-Types/Integer-Types/Char,-Short,-Int-and-Long-Types/Char,-Short,-Int-and-Long-Types.md) type variable to place result.

Return Value

true – success, false – unable to get property value.

Note

The position should be selected using the [Select](../Select/Select.md) (by ticket) or [SelectByIndex](../SelectByIndex/SelectByIndex.md) (by index) methods.