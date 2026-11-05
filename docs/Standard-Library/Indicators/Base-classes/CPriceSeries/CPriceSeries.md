# CPriceSeries

CPriceSeries

CPriceSeries is a base class for access to the price data.

Description

CSeries class provides the simplified access to MQL5 API general functions for working with price data to all its descendants.

Declaration

|  |
| --- |
| class CPriceSeries: public CSeries |

Title

|  |
| --- |
| #include <Indicators\TimeSeries.mqh> |

|  |
| --- |
| Inheritance hierarchy    [CObject](../../../Basic-Class-CObject/Basic-Class-CObject.md)        [CArray](../../../Data-Collections/CArray/CArray.md)            [CArrayObj](../../../Data-Collections/CArrayObj/CArrayObj.md)                [CSeries](../CSeries/CSeries.md)                    CPriceSeries  Direct descendants  [CiClose](../../Timeseries-classes/CiClose/CiClose.md), [CiHigh](../../Timeseries-classes/CiHigh/CiHigh.md), [CiLow](../../Timeseries-classes/CiLow/CiLow.md), [CiOpen](../../Timeseries-classes/CiOpen/CiOpen.md) |

Class Methods by Groups

| Create |  |
| --- | --- |
| virtual [BufferResize](BufferResize/BufferResize.md) | Sets size of the series buffer |
| Data Access |  |
| virtual [GetData](GetData/GetData.md) | Gets the specified series buffer element |
| Data Update |  |
| virtual [Refresh](Refresh/Refresh.md) | Updates timeseries data |
| Search for Extreme Values |  |
| virtual [MinIndex](MinIndex/MinIndex.md) | Gets the index of minimal value in the specified range |
| virtual [MinValue](MinValue/MinValue.md) | Gets the minimal value in the specified range |
| virtual [MaxIndex](MaxIndex/MaxIndex.md) | Gets the index of maximal value in the specified range |
| virtual [MaxValue](MaxValue/MaxValue.md) | Gets the maximal value in the specified range |

| Methods inherited from class CObject  Prev, Prev, Next, Next, [Compare](../../../Basic-Class-CObject/Compare/Compare.md) |
| --- |
| Methods inherited from class CArray  [Step](../../../Data-Collections/CArray/Step/Step.md), [Step](../../../Data-Collections/CArray/Step/Step.md), [Total](../../../Data-Collections/CArray/Total/Total.md), [Available](../../../Data-Collections/CArray/Available/Available.md), [Max](../../../Data-Collections/CArray/Max/Max.md), [IsSorted](../../../Data-Collections/CArray/IsSorted/IsSorted.md), [SortMode](../../../Data-Collections/CArray/SortMode/SortMode.md), [Clear](../../../Data-Collections/CArray/Clear/Clear.md), [Sort](../../../Data-Collections/CArray/Sort/Sort.md) |
| Methods inherited from class CArrayObj  [FreeMode](../../../Data-Collections/CArrayObj/FreeMode/FreeMode.md), [FreeMode](../../../Data-Collections/CArrayObj/FreeMode/FreeMode.md), [Type](../../../Data-Collections/CArrayObj/Type/Type.md), [Save](../../../Data-Collections/CArrayObj/Save/Save.md), [Load](../../../Data-Collections/CArrayObj/Load/Load.md), [CreateElement](../../../Data-Collections/CArrayObj/CreateElement/CreateElement.md), [Reserve](../../../Data-Collections/CArrayObj/Reserve/Reserve.md), [Resize](../../../Data-Collections/CArrayObj/Resize/Resize.md), [Shutdown](../../../Data-Collections/CArrayObj/Shutdown/Shutdown.md), [Add](../../../Data-Collections/CArrayObj/Add/Add.md), [AddArray](../../../Data-Collections/CArrayObj/AddArray/AddArray.md), [Insert](../../../Data-Collections/CArrayObj/Insert/Insert.md), [InsertArray](../../../Data-Collections/CArrayObj/InsertArray/InsertArray.md), [AssignArray](../../../Data-Collections/CArrayObj/AssignArray/AssignArray.md), [At](../../../Data-Collections/CArrayObj/At/At.md), [Update](../../../Data-Collections/CArrayObj/Update/Update.md), [Shift](../../../Data-Collections/CArrayObj/Shift/Shift.md), [Detach](../../../Data-Collections/CArrayObj/Detach/Detach.md), [Delete](../../../Data-Collections/CArrayObj/Delete/Delete.md), [DeleteRange](../../../Data-Collections/CArrayObj/DeleteRange/DeleteRange.md), [Clear](../../../Data-Collections/CArrayObj/Clear/Clear.md), [CompareArray](../../../Data-Collections/CArrayObj/CompareArray/CompareArray.md), [InsertSort](../../../Data-Collections/CArrayObj/InsertSort/InsertSort.md), [Search](../../../Data-Collections/CArrayObj/Search/Search.md), [SearchGreat](../../../Data-Collections/CArrayObj/SearchGreat/SearchGreat.md), [SearchLess](../../../Data-Collections/CArrayObj/SearchLess/SearchLess.md), [SearchGreatOrEqual](../../../Data-Collections/CArrayObj/SearchGreatOrEqual/SearchGreatOrEqual.md), [SearchLessOrEqual](../../../Data-Collections/CArrayObj/SearchLessOrEqual/SearchLessOrEqual.md), [SearchFirst](../../../Data-Collections/CArrayObj/SearchFirst/SearchFirst.md), [SearchLast](../../../Data-Collections/CArrayObj/SearchLast/SearchLast.md) |
| Methods inherited from class CSeries  [Name](../CSeries/Name/Name.md), [BuffersTotal](../CSeries/BuffersTotal/BuffersTotal.md), [BufferSize](../CSeries/BufferSize/BufferSize.md), [Timeframe](../CSeries/Timeframe/Timeframe.md), [Symbol](../CSeries/Symbol/Symbol.md), [Period](../CSeries/Period/Period.md), [PeriodDescription](../CSeries/PeriodDescription/PeriodDescription.md), [RefreshCurrent](../CSeries/RefreshCurrent/RefreshCurrent.md) |
