# TrailingOrderShort

TrailingOrderShort

It modifies parameters of Sell Limit/Stop trailing order.

|  |
| --- |
| virtual bool  TrailingOrderShort(     double    delta    // delta     ) |

Parameters

delta

[in]  Price delta.

Return Value

true - trade operation has been executed, otherwise - false.

Note

It modifies parameters of Sell Limit/Stop trailing order (OrderModify(...) method of CTrade class object).

Implementation

|  |
| --- |
| //+------------------------------------------------------------------+  //| Trailing short limit/stop order                                  |  //| INPUT:  delta - price change.                                    |  //| OUTPUT: true-if trade operation successful, false otherwise.     |  //| REMARK: no.                                                      |  //+------------------------------------------------------------------+  bool CExpert::TrailingOrderShort(double delta)    {     ulong  ticket=m\_order.Ticket();     double price =m\_order.PriceOpen()-delta;     double sl    =m\_order.StopLoss()-delta;     double tp    =m\_order.TakeProfit()-delta;  //--- modifying the short order     return(m\_trade.OrderModify(ticket,price,sl,tp,m\_order.TypeTime(),m\_order.TimeExpiration()));    } |
