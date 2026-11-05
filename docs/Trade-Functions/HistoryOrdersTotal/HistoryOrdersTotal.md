# HistoryOrdersTotal

HistoryOrdersTotal

Returns the number of orders in the history. Prior to calling HistoryOrdersTotal(), first it is necessary to receive the history of deals and orders using the [HistorySelect()](../HistorySelect/HistorySelect.md) or [HistorySelectByPosition()](../HistorySelectByPosition/HistorySelectByPosition.md) function.

|  |
| --- |
| int  HistoryOrdersTotal(); |

Return Value

Value of the [int](../../Language-Basics/Data-Types/Integer-Types/Char,-Short,-Int-and-Long-Types/Char,-Short,-Int-and-Long-Types.md) type.

Note

Do not confuse orders of a trading history with current [pending orders](../OrdersTotal/OrdersTotal.md) that appear on the "Trade" tab of the "Toolbox" bar. The list of [orders](../../Constants,-Enumerations-and-Structures/Trade-Constants/Order-Properties/Order-Properties.md) that were canceled or have led to a transaction, can be viewed in the "History" tab of "Toolbox" of the client terminal.

Example:

|  |
| --- |
| //+------------------------------------------------------------------+  //| Script program start function                                    |  //+------------------------------------------------------------------+  void OnStart()    {  //--- request all the existing history on the account     if(!HistorySelect(0, TimeCurrent()))       {        Print("HistorySelect() failed. Error ", GetLastError());        return;       }     //--- get the number of orders in the list and display it in the journal     int total=HistoryOrdersTotal();     Print("Number of historical orders on the account: ", total);     /\*     result:     Number of historical orders on the account: 496     \*/    } |

See also

[HistorySelect()](../HistorySelect/HistorySelect.md), [HistoryOrderSelect()](../HistoryOrderSelect/HistoryOrderSelect.md), [HistoryOrderGetTicket()](../HistoryOrderGetTicket/HistoryOrderGetTicket.md), [Order Properties](../../Constants,-Enumerations-and-Structures/Trade-Constants/Order-Properties/Order-Properties.md)
