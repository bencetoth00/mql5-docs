# GetInteger


The function returns the value of the corresponding chart property. The chart property should be of the [integer](../../../Language-Basics/Data-Types/Integer-Types/Integer-Types.md) type. There are two variants of the function.

1. Immediately returns the property value.

```cpp
long  GetInteger(
   ENUM_CHART_PROPERTY_INTEGER  prop_id,          // property identifier
   int                          sub_window=0      // subwindow number
   ) const
```

2. If successful, puts the value of property to the specified variable of integer type, passed by reference as last parameter.

```cpp
bool  GetInteger(
   ENUM_CHART_PROPERTY_INTEGER  prop_id,        // property identifier
   int                          sub_window,     // subwindow number
   long&                        value           // link to the variable
   ) const
```

Parameters

prop\_id

[in]  Property identifier ([ENUM\_CHART\_PROPERTY\_INTEGER](../../../Constants,-Enumerations-and-Structures/Chart-Constants/Chart-Properties/Chart-Properties.md#enum_chart_property_integer) enumeration).

sub\_window

[in]  Chart subwindow number.

value

[in]  Link to the variable that receives the value of the requested property.

Return Value

Value of property of the chart assigned to the class instance. If there is not any chart assigned, it returns -1.

For the second variant, the function returns true, if this property is maintained and the value has been placed into the value variable, otherwise it returns false. To read more about the [error](../../../Constants,-Enumerations-and-Structures/Codes-of-Errors-and-Warnings/Runtime-Errors/Runtime-Errors.md), call [GetLastError()](../../../Checkup/GetLastError/GetLastError.md).