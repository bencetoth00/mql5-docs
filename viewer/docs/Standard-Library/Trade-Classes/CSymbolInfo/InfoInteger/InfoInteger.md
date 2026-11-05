# InfoInteger


Gets the value of specified integer type property.

```cpp
bool  InfoInteger(
   ENUM_SYMBOL_INFO_INTEGER  prop_id,     // property ID
   long&                     var          // reference to variable
   ) const
```

Parameters

prop\_id

[in]  ID of integer type property from [ENUM\_SYMBOL\_INFO\_INTEGER](../../../../Constants,-Enumerations-and-Structures/Environment-State/Symbol-Properties/Symbol-Properties.md#enum_symbol_info_integer) enumeration.

var

[out]  Reference to [long](../../../../Language-Basics/Data-Types/Integer-Types/Char,-Short,-Int-and-Long-Types/Char,-Short,-Int-and-Long-Types.md) type variable to place result.

Return Value

true – success, false – unable to get property value.

Note

The symbol should be selected by [Name](../Name/Name.md) method.