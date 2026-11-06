# OnDragProcess


A „DragProcess” (húzás) esemény virtuális kezelője.

```cpp
virtual bool  OnDragProcess(
   const int  x,     // x coordinate
   const int  y      // y coordinate
   )
```

Paraméterek

x

[in] Az egérmutató aktuális X koordinátája.

y

[in]  Az egérmutató aktuális Y koordinátája.

Visszatérési érték

true, ha az esemény feldolgozása megtörtént, egyébként false.

Megjegyzés

A „DragProcess” esemény akkor következik be, amikor a vezérlőt húzzák.
