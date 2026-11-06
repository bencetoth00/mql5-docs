# RefreshCurrent


Frissíti az aktuális (nulladik) pufferelemet.

```cpp
bool  RefreshCurrent(
   const int  handle,     // handle of the indicator
   const int  num         // buffer number
   )
```

Paraméterek

handle

[in]  Az indikátor kezelője.

num

[in]  Az indikátorpuffer sorszáma.

Visszatérési érték

Siker esetén true, ha a puffer nem frissíthető, false.
