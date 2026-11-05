# CExpert

CExpert

CExpert is a base class for trading strategies.

It already has some elementary trading "skills". It has built-in algorithms for working with time series and indicators and a set of virtual methods for trading strategy.

How to use it:

1. Prepare an algorithm of the strategy;  
2. Create your own class, inherited from CExpert class;  
3. Override the virtual methods in your class with your own algorithms.

Description

The CExpert class is a set of virtual methods for implementation of trading strategies.

Note

A position is recognized as belonging to an Expert Advisor and managed by it based on the pair of properties m\_symbol and m\_magic. In the "hedging" mode, multiple positions can be opened for the same symbol, therefore the m\_magic value is important.

Declaration

|  |
| --- |
| class CExpert : public CExpertBase |

Title

|  |
| --- |
| #include <Expert\Expert.mqh> |

|  |
| --- |
| Inheritance hierarchy    [CObject](../../../Basic-Class-CObject/Basic-Class-CObject.md)        [CExpertBase](../CExpertBase/CExpertBase.md)            CExpert |

Class Methods by Groups

| Initialization |  |
| --- | --- |
| [Init](Init/Init.md) | Class instance initialization method |
| virtual [InitSignal](InitSignal/InitSignal.md) | Initializes Trading Signal object |
| virtual [InitTrailing](InitTrailing/InitTrailing.md) | Initializes Trailing Stop object |
| virtual [InitMoney](InitMoney/InitMoney.md) | Initializes Money Management object |
| virtual [InitTrade](InitTrade/InitTrade.md) | Initializes Trade object |
| virtual [ValidationSettings](ValidationSettings/ValidationSettings.md) | Checks the settings |
| virtual [InitIndicators](InitIndicators/InitIndicators.md) | Initializes indicators and timeseries |
| virtual [InitParameters](InitParameters/InitParameters.md) | Expert Advisor parameters initialization method |
| virtual [Deinit](Deinit/Deinit.md) | Class instance deinitialization method |
| virtual [DeinitSignal](DeinitSignal/DeinitSignal.md) | Deinitializes Trading Signal object |
| virtual [DeinitTrailing](DeinitTrailing/DeinitTrailing.md) | Deinitializes Trailing Stop object |
| virtual [DeinitMoney](DeinitMoney/DeinitMoney.md) | Deinitializes Money Management object |
| virtual [DeinitTrade](DeinitTrade/DeinitTrade.md) | Deinitializes Trade object |
| virtual [DeinitIndicators](DeinitIndicators/DeinitIndicators.md) | Deinitializes indicators and timeseries |
| Parameters |  |
| [Magic](Magic/Magic.md) | Sets the Expert Advisor ID |
| [MaxOrders](MaxOrders/MaxOrders.md) | Gets/sets the maximum amount of allowed orders |
| [OnTickProcess](OnTickProcess/OnTickProcess.md) | Sets a flag to proceed the "OnTick" event |
| [OnTradeProcess](OnTradeProcess/OnTradeProcess.md) | Sets a flag to proceed the "OnTrade" event |
| [OnTimerProcess](OnTimerProcess/OnTimerProcess.md) | Sets a flag to proceed the "OnTimer" event |
| [OnChartEventProcess](OnChartEventProcess/OnChartEventProcess.md) | Sets a flag to proceed the "OnChartEvent" event |
| [OnBookEventProcess](OnBookEventProcess/OnBookEventProcess.md) | Sets a flag to proceed the "OnBookEvent" event |
| Event Processing Methods |  |
| [OnTick](OnTick/OnTick.md) | OnTick event handler |
| [OnTrade](OnTrade/OnTrade.md) | OnTrade event handler |
| [OnTimer](OnTimer/OnTimer.md) | OnTimer event handler |
| [OnChartEvent](OnChartEvent/OnChartEvent.md) | OnChartEvent event handler |
| [OnBookEvent](OnBookEvent/OnBookEvent.md) | OnBookEvent event handler |
| Update Methods |  |
| [Refresh](Refresh/Refresh.md) | Updates all data |
| Processing |  |
| [Processing](Processing/Processing.md) | Main processing algorithm |
| Market Entry Methods |  |
| [CheckOpen](CheckOpen/CheckOpen.md) | Checks position opening conditions |
| [CheckOpenLong](CheckOpenLong/CheckOpenLong.md) | Checks conditions to open long position |
| [CheckOpenShort](CheckOpenShort/CheckOpenShort.md) | Checks conditions to open short position |
| [OpenLong](OpenLong/OpenLong.md) | Opens a long position |
| [OpenShort](OpenShort/OpenShort.md) | Opens a short position |
| Market Exit Methods |  |
| [CheckClose](CheckClose/CheckClose.md) | Checks conditions to close current position |
| [CheckCloseLong](CheckCloseLong/CheckCloseLong.md) | Checks conditions to close long position |
| [CheckCloseShort](CheckCloseShort/CheckCloseShort.md) | Checks conditions to close short position |
| [CloseAll](CloseAll/CloseAll.md) | Closes the opened position and deletes all orders |
| [Close](Close/Close.md) | Closes the opened position |
| [CloseLong](CloseLong/CloseLong.md) | Closes the long position |
| [CloseShort](CloseShort/CloseShort.md) | Closes the short position |
| Position Reverse Methods |  |
| [CheckReverse](CheckReverse/CheckReverse.md) | Checks conditions to reverse opened position |
| [CheckReverseLong](CheckReverseLong/CheckReverseLong.md) | Checks conditions to reverse long position |
| [CheckReverseShort](CheckReverseShort/CheckReverseShort.md) | Checks conditions to reverse short position |
| [ReverseLong](ReverseLong/ReverseLong.md) | Performs reverse operation of long position |
| [ReverseShort](ReverseShort/ReverseShort.md) | Performs reverse operation of short position |
| Position/Order Trailing Methods |  |
| [CheckTrailingStop](CheckTrailingStop/CheckTrailingStop.md) | Checks conditions to modify position parameters |
| [CheckTrailingStopLong](CheckTrailingStopLong/CheckTrailingStopLong.md) | Checks Trailing Stop conditions of long position |
| [CheckTrailingStopShort](CheckTrailingStopShort/CheckTrailingStopShort.md) | Checks Trailing Stop conditions of short position |
| [TrailingStopLong](TrailingStopLong/TrailingStopLong.md) | Performs Trailing Stop for long position |
| [TrailingStopShort](TrailingStopShort/TrailingStopShort.md) | Performs Trailing Stop for short position |
| [CheckTrailingOrderLong](CheckTrailingOrderLong/CheckTrailingOrderLong.md) | Checks Trailing Stop conditions of Buy Limit/Stop order |
| [CheckTrailingOrderShort](CheckTrailingOrderShort/CheckTrailingOrderShort.md) | Checks Trailing Stop conditions of Sell Limit/Stop order |
| [TrailingOrderLong](TrailingOrderLong/TrailingOrderLong.md) | Performs Trailing Stop for Buy Limit/Stop order |
| [TrailingOrderShort](TrailingOrderShort/TrailingOrderShort.md) | Performs Trailing Stop for Sell Limit/Stop order |
| Order Delete Methods |  |
| [CheckDeleteOrderLong](CheckDeleteOrderLong/CheckDeleteOrderLong.md) | Checks conditions to delete Buy order |
| [CheckDeleteOrderShort](CheckDeleteOrderShort/CheckDeleteOrderShort.md) | Checks conditions to delete Sell order |
| [DeleteOrders](DeleteOrders/DeleteOrders.md) | Deletes all orders |
| [DeleteOrder](DeleteOrder/DeleteOrder.md) | Deletes Stop/Limit order |
| [DeleteOrderLong](DeleteOrderLong/DeleteOrderLong.md) | Deletes Buy Limit/Stop order |
| [DeleteOrderShort](DeleteOrderShort/DeleteOrderShort.md) | Deletes Sell Limit/Stop order |
| Trade Volume Methods |  |
| [LotOpenLong](LotOpenLong/LotOpenLong.md) | Gets trade volume for buy operation |
| [LotOpenShort](LotOpenShort/LotOpenShort.md) | Gets trade volume for sell operation |
| [LotReverse](LotReverse/LotReverse.md) | Gets trade volume for position reverse operation |
| Trade History Methods |  |
| [PrepareHistoryDate](PrepareHistoryDate/PrepareHistoryDate.md) | Sets starting date for trade history tracking |
| [HistoryPoint](HistoryPoint/HistoryPoint.md) | Creates a checkpoint of trade history (saves number of positions, orders, deals and historical orders) |
| [CheckTradeState](CheckTradeState/CheckTradeState.md) | Compares the current state with the saved one and calls the corresponding event handler |
| Event flags |  |
| [WaitEvent](WaitEvent/WaitEvent.md) | Sets the trading event waiting flag |
| [NoWaitEvent](NoWaitEvent/NoWaitEvent.md) | Resets the trading event waiting flag |
| Trade Event Processing Methods |  |
| [TradeEventPositionStopTake](TradeEventPositionStopTake/TradeEventPositionStopTake.md) | Event handler of the "Position Stop Loss/Take Profit triggered" event |
| [TradeEventOrderTriggered](TradeEventOrderTriggered/TradeEventOrderTriggered.md) | Event handler of the "Pending Order Triggered" event |
| [TradeEventPositionOpened](TradeEventPositionOpened/TradeEventPositionOpened.md) | Event handler of the "Position Opened" event |
| [TradeEventPositionVolumeChanged](TradeEventPositionVolumeChanged/TradeEventPositionVolumeChanged.md) | Event handler of the "Position Volume Changed" event |
| [TradeEventPositionModified](TradeEventPositionModified/TradeEventPositionModified.md) | Event handler of the "Position Modified" event |
| [TradeEventPositionClosed](TradeEventPositionClosed/TradeEventPositionClosed.md) | Event handler of the "Position Closed" event |
| [TradeEventOrderPlaced](TradeEventOrderPlaced/TradeEventOrderPlaced.md) | Event handler of the "Pending Order Placed" event |
| [TradeEventOrderModified](TradeEventOrderModified/TradeEventOrderModified.md) | Event handler of the "Pending Order Modified" event |
| [TradeEventOrderDeleted](TradeEventOrderDeleted/TradeEventOrderDeleted.md) | Event handler of the "Pending Order Deleted" event |
| [TradeEventNotIdentified](TradeEventNotIdentified/TradeEventNotIdentified.md) | Event handler of the non-identified event |
| Service methods |  |
| [TimeframeAdd](TimeframeAdd/TimeframeAdd.md) | Adds a timeframe to track |
| [TimeframesFlags](TimeframesFlags/TimeframesFlags.md) | Forms timeframe flags |
| [SelectPosition](SelectPosition/SelectPosition.md) | Selects a position to work with |

