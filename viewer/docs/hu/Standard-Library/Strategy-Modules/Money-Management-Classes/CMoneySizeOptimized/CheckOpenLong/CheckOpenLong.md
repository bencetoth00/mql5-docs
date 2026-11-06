# CheckOpenLong


Lekéri a long pozíció kereskedési volumenét.

```cpp
virtual double  CheckOpenLong(
   double  price,     // price
   double  sl         // Stop Loss price
   )
```

Paraméterek

price

[in]  A becsült nyitási ár.

sl

[in]  A Stop Loss becsült ára.

Visszatérési érték

A long pozíció kereskedési volumene.

Megjegyzés

A függvény a korábbi ügyletek eredményeit figyelembe véve adja vissza a long pozíció kereskedési volumenét.
