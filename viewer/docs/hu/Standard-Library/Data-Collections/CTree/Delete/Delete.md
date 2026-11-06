# Delete


Törli a megadott csomópontot a fából.

```cpp
bool  Delete(
   CTreeNode*  node      // node
   )
```

Paraméterek

node

[in]  A törlendő csomópontra mutató pointer.

Visszatérési érték

Siker esetén true, egyébként false.

Megjegyzés

Törlés után a csomópontra mutató pointer felszabadul. A fa kiegyensúlyozott marad.
