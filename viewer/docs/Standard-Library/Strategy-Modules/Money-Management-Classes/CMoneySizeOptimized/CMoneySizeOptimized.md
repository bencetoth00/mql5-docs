# CMoneySizeOptimized


CMoneySizeOptimized is a class with implementation of money and risk management algorithm depending on results of the previous deals.

### Description

CMoneySizeOptimized implements the market entry algorithm with the lot size depending on results of the previous deals.

### Declaration

```cpp
   class CMoneySizeOptimized: public CExpertMoney
```

### Title

```cpp
   #include <Expert\Money\MoneySizeOptimized.mqh>
```

|  |
| --- |
| Inheritance hierarchy    [CObject](../../../Basic-Class-CObject/Basic-Class-CObject.md)        [CExpertBase](../../Base-classes-for-Expert-Advisors/CExpertBase/CExpertBase.md)            [CExpertMoney](../../Base-classes-for-Expert-Advisors/CExpertMoney/CExpertMoney.md)                CMoneySizeOptimized |

### Class Methods by Groups

| Initialization |  |
| --- | --- |
| [DecreaseFactor](DecreaseFactor/DecreaseFactor.md) | Sets the parameter value |
| virtual [ValidationSettings](ValidationSettings/ValidationSettings.md) | Checks the settings |
| Money and Risk Management Methods |  |
| virtual [CheckOpenLong](CheckOpenLong/CheckOpenLong.md) | Gets trade volume for a long position |
| virtual [CheckOpenShort](CheckOpenShort/CheckOpenShort.md) | Gets trade volume for a short position |

| Methods inherited from class CObject  Prev, Prev, Next, Next, [Save](../../../Basic-Class-CObject/Save/Save.md), [Load](../../../Basic-Class-CObject/Load/Load.md), [Type](../../../Basic-Class-CObject/Type/Type.md), [Compare](../../../Basic-Class-CObject/Compare/Compare.md) |
| --- |
| Methods inherited from class CExpertBase  [InitPhase](../../Base-classes-for-Expert-Advisors/CExpertBase/InitPhase/InitPhase.md), [TrendType](../../Base-classes-for-Expert-Advisors/CExpertBase/TrendType/TrendType.md), [UsedSeries](../../Base-classes-for-Expert-Advisors/CExpertBase/UsedSeries/UsedSeries.md), [EveryTick](../../Base-classes-for-Expert-Advisors/CExpertBase/EveryTick/EveryTick.md), [Open](../../Base-classes-for-Expert-Advisors/CExpertBase/Open/Open.md), [High](../../Base-classes-for-Expert-Advisors/CExpertBase/High/High.md), [Low](../../Base-classes-for-Expert-Advisors/CExpertBase/Low/Low.md), [Close](../../Base-classes-for-Expert-Advisors/CExpertBase/Close/Close.md), [Spread](../../Base-classes-for-Expert-Advisors/CExpertBase/Spread/Spread.md), [Time](../../Base-classes-for-Expert-Advisors/CExpertBase/Time/Time.md), [TickVolume](../../Base-classes-for-Expert-Advisors/CExpertBase/TickVolume/TickVolume.md), [RealVolume](../../Base-classes-for-Expert-Advisors/CExpertBase/RealVolume/RealVolume.md), [Init](../../Base-classes-for-Expert-Advisors/CExpertBase/Init/Init.md), [Symbol](../../Base-classes-for-Expert-Advisors/CExpertBase/Symbol/Symbol.md), [Period](../../Base-classes-for-Expert-Advisors/CExpertBase/Period/Period.md), [Magic](../../Base-classes-for-Expert-Advisors/CExpertBase/Magic/Magic.md), SetMarginMode, [SetPriceSeries](../../Base-classes-for-Expert-Advisors/CExpertBase/SetPriceSeries/SetPriceSeries.md), [SetOtherSeries](../../Base-classes-for-Expert-Advisors/CExpertBase/SetOtherSeries/SetOtherSeries.md), [InitIndicators](../../Base-classes-for-Expert-Advisors/CExpertBase/InitIndicators/InitIndicators.md) |
| Methods inherited from class CExpertMoney  [Percent](../../Base-classes-for-Expert-Advisors/CExpertMoney/Percent/Percent.md), [CheckReverse](../../Base-classes-for-Expert-Advisors/CExpertMoney/CheckReverse/CheckReverse.md), [CheckClose](../../Base-classes-for-Expert-Advisors/CExpertMoney/CheckClose/CheckClose.md) |