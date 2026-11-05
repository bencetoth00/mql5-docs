# PositionClosePartial


Partially closes a position on a specified symbol in case of a "hedging" accounting.

```cpp
bool  PositionClosePartial(
   const string  symbol,                  // symbol
   const double  volume,                  // volume
   ulong         deviation=ULONG_MAX      // deviation
   )
```

Partially closes a position having a specified ticket in case of a "hedging" accounting.

```cpp
bool  PositionClosePartial(
   const ulong   ticket,                  // position ticket
   const double  volume,                  // volume
   ulong         deviation=ULONG_MAX      // deviation
   )
```

Parameters

symbol

[in]  Name of a trading instrument, on which a position is closed partially. If a symbol (not a ticket) is specified for a position partial closing, the first detected position having a specified MagicNumber ([Expert Advisor ID](../SetExpertMagicNumber/SetExpertMagicNumber.md)) on the symbol is selected. Therefore, it is sometimes better to use PositionClosePartial() with a specified position ticket.

volume

[in]  Volume, by which a position should be decreased. If the value exceeds the volume of a partially closed position, it is closed in full. No position in the opposite direction is opened.

ticket

[in]  Closed position ticket.

deviation=[ULONG\_MAX](../../../../Constants,-Enumerations-and-Structures/Named-Constants/Numerical-Type-Constants/Numerical-Type-Constants.md)

[in]  The maximum deviation from the current price (in points).

Return Value

true if the basic check of structures is successful, otherwise false.

Note

A successful completion of the PositionClosePartial(...) method does not always mean a successful execution of a trading operation. You should call the [ResultRetcode()](../ResultRetcode/ResultRetcode.md) method to check the result of a trade request (trade server return code).

In the "netting" system ([ACCOUNT\_MARGIN\_MODE\_RETAIL\_NETTING](../../../../Constants,-Enumerations-and-Structures/Environment-State/Account-Properties/Account-Properties.md#enum_account_info_integer) and [ACCOUNT\_MARGIN\_MODE\_EXCHANGE](../../../../Constants,-Enumerations-and-Structures/Environment-State/Account-Properties/Account-Properties.md#enum_account_info_integer)), for each [symbol](../../../../Checkup/Symbol/Symbol.md), at any given moment of time, only one [position](../../../../Constants,-Enumerations-and-Structures/Trade-Constants/Position-Properties/Position-Properties.md) can be open, which is the result of one or more [deals](../../../../Constants,-Enumerations-and-Structures/Trade-Constants/Deal-Properties/Deal-Properties.md). Do not confuse the current [pending orders](../../../../Constants,-Enumerations-and-Structures/Trade-Constants/Order-Properties/Order-Properties.md) with positions that are also displayed on the "Trade" tab of the client terminal's "Toolbox" panel.

In case of the position representation ([ACCOUNT\_MARGIN\_MODE\_RETAIL\_HEDGING](../../../../Constants,-Enumerations-and-Structures/Environment-State/Account-Properties/Account-Properties.md#enum_account_info_integer)), multiple positions can be opened on each symbol simultaneously. In this case, PositionClose closes a position having a least ticket.