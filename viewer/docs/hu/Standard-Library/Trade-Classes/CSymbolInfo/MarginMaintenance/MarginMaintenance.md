# MarginMaintenance


Lekéri a fenntartási letét értékét.

```cpp
double  MarginMaintenance()
```

Visszatérési érték

A fenntartási letét értéke.

Megjegyzés

Azt a letétösszeget adja vissza (az instrumentum letéti pénznemében), amelyet egy lot után számítanak fel. A számla állapotának változásakor az ügyfél saját tőkéjének ellenőrzésére használják. Ha a fenntartási letét értéke 0, akkor a kezdeti letétet használja.

A szimbólumot a [Name](../Name/Name.md) metódussal kell kiválasztani.
