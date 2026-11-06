# TryGetValue


Lekéri a lista megadott indexű elemét.

```cpp
bool TryGetValue(
   const int  index,     // index
   T&         value      // a variable to write
   );
```

Paraméterek

index

[in]  Annak a listaelemnek az indexe, amelynek az értékét le kell kérni.

&value

[out]  A változó, amelybe az elem értéke kerül.

Visszatérési érték

Siker esetén true, ellenkező esetben false értéket ad vissza.
