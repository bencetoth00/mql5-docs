# CheckReverse


Lekéri a pozíció megfordításához szükséges volument.

```cpp
virtual double  CheckReverse(
   CPositionInfo*  position,     // pointer
   double          sl            // Stop Loss
   )
```

Paraméterek

position

[in]  A [CPositionInfo](../../../../Trade-Classes/CPositionInfo/CPositionInfo.md) osztály objektumára mutató pointer.

sl

[in]  A Stop Loss ára.

Visszatérési érték

A pozíció megfordításához szükséges volumen.
