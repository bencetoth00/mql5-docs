# CTrailingFixedPips

CTrailingFixedPips

CTrailingFixedPips is a class with implementation of Trailing Stop algorithm based on fixed points trailing.

CTrailingFixedPips class implements the following algorithm of trailing open positions: If Stop Loss level is equal to zero, Stop Loss order modification condition is considered unfulfilled, therefore there is no suggestion to change a position's Stop Loss. Otherwise, the check of whether the price has moved in favorable direction is performed.

If a position has a Stop Loss order, it checks the minimal allowed Stop Loss distance to the current price. If the position has no Stop Loss level, the distance between the current and open prices is checked. If the distance exceeds Stop Loss level, the system suggests to set a new Stop Loss price.

If Stop Loss modification condition is fulfilled and Take Profit is not equal to zero, the system suggests setting a new Take Profit price.

If Expert Advisor class has been [initialized](../../Base-classes-for-Expert-Advisors/CExpert/Init/Init.md) with the flag every\_tick=false, it will perform all operations (trading, trailing, etc) only at the new bar on a working symbol and timeframe. In this case, setting Take Profit order allows you to close position when the price moves in the position direction before a new bar appears.

Description

CTrailingFixedPips implements the Trailing Stop algorithm at a specified "distance" from the current price (in points).

Declaration

|  |
| --- |
| class CTrailingFixedPips: public CExpertTrailing |

Title

|  |
| --- |
| #include <Expert\Trailing\CTrailingFixedPips.mqh> |

|  |
| --- |
| Inheritance hierarchy    [CObject](../../../Basic-Class-CObject/Basic-Class-CObject.md)        [CExpertBase](../../Base-classes-for-Expert-Advisors/CExpertBase/CExpertBase.md)            [CExpertTrailing](../../Base-classes-for-Expert-Advisors/CExpertTrailing/CExpertTrailing.md)                CTrailingFixedPips |

Class Methods by Groups

| Initialization |  |
| --- | --- |
| [StopLevel](StopLevel/StopLevel.md) | Sets the value of Stop Loss level |
| [ProfitLevel](ProfitLevel/ProfitLevel.md) | Sets the value of Take Profit level |
| virtual [ValidationSettings](ValidationSettings/ValidationSettings.md) | Checks the settings |
| Check Trailing Methods |  |
| virtual [CheckTrailingStopLong](CheckTrailingStopLong/CheckTrailingStopLong.md) | Check Trailing Stop conditions of a long position |
| virtual [CheckTrailingStopShort](CheckTrailingStopShort/CheckTrailingStopShort.md) | Check Trailing Stop conditions of a short position |

| Methods inherited from class CObject  Prev, Prev, Next, Next, [Save](../../../Basic-Class-CObject/Save/Save.md), [Load](../../../Basic-Class-CObject/Load/Load.md), [Type](../../../Basic-Class-CObject/Type/Type.md), [Compare](../../../Basic-Class-CObject/Compare/Compare.md) |
| --- |
| Methods inherited from class CExpertBase  [InitPhase](../../Base-classes-for-Expert-Advisors/CExpertBase/InitPhase/InitPhase.md), [TrendType](../../Base-classes-for-Expert-Advisors/CExpertBase/TrendType/TrendType.md), [UsedSeries](../../Base-classes-for-Expert-Advisors/CExpertBase/UsedSeries/UsedSeries.md), [EveryTick](../../Base-classes-for-Expert-Advisors/CExpertBase/EveryTick/EveryTick.md), [Open](../../Base-classes-for-Expert-Advisors/CExpertBase/Open/Open.md), [High](../../Base-classes-for-Expert-Advisors/CExpertBase/High/High.md), [Low](../../Base-classes-for-Expert-Advisors/CExpertBase/Low/Low.md), [Close](../../Base-classes-for-Expert-Advisors/CExpertBase/Close/Close.md), [Spread](../../Base-classes-for-Expert-Advisors/CExpertBase/Spread/Spread.md), [Time](../../Base-classes-for-Expert-Advisors/CExpertBase/Time/Time.md), [TickVolume](../../Base-classes-for-Expert-Advisors/CExpertBase/TickVolume/TickVolume.md), [RealVolume](../../Base-classes-for-Expert-Advisors/CExpertBase/RealVolume/RealVolume.md), [Init](../../Base-classes-for-Expert-Advisors/CExpertBase/Init/Init.md), [Symbol](../../Base-classes-for-Expert-Advisors/CExpertBase/Symbol/Symbol.md), [Period](../../Base-classes-for-Expert-Advisors/CExpertBase/Period/Period.md), [Magic](../../Base-classes-for-Expert-Advisors/CExpertBase/Magic/Magic.md), SetMarginMode, [SetPriceSeries](../../Base-classes-for-Expert-Advisors/CExpertBase/SetPriceSeries/SetPriceSeries.md), [SetOtherSeries](../../Base-classes-for-Expert-Advisors/CExpertBase/SetOtherSeries/SetOtherSeries.md), [InitIndicators](../../Base-classes-for-Expert-Advisors/CExpertBase/InitIndicators/InitIndicators.md) |
