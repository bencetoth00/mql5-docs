# CiStdDev

CiStdDev

CiStdDev is a class intended for using the Standard Deviation technical indicator.

Description

CiStdDev class provides the creation, setup, and access to the data of the Standard Deviation indicator.

Declaration

|  |
| --- |
| class CiStdDev: public CIndicator |

Title

|  |
| --- |
| #include <Indicators\Trend.mqh> |

|  |
| --- |
| Inheritance hierarchy    [CObject](../../../Basic-Class-CObject/Basic-Class-CObject.md)        [CArray](../../../Data-Collections/CArray/CArray.md)            [CArrayObj](../../../Data-Collections/CArrayObj/CArrayObj.md)                [CSeries](../../Base-classes/CSeries/CSeries.md)                    [CIndicator](../../Base-classes/CIndicator/CIndicator.md)                        CiStdDev |

Class Methods by Groups

| Attributes |  |
| --- | --- |
| [MaPeriod](MaPeriod/MaPeriod.md) | Returns the averaging period |
| [MaShift](MaShift/MaShift.md) | Returns the horizontal shift |
| [MaMethod](MaMethod/MaMethod.md) | Returns the averaging method |
| [Applied](Applied/Applied.md) | Returns the price type or handle to apply |
| Create |  |
| [Create](Create/Create.md) | Creates the indicator |
| Data Access |  |
| [Main](Main/Main.md) | Returns the buffer data |
| Input/output |  |
| virtual [Type](Type/Type.md) | Virtual identification method |

| Methods inherited from class CObject  Prev, Prev, Next, Next, [Compare](../../../Basic-Class-CObject/Compare/Compare.md) |
| --- |
| Methods inherited from class CArray  [Step](../../../Data-Collections/CArray/Step/Step.md), [Step](../../../Data-Collections/CArray/Step/Step.md), [Total](../../../Data-Collections/CArray/Total/Total.md), [Available](../../../Data-Collections/CArray/Available/Available.md), [Max](../../../Data-Collections/CArray/Max/Max.md), [IsSorted](../../../Data-Collections/CArray/IsSorted/IsSorted.md), [SortMode](../../../Data-Collections/CArray/SortMode/SortMode.md), [Clear](../../../Data-Collections/CArray/Clear/Clear.md), [Sort](../../../Data-Collections/CArray/Sort/Sort.md) |
| Methods inherited from class CArrayObj  [FreeMode](../../../Data-Collections/CArrayObj/FreeMode/FreeMode.md), [FreeMode](../../../Data-Collections/CArrayObj/FreeMode/FreeMode.md), [Save](../../../Data-Collections/CArrayObj/Save/Save.md), [Load](../../../Data-Collections/CArrayObj/Load/Load.md), [CreateElement](../../../Data-Collections/CArrayObj/CreateElement/CreateElement.md), [Reserve](../../../Data-Collections/CArrayObj/Reserve/Reserve.md), [Resize](../../../Data-Collections/CArrayObj/Resize/Resize.md), [Shutdown](../../../Data-Collections/CArrayObj/Shutdown/Shutdown.md), [Add](../../../Data-Collections/CArrayObj/Add/Add.md), [AddArray](../../../Data-Collections/CArrayObj/AddArray/AddArray.md), [Insert](../../../Data-Collections/CArrayObj/Insert/Insert.md), [InsertArray](../../../Data-Collections/CArrayObj/InsertArray/InsertArray.md), [AssignArray](../../../Data-Collections/CArrayObj/AssignArray/AssignArray.md), [At](../../../Data-Collections/CArrayObj/At/At.md), [Update](../../../Data-Collections/CArrayObj/Update/Update.md), [Shift](../../../Data-Collections/CArrayObj/Shift/Shift.md), [Detach](../../../Data-Collections/CArrayObj/Detach/Detach.md), [Delete](../../../Data-Collections/CArrayObj/Delete/Delete.md), [DeleteRange](../../../Data-Collections/CArrayObj/DeleteRange/DeleteRange.md), [Clear](../../../Data-Collections/CArrayObj/Clear/Clear.md), [CompareArray](../../../Data-Collections/CArrayObj/CompareArray/CompareArray.md), [InsertSort](../../../Data-Collections/CArrayObj/InsertSort/InsertSort.md), [Search](../../../Data-Collections/CArrayObj/Search/Search.md), [SearchGreat](../../../Data-Collections/CArrayObj/SearchGreat/SearchGreat.md), [SearchLess](../../../Data-Collections/CArrayObj/SearchLess/SearchLess.md), [SearchGreatOrEqual](../../../Data-Collections/CArrayObj/SearchGreatOrEqual/SearchGreatOrEqual.md), [SearchLessOrEqual](../../../Data-Collections/CArrayObj/SearchLessOrEqual/SearchLessOrEqual.md), [SearchFirst](../../../Data-Collections/CArrayObj/SearchFirst/SearchFirst.md), [SearchLast](../../../Data-Collections/CArrayObj/SearchLast/SearchLast.md) |
| Methods inherited from class CSeries  [Name](../../Base-classes/CSeries/Name/Name.md), [BuffersTotal](../../Base-classes/CSeries/BuffersTotal/BuffersTotal.md), [BufferSize](../../Base-classes/CSeries/BufferSize/BufferSize.md), [Timeframe](../../Base-classes/CSeries/Timeframe/Timeframe.md), [Symbol](../../Base-classes/CSeries/Symbol/Symbol.md), [Period](../../Base-classes/CSeries/Period/Period.md), [PeriodDescription](../../Base-classes/CSeries/PeriodDescription/PeriodDescription.md), [RefreshCurrent](../../Base-classes/CSeries/RefreshCurrent/RefreshCurrent.md) |
| Methods inherited from class CIndicator  [Handle](../../Base-classes/CIndicator/Handle/Handle.md), [Status](../../Base-classes/CIndicator/Status/Status.md), [FullRelease](../../Base-classes/CIndicator/FullRelease/FullRelease.md), Redrawer, [Create](../../Base-classes/CIndicator/Create/Create.md), [BufferResize](../../Base-classes/CIndicator/BufferResize/BufferResize.md), [BarsCalculated](../../Base-classes/CIndicator/BarsCalculated/BarsCalculated.md), [GetData](../../Base-classes/CIndicator/GetData/GetData.md), [GetData](../../Base-classes/CIndicator/GetData/GetData.md), [GetData](../../Base-classes/CIndicator/GetData/GetData.md), [GetData](../../Base-classes/CIndicator/GetData/GetData.md), [Minimum](../../Base-classes/CIndicator/Minimum/Minimum.md), [MinValue](../../Base-classes/CIndicator/MinValue/MinValue.md), [Maximum](../../Base-classes/CIndicator/Maximum/Maximum.md), [MaxValue](../../Base-classes/CIndicator/MaxValue/MaxValue.md), [Refresh](../../Base-classes/CIndicator/Refresh/Refresh.md), [AddToChart](../../Base-classes/CIndicator/AddToChart/AddToChart.md), [DeleteFromChart](../../Base-classes/CIndicator/DeleteFromChart/DeleteFromChart.md), [MethodDescription](../../Base-classes/CIndicator/MethodDescription/MethodDescription.md), [PriceDescription](../../Base-classes/CIndicator/PriceDescription/PriceDescription.md), [VolumeDescription](../../Base-classes/CIndicator/VolumeDescription/VolumeDescription.md) |
