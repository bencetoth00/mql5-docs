# CheckOpenShort

CheckOpenShort

Checks necessity and conditions to open a short position.

|  |
| --- |
| virtual bool  CheckOpenShort() |

Return Value

true - a trade operation has been executed, otherwise - false.

Note

It checks the necessity to open a short position (CheckOpenShort() method of Signal object) and does that with the parameters set by Signal object ([OpenShort()](../OpenShort/OpenShort.md) method) if the conditions are met.

Implementation

|  |
| --- |
| //+------------------------------------------------------------------+  //| Check for short position open or limit/stop order set            |  //| INPUT:  no.                                                      |  //| OUTPUT: true-if trade operation processed, false otherwise.      |  //| REMARK: no.                                                      |  //+------------------------------------------------------------------+  bool CExpert::CheckOpenShort()    {     double   price=EMPTY\_VALUE;     double   sl=0.0;     double   tp=0.0;     datetime expiration=TimeCurrent();  //--- check signal for short enter operations     if(m\_signal.CheckOpenShort(price,sl,tp,expiration))       {        if(!m\_trade.SetOrderExpiration(expiration))          {           m\_expiration=expiration;          }        return(OpenShort(price,sl,tp));       }  //--- return without operations     return(false);    } |
