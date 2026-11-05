# SetInteger

SetInteger

Sets new value for the property of the integer type.

|  |
| --- |
| bool  SetInteger(     ENUM\_CHART\_PROPERTY\_INTEGER  prop\_id,     // property identifier     long                         value        // value     ) |

Parameters

prop\_id

[in]  Chart property identifier (from [ENUM\_CHART\_PROPERTY\_INTEGER](../../../Constants,-Enumerations-and-Structures/Chart-Constants/Chart-Properties/Chart-Properties.md#enum_chart_property_integer) enumeration).

value

[in]  New value of the property.

Return Value

true - successful, false - cannot change the integer property.
