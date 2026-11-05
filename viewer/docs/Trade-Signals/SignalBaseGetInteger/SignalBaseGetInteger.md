# SignalBaseGetInteger


Returns the value of [integer](../../Language-Basics/Data-Types/Integer-Types/Integer-Types.md) type property for selected signal.

```cpp
long  SignalBaseGetInteger(
   ENUM_SIGNAL_BASE_INTEGER     property_id,     // property identifier
   );
```

Parameters

property\_id

[in]  Signal property identifier. The value can be one of the values of the [ENUM\_SIGNAL\_BASE\_INTEGER](../../Constants,-Enumerations-and-Structures/Trade-Constants/Signal-Properties/Signal-Properties.md#enum_signal_base_integer) enumeration.

Return Value

The value of [integer](../../Language-Basics/Data-Types/Integer-Types/Integer-Types.md) type property of the selected signal.