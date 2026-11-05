# CheckDeleteOrderShort

CheckDeleteOrderShort

It checks conditions to delete Sell Limit/Stop order.

|  |
| --- |
| virtual bool  CheckDeleteOrderShort() |

Return Value

true - trade operation has been executed, otherwise - false.

Note

1. It checks the order expiration time.

2. It checks conditions to delete the Sell Limit/Stop order (CheckCloseShort(...) method of Signal class object) and deletes the order if one of the conditions is satisfied ([DeleteOrderShort()](../DeleteOrderShort/DeleteOrderShort.md) method).

Implementation

|  |
| --- |
| //+------------------------------------------------------------------+  //| Check for delete short limit/stop order                          |  //| INPUT:  no.                                                      |  //| OUTPUT: true-if trade operation processed, false otherwise.      |  //| REMARK: no.                                                      |  //+------------------------------------------------------------------+  bool CExpert::CheckDeleteOrderShort()    {     double price;  //--- check the possibility of deleting the short order     if(m\_expiration!=0 && TimeCurrent()>m\_expiration)       {        m\_expiration=0;        return(DeleteOrderShort());       }     if(m\_signal.CheckCloseShort(price))        return(DeleteOrderShort());  //--- return without operations     return(false);    } |
