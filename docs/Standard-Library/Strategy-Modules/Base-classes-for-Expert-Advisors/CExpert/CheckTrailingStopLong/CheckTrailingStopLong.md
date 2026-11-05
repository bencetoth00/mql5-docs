# CheckTrailingStopLong

CheckTrailingStopLong

It checks Trailing Stop conditions of the opened long position.

|  |
| --- |
| virtual bool  CheckTrailingStopLong() |

Return Value

true - trade operation has been executed, otherwise - false.

Note

It checks Trailing Stop conditions of the opened long position (CheckTrailingStopLong(...) method of Expert Trailing object). If conditions are satisfied, it modifies the position parameters ([TrailingStopLong(...)](../TrailingStopLong/TrailingStopLong.md) method).

Implementation

|  |
| --- |
| //+------------------------------------------------------------------+  //| Check for trailing stop/profit long position                     |  //| INPUT:  no.                                                      |  //| OUTPUT: true-if trade operation processed, false otherwise.      |  //| REMARK: no.                                                      |  //+------------------------------------------------------------------+  bool CExpert::CheckTrailingStopLong()    {     double sl=EMPTY\_VALUE;     double tp=EMPTY\_VALUE;  //--- check for long trailing stop operations     if(m\_trailing.CheckTrailingStopLong(GetPointer(m\_position),sl,tp))       {        if(sl==EMPTY\_VALUE) sl=m\_position.StopLoss();        if(tp==EMPTY\_VALUE) tp=m\_position.TakeProfit();        //--- long trailing stop operations        return(TrailingStopLong(sl,tp));       }  //--- return without operations     return(false);    } |
