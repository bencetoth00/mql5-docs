# TryGetValue


Lekéri a listaelem értékét a megadott indexen.

```cpp
bool TryGetValue(
   const int  index,     // element index
   T&         value      // a variable for writing
   );
```

Paraméterek

index

[in]  A listaelem indexe.

&value

[out]  Az a változó, amelybe a listaelem megadott értéke kerül.

Visszatérési érték

Siker esetén true, ellenkező esetben false értéket ad vissza.
