# CExpertTrailing

CExpertTrailing

CExpertTrailing is a base class for trailing algorithms, it does nothing but provides the interfaces.

How to use it:

1. Prepare an algorithm for trailing;  
2. Create your own trailing class inherited from CExpertTrailing class;  
3. Override the virtual methods in your class with your own algorithms.

You can find an examples of trailing classes in the Expert\Trailing\ folder.

Description

CExpertTrailing is a base class for implementation of trailing stop algorithms.

Declaration

|  |
| --- |
| class CExpertTrailing : public CExpertBase |

Title

|  |
| --- |
| #include <Expert\ExpertTrailing.mqh> |

|  |
| --- |
| Inheritance hierarchy    [CObject](../../../Basic-Class-CObject/Basic-Class-CObject.md)        [CExpertBase](../CExpertBase/CExpertBase.md)            CExpertTrailing  Direct descendants  [CTrailingFixedPips](../../Trailing-Stop-Classes/CTrailingFixedPips/CTrailingFixedPips.md), [CTrailingMA](../../Trailing-Stop-Classes/CTrailingMA/CTrailingMA.md), [CTrailingNone](../../Trailing-Stop-Classes/CTrailingNone/CTrailingNone.md), [CTrailingPSAR](../../Trailing-Stop-Classes/CTrailingPSAR/CTrailingPSAR.md) |

Class Methods by Groups

| Checking of Trailing Stop Conditions |  |
| --- | --- |
| virtual [CheckTrailingStopLong](CheckTrailingStopLong/CheckTrailingStopLong.md) | Checks conditions to modify parameters of the long position |
| virtual [CheckTrailingStopShort](CheckTrailingStopShort/CheckTrailingStopShort.md) | Checks conditions to modify parameters of the short position |

| Methods inherited from class CObject  Prev, Prev, Next, Next, [Save](../../../Basic-Class-CObject/Save/Save.md), [Load](../../../Basic-Class-CObject/Load/Load.md), [Type](../../../Basic-Class-CObject/Type/Type.md), [Compare](../../../Basic-Class-CObject/Compare/Compare.md) |
| --- |
| Methods inherited from class CExpertBase  [InitPhase](../CExpertBase/InitPhase/InitPhase.md), [TrendType](../CExpertBase/TrendType/TrendType.md), [UsedSeries](../CExpertBase/UsedSeries/UsedSeries.md), [EveryTick](../CExpertBase/EveryTick/EveryTick.md), [Open](../CExpertBase/Open/Open.md), [High](../CExpertBase/High/High.md), [Low](../CExpertBase/Low/Low.md), [Close](../CExpertBase/Close/Close.md), [Spread](../CExpertBase/Spread/Spread.md), [Time](../CExpertBase/Time/Time.md), [TickVolume](../CExpertBase/TickVolume/TickVolume.md), [RealVolume](../CExpertBase/RealVolume/RealVolume.md), [Init](../CExpertBase/Init/Init.md), [Symbol](../CExpertBase/Symbol/Symbol.md), [Period](../CExpertBase/Period/Period.md), [Magic](../CExpertBase/Magic/Magic.md), SetMarginMode, [ValidationSettings](../CExpertBase/ValidationSettings/ValidationSettings.md), [SetPriceSeries](../CExpertBase/SetPriceSeries/SetPriceSeries.md), [SetOtherSeries](../CExpertBase/SetOtherSeries/SetOtherSeries.md), [InitIndicators](../CExpertBase/InitIndicators/InitIndicators.md) |
