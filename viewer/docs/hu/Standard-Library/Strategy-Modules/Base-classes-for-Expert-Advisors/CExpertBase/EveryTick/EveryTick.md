# EveryTick


Beállítja az „Every tick” jelzőt.

```cpp
void  EveryTick(
   bool    value         // flag
   )
```

Paraméterek

value

[in]  A jelző új értéke.

Visszatérési érték

Nincs.

Megjegyzés

Ha a jelző be van állítva, a rendszer feldolgozza a munkaszimbólum minden ár (tick) változását.

Ha nincs beállítva, a feldolgozási metódus csak új gyertya megjelenésekor fut le a munkaszimbólum megadott idősíkján.
