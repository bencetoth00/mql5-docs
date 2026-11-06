# LoadNode


Fájlból olvassa be a csomópont adatait.

```cpp
bool  LoadNode(
   int         file_handle,     // handle
   CTreeNode*  main             // node
   )
```

Paraméterek

file\_handle

[in] Bináris fájl kezelője, amelyet korábban olvasásra nyitottak meg.

main

[in]  Az adatokat tartalmazó csomópont.

Visszatérési érték

Siker esetén true, egyébként false.
