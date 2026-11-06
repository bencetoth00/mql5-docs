# TrySetValue


Módosítja a gyűjtemény kulcs/érték párjának értékét a megadott kulcsnál.

```cpp
bool TrySetValue(
   TKey    key,      // key
   TValue  value     // new value
   );
```

Paraméterek

key

[in]  A kulcs.

value

[in] Az adott kulcs/érték párhoz rendelendő új érték.

Visszatérési érték

Sikeres végrehajtás esetén true, egyébként false.
