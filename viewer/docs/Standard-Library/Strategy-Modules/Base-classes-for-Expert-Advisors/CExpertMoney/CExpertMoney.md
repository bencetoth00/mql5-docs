# CExpertMoney


CExpertMoney is a base class for money and risk management algorithms.

### Description

CExpertMoney is a base class for implementation of money and risk management classes.

### Declaration

```cpp
   class CExpertMoney : public CObject
```

### Title

```cpp
   #include <Expert\ExpertMoney.mqh>
```

|  |
| --- |
| Inheritance hierarchy    [CObject](../../../Basic-Class-CObject/Basic-Class-CObject.md)        [CExpertBase](../CExpertBase/CExpertBase.md)            CExpertMoney  Direct descendants  [CMoneyFixedLot](../../Money-Management-Classes/CMoneyFixedLot/CMoneyFixedLot.md), [CMoneyFixedMargin](../../Money-Management-Classes/CMoneyFixedMargin/CMoneyFixedMargin.md), [CMoneyFixedRisk](../../Money-Management-Classes/CMoneyFixedRisk/CMoneyFixedRisk.md), [CMoneyNone](../../Money-Management-Classes/CMoneyNone/CMoneyNone.md), [CMoneySizeOptimized](../../Money-Management-Classes/CMoneySizeOptimized/CMoneySizeOptimized.md) |

### Class Methods by Groups

| Access to Protected Data |  |
| --- | --- |
| [Percent](Percent/Percent.md) | Sets the value of "Risk percent" parameter |
| Initialization |  |
| virtual [ValidationSettings](ValidationSettings/ValidationSettings.md) | Checks the settings |
| Checking Trading Conditions |  |
| virtual [CheckOpenLong](CheckOpenLong/CheckOpenLong.md) | Gets the volume for a long position |
| virtual [CheckOpenShort](CheckOpenShort/CheckOpenShort.md) | Gets the volume for a short position |
| virtual [CheckReverse](CheckReverse/CheckReverse.md) | Gets the volume for a reverse of the position |
| virtual [CheckClose](CheckClose/CheckClose.md) | Checks conditions to close an opened position |

| Methods inherited from class CObject  Prev, Prev, Next, Next, [Save](../../../Basic-Class-CObject/Save/Save.md), [Load](../../../Basic-Class-CObject/Load/Load.md), [Type](../../../Basic-Class-CObject/Type/Type.md), [Compare](../../../Basic-Class-CObject/Compare/Compare.md) |
| --- |
| Methods inherited from class CExpertBase  [InitPhase](../CExpertBase/InitPhase/InitPhase.md), [TrendType](../CExpertBase/TrendType/TrendType.md), [UsedSeries](../CExpertBase/UsedSeries/UsedSeries.md), [EveryTick](../CExpertBase/EveryTick/EveryTick.md), [Open](../CExpertBase/Open/Open.md), [High](../CExpertBase/High/High.md), [Low](../CExpertBase/Low/Low.md), [Close](../CExpertBase/Close/Close.md), [Spread](../CExpertBase/Spread/Spread.md), [Time](../CExpertBase/Time/Time.md), [TickVolume](../CExpertBase/TickVolume/TickVolume.md), [RealVolume](../CExpertBase/RealVolume/RealVolume.md), [Init](../CExpertBase/Init/Init.md), [Symbol](../CExpertBase/Symbol/Symbol.md), [Period](../CExpertBase/Period/Period.md), [Magic](../CExpertBase/Magic/Magic.md), SetMarginMode, [SetPriceSeries](../CExpertBase/SetPriceSeries/SetPriceSeries.md), [SetOtherSeries](../CExpertBase/SetOtherSeries/SetOtherSeries.md), [InitIndicators](../CExpertBase/InitIndicators/InitIndicators.md) |