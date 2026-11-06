# OnSetText


A vezérlő „SetText” eseményének virtuális kezelője (az [OBJPROP\_TEXT](../../../../Constants,-Enumerations-and-Structures/Objects-Constants/Object-Properties/Object-Properties.md#enum_object_property_double) tulajdonság módosításakor).

```cpp
virtual bool  OnSetText()
```

Visszatérési érték

true, ha az esemény feldolgozása megtörtént, egyébként false.

Megjegyzés

Az alaposztály metódusa nem végez műveletet, és mindig true értéket ad vissza.
