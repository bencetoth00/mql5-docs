# PositionClose


Closes a position by the specified symbol.

```cpp
bool  PositionClose(
   const string  symbol,                  // symbol
   ulong         deviation=ULONG_MAX      // deviation
   )
```

Closes a position with the specified ticket.

```cpp
bool  PositionClose(
   const ulong   ticket,                  // position ticket
   ulong         deviation=ULONG_MAX      // deviation
   )
```

Parameters

symbol

[in]  Name of trade instrument, by which it is intended to close position.

ticket

[in]  Ticket of a closed position.

deviation=[ULONG\_MAX](../../../../Constants,-Enumerations-and-Structures/Named-Constants/Numerical-Type-Constants/Numerical-Type-Constants.md)

[in] Maximal deviation from the current price (in points).

Return Value

true - successful check of the basic structures, otherwise - false.

Note

Successful completion of the PositionClose(...) method does not always mean successful execution of the trade operation. It is necessary to check the result of trade request (trade server return code) using [ResultRetcode()](../ResultRetcode/ResultRetcode.md).

For the "netting" interpretation of positions ([ACCOUNT\_MARGIN\_MODE\_RETAIL\_NETTING](../../../../Constants,-Enumerations-and-Structures/Environment-State/Account-Properties/Account-Properties.md#enum_account_info_integer) and [ACCOUNT\_MARGIN\_MODE\_EXCHANGE](../../../../Constants,-Enumerations-and-Structures/Environment-State/Account-Properties/Account-Properties.md#enum_account_info_integer)), only one [position](../../../../Constants,-Enumerations-and-Structures/Trade-Constants/Position-Properties/Position-Properties.md) can exist for a [symbol](../../../../Checkup/Symbol/Symbol.md) at any moment of time. This position is a result of one or more [deals](../../../../Constants,-Enumerations-and-Structures/Trade-Constants/Deal-Properties/Deal-Properties.md). Do not confuse positions with valid [pending orders](../../../../Constants,-Enumerations-and-Structures/Trade-Constants/Order-Properties/Order-Properties.md), which are also displayed on the Trading tab of the Toolbox window.

If individual positions are allowed ([ACCOUNT\_MARGIN\_MODE\_RETAIL\_HEDGING](../../../../Constants,-Enumerations-and-Structures/Environment-State/Account-Properties/Account-Properties.md#enum_account_info_integer)), multiple positions can be open for one symbol. In this case, PositionClose will close a position with the lowest ticket.