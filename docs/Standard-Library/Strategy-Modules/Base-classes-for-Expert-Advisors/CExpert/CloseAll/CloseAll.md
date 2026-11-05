# CloseAll

CloseAll

It performs partial of full position closing.

|  |
| --- |
| virtual bool  CloseAll(     double    lot    // lot     ) |

Parameters

lot

[in]  Number of lots to reduce the position.

Return Value

true - trade operation has been executed, otherwise - false.

Note

In the "netting" mode, a position is closed using the CExpertTrade::Buy or CExpertTrade::Sell methods. In the "hedging" mode, the CTrade::PositionClose method is used, which can also be used on accounts with the netting mode. The [DeleteOrders()](../DeleteOrders/DeleteOrders.md) method is used to delete orders.

Implementation

|  |
| --- |
| //+------------------------------------------------------------------+  //| Position close and orders delete                                 |  //| INPUT:  lot - volume for close.                                  |  //| OUTPUT: true-if trade operation processed, false otherwise.      |  //| REMARK: no.                                                      |  //+------------------------------------------------------------------+  bool CExpert::CloseAll(double lot)    {     bool result=false;  //--- check for close operations     if(m\_margin\_mode==ACCOUNT\_MARGIN\_MODE\_RETAIL\_HEDGING)        result=m\_trade.PositionCloseByTicket(m\_position.Identifier());     else       {        if(m\_position.PositionType()==POSITION\_TYPE\_BUY)           result=m\_trade.Sell(lot,0,0,0);        else           result=m\_trade.Buy(lot,0,0,0);       }     result|=DeleteOrders();  //---     return(result);    } |
