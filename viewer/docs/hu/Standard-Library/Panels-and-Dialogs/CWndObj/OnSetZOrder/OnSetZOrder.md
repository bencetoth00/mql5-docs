# OnSetZOrder


A „SetZOrder” esemény virtuális kezelője (az [OBJPROP\_ZORDER](../../../../Constants,-Enumerations-and-Structures/Objects-Constants/Object-Properties/Object-Properties.md#enum_object_property_integer) tulajdonság módosításakor).

```cpp
virtual bool  OnSetZOrder()
```

Visszatérési érték

true, ha az esemény feldolgozása megtörtént, egyébként false.

Megjegyzés

Az alaposztály metódusa nem végez műveletet, és mindig true értéket ad vissza.
