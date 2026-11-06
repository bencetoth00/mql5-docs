# CheckOpenShort


Lekéri a rövid pozíció kereskedési volumenét.

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

[in]  A becsült Stop Loss ár.

Visszatérési érték

A rövid pozíció kereskedési volumene.

Megjegyzés

A függvény mindig a minimális lotméretet adja vissza.
