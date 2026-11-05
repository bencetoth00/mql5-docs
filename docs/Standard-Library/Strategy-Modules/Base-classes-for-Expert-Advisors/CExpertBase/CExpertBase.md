# CExpertBase

CExpertBase

CExpertBase is a base class for the [CExpert](../CExpert/CExpert.md) class and all auxiliary trading strategy classes.

Description

CExpertBase provides the data and methods, which are common to all objects of the Expert Advisor.

Declaration

|  |
| --- |
| class CExpertBase : public CObject |

Title

|  |
| --- |
| #include <Expert\ExpertBase.mqh> |

|  |
| --- |
| Inheritance hierarchy    [CObject](../../../Basic-Class-CObject/Basic-Class-CObject.md)        CExpertBase  Direct descendants  [CExpert](../CExpert/CExpert.md), [CExpertMoney](../CExpertMoney/CExpertMoney.md), [CExpertSignal](../CExpertSignal/CExpertSignal.md), [CExpertTrailing](../CExpertTrailing/CExpertTrailing.md) |

Class Methods by Groups

Public Methods:

| Initialization |  |
| --- | --- |
| virtual [Init](Init/Init.md) | Initializes the object |
| virtual [ValidationSettings](ValidationSettings/ValidationSettings.md) | Checks the settings |
| Parameters |  |
| [Symbol](Symbol/Symbol.md) | Sets the symbol |
| [Period](Period/Period.md) | Sets the timeframe |
| [Magic](Magic/Magic.md) | Sets the Expert Advisor ID |
| Indicators and Timeseries |  |
| virtual [SetPriceSeries](SetPriceSeries/SetPriceSeries.md) | Sets pointers to external timeseries (price series) |
| virtual [SetOtherSeries](SetOtherSeries/SetOtherSeries.md) | Sets pointers to external timeseries (non-price series) |
| virtual [InitIndicators](InitIndicators/InitIndicators.md) | Initializes the indicators and timeseries |
| Access to Protected Data |  |
| [InitPhase](InitPhase/InitPhase.md) | Gets the current phase of object initialization |
| [TrendType](TrendType/TrendType.md) | Sets trend type |
| [UsedSeries](UsedSeries/UsedSeries.md) | Gets bitmask of timeseries used |
| [EveryTick](EveryTick/EveryTick.md) | Sets the "Every tick" flag |
| Access to Timeseries |  |
| [Open](Open/Open.md) | Gets the element of the Open timeseries by index |
| [High](High/High.md) | Gets the element of the High timeseries by index |
| [Low](Low/Low.md) | Gets the element of the Low timeseries by index |
| [Close](Close/Close.md) | Gets the element of the Close timeseries by index |
| [Spread](Spread/Spread.md) | Gets the element of the Spread timeseries by index |
| [Time](Time/Time.md) | Gets the element of the Time timeseries by index |
| [TickVolume](TickVolume/TickVolume.md) | Gets the element of the TickVolume timeseries by index |
| [RealVolume](RealVolume/RealVolume.md) | Gets the element of the RealVolume timeseries by index |

Protected Methods:

| Initialization of Timeseries |  |
| --- | --- |
| [InitOpen](InitOpen/InitOpen.md) | Open timeseries initialization method |
| [InitHigh](InitHigh/InitHigh.md) | High timeseries initialization method |
| [InitLow](InitLow/InitLow.md) | Low timeseries initialization method |
| [InitClose](InitClose/InitClose.md) | Close timeseries initialization method |
| [InitSpread](InitSpread/InitSpread.md) | Spread timeseries initialization method |
| [InitTime](InitTime/InitTime.md) | Time timeseries initialization method |
| [InitTickVolume](InitTickVolume/InitTickVolume.md) | TickVolume timeseries initialization method |
| [InitRealVolume](InitRealVolume/InitRealVolume.md) | RealVolume timeseries initialization method |
| Service Methods |  |
| virtual [PriceLevelUnit](PriceLevelUnit/PriceLevelUnit.md) | Gets the price level unit |
| virtual [StartIndex](StartIndex/StartIndex.md) | Gets the index of starting bar to analyze |
| virtual [CompareMagic](CompareMagic/CompareMagic.md) | Compares the Expert Advisor ID with the specified value |

|  |
| --- |
| Methods inherited from class CObject  Prev, Prev, Next, Next, [Save](../../../Basic-Class-CObject/Save/Save.md), [Load](../../../Basic-Class-CObject/Load/Load.md), [Type](../../../Basic-Class-CObject/Type/Type.md), [Compare](../../../Basic-Class-CObject/Compare/Compare.md) |
