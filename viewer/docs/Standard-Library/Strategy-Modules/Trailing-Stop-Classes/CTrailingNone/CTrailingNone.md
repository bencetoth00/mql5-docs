# CTrailingNone


CTrailingNone is a stub class. This class should be used at initialization of trailing object in CExpert class if your strategy does not use Trailing Stop.

### Description

CTrailingNone class does not implement any Trailing Stop algorithm. The methods of checking Trailing Stop conditions always return false.

### Declaration

```cpp
class CTrailingNone: public CExpertTrailing
```

### Title

```cpp
   #include <Expert\Trailing\TrailingNone.mqh>
```

|  |
| --- |
| Inheritance hierarchy    [CObject](../../../Basic-Class-CObject/Basic-Class-CObject.md)        [CExpertBase](../../Base-classes-for-Expert-Advisors/CExpertBase/CExpertBase.md)            [CExpertTrailing](../../Base-classes-for-Expert-Advisors/CExpertTrailing/CExpertTrailing.md)                CTrailingNone |

### Class Methods by Groups

| Check Trailing Methods |  |
| --- | --- |
| virtual [CheckTrailingStopLong](CheckTrailingStopLong/CheckTrailingStopLong.md) | A stub method for checking Trailing Stop conditions of a long position |
| virtual [CheckTrailingStopShort](CheckTrailingStopShort/CheckTrailingStopShort.md) | A stub method for checking Trailing Stop conditions of a short position |

| Methods inherited from class CObject  Prev, Prev, Next, Next, [Save](../../../Basic-Class-CObject/Save/Save.md), [Load](../../../Basic-Class-CObject/Load/Load.md), [Type](../../../Basic-Class-CObject/Type/Type.md), [Compare](../../../Basic-Class-CObject/Compare/Compare.md) |
| --- |
| Methods inherited from class CExpertBase  [InitPhase](../../Base-classes-for-Expert-Advisors/CExpertBase/InitPhase/InitPhase.md), [TrendType](../../Base-classes-for-Expert-Advisors/CExpertBase/TrendType/TrendType.md), [UsedSeries](../../Base-classes-for-Expert-Advisors/CExpertBase/UsedSeries/UsedSeries.md), [EveryTick](../../Base-classes-for-Expert-Advisors/CExpertBase/EveryTick/EveryTick.md), [Open](../../Base-classes-for-Expert-Advisors/CExpertBase/Open/Open.md), [High](../../Base-classes-for-Expert-Advisors/CExpertBase/High/High.md), [Low](../../Base-classes-for-Expert-Advisors/CExpertBase/Low/Low.md), [Close](../../Base-classes-for-Expert-Advisors/CExpertBase/Close/Close.md), [Spread](../../Base-classes-for-Expert-Advisors/CExpertBase/Spread/Spread.md), [Time](../../Base-classes-for-Expert-Advisors/CExpertBase/Time/Time.md), [TickVolume](../../Base-classes-for-Expert-Advisors/CExpertBase/TickVolume/TickVolume.md), [RealVolume](../../Base-classes-for-Expert-Advisors/CExpertBase/RealVolume/RealVolume.md), [Init](../../Base-classes-for-Expert-Advisors/CExpertBase/Init/Init.md), [Symbol](../../Base-classes-for-Expert-Advisors/CExpertBase/Symbol/Symbol.md), [Period](../../Base-classes-for-Expert-Advisors/CExpertBase/Period/Period.md), [Magic](../../Base-classes-for-Expert-Advisors/CExpertBase/Magic/Magic.md), SetMarginMode, [ValidationSettings](../../Base-classes-for-Expert-Advisors/CExpertBase/ValidationSettings/ValidationSettings.md), [SetPriceSeries](../../Base-classes-for-Expert-Advisors/CExpertBase/SetPriceSeries/SetPriceSeries.md), [SetOtherSeries](../../Base-classes-for-Expert-Advisors/CExpertBase/SetOtherSeries/SetOtherSeries.md), [InitIndicators](../../Base-classes-for-Expert-Advisors/CExpertBase/InitIndicators/InitIndicators.md) |
| Methods inherited from class CExpertTrailing  [CheckTrailingStopLong](../../Base-classes-for-Expert-Advisors/CExpertTrailing/CheckTrailingStopLong/CheckTrailingStopLong.md), [CheckTrailingStopShort](../../Base-classes-for-Expert-Advisors/CExpertTrailing/CheckTrailingStopShort/CheckTrailingStopShort.md) |