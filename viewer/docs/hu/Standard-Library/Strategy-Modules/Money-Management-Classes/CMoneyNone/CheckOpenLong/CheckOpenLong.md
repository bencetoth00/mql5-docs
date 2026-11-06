# CheckOpenLong


Lekéri a hosszú pozíció kereskedési volumenét.

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

[in]  A becsült Stop Loss ár.

Visszatérési érték

A hosszú pozíció kereskedési volumene.

Megjegyzés

A függvény mindig a minimális lotméretet adja vissza.
