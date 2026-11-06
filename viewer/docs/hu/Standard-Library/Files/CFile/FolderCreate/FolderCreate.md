# FolderCreate


Létrehoz egy új mappát.

```cpp
bool  FolderCreate(
   const string  folder_name      // folder name
   )
```

Paraméterek

folder\_name

[in]  A létrehozandó mappa neve. A FILE\_COMMON jelző által meghatározott mappához viszonyított elérési utat tartalmazza.

Visszatérési érték

Siker esetén true, false, ha a mappa nem hozható létre.

Megjegyzés

A munkamappa helye attól a jelzőtől függ, amelyet korábban a SetCommon() metódussal állítottak be vagy visszaállítottak.
