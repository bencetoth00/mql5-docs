# InfoDouble


Gets the value of specified double type property.

```cpp
bool  InfoDouble(
   ENUM_SYMBOL_INFO_DOUBLE  prop_id,     // property ID
   double&                  var          // reference to variable
   ) const
```

Parameters

prop\_id

[in]  ID of double type property from [ENUM\_SYMBOL\_INFO\_DOUBLE](../../../../Constants,-Enumerations-and-Structures/Environment-State/Symbol-Properties/Symbol-Properties.md#enum_symbol_info_double) enumeration.

var

[out]  Reference to [double](../../../../Language-Basics/Data-Types/Real-Types-(double,-float)/Real-Types-(double,-float).md) type variable to place result.

Return Value

true – success, false – unable to get property value.

Note

The symbol should be selected by [Name](../Name/Name.md) method.