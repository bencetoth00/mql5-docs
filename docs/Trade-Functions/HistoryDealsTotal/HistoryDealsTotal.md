# HistoryDealsTotal

HistoryDealsTotal

Returns the number of deal in history. Prior to calling HistoryDealsTotal(), first it is necessary to receive the history of deals and orders using the [HistorySelect()](../HistorySelect/HistorySelect.md) or [HistorySelectByPosition()](../HistorySelectByPosition/HistorySelectByPosition.md) function.

|  |
| --- |
| int  HistoryDealsTotal(); |

Return Value

Value of the [int](../../Language-Basics/Data-Types/Integer-Types/Char,-Short,-Int-and-Long-Types/Char,-Short,-Int-and-Long-Types.md) type.

Note

Do not confuse [orders](../../Constants,-Enumerations-and-Structures/Trade-Constants/Order-Properties/Order-Properties.md), [deals](../../Constants,-Enumerations-and-Structures/Trade-Constants/Deal-Properties/Deal-Properties.md) and [positions](../../Constants,-Enumerations-and-Structures/Trade-Constants/Position-Properties/Position-Properties.md). Each deal is the result of the execution of an order, each position is the summary result of one or more deals.

Example:

|  |
| --- |
| //+------------------------------------------------------------------+  //| Script program start function                                    |  //+------------------------------------------------------------------+  void OnStart()    {  //--- request all the existing history on the account     if(!HistorySelect(0, TimeCurrent()))       {        Print("HistorySelect() failed. Error ", GetLastError());        return;       }     //--- get the number of deals in the list and display it in the journal     int total=HistoryDealsTotal();     Print("Number of historical deals on the account: ", total);     /\*     result:     Number of historical deals on the account: 339     \*/    } |

See also

[HistorySelect()](../HistorySelect/HistorySelect.md), [HistoryDealGetTicket()](../HistoryDealGetTicket/HistoryDealGetTicket.md), [Deal Properties](../../Constants,-Enumerations-and-Structures/Trade-Constants/Deal-Properties/Deal-Properties.md)
