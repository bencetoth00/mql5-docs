# Market Info

Getting Market Information

These are functions intended for receiving information about the market state.

| Function | Action |
| --- | --- |
| [SymbolsTotal](SymbolsTotal/SymbolsTotal.md) | Returns the number of available (selected in Market Watch or all) symbols |
| [SymbolExist](SymbolExist/SymbolExist.md) | Checks if a symbol with a specified name exists |
| [SymbolName](SymbolName/SymbolName.md) | Returns the name of a specified symbol |
| [SymbolSelect](SymbolSelect/SymbolSelect.md) | Selects a symbol in the Market Watch window or removes a symbol from the window |
| [SymbolIsSynchronized](SymbolIsSynchronized/SymbolIsSynchronized.md) | Checks whether data of a selected symbol in the terminal are [synchronized](../Timeseries-and-Indicators-Access/Organizing-Data-Access/Organizing-Data-Access.md#synchronized) with data on the trade server |
| [SymbolInfoDouble](SymbolInfoDouble/SymbolInfoDouble.md) | Returns the double value of the symbol for the corresponding property |
| [SymbolInfoInteger](SymbolInfoInteger/SymbolInfoInteger.md) | Returns a value of an integer type (long, datetime, int or bool) of a specified symbol for the corresponding property |
| [SymbolInfoString](SymbolInfoString/SymbolInfoString.md) | Returns a value of the string type of a specified symbol for the corresponding property |
| [SymbolInfoMarginRate](SymbolInfoMarginRate/SymbolInfoMarginRate.md) | Returns the margin rates depending on the order type and direction |
| [SymbolInfoTick](SymbolInfoTick/SymbolInfoTick.md) | Returns the current prices for the specified symbol in a variable of the [MqlTick](../Constants,-Enumerations-and-Structures/Data-Structures/Price-Data-Structure/Price-Data-Structure.md) type |
| [SymbolInfoSessionQuote](SymbolInfoSessionQuote/SymbolInfoSessionQuote.md) | Allows receiving time of beginning and end of the specified quoting sessions for a specified symbol and day of week. |
| [SymbolInfoSessionTrade](SymbolInfoSessionTrade/SymbolInfoSessionTrade.md) | Allows receiving time of beginning and end of the specified trading sessions for a specified symbol and day of week. |
| [MarketBookAdd](MarketBookAdd/MarketBookAdd.md) | Provides opening of Depth of Market for a selected symbol, and subscribes for receiving notifications of the DOM changes |
| [MarketBookRelease](MarketBookRelease/MarketBookRelease.md) | Provides closing of Depth of Market for a selected symbol, and cancels the subscription for receiving notifications of the DOM changes |
| [MarketBookGet](MarketBookGet/MarketBookGet.md) | Returns a structure array [MqlBookInfo](../Constants,-Enumerations-and-Structures/Data-Structures/Order-Book-Structure/Order-Book-Structure.md) containing records of the Depth of Market of a specified symbol |
