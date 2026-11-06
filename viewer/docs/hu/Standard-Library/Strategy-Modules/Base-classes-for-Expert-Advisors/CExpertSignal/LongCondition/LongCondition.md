# LongCondition


Ellenőrzi a long pozíció nyitásának feltételeit.

```cpp
virtual int  LongCondition()
```

Visszatérési érték

Ha a feltételek teljesülnek, 1 és 100 közötti értéket ad vissza (a jel erősségétől függően). Ha nincs long pozíció nyitására szolgáló jel, 0 értéket ad vissza.

Megjegyzés

Az alaposztály nem valósítja meg a long pozíció nyitási feltételeinek ellenőrzését, ezért mindig 0 értéket ad vissza.
