# CheckCloseLong

CheckCloseLong

Checks conditions to close a long position.

|  |
| --- |
| virtual bool  CheckCloseLong() |

Return Value

true - trade operation has been executed, otherwise - false.

Note

It checks conditions to close a long position (CheckCloseLong() method of Signal object) and if they are satisfied, it closes the open position ([CloseLong(...)](../CloseLong/CloseLong.md) method).

Implementation

|  |
| --- |
| //+------------------------------------------------------------------+  //| Check for long position close or limit/stop order delete         |  //| INPUT:  no.                                                      |  //| OUTPUT: true-if trade operation processed, false otherwise.      |  //| REMARK: no.                                                      |  //+------------------------------------------------------------------+  bool CExpert::CheckCloseLong()    {     double price=EMPTY\_VALUE;  //--- check for long close operations     if(m\_signal.CheckCloseLong(price))        return(CloseLong(price));  //--- return without operations     return(false);    } |
