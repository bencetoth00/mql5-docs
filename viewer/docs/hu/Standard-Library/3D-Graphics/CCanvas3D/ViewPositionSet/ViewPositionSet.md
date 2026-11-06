# ViewPositionSet


Beállítja a nézőpontot egy 3D-s jelenetben.

```cpp
void  ViewPositionSet(
   const DXVector3  &position      // viewpoint position
   );
```

Paraméterek

&position

[in]  A 3D-s jelenet nézőpontjának beállítása.

Visszatérési érték

Nincs.

Megjegyzés

A nézőpont ViewPositionSet() metódussal történő beállítása módosítja a [ViewMatrixGet()](../ViewMatrixGet/ViewMatrixGet.md) metódussal lekért nézeti mátrixot.
