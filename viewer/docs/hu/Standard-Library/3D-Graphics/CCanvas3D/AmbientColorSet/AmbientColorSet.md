# AmbientColorSet


Beállítja a környezeti, minden irányból érkező megvilágítás színét és intenzitását.

```cpp
void  AmbientColorSet(
   const DXColor  &ambient_color      // all-round lighting color and intensity
   );
```

Paraméterek

&ambient\_color

[in]  A környezeti megvilágítás színe.

Visszatérési érték

Nincs.

Megjegyzés

Az intenzitás a DXColor struktúra alfa csatornájában van beállítva.
