# TrailingOrderLong

TrailingOrderLong

It modifies parameters of Buy Limit/Stop trailing order.

|  |
| --- |
| virtual bool  TrailingOrderLong(     double    delta    // delta     ) |

Parameters

delta

[in]  Price delta.

Return Value

true - trade operation has been executed, otherwise - false.

Note

It modifies parameters of Buy Limit/Stop trailing order (OrderModify(...) method of CTrade class object).

Implementation

|  |
| --- |
| //+------------------------------------------------------------------+  //| Trailing long limit/stop order                                   |  //| INPUT:  delta - price change.                                    |  //| OUTPUT: true-if trade operation successful, false otherwise.     |  //| REMARK: no.                                                      |  //+------------------------------------------------------------------+  bool CExpert::TrailingOrderLong(double delta)    {     ulong  ticket=m\_order.Ticket();     double price =m\_order.PriceOpen()-delta;     double sl    =m\_order.StopLoss()-delta;     double tp    =m\_order.TakeProfit()-delta;  //--- modifying the long order     return(m\_trade.OrderModify(ticket,price,sl,tp,m\_order.TypeTime(),m\_order.TimeExpiration()));    } |
