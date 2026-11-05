# CheckCloseShort

CheckCloseShort

Checks conditions to close a short position.

|  |
| --- |
| virtual bool  CheckCloseShort() |

Return Value

true - trade operation has been executed, otherwise - false.

Note

It checks conditions to close a short position (CheckCloseShort() method of Signal object) and if they are satisfied, it closes the position ( [CloseShort()](../CloseShort/CloseShort.md) method).

Implementation

|  |
| --- |
| //+------------------------------------------------------------------+  //| Check for short position close or limit/stop order delete        |  //| INPUT:  no.                                                      |  //| OUTPUT: true-if trade operation processed, false otherwise.      |  //| REMARK: no.                                                      |  //+------------------------------------------------------------------+  bool CExpert::CheckCloseShort()    {     double price=EMPTY\_VALUE;  //--- check for short close operations     if(m\_signal.CheckCloseShort(price))        return(CloseShort(price));  //--- return without operations     return(false);    } |
