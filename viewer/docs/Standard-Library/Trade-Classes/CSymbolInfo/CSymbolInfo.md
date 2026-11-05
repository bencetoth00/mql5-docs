# CSymbolInfo


CSymbolInfo is a class for easy access to the symbol properties.

### Description

CSymbolInfo class provides access to the symbol properties.

### Declaration

```cpp
   class CSymbolInfo : public CObject
```

### Title

```cpp
   #include <Trade\SymbolInfo.mqh>
```

|  |
| --- |
| Inheritance hierarchy    [CObject](../../Basic-Class-CObject/Basic-Class-CObject.md)        CSymbolInfo |

### Class methods by groups

| Controlling |  |
| --- | --- |
| [Refresh](Refresh/Refresh.md) | Refreshes the symbol data |
| [RefreshRates](RefreshRates/RefreshRates.md) | Refreshes the symbol quotes |
| Properties |  |
| [Name](Name/Name.md) | Gets/sets symbol name |
| [Select](Select/Select.md) | Gets/sets the "Market Watch" symbol flag |
| [IsSynchronized](IsSynchronized/IsSynchronized.md) | Checks the symbol synchronization with server |
| Volumes |  |
| [Volume](Volume/Volume.md) | Gets the volume of last deal |
| [VolumeHigh](VolumeHigh/VolumeHigh.md) | Gets the maximal volume for a day |
| [VolumeLow](VolumeLow/VolumeLow.md) | Gets the minimal volume for a day |
| Miscellaneous |  |
| [Time](Time/Time.md) | Gets the time of last quote |
| [Spread](Spread/Spread.md) | Gets the amount of spread (in points) |
| [SpreadFloat](SpreadFloat/SpreadFloat.md) | Gets the flag of floating spread |
| [TicksBookDepth](TicksBookDepth/TicksBookDepth.md) | Gets the depth of ticks saving |
| Levels |  |
| [StopsLevel](StopsLevel/StopsLevel.md) | Gets the minimal indent for orders (in points) |
| [FreezeLevel](FreezeLevel/FreezeLevel.md) | Gets the distance of freezing trade operations (in points) |
| Bid prices |  |
| [Bid](Bid/Bid.md) | Gets the current Bid price |
| [BidHigh](BidHigh/BidHigh.md) | Gets the maximal Bid price for a day |
| [BidLow](BidLow/BidLow.md) | Gets the minimal Bid price for a day |
| Ask prices |  |
| [Ask](Ask/Ask.md) | Gets the current Ask price |
| [AskHigh](AskHigh/AskHigh.md) | Gets the maximal Ask price for a day |
| [AskLow](AskLow/AskLow.md) | Gets the minimal Ask price for a day |
| Prices |  |
| [Last](Last/Last.md) | Gets the current Last price |
| [LastHigh](LastHigh/LastHigh.md) | Gets the maximal Last price for a day |
| [LastLow](LastLow/LastLow.md) | Gets the minimal Last price for a day |
| Trade modes |  |
| [TradeCalcMode](TradeCalcMode/TradeCalcMode.md) | Gets the mode of contract cost calculation |
| [TradeCalcModeDescription](TradeCalcModeDescription/TradeCalcModeDescription.md) | Gets the mode of contract cost calculation as a string |
| [TradeMode](TradeMode/TradeMode.md) | Gets the type of order execution |
| [TradeModeDescription](TradeModeDescription/TradeModeDescription.md) | Gets the type of order execution as a string |
| [TradeExecution](TradeExecution/TradeExecution.md) | Gets the trade execution mode |
| [TradeExecutionDescription](TradeExecutionDescription/TradeExecutionDescription.md) | Gets the execution mode as a string |
| Swaps |  |
| [SwapMode](SwapMode/SwapMode.md) | Gets the swap calculation mode |
| [SwapModeDescription](SwapModeDescription/SwapModeDescription.md) | Gets the swap calculation mode as a string |
| [SwapRollover3days](SwapRollover3days/SwapRollover3days.md) | Gets the day of triple swap charge |
| [SwapRollover3daysDescription](SwapRollover3daysDescription/SwapRollover3daysDescription.md) | Gets the day of triple swap charge as a string |
| Margins and flags |  |
| [MarginInitial](MarginInitial/MarginInitial.md) | Gets the value of initial margin |
| [MarginMaintenance](MarginMaintenance/MarginMaintenance.md) | Gets the value of maintenance margin |
| [MarginLong](MarginLong/MarginLong.md) | Gets the rate of margin charging for long positions |
| [MarginShort](MarginShort/MarginShort.md) | Gets the rate of margin charging for short positions |
| [MarginLimit](MarginLimit/MarginLimit.md) | Gets the rate of margin charging for Limit orders |
| [MarginStop](MarginStop/MarginStop.md) | Gets the rate of margin charging for Stop orders |
| [MarginStopLimit](MarginStopLimit/MarginStopLimit.md) | Gets the rate of margin charging for StopLimit orders |
| [TradeTimeFlags](TradeTimeFlags/TradeTimeFlags.md) | Gets the flags of allowed expiration modes |
| [TradeFillFlags](TradeFillFlags/TradeFillFlags.md) | Gets the flags of allowed filling modes |
| Quantization |  |
| [Digits](Digits/Digits.md) | Gets the number of digits after period |
| [Point](Point/Point.md) | Gets the value of one point |
| [TickValue](TickValue/TickValue.md) | Gets the tick value (minimal change of price) |
| [TickValueProfit](TickValueProfit/TickValueProfit.md) | Gets the calculated tick price for a profitable position |
| [TickValueLoss](TickValueLoss/TickValueLoss.md) | Gets the calculated tick price for a losing position |
| [TickSize](TickSize/TickSize.md) | Gets the minimal change of price |
| Contracts sizes |  |
| [ContractSize](ContractSize/ContractSize.md) | Gets the amount of trade contract |
| [LotsMin](LotsMin/LotsMin.md) | Gets the minimal volume to close a deal |
| [LotsMax](LotsMax/LotsMax.md) | Gets the maximal volume to close a deal |
| [LotsStep](LotsStep/LotsStep.md) | Gets the minimal step of volume change to close a deal |
| [LotsLimit](LotsLimit/LotsLimit.md) | Gets the maximal allowed volume of opened position and pending orders (direction insensitive) for one symbol |
| Swaps sizes |  |
| [SwapLong](SwapLong/SwapLong.md) | Gets the value of long position swap |
| [SwapShort](SwapShort/SwapShort.md) | Gets the value of short position swap |
| Text properties |  |
| [CurrencyBase](CurrencyBase/CurrencyBase.md) | Gets the name of symbol base currency |
| [CurrencyProfit](CurrencyProfit/CurrencyProfit.md) | Gets the profit currency name |
| [CurrencyMargin](CurrencyMargin/CurrencyMargin.md) | Gets the margin currency name |
| [Bank](Bank/Bank.md) | Gets the name of current quote source |
| [Description](Description/Description.md) | Gets the string description of symbol |
| [Path](Path/Path.md) | Gets the path in symbols tree |
| Symbol properties |  |
| [SessionDeals](SessionDeals/SessionDeals.md) | Gets the number of deals in the current session |
| [SessionBuyOrders](SessionBuyOrders/SessionBuyOrders.md) | Gets the number of Buy orders at the moment |
| [SessionSellOrders](SessionSellOrders/SessionSellOrders.md) | Gets the number of Sell orders at the moment |
| [SessionTurnover](SessionTurnover/SessionTurnover.md) | Gets the summary of turnover of the current session |
| [SessionInterest](SessionInterest/SessionInterest.md) | Gets the summary of open interest of the current session |
| [SessionBuyOrdersVolume](SessionBuyOrdersVolume/SessionBuyOrdersVolume.md) | Gets the current volume of Buy orders |
| [SessionSellOrdersVolume](SessionSellOrdersVolume/SessionSellOrdersVolume.md) | Gets the current volume of Sell orders |
| [SessionOpen](SessionOpen/SessionOpen.md) | Gets the open price of the current session |
| [SessionClose](SessionClose/SessionClose.md) | Gets the close price of the current session |
| [SessionAW](SessionAW/SessionAW.md) | Gets the average weighted price of the current session |
| [SessionPriceSettlement](SessionPriceSettlement/SessionPriceSettlement.md) | Gets the settlement price of the current session |
| [SessionPriceLimitMin](SessionPriceLimitMin/SessionPriceLimitMin.md) | Gets the minimal price of the current session |
| [SessionPriceLimitMax](SessionPriceLimitMax/SessionPriceLimitMax.md) | Gets the maximal price of the current session |
| Access to MQL5 API functions |  |
| [InfoInteger](InfoInteger/InfoInteger.md) | Gets the value of specified integer type property |
| [InfoDouble](InfoDouble/InfoDouble.md) | Gets the value of specified double type property |
| [InfoString](InfoString/InfoString.md) | Gets the value of specified string type property |
| Service functions |  |
| [NormalizePrice](NormalizePrice/NormalizePrice.md) | Returns the value of price, normalized using the symbol properties |

|  |
| --- |
| Methods inherited from class CObject  Prev, Prev, Next, Next, [Save](../../Basic-Class-CObject/Save/Save.md), [Load](../../Basic-Class-CObject/Load/Load.md), [Type](../../Basic-Class-CObject/Type/Type.md), [Compare](../../Basic-Class-CObject/Compare/Compare.md) |