# OrdersTotal


Returns the number of current orders.

```cpp
int  OrdersTotal();
```

Return Value

Value of the [int](../../Language-Basics/Data-Types/Integer-Types/Char,-Short,-Int-and-Long-Types/Char,-Short,-Int-and-Long-Types.md) type.

Note

Do not confuse current [pending orders](../../Constants,-Enumerations-and-Structures/Trade-Constants/Order-Properties/Order-Properties.md) with positions, which are also displayed on the "Trade" tab of the "Toolbox" of the client terminal. An order is a request to conduct a [transaction](../../Constants,-Enumerations-and-Structures/Trade-Constants/Trade-Operation-Types/Trade-Operation-Types.md), while a position is a result of one or more [deals](../../Constants,-Enumerations-and-Structures/Trade-Constants/Deal-Properties/Deal-Properties.md).

For the "netting" interpretation of positions ([ACCOUNT\_MARGIN\_MODE\_RETAIL\_NETTING](../../Constants,-Enumerations-and-Structures/Environment-State/Account-Properties/Account-Properties.md#enum_account_info_integer) and [ACCOUNT\_MARGIN\_MODE\_EXCHANGE](../../Constants,-Enumerations-and-Structures/Environment-State/Account-Properties/Account-Properties.md#enum_account_info_integer)), only one [position](../../Constants,-Enumerations-and-Structures/Trade-Constants/Position-Properties/Position-Properties.md) can exist for a [symbol](../../Checkup/Symbol/Symbol.md) at any moment of time. This position is a result of one or more [deals](../../Constants,-Enumerations-and-Structures/Trade-Constants/Deal-Properties/Deal-Properties.md). Do not confuse positions with valid [pending orders](../../Constants,-Enumerations-and-Structures/Trade-Constants/Order-Properties/Order-Properties.md), which are also displayed on the Trading tab of the Toolbox window.

If individual positions are allowed ([ACCOUNT\_MARGIN\_MODE\_RETAIL\_HEDGING](../../Constants,-Enumerations-and-Structures/Environment-State/Account-Properties/Account-Properties.md#enum_account_info_integer)), multiple positions can be open for one symbol.

Example:

```cpp
//+------------------------------------------------------------------+
//| Script program start function                                    |
//+------------------------------------------------------------------+
void OnStart()
  {
//--- get and print in the journal the number of active pending orders on the account
   int total=OrdersTotal();
   Print("Number of active pending orders on the account: ", total);
   /*
   result:
   Number of active pending orders on the account: 2
   */
  }
```

See also

[OrderSelect()](../OrderSelect/OrderSelect.md), [OrderGetTicket()](../OrderGetTicket/OrderGetTicket.md), [Order Properties](../../Constants,-Enumerations-and-Structures/Trade-Constants/Order-Properties/Order-Properties.md)