# Open


Megnyitja a megadott szövegfájlt, és siker esetén hozzárendeli az osztálypéldányhoz.

```cpp
int  Open(
   const string  file_name,     // file name
   int           flags          // flags
   )
```

Paraméterek

file\_name

[in]  A megnyitandó fájl neve.

flags

[in]  Fájlmegnyitási jelzők (a FILE\_TXT jelző kötelezően be van állítva).

Visszatérési érték

A megnyitott fájl kezelője.
