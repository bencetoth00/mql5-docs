# TimeSetupMsc


Lekéri a megbízás végrehajtásra történő beadásának idejét az 1970.01.01. óta eltelt ezredmásodpercekben.

```cpp
ulong  TimeSetupMsc() const
```

Visszatérési érték

A megbízás végrehajtásra történő beadásának ideje az 1970.01.01. óta eltelt ezredmásodpercekben.

Megjegyzés

A korábbi megbízást a hozzáférés előtt ki kell választani a [Ticket](../Ticket/Ticket.md) (jegy alapján) vagy a [SelectByIndex](../SelectByIndex/SelectByIndex.md) (index alapján) metódussal.
