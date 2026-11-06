# FolderClean


Kiüríti a megadott mappát.

```cpp
bool  FolderClean(
   const string  folder_name      // folder name
   )
```

Paraméterek

folder\_name

[in]  A kiürítendő mappa neve. A FILE\_COMMON jelző által meghatározott mappához viszonyított elérési utat tartalmazza.

Visszatérési érték

Siker esetén true, false, ha a mappa nem módosítható.

Megjegyzés

A munkamappa helye a SetCommon() metódussal korábban beállított vagy visszaállított jelzőtől függ.
