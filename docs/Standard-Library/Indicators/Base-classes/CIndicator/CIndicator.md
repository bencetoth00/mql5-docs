# CIndicator

CIndicator

CIndicator is a base class for technical indicator classes of the MQL5 standard library.

Description

The CIndicator class provides the simplified access for all of its descendants to general MQL5 API technical indicator functions.

Declaration

|  |
| --- |
| class CIndicator: public CSeries |

Title

|  |
| --- |
| #include <Indicators\Indicator.mqh> |

|  |
| --- |
| Inheritance hierarchy    [CObject](../../../Basic-Class-CObject/Basic-Class-CObject.md)        [CArray](../../../Data-Collections/CArray/CArray.md)            [CArrayObj](../../../Data-Collections/CArrayObj/CArrayObj.md)                [CSeries](../CSeries/CSeries.md)                    CIndicator  Direct descendants  [CiAC](../../Bill-Williams-Indicators/CiAC/CiAC.md), [CiAD](../../Volume-Indicators/CiAD/CiAD.md), [CiADX](../../Trend-Indicators/CiADX/CiADX.md), [CiADXWilder](../../Trend-Indicators/CiADXWilder/CiADXWilder.md), [CiAlligator](../../Bill-Williams-Indicators/CiAlligator/CiAlligator.md), [CiAMA](../../Trend-Indicators/CiAMA/CiAMA.md), [CiAO](../../Bill-Williams-Indicators/CiAO/CiAO.md), [CiATR](../../Oscillators/CiATR/CiATR.md), [CiBands](../../Trend-Indicators/CiBands/CiBands.md), [CiBearsPower](../../Oscillators/CiBearsPower/CiBearsPower.md), [CiBullsPower](../../Oscillators/CiBullsPower/CiBullsPower.md), [CiBWMFI](../../Bill-Williams-Indicators/CiBWMFI/CiBWMFI.md), [CiCCI](../../Oscillators/CiCCI/CiCCI.md), [CiChaikin](../../Oscillators/CiChaikin/CiChaikin.md), CiCustom, [CiDEMA](../../Trend-Indicators/CiDEMA/CiDEMA.md), [CiDeMarker](../../Oscillators/CiDeMarker/CiDeMarker.md), [CiEnvelopes](../../Trend-Indicators/CiEnvelopes/CiEnvelopes.md), [CiForce](../../Oscillators/CiForce/CiForce.md), [CiFractals](../../Bill-Williams-Indicators/CiFractals/CiFractals.md), [CiFrAMA](../../Trend-Indicators/CiFrAMA/CiFrAMA.md), [CiGator](../../Bill-Williams-Indicators/CiGator/CiGator.md), [CiIchimoku](../../Trend-Indicators/CiIchimoku/CiIchimoku.md), [CiMA](../../Trend-Indicators/CiMA/CiMA.md), [CiMACD](../../Oscillators/CiMACD/CiMACD.md), [CiMFI](../../Volume-Indicators/CiMFI/CiMFI.md), [CiMomentum](../../Oscillators/CiMomentum/CiMomentum.md), [CiOBV](../../Volume-Indicators/CiOBV/CiOBV.md), [CiOsMA](../../Oscillators/CiOsMA/CiOsMA.md), [CiRSI](../../Oscillators/CiRSI/CiRSI.md), [CiRVI](../../Oscillators/CiRVI/CiRVI.md), [CiSAR](../../Trend-Indicators/CiSAR/CiSAR.md), [CiStdDev](../../Trend-Indicators/CiStdDev/CiStdDev.md), [CiStochastic](../../Oscillators/CiStochastic/CiStochastic.md), [CiTEMA](../../Trend-Indicators/CiTEMA/CiTEMA.md), [CiTriX](../../Oscillators/CiTriX/CiTriX.md), [CiVIDyA](../../Trend-Indicators/CiVIDyA/CiVIDyA.md), [CiVolumes](../../Volume-Indicators/CiVolumes/CiVolumes.md), [CiWPR](../../Oscillators/CiWPR/CiWPR.md) |

Class Methods by Groups

