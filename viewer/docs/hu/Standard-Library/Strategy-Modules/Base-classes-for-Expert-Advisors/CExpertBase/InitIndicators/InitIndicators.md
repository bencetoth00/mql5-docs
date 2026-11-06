# InitIndicators


Inicializálja az összes indikátort és idősorozatot.

```cpp
virtual bool  InitIndicators(
   CIndicators*  indicators=NULL    // pointer
   )
```

Paraméterek

indicators

[in]  Az indikátorok és idősorozatok gyűjteményére mutató pointer.

Visszatérési érték

Siker esetén true, ellenkező esetben false.

Megjegyzés

Az idősorozatok csak akkor inicializálódnak, ha az objektum az inicializáláskor megadott szimbólumtól vagy idősíktól eltérőt használ.
