# CExpertSignal


CExpertSignal is a base class for trading signals, it does nothing (except [CheckReverseLong()](CheckReverseLong/CheckReverseLong.md) and [CheckReverseShort()](CheckReverseShort/CheckReverseShort.md) methods) but provides the interfaces.

How to use it:

1. Prepare an algorithm for trading signals;  
2. Create your own trading signal class, inherited from CExpertSignal class;  
3. Override the virtual methods in your class with your own algorithms.

You can find an examples of trading signal classes in the Expert\Signal\ folder.

### Description

CExpertSignal is a base class for implementation of trading signal algorithms.

### Declaration

```cpp
   class CExpertSignal : public CExpertBase
```

### Title

```cpp
   #include <Expert\ExpertSignal.mqh>
```

|  |
| --- |
| Inheritance hierarchy    [CObject](../../../Basic-Class-CObject/Basic-Class-CObject.md)        [CExpertBase](../CExpertBase/CExpertBase.md)            CExpertSignal  Direct descendants  CSignalAC, CSignalAMA, CSignalAO, CSignalBearsPower, CSignalBullsPower, CSignalCCI, CSignalDeM, CSignalDEMA, CSignalEnvelopes, CSignalFrAMA, CSignalRSI, CSignalRVI, CSignalSAR, CSignalStoch, CSignalTEMA, CSignalTriX, CSignalWPR |

### Class Methods by Groups

| Initialization |  |
| --- | --- |
| virtual [InitIndicators](InitIndicators/InitIndicators.md) | Initializes indicators and timeseries |
| virtual [ValidationSettings](ValidationSettings/ValidationSettings.md) | Checks the object settings |
| virtual [AddFilter](AddFilter/AddFilter.md) | Adds a filter to combined signal |
| Access to Protected Data |  |
| [BasePrice](BasePrice/BasePrice.md) | Sets base price level |
| [UsedSeries](UsedSeries/UsedSeries.md) | Gets the flags of timeseries used |
| Parameters Setting |  |
| [Weight](Weight/Weight.md) | Sets the value of "Weight" parameter |
| [PatternsUsage](PatternsUsage/PatternsUsage.md) | Sets the value of "PatternsUsage" parameter |
| [General](General/General.md) | Sets the value of "General" parameter |
| [Ignore](Ignore/Ignore.md) | Sets the value of "Ignore" parameter |
| [Invert](Invert/Invert.md) | Sets the value of "Invert" parameter |
| [ThresholdOpen](ThresholdOpen/ThresholdOpen.md) | Sets the value of "ThresholdOpen" parameter |
| [ThresholdClose](ThresholdClose/ThresholdClose.md) | Sets the value of "ThresholdClose" parameter |
| [PriceLevel](PriceLevel/PriceLevel.md) | Sets the value of "PriceLevel" parameter |
| [StopLevel](StopLevel/StopLevel.md) | Sets the value of "StopLevel" parameter |
| [TakeLevel](TakeLevel/TakeLevel.md) | Sets the value of "TakeLevel" parameter |
| [Expiration](Expiration/Expiration.md) | Sets the value of "Expiration" parameter |
| [Magic](Magic/Magic.md) | Sets the value of "Magic" parameter |
| Checking Trading Conditions |  |
| virtual [CheckOpenLong](CheckOpenLong/CheckOpenLong.md) | Checks conditions to open long position |
| virtual [CheckCloseLong](CheckCloseLong/CheckCloseLong.md) | Checks conditions to close long position |
| virtual [CheckOpenShort](CheckOpenShort/CheckOpenShort.md) | Checks conditions to open short position |
| virtual [CheckCloseShort](CheckCloseShort/CheckCloseShort.md) | Checks conditions to close short position |
| virtual [CheckReverseLong](CheckReverseLong/CheckReverseLong.md) | Checks conditions of long position reversal |
| virtual [CheckReverseShort](CheckReverseShort/CheckReverseShort.md) | Checks conditions of short position reversal |
| Trade Parameters Setting |  |
| virtual [OpenLongParams](OpenLongParams/OpenLongParams.md) | Sets parameters for long position opening |
| virtual [OpenShortParams](OpenShortParams/OpenShortParams.md) | Sets parameters for short position opening |
| virtual [CloseLongParams](CloseLongParams/CloseLongParams.md) | Sets parameters for long position closing |
| virtual [CloseShortParams](CloseShortParams/CloseShortParams.md) | Sets parameters for short position closing |
| Checking of Order Trailing Conditions |  |
| virtual [CheckTrailingOrderLong](CheckTrailingOrderLong/CheckTrailingOrderLong.md) | Checks conditions to modify parameters of Buy Pending order |
| virtual [CheckTrailingOrderShort](CheckTrailingOrderShort/CheckTrailingOrderShort.md) | Checks conditions to modify parameters of Sell Pending order |
| Methods to Check Formation of Market Orders |  |
| virtual [LongCondition](LongCondition/LongCondition.md) | Gets the result of checking buy conditions |
| virtual [ShortCondition](ShortCondition/ShortCondition.md) | Gets the result of checking sell conditions |
| virtual [Direction](Direction/Direction.md) | Gets the "weighted" direction of price |

| Methods inherited from class CObject  Prev, Prev, Next, Next, [Save](../../../Basic-Class-CObject/Save/Save.md), [Load](../../../Basic-Class-CObject/Load/Load.md), [Type](../../../Basic-Class-CObject/Type/Type.md), [Compare](../../../Basic-Class-CObject/Compare/Compare.md) |
| --- |
| Methods inherited from class CExpertBase  [InitPhase](../CExpertBase/InitPhase/InitPhase.md), [TrendType](../CExpertBase/TrendType/TrendType.md), [UsedSeries](../CExpertBase/UsedSeries/UsedSeries.md), [EveryTick](../CExpertBase/EveryTick/EveryTick.md), [Open](../CExpertBase/Open/Open.md), [High](../CExpertBase/High/High.md), [Low](../CExpertBase/Low/Low.md), [Close](../CExpertBase/Close/Close.md), [Spread](../CExpertBase/Spread/Spread.md), [Time](../CExpertBase/Time/Time.md), [TickVolume](../CExpertBase/TickVolume/TickVolume.md), [RealVolume](../CExpertBase/RealVolume/RealVolume.md), [Init](../CExpertBase/Init/Init.md), [Symbol](../CExpertBase/Symbol/Symbol.md), [Period](../CExpertBase/Period/Period.md), [Magic](../CExpertBase/Magic/Magic.md), SetMarginMode, [SetPriceSeries](../CExpertBase/SetPriceSeries/SetPriceSeries.md), [SetOtherSeries](../CExpertBase/SetOtherSeries/SetOtherSeries.md) |