| Attributes |  |
| --- | --- |
| [Handle](Handle/Handle.md) | Gets the indicator's handle. |
| [Status](Status/Status.md) | Gets the status of the indicator. |
| [FullRelease](FullRelease/FullRelease.md) | Sets a flag to release the handle. |
| Creation |  |
| [Create](Create/Create.md) | Creates the indicator |
| [BufferResize](BufferResize/BufferResize.md) | Sets the new buffer sizes |
| Data Access |  |
| [GetData](GetData/GetData.md) | Copies the data from the indicator buffer |
| Data Update Methods |  |
| [Refresh](Refresh/Refresh.md) | Updates the indicator data |
| Finding Min/Max Values |  |
| [Minimum](Minimum/Minimum.md) | Gets the index of minimal value in a specified range. |
| [MinValue](MinValue/MinValue.md) | Gets the minimal value in a specified range. |
| [Maximum](Maximum/Maximum.md) | Gets the index of maximal value in a specified range. |
| [MaxValue](MaxValue/MaxValue.md) | Gets the maximal value in a specified range. |
| Conversion of Enumerations |  |
| [MethodDescription](MethodDescription/MethodDescription.md) | Converts [ENUM\_MA\_METHOD](../../../../Constants,-Enumerations-and-Structures/Indicator-Constants/Smoothing-Methods/Smoothing-Methods.md) into a string |
| [PriceDescription](PriceDescription/PriceDescription.md) | Converts [ENUM\_APPLIED\_PRICE](../../../../Constants,-Enumerations-and-Structures/Indicator-Constants/Price-Constants/Price-Constants.md#enum_applied_price_enum) into a string |
| [VolumeDescription](VolumeDescription/VolumeDescription.md) | Converts [ENUM\_APPLIED\_VOLUME](../../../../Constants,-Enumerations-and-Structures/Indicator-Constants/Price-Constants/Price-Constants.md#enum_applied_price_enum) into a string |
| Working with chart |  |
| [AddToChart](AddToChart/AddToChart.md) | Adds an indicator to the chart |
| [DeleteFromChart](DeleteFromChart/DeleteFromChart.md) | Deletes an indicator from the chart |

| Methods inherited from class CObject  Prev, Prev, Next, Next, [Compare](../../../Basic-Class-CObject/Compare/Compare.md) |
| --- |
| Methods inherited from class CArray  [Step](../../../Data-Collections/CArray/Step/Step.md), [Step](../../../Data-Collections/CArray/Step/Step.md), [Total](../../../Data-Collections/CArray/Total/Total.md), [Available](../../../Data-Collections/CArray/Available/Available.md), [Max](../../../Data-Collections/CArray/Max/Max.md), [IsSorted](../../../Data-Collections/CArray/IsSorted/IsSorted.md), [SortMode](../../../Data-Collections/CArray/SortMode/SortMode.md), [Clear](../../../Data-Collections/CArray/Clear/Clear.md), [Sort](../../../Data-Collections/CArray/Sort/Sort.md) |
| Methods inherited from class CArrayObj  [FreeMode](../../../Data-Collections/CArrayObj/FreeMode/FreeMode.md), [FreeMode](../../../Data-Collections/CArrayObj/FreeMode/FreeMode.md), [Type](../../../Data-Collections/CArrayObj/Type/Type.md), [Save](../../../Data-Collections/CArrayObj/Save/Save.md), [Load](../../../Data-Collections/CArrayObj/Load/Load.md), [CreateElement](../../../Data-Collections/CArrayObj/CreateElement/CreateElement.md), [Reserve](../../../Data-Collections/CArrayObj/Reserve/Reserve.md), [Resize](../../../Data-Collections/CArrayObj/Resize/Resize.md), [Shutdown](../../../Data-Collections/CArrayObj/Shutdown/Shutdown.md), [Add](../../../Data-Collections/CArrayObj/Add/Add.md), [AddArray](../../../Data-Collections/CArrayObj/AddArray/AddArray.md), [Insert](../../../Data-Collections/CArrayObj/Insert/Insert.md), [InsertArray](../../../Data-Collections/CArrayObj/InsertArray/InsertArray.md), [AssignArray](../../../Data-Collections/CArrayObj/AssignArray/AssignArray.md), [At](../../../Data-Collections/CArrayObj/At/At.md), [Update](../../../Data-Collections/CArrayObj/Update/Update.md), [Shift](../../../Data-Collections/CArrayObj/Shift/Shift.md), [Detach](../../../Data-Collections/CArrayObj/Detach/Detach.md), [Delete](../../../Data-Collections/CArrayObj/Delete/Delete.md), [DeleteRange](../../../Data-Collections/CArrayObj/DeleteRange/DeleteRange.md), [Clear](../../../Data-Collections/CArrayObj/Clear/Clear.md), [CompareArray](../../../Data-Collections/CArrayObj/CompareArray/CompareArray.md), [InsertSort](../../../Data-Collections/CArrayObj/InsertSort/InsertSort.md), [Search](../../../Data-Collections/CArrayObj/Search/Search.md), [SearchGreat](../../../Data-Collections/CArrayObj/SearchGreat/SearchGreat.md), [SearchLess](../../../Data-Collections/CArrayObj/SearchLess/SearchLess.md), [SearchGreatOrEqual](../../../Data-Collections/CArrayObj/SearchGreatOrEqual/SearchGreatOrEqual.md), [SearchLessOrEqual](../../../Data-Collections/CArrayObj/SearchLessOrEqual/SearchLessOrEqual.md), [SearchFirst](../../../Data-Collections/CArrayObj/SearchFirst/SearchFirst.md), [SearchLast](../../../Data-Collections/CArrayObj/SearchLast/SearchLast.md) |
| Methods inherited from class CSeries  [Name](../CSeries/Name/Name.md), [BuffersTotal](../CSeries/BuffersTotal/BuffersTotal.md), [BufferSize](../CSeries/BufferSize/BufferSize.md), [Timeframe](../CSeries/Timeframe/Timeframe.md), [Symbol](../CSeries/Symbol/Symbol.md), [Period](../CSeries/Period/Period.md), [PeriodDescription](../CSeries/PeriodDescription/PeriodDescription.md), [RefreshCurrent](../CSeries/RefreshCurrent/RefreshCurrent.md) |