| Methods inherited from class CObject  Prev, Prev, Next, Next, [Save](../../../Basic-Class-CObject/Save/Save.md), [Load](../../../Basic-Class-CObject/Load/Load.md), [Type](../../../Basic-Class-CObject/Type/Type.md), [Compare](../../../Basic-Class-CObject/Compare/Compare.md) |
| --- |
| Methods inherited from class CExpertBase  [InitPhase](../CExpertBase/InitPhase/InitPhase.md), [TrendType](../CExpertBase/TrendType/TrendType.md), [UsedSeries](../CExpertBase/UsedSeries/UsedSeries.md), [EveryTick](../CExpertBase/EveryTick/EveryTick.md), [Open](../CExpertBase/Open/Open.md), [High](../CExpertBase/High/High.md), [Low](../CExpertBase/Low/Low.md), [Close](../CExpertBase/Close/Close.md), [Spread](../CExpertBase/Spread/Spread.md), [Time](../CExpertBase/Time/Time.md), [TickVolume](../CExpertBase/TickVolume/TickVolume.md), [RealVolume](../CExpertBase/RealVolume/RealVolume.md), [Symbol](../CExpertBase/Symbol/Symbol.md), [Period](../CExpertBase/Period/Period.md), [Magic](../CExpertBase/Magic/Magic.md), SetMarginMode, [SetPriceSeries](../CExpertBase/SetPriceSeries/SetPriceSeries.md), [SetOtherSeries](../CExpertBase/SetOtherSeries/SetOtherSeries.md) |
