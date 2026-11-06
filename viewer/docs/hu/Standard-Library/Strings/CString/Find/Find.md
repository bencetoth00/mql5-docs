# Find


Megkeresi egy részkarakterlánc első előfordulását a megadott pozíciótól kezdve.

```cpp
int  Find(
   uint          start,         // position
   const string  substring      // substring
   ) const;
```

Paraméterek

start

[in]  A részkarakterlánc-keresés kezdőpozíciója.

substring

[in]  A keresendő részkarakterlánc.

Visszatérési érték

A részkarakterlánc első előfordulásának indexe (-1, ha a részkarakterlánc nem található).
