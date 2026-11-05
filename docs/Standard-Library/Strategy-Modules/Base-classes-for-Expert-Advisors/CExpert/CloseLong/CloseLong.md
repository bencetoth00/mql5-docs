# CloseLong

CloseLong

Closes the long position.

|  |
| --- |
| virtual bool  CloseLong(     double    price    // price     ) |

Parameters

price

[in]  Market entry price.

Return Value

true - trade operation has been executed, otherwise - false.

Note

In the "netting" mode, a position is closed using the CExpertTrade::Buy or CExpertTrade::Sell methods. In the "hedging" mode, the CTrade::PositionCloseByTicket method is used.

Implementation

|  |
| --- |
| //+------------------------------------------------------------------+  //| Long position close                                              |  //| INPUT:  price - price for close.                                 |  //| OUTPUT: true-if trade operation processed, false otherwise.      |  //| REMARK: no.                                                      |  //+------------------------------------------------------------------+  bool CExpert::CloseLong(double price)    {     bool result=false;  //---     if(price==EMPTY\_VALUE)        return(false);     if(m\_margin\_mode==ACCOUNT\_MARGIN\_MODE\_RETAIL\_HEDGING)        result=m\_trade.PositionCloseByTicket(m\_position.Identifier());     else        result=m\_trade.Sell(m\_position.Volume(),price,0,0);  //---     return(result);    } |
