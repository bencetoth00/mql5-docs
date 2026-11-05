# CheckOpen

CheckOpen

Checks conditions to open a position.

|  |
| --- |
| virtual bool  CheckOpen() |

Return Value

true - a trade operation has been executed, otherwise - false.

Note

It checks the necessity to open long ([CheckOpenLong()](../CheckOpenLong/CheckOpenLong.md)) and short ([CheckOpenShort()](../CheckOpenShort/CheckOpenShort.md)) positions.

Implementation

|  |
| --- |
| //+------------------------------------------------------------------+  //| Check for position open or limit/stop order set                  |  //| INPUT:  no.                                                      |  //| OUTPUT: true-if trade operation processed, false otherwise.      |  //| REMARK: no.                                                      |  //+------------------------------------------------------------------+  bool CExpert::CheckOpen()    {     if(CheckOpenLong())  return(true);     if(CheckOpenShort()) return(true);  //--- return without operations     return(false);    } |
