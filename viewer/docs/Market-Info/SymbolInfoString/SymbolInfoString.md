# SymbolInfoString


Returns the corresponding property of a specified symbol. There are 2 variants of the function.

1. Immediately returns the property value.

```cpp
string  SymbolInfoString(
   string                   name,        // Symbol
   ENUM_SYMBOL_INFO_STRING  prop_id      // Property identifier
   );
```

2. Returns true or false, depending on the success of a function. If successful, the value of the property is placed in a placeholder variable passed by reference in the last parameter.

```cpp
bool  SymbolInfoString(
   string                   name,        // Symbol
   ENUM_SYMBOL_INFO_STRING  prop_id,     // Property identifier
   string&                  string_var   // here we accept the property value
   );
```

Parameters

name

[in] Symbol name.

prop\_id

[in] Identifier of a symbol property. The value can be one of the values of the [ENUM\_SYMBOL\_INFO\_STRING](../../Constants,-Enumerations-and-Structures/Environment-State/Symbol-Properties/Symbol-Properties.md#enum_symbol_info_string) enumeration.

string\_var

[out] Variable of the string type receiving the value of the requested property.

Return Value

The value of string type. In case of execution failure, information about the [error](../../Constants,-Enumerations-and-Structures/Codes-of-Errors-and-Warnings/Runtime-Errors/Runtime-Errors.md) can be obtained using [GetLastError()](../../Checkup/GetLastError/GetLastError.md) function:

- 5040 – invalid string parameter for specifying a symbol name,
- 4301 – unknown symbol (financial instrument),
- 4302 – symbol is not selected in "Market Watch" (not found in the list of available ones),
- 4303 – invalid identifier of a symbol property.

Note

It is recommended to use [SymbolInfoTick()](../SymbolInfoTick/SymbolInfoTick.md) if the function is used for getting information about the last tick. It may well be that not a single quote has appeared yet since the terminal is connected to a trading account. In such a case, the requested value will be indefinite.

In most cases, it is enough to use [SymbolInfoTick()](../SymbolInfoTick/SymbolInfoTick.md) function allowing a user to receive the values of Ask, Bid, Last, Volume and the time of the last tick's arrival during a single call.

Example:

```cpp
#define SYMBOL_NAME "USDJPY"
//+------------------------------------------------------------------+
//| Script program start function                                    |
//+------------------------------------------------------------------+
void OnStart()
  {
//--- get string data for SYMBOL_NAME symbol
   string currency_base   = SymbolInfoString(SYMBOL_NAME, SYMBOL_CURRENCY_BASE);    // Base currency of the symbol
   string currency_profit = SymbolInfoString(SYMBOL_NAME, SYMBOL_CURRENCY_PROFIT);  // Profit currency
   string currency_margin = SymbolInfoString(SYMBOL_NAME, SYMBOL_CURRENCY_MARGIN);  // Margin currency
   string symbol_descript = SymbolInfoString(SYMBOL_NAME, SYMBOL_DESCRIPTION);      // String description of the symbol
//--- create a message text with the obtained data
   string text=StringFormat("Symbol %s:\n"+
                            "- Currency Base: %s\n"+
                            "- Currensy Profit: %s\n"+
                            "- Currency Margin: %s\n"+
                            "- Symbol Description: %s",
                            SYMBOL_NAME, currency_base,
                            currency_profit, currency_margin,
                            symbol_descript);
//--- send the obtained data to the journal
   Print(text);
   /*
   Symbol USDJPY:
   - Currency Base: USD
   - Currensy Profit: JPY
   - Currency Margin: USD
   - Symbol Description: US Dollar vs Yen
   */
  }
```