# CheckTrailingStopShort

CheckTrailingStopShort

It checks Trailing Stop conditions of the opened short position.

|  |
| --- |
| virtual bool  CheckTrailingStopShort() |

Return Value

true - trade operation has been executed, otherwise - false.

Note

It checks Trailing Stop conditions of the opened short position (CheckTrailingStopShort(...) method of Expert Trailing object). If conditions are satisfied, it modifies the position parameters ([TrailingStopShort(...)](../TrailingStopShort/TrailingStopShort.md) method).

Implementation

|  |
| --- |
| //+------------------------------------------------------------------+  //| Check for trailing stop/profit short position                    |  //| INPUT:  no.                                                      |  //| OUTPUT: true-if trade operation processed, false otherwise.      |  //| REMARK: no.                                                      |  //+------------------------------------------------------------------+  bool CExpert::CheckTrailingStopShort()    {     double sl=EMPTY\_VALUE;     double tp=EMPTY\_VALUE;  //--- check for short trailing stop operations     if(m\_trailing.CheckTrailingStopShort(GetPointer(m\_position),sl,tp))       {        if(sl==EMPTY\_VALUE) sl=m\_position.StopLoss();        if(tp==EMPTY\_VALUE) tp=m\_position.TakeProfit();        //--- short trailing stop operations        return(TrailingStopShort(sl,tp));       }  //--- return without operations     return(false);    } |
