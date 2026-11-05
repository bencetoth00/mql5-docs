# FormatRequestResult


Prepares the formatted string with results of the last request execution.

```cpp
string  FormatRequestResult(
   string&                 str,         // string
   const MqlTradeRequest&  request,     // request
   const MqlTradeResult&   result       // result
   ) const
```

Parameters

str

[in]  Target string passed by reference.

request

[in]   A structure of [MqlTradeRequest](../../../../Constants,-Enumerations-and-Structures/Data-Structures/Trade-Request-Structure/Trade-Request-Structure.md) type with parameters of the last request.

result

[in]   A structure of [MqlTradeResult](../../../../Constants,-Enumerations-and-Structures/Data-Structures/Trade-Request-Result-Structure/Trade-Request-Result-Structure.md) type with results of the last request.

Return Value

None.