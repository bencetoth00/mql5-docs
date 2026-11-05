# TerminalInfoInteger

TerminalInfoInteger

Returns the value of a corresponding property of the mql5 program environment.

|  |
| --- |
| int  TerminalInfoInteger(     int  property\_id      // identifier of a property     ); |

Parameters

property\_id

[in] Identifier of a property. Can be one of the values of the [ENUM\_TERMINAL\_INFO\_INTEGER](../../Constants,-Enumerations-and-Structures/Environment-State/Client-Terminal-Properties/Client-Terminal-Properties.md#enum_terminal_info_integer) enumeration.

Return Value

Value of int type.

Example:

|  |
| --- |
| //+------------------------------------------------------------------+  //| Script program start function                                    |  //+------------------------------------------------------------------+  void OnStart()    {  //--- get the build number of the running terminal and its "64-bit terminal" property     int  build = TerminalInfoInteger(TERMINAL\_BUILD);     bool x64   = TerminalInfoInteger(TERMINAL\_X64);       //--- print the obtained terminal data in the journal     PrintFormat("MetaTrader 5 %s build %d", (x64 ? "x64" : "x32"), build);     /\*     result:     MetaTrader 5 x64 build 4330     \*/    } |
