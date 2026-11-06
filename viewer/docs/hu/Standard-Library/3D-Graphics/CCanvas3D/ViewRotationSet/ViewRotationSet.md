# ViewRotationSet


Beállítja a 3D-s jelenet felé irányuló nézés irányát.

```cpp
void  ViewRotationSet(
   const DXVector3  &rotation      // vector of turning angles
   );
```

Paraméterek

&rotation

[in]  Az Euler-szögeket tartalmazó vektor, amelyből a 3D-s jelenet felé irányuló nézés iránya számítható.

Visszatérési érték

Nincs.

Megjegyzés

A nézés irányának ViewRotationSet() metódussal történő beállítása módosítja a [ViewMatrixGet()](../ViewMatrixGet/ViewMatrixGet.md) metódussal lekért nézeti mátrixot.
