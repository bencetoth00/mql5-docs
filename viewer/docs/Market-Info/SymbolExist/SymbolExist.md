# SymbolExist


Checks if a symbol with a specified name exists.

```cpp
bool  SymbolExist(
   const string  name,    // symbol name
   bool&   is_custom      // custom symbol property
   );
```

Parameters

name

[in]  Symbol name.

is\_custom

[out]  Custom symbol property set upon successful execution. If true, the detected symbol is a [custom](../../Custom-Symbols/Custom-Symbols.md) one.

Return Value

If false, the symbol is not found among standard and [custom ones](../../Custom-Symbols/Custom-Symbols.md).

Example:

```cpp
#define SYMBOL_NAME "GBPUSDn"
//+------------------------------------------------------------------+
//| Script program start function                                    |
//+------------------------------------------------------------------+
void OnStart()
  {
//--- declare the custom symbol flag and check the presence of a symbol having its name specified in SYMBOL_NAME
   bool custom = false;
   bool result = SymbolExist(SYMBOL_NAME, custom);
//--- declare the default 'symbol not found' message text
   string text = StringFormat("The symbol '%s' was not found among either the standard or custom symbols.", SYMBOL_NAME);
//--- if a symbol is found, create a message text depending on which list the symbol is found in
   if(result)
     {
      //--- if this is a standard symbol
      if(!custom)
         text = StringFormat("The '%s' symbol is available on the server.", SYMBOL_NAME);
      //--- if this is a custom symbol
      else
         text = StringFormat("The symbol '%s' was found in the list of custom symbols.", SYMBOL_NAME);
     }
//--- send the message about the check result to the journal
   Print(text);
   /*
   result for standard 'GBPUSD' symbol:
   The 'GBPUSD' symbol is available on the server.
   result for custom 'GBPUSDx' symbol:
   The symbol 'GBPUSDx' was found in the list of custom symbols.
   result for missing 'GBPUSDn' symbol:
   The symbol 'GBPUSDn' was not found among either the standard or custom symbols.
   */
  }
```

See also

[SymbolsTotal](../SymbolsTotal/SymbolsTotal.md), [SymbolSelect](../SymbolSelect/SymbolSelect.md), [Custom symbols](../../Custom-Symbols/Custom-Symbols.md)