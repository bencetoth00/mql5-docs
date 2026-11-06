# IsHermitian


Ellenőrzi, hogy egy négyzetes komplex mátrix Hermitikus-e.

```cpp
bool matrixc::IsHermitian();
```

Visszatérési érték

True értéket ad vissza, ha a négyzetes komplex mátrix Hermitikus.

Megjegyzés

Az n×n méretű nullmátrix Hermitikus. Az átlómátrix csak akkor Hermitikus, ha az átló minden elemének képzetes része 0.

Ez a metódus valós (nem komplex) mátrixra is alkalmazható. Ebben az esetben a szimmetriát ellenőrzi.
