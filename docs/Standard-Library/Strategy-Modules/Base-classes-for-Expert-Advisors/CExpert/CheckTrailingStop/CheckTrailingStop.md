# CheckTrailingStop

CheckTrailingStop

It checks Trailing Stop conditions of the opened position.

|  |
| --- |
| virtual bool  CheckTrailingStop() |

Return Value

true - a trade operation has been executed, otherwise - false.

Note

It checks Trailing Stop conditions of the opened position ([CheckTrailingStopLong()](../CheckTrailingStopLong/CheckTrailingStopLong.md) or [CheckTrailingStopShort()](../CheckTrailingStopShort/CheckTrailingStopShort.md) for long and short positions).

Implementation

|  |
| --- |
| //+------------------------------------------------------------------+  //| Check for trailing stop/profit position                          |  //| INPUT:  no.                                                      |  //| OUTPUT: true-if trade operation processed, false otherwise.      |  //| REMARK: no.                                                      |  //+------------------------------------------------------------------+  bool CExpert::CheckTrailingStop()    {  //--- position must be selected before call     if(m\_position.PositionType()==POSITION\_TYPE\_BUY)       {        //--- check the possibility of modifying the long position        if(CheckTrailingStopLong()) return(true);       }     else       {        //--- check the possibility of modifying the short position        if(CheckTrailingStopShort()) return(true);       }  //--- return without operations     return(false);    } |
