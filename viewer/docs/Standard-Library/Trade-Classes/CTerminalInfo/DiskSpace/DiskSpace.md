# DiskSpace


Gets the information about free disk space available for MQL5\Files folder of the terminal/agent (in Mb).

```cpp
int  MDiskSpace() const
```

Return Value

Free disk space.

Note

Free disk space is defined by [TerminalInfoInteger()](../../../../Checkup/TerminalInfoInteger/TerminalInfoInteger.md) function ([TERMINAL\_DISK\_SPACE](../../../../Constants,-Enumerations-and-Structures/Environment-State/Client-Terminal-Properties/Client-Terminal-Properties.md#enum_terminal_info_integer) property).