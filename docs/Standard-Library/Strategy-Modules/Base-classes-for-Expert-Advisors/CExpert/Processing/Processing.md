# Processing

Processing

Main processing algorithm.

|  |
| --- |
| virtual bool  Processing() |

Return Value

true - trade operation has been executed, otherwise - false.

Note

It does the following steps:

1. Checks the presence of the opened position on the symbol. If there is no opened position, skip steps 2, 3, and 4.  
2. Checks conditions to reverse opened position ([CheckReverse()](../CheckReverse/CheckReverse.md) method). If position has been "reversed", exit.  
3. Checks conditions to close position ([CheckClose()](../CheckClose/CheckClose.md) method). If position has been closed, skip step 4.  
4. Checks conditions to modify position parameters ([CheckTrailingStop()](../CheckTrailingStop/CheckTrailingStop.md) method). If position parameters have been modified, exit.  
5. Check the presence of pending orders on the symbol. If there is no any pending order, go to step 9.  
6. Checks condition to delete order ([CheckDeleteOrderLong()](../CheckDeleteOrderLong/CheckDeleteOrderLong.md) for buy pending orders or [CheckDeleteOrderShort()](../CheckDeleteOrderShort/CheckDeleteOrderShort.md) for sell pending orders). If the order has been deleted, go to step 9.  
7. Check conditions to modify pending order parameters ([CheckTrailingOrderLong()](../CheckTrailingOrderLong/CheckTrailingOrderLong.md) for buy orders or [CheckTrailingOrderShort()](../CheckTrailingOrderShort/CheckTrailingOrderShort.md) for sell orders). If the order parameters have been modified, exit.  
8. Exit.  
9. Checks conditions to open position ([CheckOpen()](../CheckOpen/CheckOpen.md) method).

If you want to implement your own algorithm, you need to override the [Processing()](Processing.md)  method of the descendant class.

Implementation

|  |
| --- |
| //+------------------------------------------------------------------+  //| Main function                                                    |  //| INPUT:  no.                                                      |  //| OUTPUT: true-if any trade operation processed, false otherwise.  |  //| REMARK: no.                                                      |  //+------------------------------------------------------------------+  bool CExpert::Processing()    {  //--- check if open positions     if(m\_position.Select(m\_symbol.Name()))       {        //--- open position is available        //--- check the possibility of reverse the position        if(CheckReverse()) return(true);        //--- check the possibility of closing the position/delete pending orders        if(!CheckClose())          {           //--- check the possibility of modifying the position           if(CheckTrailingStop()) return(true);           //--- return without operations           return(false);          }       }  //--- check if placed pending orders     int total=OrdersTotal();     if(total!=0)       {        for(int i=total-1;i>=0;i--)          {           m\_order.SelectByIndex(i);           if(m\_order.Symbol()!=m\_symbol.Name()) continue;           if(m\_order.OrderType()==ORDER\_TYPE\_BUY\_LIMIT || m\_order.OrderType()==ORDER\_TYPE\_BUY\_STOP)             {              //--- check the ability to delete a pending order to buy              if(CheckDeleteOrderLong()) return(true);              //--- check the possibility of modifying a pending order to buy              if(CheckTrailingOrderLong()) return(true);             }           else             {              //--- check the ability to delete a pending order to sell              if(CheckDeleteOrderShort()) return(true);              //--- check the possibility of modifying a pending order to sell              if(CheckTrailingOrderShort()) return(true);             }           //--- return without operations           return(false);          }       }  //--- check the possibility of opening a position/setting pending order     if(CheckOpen()) return(true);  //--- return without operations     return(false);    } |
