# SetString


Sets new value for the chart property of the string type.

```cpp
bool  SetString(
   ENUM_CHART_PROPERTY_STRING  prop_id,     // property identifier
   string                      value        // value
   )
```

Parameters

prop\_id

[in]  Chart property identifier (from [ENUM\_CHART\_PROPERTY\_STRING](../../../Constants,-Enumerations-and-Structures/Chart-Constants/Chart-Properties/Chart-Properties.md#enum_chart_property_string) enumeration).

value

[in]  New value for the property.

Return Value

true - successful, false - cannot change the string property.