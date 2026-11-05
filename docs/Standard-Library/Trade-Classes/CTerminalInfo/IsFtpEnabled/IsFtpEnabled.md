# IsFtpEnabled

IsFtpEnabled

Gets the information about permission to send trade reports to FTP server and login specified in the terminal settings.

|  |
| --- |
| bool  IsFtpEnabled() const |

Return Value

true - sending trade reports to FTP server is allowed, otherwise - false.

Note

Permission to send trade reports is defined [TerminalInfoInteger()](../../../../Checkup/TerminalInfoInteger/TerminalInfoInteger.md) function ([TERMINAL\_FTP\_ENABLED](../../../../Constants,-Enumerations-and-Structures/Environment-State/Client-Terminal-Properties/Client-Terminal-Properties.md#enum_terminal_info_integer) property).
