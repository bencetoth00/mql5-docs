# CheckReverse

CheckReverse

Checks necessity and conditions to reverse an open position.

|  |
| --- |
| virtual bool  CheckReverse() |

Return Value

true - a trade operation has been executed, otherwise - false.

Note

It checks the necessity to reverse long ([CheckReverseLong()](../CheckReverseLong/CheckReverseLong.md)) and short ([CheckReverseShort()](../CheckReverseShort/CheckReverseShort.md)) positions.

Implementation

|  |
| --- |
| //+------------------------------------------------------------------+  //| Check for position reverse                                       |  //| INPUT:  no.                                                      |  //| OUTPUT: true-if trade operation processed, false otherwise.      |  //| REMARK: no.                                                      |  //+------------------------------------------------------------------+  bool CExpert::CheckReverse()    {     if(m\_position.PositionType()==POSITION\_TYPE\_BUY)       {        //--- check the possibility of reverse the long position        if(CheckReverseLong())  return(true);       }     else        //--- check the possibility of reverse the short position        if(CheckReverseShort()) return(true);  //--- return without operations     return(false);    } |
