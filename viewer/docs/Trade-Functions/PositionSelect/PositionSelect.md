# PositionSelect


Chooses an open position for further working with it. Returns true if the function is successfully completed. Returns false in case of failure. To obtain information about the error, call [GetLastError()](../../Checkup/GetLastError/GetLastError.md).

```cpp
bool  PositionSelect(
   string  symbol      // Symbol name
   );
```

Parameters

symbol

[in]  Name of the financial security.

Return Value

Value of the bool type.

Note

For the "netting" interpretation of positions ([ACCOUNT\_MARGIN\_MODE\_RETAIL\_NETTING](../../Constants,-Enumerations-and-Structures/Environment-State/Account-Properties/Account-Properties.md#enum_account_info_integer) and [ACCOUNT\_MARGIN\_MODE\_EXCHANGE](../../Constants,-Enumerations-and-Structures/Environment-State/Account-Properties/Account-Properties.md#enum_account_info_integer)), only one [position](../../Constants,-Enumerations-and-Structures/Trade-Constants/Position-Properties/Position-Properties.md) can exist for a [symbol](../../Checkup/Symbol/Symbol.md) at any moment of time. This position is a result of one or more [deals](../../Constants,-Enumerations-and-Structures/Trade-Constants/Deal-Properties/Deal-Properties.md). Do not confuse positions with valid [pending orders](../../Constants,-Enumerations-and-Structures/Trade-Constants/Order-Properties/Order-Properties.md), which are also displayed on the Trading tab of the Toolbox window.

If individual positions are allowed ([ACCOUNT\_MARGIN\_MODE\_RETAIL\_HEDGING](../../Constants,-Enumerations-and-Structures/Environment-State/Account-Properties/Account-Properties.md#enum_account_info_integer)), multiple positions can be open for one symbol. In this case, PositionSelect will select a position with the lowest ticket.

Function PositionSelect() copies data about a position into the program environment, and further calls of [PositionGetDouble()](../PositionGetDouble/PositionGetDouble.md), [PositionGetInteger()](../PositionGetInteger/PositionGetInteger.md) and [PositionGetString()](../PositionGetString/PositionGetString.md) return the earlier copied data. This means that the position itself may no longer exist (or its volume, direction, etc. has changed), but data of this position still can be obtained. To ensure receipt of fresh data about a position, it is recommended to call PositionSelect() right before referring to them.

Example:

```cpp
#define   SYMBOL_NAME   "EURUSD"
//+------------------------------------------------------------------+
//| Script program start function                                    |
//+------------------------------------------------------------------+
void OnStart()
  {
//--- select a position on a specified symbol
   if(!PositionSelect(SYMBOL_NAME))
     {
      PrintFormat("PositionSelect(%s) failed. Error %d",SYMBOL_NAME, GetLastError());
      return;
     }
//--- if a position is selected, we can obtain its data using PositionGetDouble(), PositionGetInteger() and PositionGetString()
//--- get the selected position ticket
   ResetLastError();
   long ticket=PositionGetInteger(POSITION_TICKET);
   if(ticket==0)
     {
      PrintFormat("Failed to get %s position ticket. Error %d", SYMBOL_NAME, GetLastError());
      return;
     }
//--- if a ticket is successfully received, print the selected position symbol and ticket in the journal
   PrintFormat("The position that is selected on the %s symbol has ticket %I64d", SYMBOL_NAME, ticket);
   /*
   result:
   The position that is selected on the EURUSD symbol has ticket 2810846623
   */
  }
```

See also

[PositionGetSymbol()](../PositionGetSymbol/PositionGetSymbol.md), [PositionsTotal()](../PositionsTotal/PositionsTotal.md), [Position Properties](../../Constants,-Enumerations-and-Structures/Trade-Constants/Position-Properties/Position-Properties.md)