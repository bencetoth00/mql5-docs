# GetString


The function returns the value of the corresponding chart property. The chart property should be of the string type. There are two variants of the function.

1. Immediately returns the property value.

```cpp
string  GetString(
   ENUM_CHART_PROPERTY_STRING  prop_id      // property identifier
   ) const
```

2. If successful, puts the value of property to the specified variable of string type, passed by reference as last parameter.

```cpp
bool  GetString(
   ENUM_CHART_PROPERTY_STRING  prop_id,     // property identifier
   string&                     value        // link to the variable
   ) const
```

Parameters

prop\_id

[in]  Chart property identifier (from [ENUM\_CHART\_PROPERTY\_STRING](../../../Constants,-Enumerations-and-Structures/Chart-Constants/Chart-Properties/Chart-Properties.md#enum_chart_property_string) enumeration).

value

[in]  Link to the variable that receives the value of the requested property.

Return Value

Value of a chart property assigned to the class instance. If there is no chart assigned, it returns "".

For the second variant, the function returns true, if this property is maintained and the value has been placed into the value variable, otherwise it returns false. To read more about the [error](../../../Constants,-Enumerations-and-Structures/Codes-of-Errors-and-Warnings/Runtime-Errors/Runtime-Errors.md), call [GetLastError()](../../../Checkup/GetLastError/GetLastError.md).