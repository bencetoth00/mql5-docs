# CheckOpenShort


Lekéri a short pozíció kereskedési volumenét.

```cpp
virtual double  CheckOpenShort(
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

A függvény a korábbi ügyletek eredményeit figyelembe véve adja vissza a short pozíció kereskedési volumenét.
