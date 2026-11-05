# MemoryTotal


Gets the information about the total memory available to the terminal/agent (in Mb).

```cpp
int  MemoryTotal() const
```

Return Value

Total memory (in Mb) available to the terminal/agent.

Note

The total memory available to the terminal/agent is defined by [TerminalInfoInteger()](../../../../Checkup/TerminalInfoInteger/TerminalInfoInteger.md) function ([TERMINAL\_MEMORY\_TOTAL](../../../../Constants,-Enumerations-and-Structures/Environment-State/Client-Terminal-Properties/Client-Terminal-Properties.md#enum_terminal_info_integer) property).