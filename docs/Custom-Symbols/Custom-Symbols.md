# Custom Symbols

Custom symbols

Functions for creating and editing the custom symbol properties.

When connecting the terminal to a certain trade server, a user is able to [work with time series](../Timeseries-and-Indicators-Access/Timeseries-and-Indicators-Access.md) of the financial symbols provided by a broker. Available financial symbols are displayed as a list in the Market Watch window. A separate group of functions allows [receiving data on the symbol properties](../Market-Info/Market-Info.md), trading sessions and market depth updates.

The group of functions described in this section allows creating custom symbols. To do this, users are able to apply the trade server's existing symbols, text files or external data sources.

| Function | Action |
| --- | --- |
| [CustomSymbolCreate](CustomSymbolCreate/CustomSymbolCreate.md) | Create a custom symbol with the specified name in the specified group |
| [CustomSymbolDelete](CustomSymbolDelete/CustomSymbolDelete.md) | Delete a custom symbol with the specified name |
| [CustomSymbolSetInteger](CustomSymbolSetInteger/CustomSymbolSetInteger.md) | Set the integer type property value for a custom symbol |
| [CustomSymbolSetDouble](CustomSymbolSetDouble/CustomSymbolSetDouble.md) | Set the real type property value for a custom symbol |
| [CustomSymbolSetString](CustomSymbolSetString/CustomSymbolSetString.md) | Set the string type property value for a custom symbol |
| [CustomSymbolSetMarginRate](CustomSymbolSetMarginRate/CustomSymbolSetMarginRate.md) | Set the margin rates depending on the order type and direction for a custom symbol |
| [CustomSymbolSetSessionQuote](CustomSymbolSetSessionQuote/CustomSymbolSetSessionQuote.md) | Set the start and end time of the specified quotation session for the specified symbol and week day |
| [CustomSymbolSetSessionTrade](CustomSymbolSetSessionTrade/CustomSymbolSetSessionTrade.md) | Set the start and end time of the specified trading session for the specified symbol and week day |
| [CustomRatesDelete](CustomRatesDelete/CustomRatesDelete.md) | Delete all bars from the price history of the custom symbol in the specified time interval |
| [CustomRatesReplace](CustomRatesReplace/CustomRatesReplace.md) | Fully replace the price history of the custom symbol within the specified time interval with the data from the MqlRates type array |
| [CustomRatesUpdate](CustomRatesUpdate/CustomRatesUpdate.md) | Add missing bars to the custom symbol history and replace existing data with the ones from the MqlRates type array |
| [CustomTicksAdd](CustomTicksAdd/CustomTicksAdd.md) | Adds data from an array of the MqlTick type to the price history of a custom symbol. The custom symbol must be selected in the Market Watch window |
| [CustomTicksDelete](CustomTicksDelete/CustomTicksDelete.md) | Delete all ticks from the price history of the custom symbol in the specified time interval |
| [CustomTicksReplace](CustomTicksReplace/CustomTicksReplace.md) | Fully replace the price history of the custom symbol within the specified time interval with the data from the MqlTick type array |
| [CustomBookAdd](CustomBookAdd/CustomBookAdd.md) | Passes the status of the Depth of Market for a custom symbol |
