# SetTypeFillingBySymbol

SetTypeFillingBySymbol

Sets [filling](../../../../Constants,-Enumerations-and-Structures/Trade-Constants/Order-Properties/Order-Properties.md#enum_order_type_filling) type of the order according to the specified symbol settings.

|  |
| --- |
| bool  SetTypeFillingBySymbol(     const string   symbol      // symbol name     ) |

Parameters

symbol

[in] Name of the symbol, in which [SYMBOL\_FILLING\_MODE](../../../../Constants,-Enumerations-and-Structures/Environment-State/Symbol-Properties/Symbol-Properties.md#symbol_filling_mode) contains allowed order filling policies.

Return Value

true – successful execution, false – failed to define the filling policy.

Note

If [SYMBOL\_FILLING\_FOK](../../../../Constants,-Enumerations-and-Structures/Environment-State/Symbol-Properties/Symbol-Properties.md#symbol_filling_mode) and [SYMBOL\_FILLING\_IOC](../../../../Constants,-Enumerations-and-Structures/Environment-State/Symbol-Properties/Symbol-Properties.md#symbol_filling_mode) filling policies are allowed for a symbol simultaneously, the [ORDER\_FILLING\_FOK](../../../../Constants,-Enumerations-and-Structures/Trade-Constants/Order-Properties/Order-Properties.md#enum_order_type_filling) value is set for the order.
