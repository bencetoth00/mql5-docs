# SymbolInfoDouble

SymbolInfoDouble

Returns the corresponding property of a specified symbol. There are 2 variants of the function.

1. Immediately returns the property value.

|  |
| --- |
| double  SymbolInfoDouble(     string                   name,       // symbol     ENUM\_SYMBOL\_INFO\_DOUBLE  prop\_id     // identifier of the property     ); |

2. Returns true or false depending on whether a function is successfully performed. In case of success, the value of the property is placed into a recipient variable, passed by reference by the last parameter.

|  |
| --- |
| bool  SymbolInfoDouble(     string                   name,       // symbol     ENUM\_SYMBOL\_INFO\_DOUBLE  prop\_id,    // identifier of the property     double&                  double\_var  // here we accept the property value     ); |

Parameters

name

[in] Symbol name.

prop\_id

[in] Identifier of a symbol property. The value can be one of the values of the [ENUM\_SYMBOL\_INFO\_DOUBLE](../../Constants,-Enumerations-and-Structures/Environment-State/Symbol-Properties/Symbol-Properties.md#enum_symbol_info_double) enumeration.

double\_var

[out] Variable of double type receiving the value of the requested property.

Return Value

The value of double type. In case of execution failure, information about the [error](../../Constants,-Enumerations-and-Structures/Codes-of-Errors-and-Warnings/Runtime-Errors/Runtime-Errors.md) can be obtained using [GetLastError()](../../Checkup/GetLastError/GetLastError.md) function:

- 5040 – invalid string parameter for specifying a symbol name,
- 4301 – unknown symbol (financial instrument),
- 4302 – symbol is not selected in "Market Watch" (not found in the list of available ones),
- 4303 – invalid identifier of a symbol property.

Note

It is recommended to use [SymbolInfoTick()](../SymbolInfoTick/SymbolInfoTick.md) if the function is used for getting information about the last tick. It may well be that not a single quote has appeared yet since the terminal is connected to a trading account. In such a case, the requested value will be indefinite.

In most cases, it is enough to use [SymbolInfoTick()](../SymbolInfoTick/SymbolInfoTick.md) function allowing a user to receive the values of Ask, Bid, Last, Volume and the time of the last tick's arrival during a single call.

The [SymbolInfoMarginRate()](../SymbolInfoMarginRate/SymbolInfoMarginRate.md) function provides data on the amount of charged margin depending on the order type and direction.

Example:

|  |
| --- |
| void OnTick()    {  //--- obtain spread from the symbol properties     bool spreadfloat=SymbolInfoInteger(Symbol(),SYMBOL\_SPREAD\_FLOAT);     string comm=StringFormat("Spread %s = %I64d points\r\n",                              spreadfloat?"floating":"fixed",                              SymbolInfoInteger(Symbol(),SYMBOL\_SPREAD));  //--- now let's calculate the spread by ourselves     double ask=SymbolInfoDouble(Symbol(),SYMBOL\_ASK);     double bid=SymbolInfoDouble(Symbol(),SYMBOL\_BID);     double spread=ask-bid;     int spread\_points=(int)MathRound(spread/SymbolInfoDouble(Symbol(),SYMBOL\_POINT));     comm=comm+"Calculated spread = "+(string)spread\_points+" points";     Comment(comm);    } |
