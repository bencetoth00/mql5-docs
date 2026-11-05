# PositionsTotal


Returns the number of open positions.

```cpp
int  PositionsTotal();
```

Return Value

Value of [int](../../Language-Basics/Data-Types/Integer-Types/Char,-Short,-Int-and-Long-Types/Char,-Short,-Int-and-Long-Types.md) type.

Note

For the "netting" interpretation of positions ([ACCOUNT\_MARGIN\_MODE\_RETAIL\_NETTING](../../Constants,-Enumerations-and-Structures/Environment-State/Account-Properties/Account-Properties.md#enum_account_info_integer) and [ACCOUNT\_MARGIN\_MODE\_EXCHANGE](../../Constants,-Enumerations-and-Structures/Environment-State/Account-Properties/Account-Properties.md#enum_account_info_integer)), only one [position](../../Constants,-Enumerations-and-Structures/Trade-Constants/Position-Properties/Position-Properties.md) can exist for a [symbol](../../Checkup/Symbol/Symbol.md) at any moment of time. This position is a result of one or more [deals](../../Constants,-Enumerations-and-Structures/Trade-Constants/Deal-Properties/Deal-Properties.md). Do not confuse positions with valid [pending orders](../../Constants,-Enumerations-and-Structures/Trade-Constants/Order-Properties/Order-Properties.md), which are also displayed on the Trading tab of the Toolbox window.

If individual positions are allowed ([ACCOUNT\_MARGIN\_MODE\_RETAIL\_HEDGING](../../Constants,-Enumerations-and-Structures/Environment-State/Account-Properties/Account-Properties.md#enum_account_info_integer)), multiple positions can be open for one symbol.

Example:

```cpp
//+------------------------------------------------------------------+
//| Script program start function                                    |
//+------------------------------------------------------------------+
void OnStart()
  {
//--- get and print the number of open positions on the account in the journal
   int total=PositionsTotal();
   Print("Number of open positions on account: ", total);
   /*
   result:
   Number of open positions on account: 2
   */
  }
```

See also

[PositionGetSymbol()](../PositionGetSymbol/PositionGetSymbol.md), [PositionSelect()](../PositionSelect/PositionSelect.md), [Position Properties](../../Constants,-Enumerations-and-Structures/Trade-Constants/Position-Properties/Position-Properties.md)