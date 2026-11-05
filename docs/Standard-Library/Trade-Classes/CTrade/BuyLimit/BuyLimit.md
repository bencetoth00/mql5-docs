# BuyLimit

BuyLimit

Places the pending order of Buy Limit type (buy at the price lower than current market price) with specified parameters.

|  |
| --- |
| bool  BuyLimit(     double                volume,                       // order volume     double                price,                        // order price     const string          symbol=NULL,                  // symbol     double                sl=0.0,                       // stop loss price     double                tp=0.0,                       // take profit price     ENUM\_ORDER\_TYPE\_TIME  type\_time=ORDER\_TIME\_GTC,     // order lifetime     datetime              expiration=0,                 // order expiration time     const string          comment=""                    // comment     ) |

Parameters

volume

[in]  Requested order volume.

price

[in]  Order price.

symbol=[NULL](../../../../Language-Basics/Data-Types/Void-Type-and-NULL-Constant/Void-Type-and-NULL-Constant.md)

[in]  Order symbol. If the symbol is not specified, the current symbol will be used.

sl=0.0

[in]  Stop Loss price.

tp=0.0

[in]  Take Profit price.

type\_time=[ORDER\_TIME\_GTC](../../../../Constants,-Enumerations-and-Structures/Trade-Constants/Order-Properties/Order-Properties.md#enum_order_type_time)

[in]  Order lifetime from [ENUM\_ORDER\_TYPE\_TIME](../../../../Constants,-Enumerations-and-Structures/Trade-Constants/Order-Properties/Order-Properties.md#enum_order_type_time) enumeration.

expiration=0

[in]  Order expiration time (used only if type\_time=[ORDER\_TIME\_SPECIFIED](../../../../Constants,-Enumerations-and-Structures/Trade-Constants/Order-Properties/Order-Properties.md#enum_order_type_time)).

comment=""

[in]  Order comment.

Return Value

true - successful check of the structures, otherwise - false.

Note

Successful completion of the BuyLimit(...) method does not always mean successful execution of the trade operation. It is necessary to check the result of trade request (trade server [return code](../../../../Constants,-Enumerations-and-Structures/Codes-of-Errors-and-Warnings/Trade-Server-Return-Codes/Trade-Server-Return-Codes.md)) using [ResultRetcode()](../ResultRetcode/ResultRetcode.md) and value returned by [ResultOrder()](../ResultOrder/ResultOrder.md).
