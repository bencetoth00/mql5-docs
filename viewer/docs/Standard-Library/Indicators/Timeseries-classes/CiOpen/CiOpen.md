# CiOpen


CiOpen is a class designed for access to open prices of the bars in the history.

### Description

CiOpen class provides an access to open prices of the bars in the history.

### Declaration

```cpp
   class CiOpen: public CPriceSeries
```

### Title

```cpp
   #include <Indicators\TimeSeries.mqh>
```

|  |
| --- |
| Inheritance hierarchy    [CObject](../../../Basic-Class-CObject/Basic-Class-CObject.md)        [CArray](../../../Data-Collections/CArray/CArray.md)            [CArrayObj](../../../Data-Collections/CArrayObj/CArrayObj.md)                [CSeries](../../Base-classes/CSeries/CSeries.md)                    [CPriceSeries](../../Base-classes/CPriceSeries/CPriceSeries.md)                        CiOpen |

### Class Methods by Groups

| Create |  |
| --- | --- |
| [Create](Create/Create.md) | Creates a series |
| Data Access |  |
| [GetData](GetData/GetData.md) | Gets the series data |

| Methods inherited from class CObject  Prev, Prev, Next, Next, [Compare](../../../Basic-Class-CObject/Compare/Compare.md) |
| --- |
| Methods inherited from class CArray  [Step](../../../Data-Collections/CArray/Step/Step.md), [Step](../../../Data-Collections/CArray/Step/Step.md), [Total](../../../Data-Collections/CArray/Total/Total.md), [Available](../../../Data-Collections/CArray/Available/Available.md), [Max](../../../Data-Collections/CArray/Max/Max.md), [IsSorted](../../../Data-Collections/CArray/IsSorted/IsSorted.md), [SortMode](../../../Data-Collections/CArray/SortMode/SortMode.md), [Clear](../../../Data-Collections/CArray/Clear/Clear.md), [Sort](../../../Data-Collections/CArray/Sort/Sort.md) |
| Methods inherited from class CArrayObj  [FreeMode](../../../Data-Collections/CArrayObj/FreeMode/FreeMode.md), [FreeMode](../../../Data-Collections/CArrayObj/FreeMode/FreeMode.md), [Type](../../../Data-Collections/CArrayObj/Type/Type.md), [Save](../../../Data-Collections/CArrayObj/Save/Save.md), [Load](../../../Data-Collections/CArrayObj/Load/Load.md), [CreateElement](../../../Data-Collections/CArrayObj/CreateElement/CreateElement.md), [Reserve](../../../Data-Collections/CArrayObj/Reserve/Reserve.md), [Resize](../../../Data-Collections/CArrayObj/Resize/Resize.md), [Shutdown](../../../Data-Collections/CArrayObj/Shutdown/Shutdown.md), [Add](../../../Data-Collections/CArrayObj/Add/Add.md), [AddArray](../../../Data-Collections/CArrayObj/AddArray/AddArray.md), [Insert](../../../Data-Collections/CArrayObj/Insert/Insert.md), [InsertArray](../../../Data-Collections/CArrayObj/InsertArray/InsertArray.md), [AssignArray](../../../Data-Collections/CArrayObj/AssignArray/AssignArray.md), [At](../../../Data-Collections/CArrayObj/At/At.md), [Update](../../../Data-Collections/CArrayObj/Update/Update.md), [Shift](../../../Data-Collections/CArrayObj/Shift/Shift.md), [Detach](../../../Data-Collections/CArrayObj/Detach/Detach.md), [Delete](../../../Data-Collections/CArrayObj/Delete/Delete.md), [DeleteRange](../../../Data-Collections/CArrayObj/DeleteRange/DeleteRange.md), [Clear](../../../Data-Collections/CArrayObj/Clear/Clear.md), [CompareArray](../../../Data-Collections/CArrayObj/CompareArray/CompareArray.md), [InsertSort](../../../Data-Collections/CArrayObj/InsertSort/InsertSort.md), [Search](../../../Data-Collections/CArrayObj/Search/Search.md), [SearchGreat](../../../Data-Collections/CArrayObj/SearchGreat/SearchGreat.md), [SearchLess](../../../Data-Collections/CArrayObj/SearchLess/SearchLess.md), [SearchGreatOrEqual](../../../Data-Collections/CArrayObj/SearchGreatOrEqual/SearchGreatOrEqual.md), [SearchLessOrEqual](../../../Data-Collections/CArrayObj/SearchLessOrEqual/SearchLessOrEqual.md), [SearchFirst](../../../Data-Collections/CArrayObj/SearchFirst/SearchFirst.md), [SearchLast](../../../Data-Collections/CArrayObj/SearchLast/SearchLast.md) |
| Methods inherited from class CSeries  [Name](../../Base-classes/CSeries/Name/Name.md), [BuffersTotal](../../Base-classes/CSeries/BuffersTotal/BuffersTotal.md), [BufferSize](../../Base-classes/CSeries/BufferSize/BufferSize.md), [Timeframe](../../Base-classes/CSeries/Timeframe/Timeframe.md), [Symbol](../../Base-classes/CSeries/Symbol/Symbol.md), [Period](../../Base-classes/CSeries/Period/Period.md), [PeriodDescription](../../Base-classes/CSeries/PeriodDescription/PeriodDescription.md), [RefreshCurrent](../../Base-classes/CSeries/RefreshCurrent/RefreshCurrent.md) |
| Methods inherited from class CPriceSeries  [BufferResize](../../Base-classes/CPriceSeries/BufferResize/BufferResize.md), [MinIndex](../../Base-classes/CPriceSeries/MinIndex/MinIndex.md), [MinValue](../../Base-classes/CPriceSeries/MinValue/MinValue.md), [MaxIndex](../../Base-classes/CPriceSeries/MaxIndex/MaxIndex.md), [MaxValue](../../Base-classes/CPriceSeries/MaxValue/MaxValue.md), [GetData](../../Base-classes/CPriceSeries/GetData/GetData.md), [Refresh](../../Base-classes/CPriceSeries/Refresh/Refresh.md) |