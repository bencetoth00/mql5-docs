# InitTrade


Inicializálja a kereskedési objektumot.

```cpp
virtual bool  InitTrade(
   ulong            magic,       // identifier
   CExpertTrade*    trade=NULL   // pointer
   )
```

Paraméterek

magic

[in]  Az Expert Advisor azonosítója (a kereskedési kérésekben használatos).

trade

[in]  Pointer a kereskedési objektumra.

Visszatérési érték

Siker esetén true, egyébként false.
