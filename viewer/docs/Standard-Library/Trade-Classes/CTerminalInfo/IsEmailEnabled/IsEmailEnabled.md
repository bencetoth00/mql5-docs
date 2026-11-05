# IsEmailEnabled


Gets the information about permission to send e-mails to SMTP server and login specified in the terminal settings.

```cpp
bool  IsEmailEnabled() const
```

Return Value

true - sending e-mails is allowed, otherwise - false.

Note

Permission to send e-mails is defined by [TerminalInfoInteger()](../../../../Checkup/TerminalInfoInteger/TerminalInfoInteger.md) function ([TERMINAL\_EMAIL\_ENABLED](../../../../Constants,-Enumerations-and-Structures/Environment-State/Client-Terminal-Properties/Client-Terminal-Properties.md#enum_terminal_info_integer) property).