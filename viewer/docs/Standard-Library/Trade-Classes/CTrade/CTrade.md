# CTrade


CTrade is a class for easy access to the trade functions.

### Description

CTrade class provides easy access to the trade functions.

### Declaration

```cpp
   class CTrade : public CObject
```

### Title

```cpp
   #include <Trade\Trade.mqh>
```

|  |
| --- |
| Inheritance hierarchy    [CObject](../../Basic-Class-CObject/Basic-Class-CObject.md)        CTrade  Direct descendants  CExpertTrade |

### Class methods by groups

| Setting parameters |  |
| --- | --- |
| [LogLevel](LogLevel/LogLevel.md) | Sets logging level |
| [SetExpertMagicNumber](SetExpertMagicNumber/SetExpertMagicNumber.md) | Sets the expert ID |
| [SetDeviationInPoints](SetDeviationInPoints/SetDeviationInPoints.md) | Sets the allowed deviation |
| [SetTypeFilling](SetTypeFilling/SetTypeFilling.md) | Sets filling type of the order |
| [SetTypeFillingBySymbol](SetTypeFillingBySymbol/SetTypeFillingBySymbol.md) | Sets filling type of the order according to the specified symbol settings |
| [SetAsyncMode](SetAsyncMode/SetAsyncMode.md) | Sets asynchronous mode for trade operations |
| [SetMarginMode](SetMarginMode/SetMarginMode.md) | Sets margin calculation mode in accordance with the current account settings |
| Operations with orders |  |
| [OrderOpen](OrderOpen/OrderOpen.md) | Places a pending order with specified parameters |
| [OrderModify](OrderModify/OrderModify.md) | Modifies the pending order parameters |
| [OrderDelete](OrderDelete/OrderDelete.md) | Deletes a pending order |
| Operations with positions |  |
| [PositionOpen](PositionOpen/PositionOpen.md) | Opens a position with specified parameters |
| [PositionModify](PositionModify/PositionModify.md) | Modifies position parameters by the specified symbol or position ticket |
| [PositionClose](PositionClose/PositionClose.md) | Closes a position for the specified symbol |
| [PositionClosePartial](PositionClosePartial/PositionClosePartial.md) | Partially closes a position on a specified symbol or having a specified ticket |
| [PositionCloseBy](PositionCloseBy/PositionCloseBy.md) | Closes a position with the specified ticket by an opposite position |
| Additional methods |  |
| [Buy](Buy/Buy.md) | Opens a long position with specified parameters |
| [Sell](Sell/Sell.md) | Opens a short position with specified parameters |
| [BuyLimit](BuyLimit/BuyLimit.md) | Places a pending order of the Buy Limit type with specified parameters |
| [BuyStop](BuyStop/BuyStop.md) | Places a pending order of the Buy Stop type with specified parameters |
| [SellLimit](SellLimit/SellLimit.md) | Places a pending order of the Sell Limit type with specified parameters |
| [SellStop](SellStop/SellStop.md) | Places a pending order of the Sell Stop type with specified parameters |
| Access to the last request parameters |  |
| [Request](Request/Request.md) | Gets the copy of the last request structure |
| [RequestAction](RequestAction/RequestAction.md) | Gets the trade operation type |
| [RequestActionDescription](RequestActionDescription/RequestActionDescription.md) | Gets the trade operation type as string |
| [RequestMagic](RequestMagic/RequestMagic.md) | Gets the magic number of the Expert Advisor |
| [RequestOrder](RequestOrder/RequestOrder.md) | Gets the order ticket used in the last request |
| [RequestSymbol](RequestSymbol/RequestSymbol.md) | Gets the name of the symbol used in the last request |
| [RequestVolume](RequestVolume/RequestVolume.md) | Gets the trade volume (in lots) used in the last request |
| [RequestPrice](RequestPrice/RequestPrice.md) | Gets the price used in the last request |
| [RequestStopLimit](RequestStopLimit/RequestStopLimit.md) | Gets the price of  pending order of Stop Limit type used in the last request |
| [RequestSL](RequestSL/RequestSL.md) | Gets the Stop Loss price of the order used in the last request |
| [RequestTP](RequestTP/RequestTP.md) | Gets the Take Profit price of the order used in the last request |
| [RequestDeviation](RequestDeviation/RequestDeviation.md) | Gets the maximum allowable price deviation of the order used in the last request |
| [RequestType](RequestType/RequestType.md) | Gets the type of the order used in the last request |
| [RequestTypeDescription](RequestTypeDescription/RequestTypeDescription.md) | Gets the type of the order (as string) used in the last request |
| [RequestTypeFilling](RequestTypeFilling/RequestTypeFilling.md) | Gets the filling type of the order used in the last request |
| [RequestTypeFillingDescription](RequestTypeFillingDescription/RequestTypeFillingDescription.md) | Gets the filling type of the order (as string) used in the last request |
| [RequestTypeTime](RequestTypeTime/RequestTypeTime.md) | Gets the validity period of the order used in the last request |
| [RequestTypeTimeDescription](RequestTypeTimeDescription/RequestTypeTimeDescription.md) | Gets the validity period of the order (as string) used in the last request |
| [RequestExpiration](RequestExpiration/RequestExpiration.md) | Gets the expiration time of the order used in the last request |
| [RequestComment](RequestComment/RequestComment.md) | Gets the comment of the order used in the last request |
| [RequestPosition](RequestPosition/RequestPosition.md) | Gets position ticket |
| [RequestPositionBy](RequestPositionBy/RequestPositionBy.md) | Gets opposite position ticket |
| Access to the last request checking results |  |
| [CheckResult](CheckResult/CheckResult.md) | Gets the copy of the structure of the last request check result. |
| [CheckResultRetcode](CheckResultRetcode/CheckResultRetcode.md) | Gets the value of the retcode field of [MqlTradeCheckResult](../../../Constants,-Enumerations-and-Structures/Data-Structures/Request-Check-Result-Structure/Request-Check-Result-Structure.md) type, filled while checking the request correctness |
| [CheckResultRetcodeDescription](CheckResultRetcodeDescription/CheckResultRetcodeDescription.md) | Gets the string description of the retcode field of [MqlTradeCheckResult](../../../Constants,-Enumerations-and-Structures/Data-Structures/Request-Check-Result-Structure/Request-Check-Result-Structure.md) type, filled while checking the request correctness |
| [CheckResultBalance](CheckResultBalance/CheckResultBalance.md) | Gets the value of the balance field of [MqlTradeCheckResult](../../../Constants,-Enumerations-and-Structures/Data-Structures/Request-Check-Result-Structure/Request-Check-Result-Structure.md) type, filled while checking the request correctness |
| [CheckResultEquity](CheckResultEquity/CheckResultEquity.md) | Gets the value of the equity field of [MqlTradeCheckResult](../../../Constants,-Enumerations-and-Structures/Data-Structures/Request-Check-Result-Structure/Request-Check-Result-Structure.md) type, filled while checking the request correctness |
| [CheckResultProfit](CheckResultProfit/CheckResultProfit.md) | Gets the value of the floating profit after executing a trading operation. |
| [CheckResultMargin](CheckResultMargin/CheckResultMargin.md) | Gets the value of the margin field of [MqlTradeCheckResult](../../../Constants,-Enumerations-and-Structures/Data-Structures/Request-Check-Result-Structure/Request-Check-Result-Structure.md) type, filled while checking the request correctness |
| [CheckResultMarginFree](CheckResultMarginFree/CheckResultMarginFree.md) | Gets the value of the margin\_free field of [MqlTradeCheckResult](../../../Constants,-Enumerations-and-Structures/Data-Structures/Request-Check-Result-Structure/Request-Check-Result-Structure.md) type, filled while checking the request correctness |
| [CheckResultMarginLevel](CheckResultMarginLevel/CheckResultMarginLevel.md) | Gets the value of the margin\_level field of [MqlTradeCheckResult](../../../Constants,-Enumerations-and-Structures/Data-Structures/Request-Check-Result-Structure/Request-Check-Result-Structure.md) type, filled while checking the request correctness |
| [CheckResultComment](CheckResultComment/CheckResultComment.md) | Gets the value of the comment field of [MqlTradeCheckResult](../../../Constants,-Enumerations-and-Structures/Data-Structures/Request-Check-Result-Structure/Request-Check-Result-Structure.md) type, filled while checking the request correctness |
| Access to the last request execution results |  |
| [Result](Result/Result.md) | Gets the copy of the structure of the last request result |
| [ResultRetcode](ResultRetcode/ResultRetcode.md) | Gets the code of request result |
| [ResultRetcodeDescription](ResultRetcodeDescription/ResultRetcodeDescription.md) | Gets the code of request result as a string |
| [ResultDeal](ResultDeal/ResultDeal.md) | Gets the deal ticket |
| [ResultOrder](ResultOrder/ResultOrder.md) | Gets the order ticket |
| [ResultVolume](ResultVolume/ResultVolume.md) | Gets the volume of deal or order |
| [ResultPrice](ResultPrice/ResultPrice.md) | Gets the price, confirmed by broker |
| [ResultBid](ResultBid/ResultBid.md) | Gets the current bid price (the requote) |
| [ResultAsk](ResultAsk/ResultAsk.md) | Gets the current ask price (the requote) |
| [ResultComment](ResultComment/ResultComment.md) | Gets the broker comment |
| Auxiliary methods |  |
| [PrintRequest](PrintRequest/PrintRequest.md) | Prints the last request parameters into journal |
| [PrintResult](PrintResult/PrintResult.md) | Prints the results of the last request into journal |
| [FormatRequest](FormatRequest/FormatRequest.md) | Prepares the formatted string with last request parameters |
| [FormatRequestResult](FormatRequestResult/FormatRequestResult.md) | Prepares the formatted string with results of the last request execution |

|  |
| --- |
| Methods inherited from class CObject  Prev, Prev, Next, Next, [Save](../../Basic-Class-CObject/Save/Save.md), [Load](../../Basic-Class-CObject/Load/Load.md), [Type](../../Basic-Class-CObject/Type/Type.md), [Compare](../../Basic-Class-CObject/Compare/Compare.md) |