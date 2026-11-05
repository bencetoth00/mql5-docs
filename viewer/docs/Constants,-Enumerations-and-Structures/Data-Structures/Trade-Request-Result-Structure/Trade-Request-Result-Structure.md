# Trade Request Result Structure

# The Structure of a Trade Request Result (MqlTradeResult)

As result of a [trade request](../Trade-Request-Structure/Trade-Request-Structure.md), a trade server returns data about the trade request processing result as a special predefined structure of MqlTradeResult type.

```cpp
struct MqlTradeResult
  {
   uint     retcode;          // Operation return code
   ulong    deal;             // Deal ticket, if it is performed
   ulong    order;            // Order ticket, if it is placed
   double   volume;           // Deal volume, confirmed by broker
   double   price;            // Deal price, confirmed by broker
   double   bid;              // Current Bid price
   double   ask;              // Current Ask price
   string   comment;          // Broker comment to operation (by default it is filled by description of trade server return code)
   uint     request_id;       // Request ID set by the terminal during the dispatch
   int      retcode_external; // Return code of an external trading system
  };
```

Fields description

| Field | Description |
| --- | --- |
| retcode | [Return code](../../Codes-of-Errors-and-Warnings/Trade-Server-Return-Codes/Trade-Server-Return-Codes.md) of a trade server |
| deal | [Deal](../../Trade-Constants/Deal-Properties/Deal-Properties.md) ticket,  if a deal has been performed. It is available for a trade operation of [TRADE\_ACTION\_DEAL](../../Trade-Constants/Trade-Operation-Types/Trade-Operation-Types.md) type |
| order | [Order](../../Trade-Constants/Order-Properties/Order-Properties.md) ticket, if a ticket has been placed. It is available for a trade operation of [TRADE\_ACTION\_PENDING](../../Trade-Constants/Trade-Operation-Types/Trade-Operation-Types.md) type |
| volume | Deal volume, confirmed by broker. It depends on the [order filling type](../../Trade-Constants/Order-Properties/Order-Properties.md#enum_order_type_filling) |
| price | Deal price, confirmed by broker. It depends on the deviation field of the [trade request](../Trade-Request-Structure/Trade-Request-Structure.md) and/or on the [trade operation](../../Trade-Constants/Trade-Operation-Types/Trade-Operation-Types.md) |
| bid | The current market Bid price (requote price) |
| ask | The current market Ask price (requote price) |
| comment | The broker comment to operation (by default it is filled by description of trade server return code) |
| request\_id | Request ID set by the terminal when sending to the trade server |
| retcode\_external | The code of the error returned by an external trading system. The use and types of these errors depend on the broker and the external trading system, to which trading operations are sent. |

The trade operation result is returned to a variable of the MqlTradeResult type, which is passed as the second parameter to [OrderSend()](../../../Trade-Functions/OrderSend/OrderSend.md) to perform [trade operations](../../Trade-Constants/Trade-Operation-Types/Trade-Operation-Types.md).

The terminal fixes [request](../Trade-Request-Structure/Trade-Request-Structure.md) ID in request\_id field when sending it to the trade server using [OrdersSend(](../../../Trade-Functions/OrderSend/OrderSend.md)) and [OrderSendAsync()](../../../Trade-Functions/OrderSendAsync/OrderSendAsync.md) functions. The terminal receives messages about performed transactions from the trade server and submits them for processing by [OnTradeTransaction()](../../../Event-Handling/OnTradeTransaction/OnTradeTransaction.md) function containing the following components as parameters:

- description of the trade transaction in [MqlTradeTransaction](../Trade-Transaction-Structure/Trade-Transaction-Structure.md) structure;
- description of the [trade request](../Trade-Request-Structure/Trade-Request-Structure.md) sent from OrderSend() or OrdersSendAsync() function. Request ID is sent by the terminal to the trade server, while the request itself and its request\_id are stored in the terminal memory;
- the trade request execution result as MqlTradeResult structure with request\_id field containing ID of this request.

OnTradeTransaction() function receives three input parameters but the last two should be analyzed only for transactions having [TRADE\_TRANSACTION\_REQUEST](../Trade-Transaction-Structure/Trade-Transaction-Structure.md) type. In all other cases, data on the trade request and its execution result are not filled. Example of parameters analysis can be found at [Structure of a Trade Request](../Trade-Transaction-Structure/Trade-Transaction-Structure.md).

Setting request\_id by the terminal for the trade request when sending it to the server is mainly introduced for working with OrderSendAsync() asynchronous function. This identifier allows to associate the performed action (OrderSend or OrderSendAsync functions call) with the result of this action sent to [OnTradeTransaction()](../../../Event-Handling/OnTradeTransaction/OnTradeTransaction.md).

Example:

```cpp
//+------------------------------------------------------------------+
//| Sending a trade request with the result processing               |
//+------------------------------------------------------------------+
bool MyOrderSend(MqlTradeRequest request,MqlTradeResult result)
  {
//--- reset the last error code to zero
   ResetLastError();
//--- send request
   bool success=OrderSend(request,result);
//--- if the result fails - try to find out why
   if(!success)
     {
      int answer=result.retcode;
      Print("TradeLog: Trade request failed. Error = ",GetLastError());
      switch(answer)
        {
         //--- requote
         case 10004:
           {
            Print("TRADE_RETCODE_REQUOTE");
            Print("request.price = ",request.price,"   result.ask = ",
                  result.ask," result.bid = ",result.bid);
            break;
           }
         //--- order is not accepted by the server
         case 10006:
           {
            Print("TRADE_RETCODE_REJECT");
            Print("request.price = ",request.price,"   result.ask = ",
                  result.ask," result.bid = ",result.bid);
            break;
           }
         //--- invalid price
         case 10015:
           {
            Print("TRADE_RETCODE_INVALID_PRICE");
            Print("request.price = ",request.price,"   result.ask = ",
                  result.ask," result.bid = ",result.bid);
            break;
           }
         //--- invalid SL and/or TP
         case 10016:
           {
            Print("TRADE_RETCODE_INVALID_STOPS");
            Print("request.sl = ",request.sl," request.tp = ",request.tp);
            Print("result.ask = ",result.ask," result.bid = ",result.bid);
            break;
           }
         //--- invalid volume
         case 10014:
           {
            Print("TRADE_RETCODE_INVALID_VOLUME");
            Print("request.volume = ",request.volume,"   result.volume = ",
                  result.volume);
            break;
           }
         //--- not enough money for a trade operation
         case 10019:
           {
            Print("TRADE_RETCODE_NO_MONEY");
            Print("request.volume = ",request.volume,"   result.volume = ",
                  result.volume,"   result.comment = ",result.comment);
            break;
           }
         //--- some other reason, output the server response code
         default:
           {
            Print("Other answer = ",answer);
           }
        }
      //--- notify about the unsuccessful result of the trade request by returning false
      return(false);
     }
//--- OrderSend() returns true - repeat the answer
   return(true);
  }
```