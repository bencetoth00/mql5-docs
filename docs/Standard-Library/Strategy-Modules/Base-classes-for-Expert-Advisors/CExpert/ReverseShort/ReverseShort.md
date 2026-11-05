# ReverseShort

ReverseShort

Performs reverse operation of a short position.

|  |
| --- |
| virtual bool  ReverseShort(     double    price,    // price     double    sl,       // Stop Loss     double    tp        // Take Profit     ) |

Parameters

price

[in]  Market entry price.

sl

[in] Stop Loss price.

tp

[in] Take Profit price.

Return Value

true - trade operation has been executed, otherwise - false.

Note

It gets position reverse volume ([LotReverse(...)](../LotReverse/LotReverse.md) method) and perform trade operation of the short position reverse (Buy() method of Trade object) if trading volume is not equal to 0.

In the "hedging" mode of position accounting, position reversal is performed as the closure of the existing position and opening of a new opposite one with the remaining volume.

Implementation

|  |
| --- |
| //+------------------------------------------------------------------+  //| Short position reverse                                           |  //| INPUT:  price - price,                                           |  //|         sl    - stop loss,                                       |  //|         tp    - take profit.                                     |  //| OUTPUT: true-if trade operation processed, false otherwise.      |  //| REMARK: no.                                                      |  //+------------------------------------------------------------------+  bool CExpert::ReverseLong(double price,double sl,double tp)    {     if(price==EMPTY\_VALUE)        return(false);  //--- get lot for reverse     double lot=LotReverse(sl);  //--- check lot     if(lot==0.0)        return(false);  //---     bool result=true;     if(m\_margin\_mode==ACCOUNT\_MARGIN\_MODE\_RETAIL\_HEDGING)       {        //--- first close existing position        lot-=m\_position.Volume();        result=m\_trade.PositionCloseByTicket(m\_position.Identifier());       }     if(result)        result=m\_trade.Sell(lot,price,sl,tp);  //---     return(result);    } |
