# InfoString


The function returns the value of a corresponding property of the mql5 program environment. The property must be of string type.

```cpp
string  TerminalInfoString(
   int  property_id      // property ID
   );
```

Parameters

property\_id

[in] Identifier of a property. It can be one the values of the enumeration [ENUM\_TERMINAL\_INFO\_STRING](../../../../Constants,-Enumerations-and-Structures/Environment-State/Client-Terminal-Properties/Client-Terminal-Properties.md#enum_terminal_info_string).

Return Value

Value of string type.

Note

The property value is defined by [TerminalInfoString()](../../../../Checkup/TerminalInfoString/TerminalInfoString.md) function.