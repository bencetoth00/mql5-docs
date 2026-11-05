# IsConnected


Gets the information about connection to trade server.

```cpp
bool  IsConnected() const
```

Return Value

true - the terminal is connected to a trade server, otherwise - false.

Note

Connection status is defined by [TerminalInfoInteger()](../../../../Checkup/TerminalInfoInteger/TerminalInfoInteger.md) function ([TERMINAL\_CONNECTED](../../../../Constants,-Enumerations-and-Structures/Environment-State/Client-Terminal-Properties/Client-Terminal-Properties.md#enum_terminal_info_integer) property).