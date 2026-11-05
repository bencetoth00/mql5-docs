# PositionGetTicket


The function returns the ticket of a position with the specified index in the list of open positions and automatically selects the position to work with using functions [PositionGetDouble](../PositionGetDouble/PositionGetDouble.md), [PositionGetInteger](../PositionGetInteger/PositionGetInteger.md), [PositionGetString](../PositionGetString/PositionGetString.md).

```cpp
ulong  PositionGetTicket(
   int  index      // The number of a position in the list
   );
```

Parameters

index

[in]  The index of a position in the list of open positions, numeration starts with 0.

Return Value

The ticket of the position. Returns 0 if the function fails.

Note

For the "netting" interpretation of positions ([ACCOUNT\_MARGIN\_MODE\_RETAIL\_NETTING](../../Constants,-Enumerations-and-Structures/Environment-State/Account-Properties/Account-Properties.md#enum_account_info_integer) and [ACCOUNT\_MARGIN\_MODE\_EXCHANGE](../../Constants,-Enumerations-and-Structures/Environment-State/Account-Properties/Account-Properties.md#enum_account_info_integer)), only one [position](../../Constants,-Enumerations-and-Structures/Trade-Constants/Position-Properties/Position-Properties.md) can exist for a [symbol](../../Checkup/Symbol/Symbol.md) at any moment of time. This position is a result of one or more [deals](../../Constants,-Enumerations-and-Structures/Trade-Constants/Deal-Properties/Deal-Properties.md). Do not confuse positions with valid [pending orders](../../Constants,-Enumerations-and-Structures/Trade-Constants/Order-Properties/Order-Properties.md), which are also displayed on the Trading tab of the Toolbox window.

If individual positions are allowed ([ACCOUNT\_MARGIN\_MODE\_RETAIL\_HEDGING](../../Constants,-Enumerations-and-Structures/Environment-State/Account-Properties/Account-Properties.md#enum_account_info_integer)), multiple positions can be open for one symbol.

To ensure receipt of fresh data about a position, it is recommended to call [PositionSelect()](../PositionSelect/PositionSelect.md) right before referring to them.

Example:

```cpp
//+------------------------------------------------------------------+
//| Script program start function                                    |
//+------------------------------------------------------------------+
void OnStart()
  {
//--- in a loop by all account positions
   int total=PositionsTotal();
   for(int i=0; i<total; i++)
     {
      //--- get the ticket of the next position by automatically selecting a position to access its properties
      ulong ticket=PositionGetTicket(i);
      if(ticket==0)
         continue;
      //--- get the position type and display the description of the selected position to the journal
      string type=(PositionGetInteger(POSITION_TYPE)==POSITION_TYPE ? "Buy" : "Sell");
      PrintFormat("[%d] Selected position %s #%I64u", i, type, ticket);
     }
   /*
   result:
   [0] Selected position Sell #2810802718
   [1] Selected position Buy #2810802919
   */
  }
```

See also

[PositionGetSymbol()](../PositionGetSymbol/PositionGetSymbol.md), [PositionSelect()](../PositionSelect/PositionSelect.md), [Position Properties](../../Constants,-Enumerations-and-Structures/Trade-Constants/Position-Properties/Position-Properties.md)