# CloseShort

CloseShort

Closes the short position.

|  |
| --- |
| virtual bool  CloseShort(     double    price    // price     ) |

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
| //+------------------------------------------------------------------+  //| Short position close                                             |  //| INPUT:  price - price for close.                                 |  //| OUTPUT: true-if trade operation successful, false otherwise.     |  //| REMARK: no.                                                      |  //+------------------------------------------------------------------+  bool CExpert::CloseShort(double price)    {     bool result=false;  //---     if(price==EMPTY\_VALUE)        return(false);     if(m\_margin\_mode==ACCOUNT\_MARGIN\_MODE\_RETAIL\_HEDGING)        result=m\_trade.PositionCloseByTicket(m\_position.Identifier());     else        result=m\_trade.Buy(m\_position.Volume(),price,0,0);  //---     return(result);    } |
