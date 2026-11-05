# SymbolIsSynchronized

SymbolIsSynchronized

The function checks whether data of a selected symbol in the terminal are synchronized with data on the trade server.

|  |
| --- |
| bool  SymbolIsSynchronized(     string  name,       // symbol name     ); |

Parameters

name

[in]  Symbol name.

Return value

If data are [synchronized](../../Timeseries-and-Indicators-Access/Organizing-Data-Access/Organizing-Data-Access.md#synchronized), returns 'true'; otherwise returns 'false'.

Example:

|  |
| --- |
| #define SYMBOL\_NAME "EURUSD"     //+------------------------------------------------------------------+  //| Script program start function                                    |  //+------------------------------------------------------------------+  void OnStart()    {  //--- get the flag for synchronizing data in the terminal using the 'SYMBOL\_NAME' symbol with the server data     bool   sync = SymbolIsSynchronized(SYMBOL\_NAME);       //--- create a message depending on the synchronization flag     string text = StringFormat("The data on the '%s' symbol in the terminal is synchronized with the data on the trading server.", SYMBOL\_NAME);     if(!sync)        text = StringFormat("The data for the '%s' symbol in the terminal is not synchronized with the data on the trading server.", SYMBOL\_NAME);       //--- send the obtained result to the journal     Print(text);          /\*     result for synchronized data:     The data on the 'EURUSD' symbol in the terminal is synchronized with the data on the trading server.          result for data not yet synchronized:     The data for the 'GBPHKD' symbol in the terminal is not synchronized with the data on the trading server.     \*/    } |

See also

[SymbolInfoInteger](../SymbolInfoInteger/SymbolInfoInteger.md), [Organizing Data Access](../../Timeseries-and-Indicators-Access/Organizing-Data-Access/Organizing-Data-Access.md)
