# CheckTrailingOrderShort

CheckTrailingOrderShort

It checks Trailing Stop conditions of Sell Limit/Stop trailing order.

|  |
| --- |
| virtual bool  CheckTrailingOrderShort() |

Return Value

true - trade operation has been executed, otherwise - false.

Note

It checks Trailing Stop conditions for sell limit/stop trailing order (CheckTrailingOrderShort() method of Trade Signals object) and modifies the order parameters if necessary ([TrailingOrderShort()](../TrailingOrderShort/TrailingOrderShort.md) method).

Implementation

|  |
| --- |
| //+------------------------------------------------------------------+  //| Check for trailing short limit/stop order                        |  //| INPUT:  no.                                                      |  //| OUTPUT: true-if trade operation processed, false otherwise.      |  //| REMARK: no.                                                      |  //+------------------------------------------------------------------+  bool CExpert::CheckTrailingOrderShort()    {     double price;  //--- check the possibility of modifying the short order     if(m\_signal.CheckTrailingOrderShort(GetPointer(m\_order),price))        return(TrailingOrderShort(m\_order.PriceOpen()-price));  //--- return without operations     return(false);    } |
