# CTrailingPSAR

CTrailingPSAR

CTrailingPSAR is a class with implementation of Trailing Stop algorithm based on the values of Parabolic SAR indicator.

Description

CTrailingPSAR class implements the Trailing Stop algorithm based on the values of Parabolic SAR indicator of the previous (completed) bar.

Declaration

|  |
| --- |
| class CTrailingPSAR: public CExpertTrailing |

Title

|  |
| --- |
| #include <Expert\Trailing\TrailingParabolicSAR.mqh> |

|  |
| --- |
| Inheritance hierarchy    [CObject](../../../Basic-Class-CObject/Basic-Class-CObject.md)        [CExpertBase](../../Base-classes-for-Expert-Advisors/CExpertBase/CExpertBase.md)            [CExpertTrailing](../../Base-classes-for-Expert-Advisors/CExpertTrailing/CExpertTrailing.md)                CTrailingPSAR |

Class Methods by Groups

| Initialization |  |
| --- | --- |
| [Step](Step/Step.md) | Sets the value of step of Parabolic SAR indicator |
| [Maximum](Maximum/Maximum.md) | Sets the value of maximum of Parabolic SAR indicator |
| virtual [InitIndicators](InitIndicators/InitIndicators.md) | Initializes indicators and timeseries |
| Check Trailing Methods |  |
| virtual [CheckTrailingStopLong](CheckTrailingStopLong/CheckTrailingStopLong.md) | Check conditions of trailing stop of a long position |
| virtual [CheckTrailingStopShort](CheckTrailingStopShort/CheckTrailingStopShort.md) | Check conditions of trailing stop of a short position |

| Methods inherited from class CObject  Prev, Prev, Next, Next, [Save](../../../Basic-Class-CObject/Save/Save.md), [Load](../../../Basic-Class-CObject/Load/Load.md), [Type](../../../Basic-Class-CObject/Type/Type.md), [Compare](../../../Basic-Class-CObject/Compare/Compare.md) |
| --- |
| Methods inherited from class CExpertBase  [InitPhase](../../Base-classes-for-Expert-Advisors/CExpertBase/InitPhase/InitPhase.md), [TrendType](../../Base-classes-for-Expert-Advisors/CExpertBase/TrendType/TrendType.md), [UsedSeries](../../Base-classes-for-Expert-Advisors/CExpertBase/UsedSeries/UsedSeries.md), [EveryTick](../../Base-classes-for-Expert-Advisors/CExpertBase/EveryTick/EveryTick.md), [Open](../../Base-classes-for-Expert-Advisors/CExpertBase/Open/Open.md), [High](../../Base-classes-for-Expert-Advisors/CExpertBase/High/High.md), [Low](../../Base-classes-for-Expert-Advisors/CExpertBase/Low/Low.md), [Close](../../Base-classes-for-Expert-Advisors/CExpertBase/Close/Close.md), [Spread](../../Base-classes-for-Expert-Advisors/CExpertBase/Spread/Spread.md), [Time](../../Base-classes-for-Expert-Advisors/CExpertBase/Time/Time.md), [TickVolume](../../Base-classes-for-Expert-Advisors/CExpertBase/TickVolume/TickVolume.md), [RealVolume](../../Base-classes-for-Expert-Advisors/CExpertBase/RealVolume/RealVolume.md), [Init](../../Base-classes-for-Expert-Advisors/CExpertBase/Init/Init.md), [Symbol](../../Base-classes-for-Expert-Advisors/CExpertBase/Symbol/Symbol.md), [Period](../../Base-classes-for-Expert-Advisors/CExpertBase/Period/Period.md), [Magic](../../Base-classes-for-Expert-Advisors/CExpertBase/Magic/Magic.md), SetMarginMode, [ValidationSettings](../../Base-classes-for-Expert-Advisors/CExpertBase/ValidationSettings/ValidationSettings.md), [SetPriceSeries](../../Base-classes-for-Expert-Advisors/CExpertBase/SetPriceSeries/SetPriceSeries.md), [SetOtherSeries](../../Base-classes-for-Expert-Advisors/CExpertBase/SetOtherSeries/SetOtherSeries.md) |
