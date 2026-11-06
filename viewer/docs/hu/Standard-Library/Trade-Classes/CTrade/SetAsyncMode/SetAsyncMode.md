# SetAsyncMode


Aszinkron módba állítja a kereskedési műveleteket.

```cpp
void  SetAsyncMode(
   bool  mode      // asynchronous mode flag
   )
```

Paraméterek

mode

[in]  Az aszinkron módot jelző kapcsoló.

Visszatérési érték

Nincs.

Megjegyzés

Ez a mód az aszinkron kereskedési műveletekhez használható, amikor nem várjuk meg az elküldött kérésre érkező kereskedési szerver választ (lásd: [OrderSendAsync](../../../../Trade-Functions/OrderSendAsync/OrderSendAsync.md)).
