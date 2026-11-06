# OnSetColorBackground


A vezérlő „SetColorBackground” eseményének virtuális kezelője (az [OBJPROP\_BGCOLOR](../../../../Constants,-Enumerations-and-Structures/Objects-Constants/Object-Properties/Object-Properties.md#enum_object_property_integer) tulajdonság módosításakor).

```cpp
virtual bool  OnSetColorBackground()
```

Visszatérési érték

true, ha az esemény feldolgozása megtörtént, egyébként false.

Megjegyzés

Az alaposztály metódusa nem végez műveletet, és mindig true értéket ad vissza.
