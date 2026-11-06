# AmbientColorGet


Lekéri a környezeti, minden irányból érkező megvilágítás színét és intenzitását.

```cpp
void  AmbientColorGet(
   DXColor  &ambient_color      // all-round lighting color and intensity
   );
```

Paraméterek

&ambient\_color

[out]  A környezeti megvilágítás színe.

Visszatérési érték

Nincs.

Megjegyzés

Az intenzitás a DXColor struktúra alfa csatornájában van tárolva.
