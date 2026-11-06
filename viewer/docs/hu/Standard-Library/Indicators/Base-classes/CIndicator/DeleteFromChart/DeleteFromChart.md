# DeleteFromChart


Eltávolítja az indikátort a diagramról.

```cpp
bool  DeleteFromChart(
   const long  chart,     // chart ID
   const int  subwin      // subwindow index
   )
```

Paraméterek

chart

[in]  A diagram azonosítója.

subwin

[in]  A diagram alablakának indexe.

Visszatérési érték

Siker esetén true, ha az indikátor nem távolítható el a diagramról, false.
