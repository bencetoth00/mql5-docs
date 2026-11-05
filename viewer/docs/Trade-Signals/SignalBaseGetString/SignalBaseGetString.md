# SignalBaseGetString


Returns the value of [string](../../Language-Basics/Data-Types/String-Type/String-Type.md) type property for selected signal.

```cpp
string  SignalBaseGetString(
   ENUM_SIGNAL_BASE_STRING     property_id,     // property identifier
   );
```

Parameters

property\_id

[in]  Signal property identifier. The value can be one of the values of the [ENUM\_SIGNAL\_BASE\_STRING](../../Constants,-Enumerations-and-Structures/Trade-Constants/Signal-Properties/Signal-Properties.md#enum_signal_base_string) enumeration.

Return Value

The value of [string](../../Language-Basics/Data-Types/String-Type/String-Type.md) type property of the selected signal.