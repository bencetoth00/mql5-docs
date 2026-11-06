# SelectByMagic


Kiválaszt egy pozíciót a pénzügyi eszköz neve és a magic szám alapján a további műveletekhez.

```cpp
bool  SelectByMagic(
   const string  symbol, // symbol name
   const ulong   magic   // magic number
   );
```

Paraméterek

symbol

[in]  A szimbólum neve.

magic

[in]  A pozíció magic száma.

Visszatérési érték

Siker esetén true, sikertelen kiválasztás esetén false.
