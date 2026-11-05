# DeleteOrders

DeleteOrders

Deletes all orders.

|  |
| --- |
| virtual bool  DeleteOrders() |

Return Value

true - trade operation has been executed, otherwise - false.

Note

It deletes all orders ([DeleteOrder()](../DeleteOrder/DeleteOrder.md) for all orders).

Implementation

|  |
| --- |
| //+------------------------------------------------------------------+  //| Delete all limit/stop orders                                     |  //| INPUT:  no.                                                      |  //| OUTPUT: true-if trade operation successful, false otherwise.     |  //| REMARK: no.                                                      |  //+------------------------------------------------------------------+  bool CExpert::DeleteOrders()    {     bool result=false;     int  total=OrdersTotal();  //---     for(int i=total-1;i>=0;i--)       {        if(m\_order.Select(OrderGetTicket(i)))          {           if(m\_order.Symbol()!=m\_symbol.Name()) continue;           result|=DeleteOrder();          }       }  //---     return(result);    } |
