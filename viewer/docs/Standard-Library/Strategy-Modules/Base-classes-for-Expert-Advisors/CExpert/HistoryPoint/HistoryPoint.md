# HistoryPoint


Creates a checkpoint of trade history.

```cpp
void  HistoryPoint(
   bool   from_check_trade=false   // flag
   )
```

Parameters

from\_check\_trade=false

[in]  Flag to avoid recursion.

Note

It saves the amount of positions, orders, deals, and historical orders.