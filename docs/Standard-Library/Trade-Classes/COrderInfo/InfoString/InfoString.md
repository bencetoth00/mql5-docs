# InfoString

InfoString

Gets the value of specified string type property.

|  |
| --- |
| bool  InfoString(     ENUM\_ORDER\_PROPERTY\_STRING  prop\_id,     // property ID     string&                     var          // reference to variable     ) const |

Parameters

prop\_id

[in]  ID of string property from [ENUM\_ORDER\_PROPERTY\_STRING](../../../../Constants,-Enumerations-and-Structures/Trade-Constants/Order-Properties/Order-Properties.md) enumeration.

var

[out]  Reference to [string](../../../../Language-Basics/Data-Types/String-Type/String-Type.md) type variable to place result.

Return Value

true – success, false – unable to get property value.

Note

The order should be selected using the [Select](../Select/Select.md) (by ticket) or [SelectByIndex](../SelectByIndex/SelectByIndex.md) (by index) methods.
