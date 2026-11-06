# Seek


Beállítja a fájlmutató pozícióját.

```cpp
void  Seek(
   long                offset,     // offset
   ENUM_FILE_POSITION  origin      // origin
   )
```

Paraméterek

offset

[in]  Eltolás a fájlban bájtokban (negatív is lehet).

origin

[in]  Az eltolás kiindulópontja.

Visszatérési érték

Siker esetén true, ha a fájlmutató nem módosítható, false.
