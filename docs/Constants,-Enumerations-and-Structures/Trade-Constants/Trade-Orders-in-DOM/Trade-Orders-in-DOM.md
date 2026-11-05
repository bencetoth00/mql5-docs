# Trade Orders in DOM

Trade Orders in Depth Of Market

For equity securities, the Depth of Market window is available, where you can see the current Buy and Sell orders. Desired direction of a trade operation, required amount and requested price are specified for each order.

To obtain information about the current state of the DOM by MQL5 means, the [MarketBookGet()](../../../Market-Info/MarketBookGet/MarketBookGet.md) function is used, which places the DOM "screen shot" into the [MqlBookInfo](../../Data-Structures/Order-Book-Structure/Order-Book-Structure.md) array of structures. Each element of the array in the type field contains information about the direction of the order - the value of the ENUM\_BOOK\_TYPE enumeration.

ENUM\_BOOK\_TYPE

| Identifier | Description |
| --- | --- |
| BOOK\_TYPE\_SELL | Sell order (Offer) |
| BOOK\_TYPE\_BUY | Buy order (Bid) |
| BOOK\_TYPE\_SELL\_MARKET | Sell order by Market |
| BOOK\_TYPE\_BUY\_MARKET | Buy order by Market |

See also

[Structures and classes](../../../Language-Basics/Data-Types/Structures,-Classes-and-Interfaces/Structures,-Classes-and-Interfaces.md), [Structure of the DOM](../../Data-Structures/Order-Book-Structure/Order-Book-Structure.md), [Trade operation types](../Trade-Operation-Types/Trade-Operation-Types.md), [Market Info](../../../Market-Info/Market-Info.md)
