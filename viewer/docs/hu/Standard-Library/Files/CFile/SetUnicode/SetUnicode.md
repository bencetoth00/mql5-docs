# SetUnicode


Beállítja vagy törli a FILE\_UNICODE jelzőt.

```cpp
void  SetUnicode(
   bool  unicode      // flag value
   )
```

Paraméterek

unicode

[in]  A FILE\_UNICODE jelző új értéke.

Megjegyzés

A karakterlánc-műveletek eredménye a FILE\_UNICODE jelzőtől függ. Ha false, ANSI-kódokat (egy bájtos karaktereket) használ. Ha be van állítva, UNICODE-kódokat (két bájtos karaktereket) használ. Ha a fájl már meg van nyitva, a jelző nem módosítható.
