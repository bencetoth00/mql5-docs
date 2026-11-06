# Equals


Ellenőrzi, hogy az aktuális kulcs/érték pár megegyezik-e a megadott párral.

```cpp
bool Equals(
   CKeyValuePair<TKeyTValue>*  pair     // the pair to compare
   );
```

Paraméterek

*pair

[in]  Az összehasonlítandó pár.

Visszatérési érték

true értéket ad vissza, ha a kulcs/érték párok megegyeznek, egyébként false értéket.

Megjegyzés

A kulcs/érték párok összehasonlítása a kulcsuk alapján történik.
