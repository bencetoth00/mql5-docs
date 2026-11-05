# ChartSetString


Sets a value for a corresponding property of the specified chart. Chart property must be of the string type. The command is added to chart messages queue and will be executed after processing of all previous commands.

```cpp
bool  ChartSetString(
   long                         chart_id,    // Chart ID
   ENUM_CHART_PROPERTY_STRING   prop_id,     // Property ID
   string                       str_value    // Value
   );
```

Parameters

chart\_id

[in]  Chart ID. 0 means the current chart.

prop\_id

[in]  Chart property ID. Its value can be one of the [ENUM\_CHART\_PROPERTY\_STRING](../../Constants,-Enumerations-and-Structures/Chart-Constants/Chart-Properties/Chart-Properties.md#enum_chart_property_string) values (except the read-only properties).

str\_value

[in]  Property value string. String length cannot exceed 2045 characters (extra characters will be truncated).

Return Value

Returns true if the command has been added to chart queue, otherwise false. To get an information about the [error](../../Constants,-Enumerations-and-Structures/Codes-of-Errors-and-Warnings/Runtime-Errors/Runtime-Errors.md), call the [GetLastError()](../../Checkup/GetLastError/GetLastError.md) function.

Note

ChartSetString can be used for a comment output on the chart instead of the [Comment](../../Common-Functions/Comment/Comment.md) function.

The function is asynchronous, which means that the function does not wait for the execution of the command, which has been successfully added to the queue of specified the chart. Instead, it immediately returns control. The property will only change after the handling of the appropriate command from the chart queue. To immediately execute commands from the chart queue, call the [ChartRedraw](../ChartRedraw/ChartRedraw.md) function.

If you want to immediately change several chart properties at once, then the corresponding functions ([ChartSetString](ChartSetString.md), [ChartSetDouble](../ChartSetDouble/ChartSetDouble.md), [ChartSetString](ChartSetString.md)) should be executed in one code block, after which you should call [ChartRedraw](../ChartRedraw/ChartRedraw.md) once.

To check the command execution result, you can use a function, which requests the specified chart property ([ChartGetInteger](../ChartGetInteger/ChartGetInteger.md), [ChartGetDouble](../ChartGetDouble/ChartGetDouble.md), [ChartSetString](ChartSetString.md)). However, note that these functions are synchronous and wait for execution results.

Example:

```cpp
void OnTick()
  {
//---
   double Ask,Bid;
   int Spread;
   Ask=SymbolInfoDouble(Symbol(),SYMBOL_ASK);
   Bid=SymbolInfoDouble(Symbol(),SYMBOL_BID);
   Spread=SymbolInfoInteger(Symbol(),SYMBOL_SPREAD);
   string comment=StringFormat("Display prices:\nAsk = %G\nBid = %G\nSpread = %d",
                               Ask,Bid,Spread);
   ChartSetString(0,CHART_COMMENT,comment);
  }
```

See also

[Comment](../../Common-Functions/Comment/Comment.md), [ChartGetString](../ChartGetString/ChartGetString.md)