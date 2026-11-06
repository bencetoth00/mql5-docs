# TryGetValue


Lekéri a megadott kulcshoz tartozó elemet a hash táblából.

```cpp
bool TryGetValue(
   TKey     key,      // key
   TValue&  value     // a variable for writing the value
   );
```

Paraméterek

key

[in]  Kulcs.

&value

[out]  Az a változó, amelybe a kulcs/érték pár megadott értéke kerül.

Visszatérési érték

Siker esetén true, ellenkező esetben false értéket ad vissza.
