# Detach


Leválasztja a megadott csomópontot a fáról.

```cpp
bool  Detach(
   CTreeNode*  node      // node
   )
```

Paraméterek

node

[in]  A leválasztandó csomópontra mutató pointer.

Visszatérési érték

Siker esetén true, egyébként false.

Megjegyzés

Leválasztás után a csomópontra mutató pointer nem szabadul fel. A fa kiegyensúlyozott marad.
