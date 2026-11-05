# SelectPosition

SelectPosition

Selects a position to work with.

|  |
| --- |
| void  SelectPosition() |

Return Value

No.

Implementation

|  |
| --- |
| //+------------------------------------------------------------------+  //| Position select                                                  |  //| INPUT:  no.                                                      |  //| OUTPUT: no.                                                      |  //| REMARK: no.                                                      |  //+------------------------------------------------------------------+  bool CExpert::SelectPosition(void)    {     bool res=false;  //---     if(m\_margin\_mode==ACCOUNT\_MARGIN\_MODE\_RETAIL\_HEDGING)        res=m\_position.SelectByMagic(m\_symbol.Name(),m\_magic);     else        res=m\_position.Select(m\_symbol.Name());  //---     return(res);    } |
