# Ticket


Lekéri a megbízás jegyét.

```cpp
ulong  Ticket() const
```

Visszatérési érték

Siker esetén a megbízás jegye, ellenkező esetben [ULONG\_MAX](../../../../Constants,-Enumerations-and-Structures/Named-Constants/Numerical-Type-Constants/Numerical-Type-Constants.md).

Megjegyzés

A megbízást a [Select](../Select/Select.md) (jegy alapján) vagy a [SelectByIndex](../SelectByIndex/SelectByIndex.md) (index alapján) metódussal kell kiválasztani.
