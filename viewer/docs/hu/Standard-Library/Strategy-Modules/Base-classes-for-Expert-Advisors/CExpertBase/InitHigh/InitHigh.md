# InitHigh


Inicializálja a High idősorozatot.

```cpp
bool  InitHigh(
   CIndicators*  indicators    // pointer
   )
```

Paraméterek

indicators

[in]  Az indikátorok és idősorozatok gyűjteményére mutató pointer.

Visszatérési érték

Siker esetén true, ellenkező esetben false.

Megjegyzés

A High idősorozat csak akkor inicializálódik, ha az objektum az első inicializáláskor megadott szimbólumtól vagy idősíktól eltérőt használ, és az idősorozatra később is szükség van.
