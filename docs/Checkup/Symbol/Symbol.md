# Symbol

Symbol

Returns the name of a symbol of the current chart.

|  |
| --- |
| string  Symbol(); |

Return Value

Value of the [\_Symbol](../../Predefined-Variables/_Symbol/_Symbol.md) system variable, which stores the name of the current chart symbol.

Note

Unlike Expert Advisors, indicators and scripts, services are not bound to a specific chart. Therefore, [Symbol()](Symbol.md) returns an empty string ("") for a service.

Example:

|  |
| --- |
| //+------------------------------------------------------------------+  //| Script program start function                                    |  //+------------------------------------------------------------------+  void OnStart()    {  //--- get the current chart symbol name     string name = Symbol();       //--- send the obtained data to the journal     PrintFormat("Current chart symbol name: '%s'", name);     /\*     result     Current chart symbol name: 'EURUSD'     \*/    } |
