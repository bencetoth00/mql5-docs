# OpenCLSupport


Gets the information about the version of OpenCL supported by video card.

```cpp
int  OpenCLSupport() const
```

Return Value

OpenCL version having the following form: 0x00010002 = "1.2". 0 means that OpenCL is not supported.

Note

OpenCL version is defined by [TerminalInfoInteger()](../../../../Checkup/TerminalInfoInteger/TerminalInfoInteger.md) function ([TERMINAL\_OPENCL\_SUPPORT](../../../../Constants,-Enumerations-and-Structures/Environment-State/Client-Terminal-Properties/Client-Terminal-Properties.md#enum_terminal_info_integer) property).