# TimeMsc


Lekéri az ügylet végrehajtásának időpontját ezredmásodpercben 1970.01.01. óta.

```cpp
ulong  TimeMsc() const
```

Visszatérési érték

Az ügylet végrehajtásának időpontja ezredmásodpercben 1970.01.01. óta.

Megjegyzés

Az adatok eléréséhez előzetesen ki kell választani az ügyletet a [Ticket](../Ticket/Ticket.md) (jegy alapján) vagy a [SelectByIndex](../SelectByIndex/SelectByIndex.md) (index alapján) metódussal.
