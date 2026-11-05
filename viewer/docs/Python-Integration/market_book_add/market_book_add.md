# market_book_add

market\_book\_add

Subscribes the MetaTrader 5 terminal to the Market Depth change events for a specified symbol.

```cpp
market_book_add(
   symbol      // financial instrument name
)
```

symbol

[in]  Financial instrument name. Required unnamed parameter.

Return Value

True if successful, otherwise – False.

Note

The function is similar to [MarketBookAdd](../../Market-Info/MarketBookAdd/MarketBookAdd.md).

 

See also

[market\_book\_get](../market_book_get/market_book_get.md), [market\_book\_release](../market_book_release/market_book_release.md), [Market Depth structure](../../Constants,-Enumerations-and-Structures/Data-Structures/Order-Book-Structure/Order-Book-Structure.md)