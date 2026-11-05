# Sell


Opens a short position with specified parameters.

```cpp
bool  Sell(
   double        volume,          // position volume
   const string  symbol=NULL,     // symbol
   double        price=0.0,       // execution price
   double        sl=0.0,          // stop loss price
   double        tp=0.0,          // take profit price
   const string  comment=""       // comment
   )
```

Parameters

volume

[in]  Requested position volume.

symbol=[NULL](../../../../Language-Basics/Data-Types/Void-Type-and-NULL-Constant/Void-Type-and-NULL-Constant.md)

[in]  Position symbol. If the symbol is not specified, the current symbol will be used.

price=0.0

[in]  Price. If the price is not specified, the current market Bid price will be used.

sl=0.0

[in]  Stop Loss price.

tp=0.0

[in]  Take Profit price.

comment=""

[in]  Comment.

Return Value

true - successful check of the structures, otherwise - false.

Note

Successful completion of the Sell(...) method does not always mean successful execution of the trade operation. It is necessary to check the result of trade request (trade server [return code](../../../../Constants,-Enumerations-and-Structures/Codes-of-Errors-and-Warnings/Trade-Server-Return-Codes/Trade-Server-Return-Codes.md)) using [ResultRetcode()](../ResultRetcode/ResultRetcode.md) and value returned by [ResultDeal()](../ResultDeal/ResultDeal.md).