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

[in] A becsült nyitási ár.

sl

[in]  A Stop Loss megbízás becsült ára.

Visszatérési érték

A kereskedés volumene.

Megjegyzés

A függvény mindig az előre meghatározott, rögzített kereskedési volument adja vissza.
