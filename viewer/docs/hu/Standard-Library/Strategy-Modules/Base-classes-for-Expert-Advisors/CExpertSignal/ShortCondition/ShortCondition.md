# ShortCondition


Ellenőrzi a short pozíció nyitásának feltételeit.

```cpp
virtual int  ShortCondition()
```

Visszatérési érték

Ha a feltételek teljesülnek, 1 és 100 közötti értéket ad vissza (a jel erősségétől függően). Ha nincs short pozíció nyitására szolgáló jel, 0 értéket ad vissza.

Megjegyzés

Az alaposztály nem valósítja meg a short pozíció nyitási feltételeinek ellenőrzését, ezért mindig 0 értéket ad vissza.
