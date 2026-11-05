# TerminalInfoString

TerminalInfoString

Returns the value of a corresponding property of the mql5 program environment. The property must be of string type.

|  |
| --- |
| string  TerminalInfoString(     int  property\_id      // identifier of a property     ); |

Parameters

property\_id

[in] Identifier of a property. Can be one of the values of the [ENUM\_TERMINAL\_INFO\_STRING](../../Constants,-Enumerations-and-Structures/Environment-State/Client-Terminal-Properties/Client-Terminal-Properties.md#enum_terminal_info_string) enumeration.

Return Value

Value of string type.

Example:

|  |
| --- |
| //+------------------------------------------------------------------+  //| Script program start function                                    |  //+------------------------------------------------------------------+  void OnStart()    {  //--- get OS and terminal data     string os\_ver  = TerminalInfoString(TERMINAL\_OS\_VERSION);      // user's OS     string name    = TerminalInfoString(TERMINAL\_NAME);            // terminal name     string path    = TerminalInfoString(TERMINAL\_PATH);            // folder the terminal is launched from     string data    = TerminalInfoString(TERMINAL\_DATA\_PATH);       // folder for storing the terminal data     string common  = TerminalInfoString(TERMINAL\_COMMONDATA\_PATH); // common folder for all client terminals installed on the computer     //--- send the obtained data to the journal     PrintFormat("OS: %s\nTerminal: %s\n- Path: %s\n- Data path: %s\n- Common Data path: %s", os\_ver, name, path, data, common);     /\*     OS: Windows 10 build 19045     Terminal: MetaTrader 5     - Path: E:\MetaQuotes\MetaTrader 5     - Data path: E:\MetaQuotes\MetaTrader 5     - Common Data path: C:\Users\admin\AppData\Roaming\MetaQuotes\Terminal\Common     \*/    } |
