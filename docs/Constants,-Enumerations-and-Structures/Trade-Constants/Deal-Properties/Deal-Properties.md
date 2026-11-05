# Deal Properties

Deal Properties

A deal is the reflection of the fact of a [trade operation](../Trade-Operation-Types/Trade-Operation-Types.md) execution based on an [order](../Order-Properties/Order-Properties.md) that contains a trade request. Each trade is described by properties that allow to obtain information about it. In order to read values of properties, functions of the HistoryDealGet...() type are used, that return values from corresponding enumerations.

For the function [HistoryDealGetInteger()](../../../Trade-Functions/HistoryDealGetInteger/HistoryDealGetInteger.md)

ENUM\_DEAL\_PROPERTY\_INTEGER

| Identifier | Description | Type |
| --- | --- | --- |
| DEAL\_TICKET | Deal ticket. Unique number assigned to each deal | long |
| DEAL\_ORDER | Deal [order number](../../../Trade-Functions/HistoryOrderGetTicket/HistoryOrderGetTicket.md) | long |
| DEAL\_TIME | Deal time | datetime |
| DEAL\_TIME\_MSC | The time of a deal execution in milliseconds since 01.01.1970 | long |
| DEAL\_TYPE | Deal type | [ENUM\_DEAL\_TYPE](Deal-Properties.md#enum_deal_type) |
| DEAL\_ENTRY | Deal entry - entry in, entry out, reverse | [ENUM\_DEAL\_ENTRY](Deal-Properties.md#enum_deal_entry) |
| DEAL\_MAGIC | Deal magic number (see [ORDER\_MAGIC](../Order-Properties/Order-Properties.md)) | long |
| DEAL\_REASON | The reason or source for deal execution | [ENUM\_DEAL\_REASON](Deal-Properties.md#enum_deal_reason) |
| DEAL\_POSITION\_ID | [Identifier of a position](../Position-Properties/Position-Properties.md#enum_position_property_integer), in the opening, modification or closing of which this deal took part. Each position has a unique identifier that is assigned to all deals executed for the symbol during the entire lifetime of the position. | long |

For the function [HistoryDealGetDouble()](../../../Trade-Functions/HistoryDealGetDouble/HistoryDealGetDouble.md)

ENUM\_DEAL\_PROPERTY\_DOUBLE

| Identifier | Description | Type |
| --- | --- | --- |
| DEAL\_VOLUME | Deal volume | double |
| DEAL\_PRICE | Deal price | double |
| DEAL\_COMMISSION | Deal commission | double |
| DEAL\_SWAP | Cumulative swap on close | double |
| DEAL\_PROFIT | Deal profit | double |
| DEAL\_FEE | Fee for making a deal charged immediately after performing a deal | double |
| DEAL\_SL | Stop Loss level   - Entry and reversal deals use the Stop Loss values from the original order based on which the position was opened or reversed - Exit deals use the Stop Loss of a position as at the time of position closing | double |
| DEAL\_TP | Take Profit level   - Entry and reversal deals use the Take Profit values from the original order based on which the position was opened or reversed - Exit deals use the Take Profit value of a position as at the time of position closing | double |

For the function [HistoryDealGetString()](../../../Trade-Functions/HistoryDealGetString/HistoryDealGetString.md)

ENUM\_DEAL\_PROPERTY\_STRING

| Identifier | Description | Type |
| --- | --- | --- |
| DEAL\_SYMBOL | Deal symbol | string |
| DEAL\_COMMENT | Deal comment | string |
| DEAL\_EXTERNAL\_ID | Deal identifier in an external trading system (on the Exchange) | string |

 

Each deal is characterized by a type, allowed values are enumerated in ENUM\_DEAL\_TYPE. In order to obtain information about the deal type, use the [HistoryDealGetInteger()](../../../Trade-Functions/HistoryDealGetInteger/HistoryDealGetInteger.md) function with the DEAL\_TYPE modifier.

ENUM\_DEAL\_TYPE

| Identifier | Description |
| --- | --- |
| DEAL\_TYPE\_BUY | Buy |
| DEAL\_TYPE\_SELL | Sell |
| DEAL\_TYPE\_BALANCE | Balance |
| DEAL\_TYPE\_CREDIT | Credit |
| DEAL\_TYPE\_CHARGE | Additional charge |
| DEAL\_TYPE\_CORRECTION | Correction |
| DEAL\_TYPE\_BONUS | Bonus |
| DEAL\_TYPE\_COMMISSION | Additional commission |
| DEAL\_TYPE\_COMMISSION\_DAILY | Daily commission |
| DEAL\_TYPE\_COMMISSION\_MONTHLY | Monthly commission |
| DEAL\_TYPE\_COMMISSION\_AGENT\_DAILY | Daily agent commission |
| DEAL\_TYPE\_COMMISSION\_AGENT\_MONTHLY | Monthly agent commission |
| DEAL\_TYPE\_INTEREST | Interest rate |
| DEAL\_TYPE\_BUY\_CANCELED | Canceled buy deal. There can be a situation when a previously executed buy deal is canceled. In this case, the type of the previously executed deal (DEAL\_TYPE\_BUY) is changed to DEAL\_TYPE\_BUY\_CANCELED, and its profit/loss is zeroized. Previously obtained profit/loss is charged/withdrawn using a separated balance operation |
| DEAL\_TYPE\_SELL\_CANCELED | Canceled sell deal. There can be a situation when a previously executed sell deal is canceled. In this case, the type of the previously executed deal (DEAL\_TYPE\_SELL) is changed to DEAL\_TYPE\_SELL\_CANCELED, and its profit/loss is zeroized. Previously obtained profit/loss is charged/withdrawn using a separated balance operation |
| DEAL\_DIVIDEND | Dividend operations |
| DEAL\_DIVIDEND\_FRANKED | Franked (non-taxable) dividend operations |
| DEAL\_TAX | Tax charges |

 

Deals differ not only in their types set in ENUM\_DEAL\_TYPE, but also in the way they change positions. This can be a simple position opening, or accumulation of a previously opened position (market entering), position closing by an opposite deal of a corresponding volume (market exiting), or position reversing, if the opposite-direction deal covers the volume of the previously opened position.

All these situations are described by values from the ENUM\_DEAL\_ENTRY enumeration. In order to receive this information about a deal, use the [HistoryDealGetInteger()](../../../Trade-Functions/HistoryDealGetInteger/HistoryDealGetInteger.md) function with the DEAL\_ENTRY modifier.

ENUM\_DEAL\_ENTRY

| Identifier | Description |
| --- | --- |
| DEAL\_ENTRY\_IN | Entry in |
| DEAL\_ENTRY\_OUT | Entry out |
| DEAL\_ENTRY\_INOUT | Reverse |
| DEAL\_ENTRY\_OUT\_BY | Close a position by an opposite one |

 

The reason for deal execution is contained in the DEAL\_REASON property. A deal can be executed as a result of triggering of an order placed from a mobile application or an MQL5 program, as well as as a result of the StopOut event, variation margin calculation, etc. Possible values of DEAL\_REASON are described in the ENUM\_DEAL\_REASON enumeration. For non-trading deals resulting from balance, credit, commission and other operations, DEAL\_REASON\_CLIENT is indicated as the reason.

ENUM\_DEAL\_REASON

| Identifier | Description |
| --- | --- |
| DEAL\_REASON\_CLIENT | The deal was executed as a result of activation of an order placed from a desktop terminal |
| DEAL\_REASON\_MOBILE | The deal was executed as a result of activation of an order placed from a mobile application |
| DEAL\_REASON\_WEB | The deal was executed as a result of activation of an order placed from the web platform |
| DEAL\_REASON\_EXPERT | The deal was executed as a result of activation of an order placed from an MQL5 program, i.e. an Expert Advisor or a script |
| DEAL\_REASON\_SL | The deal was executed as a result of Stop Loss activation |
| DEAL\_REASON\_TP | The deal was executed as a result of Take Profit activation |
| DEAL\_REASON\_SO | The deal was executed as a result of the Stop Out event |
| DEAL\_REASON\_ROLLOVER | The deal was executed due to a rollover |
| DEAL\_REASON\_VMARGIN | The deal was executed after charging the variation margin |
| DEAL\_REASON\_SPLIT | The deal was executed after the split (price reduction) of an instrument, which had an open position during split announcement |
| DEAL\_REASON\_CORPORATE\_ACTION | The deal was executed as a result of a corporate action: merging or renaming a security, transferring a client to another account, etc. |
