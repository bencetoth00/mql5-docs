# MQLInfoString

MQLInfoString

Returns the value of a corresponding property of a running mql5 program.

|  |
| --- |
| string  MQLInfoString(     int  property\_id      // Identifier of a property     ); |

Parameters

property\_id

[in] Identifier of a property. Can be one of the [ENUM\_MQL\_INFO\_STRING](../../Constants,-Enumerations-and-Structures/Environment-State/Running-MQL5-Program-Properties/Running-MQL5-Program-Properties.md#enum_mql_info_string) enumeration.

Return Value

Value of string type.

Example:

|  |
| --- |
| //+------------------------------------------------------------------+  //| Script program start function                                    |  //+------------------------------------------------------------------+  void OnStart()    {  //--- get the launched program data     string name = MQLInfoString(MQL\_PROGRAM\_NAME);  // name of the launched MQL5 program     string path = MQLInfoString(MQL\_PROGRAM\_PATH);  // running program path       //--- send the obtained data to the journal     PrintFormat("Name of the running MQL program: '%s'\nPath of the running MQL program: %s", name, path);     /\*     result:     Name of the running MQL program: 'MQLInfoString'     Path of the running MQL program: E:\MetaQuotes\MetaTrader 5\MQL5\Scripts\MQLInfoString.ex5     \*/    } |
