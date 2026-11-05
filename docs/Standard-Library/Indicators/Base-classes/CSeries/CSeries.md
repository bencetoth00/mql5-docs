# CSeries

CSeries

CSeries is a base class for an access to the timeseries data of the Standard Library.

Description

CSeries class provides the simplified access to all the MQL5 API general functions related to working with the series data for all its descendants (timeseries and indicator classes).

Declaration

|  |
| --- |
| class CSeries: public CArrayObj |

Title

|  |
| --- |
| #include <Indicators\Series.mqh> |

|  |
| --- |
| Inheritance hierarchy    [CObject](../../../Basic-Class-CObject/Basic-Class-CObject.md)        [CArray](../../../Data-Collections/CArray/CArray.md)            [CArrayObj](../../../Data-Collections/CArrayObj/CArrayObj.md)                CSeries  Direct descendants  [CIndicator](../CIndicator/CIndicator.md), [CiRealVolume](../../Timeseries-classes/CiRealVolume/CiRealVolume.md), [CiSpread](../../Timeseries-classes/CiSpread/CiSpread.md), [CiTickVolume](../../Timeseries-classes/CiTickVolume/CiTickVolume.md), [CiTime](../../Timeseries-classes/CiTime/CiTime.md), [CPriceSeries](../CPriceSeries/CPriceSeries.md) |

Class Methods by Groups

| Attributes |  |
| --- | --- |
| [Name](Name/Name.md) | Gets the name of timeseries or indicator |
| [BuffersTotal](BuffersTotal/BuffersTotal.md) | Gets the number of buffers of timeseries or indicator |
| [Timeframe](Timeframe/Timeframe.md) | Gets the timeframe flag of timeseries or indicator |
| [Symbol](Symbol/Symbol.md) | Gets the symbol of timeseries or indicator |
| [Period](Period/Period.md) | Gets the period of timeseries or indicator |
| [RefreshCurrent](RefreshCurrent/RefreshCurrent.md) | Sets/resets the flag of updating the current data |
| Data Access |  |
| virtual [BufferResize](BufferResize/BufferResize.md) | Sets buffer size of timeseries or indicator |
| Data Update |  |
| virtual [Refresh](Refresh/Refresh.md) | Update the data of timeseries or indicator |
| [PeriodDescription](PeriodDescription/PeriodDescription.md) | Transforms [ENUM\_TIMEFRAMES](../../../../Constants,-Enumerations-and-Structures/Chart-Constants/Chart-Timeframes/Chart-Timeframes.md) into a string |

| Methods inherited from class CObject  Prev, Prev, Next, Next, [Compare](../../../Basic-Class-CObject/Compare/Compare.md) |
| --- |
| Methods inherited from class CArray  [Step](../../../Data-Collections/CArray/Step/Step.md), [Step](../../../Data-Collections/CArray/Step/Step.md), [Total](../../../Data-Collections/CArray/Total/Total.md), [Available](../../../Data-Collections/CArray/Available/Available.md), [Max](../../../Data-Collections/CArray/Max/Max.md), [IsSorted](../../../Data-Collections/CArray/IsSorted/IsSorted.md), [SortMode](../../../Data-Collections/CArray/SortMode/SortMode.md), [Clear](../../../Data-Collections/CArray/Clear/Clear.md), [Sort](../../../Data-Collections/CArray/Sort/Sort.md) |
| Methods inherited from class CArrayObj  [FreeMode](../../../Data-Collections/CArrayObj/FreeMode/FreeMode.md), [FreeMode](../../../Data-Collections/CArrayObj/FreeMode/FreeMode.md), [Type](../../../Data-Collections/CArrayObj/Type/Type.md), [Save](../../../Data-Collections/CArrayObj/Save/Save.md), [Load](../../../Data-Collections/CArrayObj/Load/Load.md), [CreateElement](../../../Data-Collections/CArrayObj/CreateElement/CreateElement.md), [Reserve](../../../Data-Collections/CArrayObj/Reserve/Reserve.md), [Resize](../../../Data-Collections/CArrayObj/Resize/Resize.md), [Shutdown](../../../Data-Collections/CArrayObj/Shutdown/Shutdown.md), [Add](../../../Data-Collections/CArrayObj/Add/Add.md), [AddArray](../../../Data-Collections/CArrayObj/AddArray/AddArray.md), [Insert](../../../Data-Collections/CArrayObj/Insert/Insert.md), [InsertArray](../../../Data-Collections/CArrayObj/InsertArray/InsertArray.md), [AssignArray](../../../Data-Collections/CArrayObj/AssignArray/AssignArray.md), [At](../../../Data-Collections/CArrayObj/At/At.md), [Update](../../../Data-Collections/CArrayObj/Update/Update.md), [Shift](../../../Data-Collections/CArrayObj/Shift/Shift.md), [Detach](../../../Data-Collections/CArrayObj/Detach/Detach.md), [Delete](../../../Data-Collections/CArrayObj/Delete/Delete.md), [DeleteRange](../../../Data-Collections/CArrayObj/DeleteRange/DeleteRange.md), [Clear](../../../Data-Collections/CArrayObj/Clear/Clear.md), [CompareArray](../../../Data-Collections/CArrayObj/CompareArray/CompareArray.md), [InsertSort](../../../Data-Collections/CArrayObj/InsertSort/InsertSort.md), [Search](../../../Data-Collections/CArrayObj/Search/Search.md), [SearchGreat](../../../Data-Collections/CArrayObj/SearchGreat/SearchGreat.md), [SearchLess](../../../Data-Collections/CArrayObj/SearchLess/SearchLess.md), [SearchGreatOrEqual](../../../Data-Collections/CArrayObj/SearchGreatOrEqual/SearchGreatOrEqual.md), [SearchLessOrEqual](../../../Data-Collections/CArrayObj/SearchLessOrEqual/SearchLessOrEqual.md), [SearchFirst](../../../Data-Collections/CArrayObj/SearchFirst/SearchFirst.md), [SearchLast](../../../Data-Collections/CArrayObj/SearchLast/SearchLast.md) |
