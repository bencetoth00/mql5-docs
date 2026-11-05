# CTimeBuffer


CTimeBuffer is a class for simplified access to opening times of the bars in the history.

### Description

The CTimeBuffer class provides a simplified access to opening times of the bars in the history.

### Declaration

```cpp
   class CTimeBuffer: public CArrayLong
```

### Title

```cpp
   #include <Indicators\TimeSeries.mqh>
```

|  |
| --- |
| Inheritance hierarchy    [CObject](../../../Basic-Class-CObject/Basic-Class-CObject.md)        [CArray](../../../Data-Collections/CArray/CArray.md)            [CArrayLong](../../../Data-Collections/CArrayLong/CArrayLong.md)                CTimeBuffer |

### Class Methods by Groups

| Attributes |  |
| --- | --- |
| [Size](Size/Size.md) | Sets buffer size |
| Settings |  |
| [SetSymbolPeriod](SetSymbolPeriod/SetSymbolPeriod.md) | Sets symbol and period |
| Data Access Methods |  |
| [At](At/At.md) | Gets the buffer element by index |
| Data Update Methods |  |
| virtual [Refresh](Refresh/Refresh.md) | Updates the buffer |
| virtual [RefreshCurrent](RefreshCurrent/RefreshCurrent.md) | Updates the current value |

| Methods inherited from class CObject  Prev, Prev, Next, Next, [Compare](../../../Basic-Class-CObject/Compare/Compare.md) |
| --- |
| Methods inherited from class CArray  [Step](../../../Data-Collections/CArray/Step/Step.md), [Step](../../../Data-Collections/CArray/Step/Step.md), [Total](../../../Data-Collections/CArray/Total/Total.md), [Available](../../../Data-Collections/CArray/Available/Available.md), [Max](../../../Data-Collections/CArray/Max/Max.md), [IsSorted](../../../Data-Collections/CArray/IsSorted/IsSorted.md), [SortMode](../../../Data-Collections/CArray/SortMode/SortMode.md), [Clear](../../../Data-Collections/CArray/Clear/Clear.md), [Sort](../../../Data-Collections/CArray/Sort/Sort.md) |
| Methods inherited from class CArrayLong  [Type](../../../Data-Collections/CArrayLong/Type/Type.md), [Save](../../../Data-Collections/CArrayLong/Save/Save.md), [Load](../../../Data-Collections/CArrayLong/Load/Load.md), [Reserve](../../../Data-Collections/CArrayLong/Reserve/Reserve.md), [Resize](../../../Data-Collections/CArrayLong/Resize/Resize.md), [Shutdown](../../../Data-Collections/CArrayLong/Shutdown/Shutdown.md), [Add](../../../Data-Collections/CArrayLong/Add/Add.md), [AddArray](../../../Data-Collections/CArrayLong/AddArray/AddArray.md), [AddArray](../../../Data-Collections/CArrayLong/AddArray/AddArray.md), [Insert](../../../Data-Collections/CArrayLong/Insert/Insert.md), [InsertArray](../../../Data-Collections/CArrayLong/InsertArray/InsertArray.md), [InsertArray](../../../Data-Collections/CArrayLong/InsertArray/InsertArray.md), [AssignArray](../../../Data-Collections/CArrayLong/AssignArray/AssignArray.md), [AssignArray](../../../Data-Collections/CArrayLong/AssignArray/AssignArray.md), [At](../../../Data-Collections/CArrayLong/At/At.md), operator, Minimum, Maximum, [Update](../../../Data-Collections/CArrayLong/Update/Update.md), [Shift](../../../Data-Collections/CArrayLong/Shift/Shift.md), [Delete](../../../Data-Collections/CArrayLong/Delete/Delete.md), [DeleteRange](../../../Data-Collections/CArrayLong/DeleteRange/DeleteRange.md), [CompareArray](../../../Data-Collections/CArrayLong/CompareArray/CompareArray.md), [CompareArray](../../../Data-Collections/CArrayLong/CompareArray/CompareArray.md), [InsertSort](../../../Data-Collections/CArrayLong/InsertSort/InsertSort.md), [Search](../../../Data-Collections/CArrayLong/Search/Search.md), [SearchGreat](../../../Data-Collections/CArrayLong/SearchGreat/SearchGreat.md), [SearchLess](../../../Data-Collections/CArrayLong/SearchLess/SearchLess.md), [SearchGreatOrEqual](../../../Data-Collections/CArrayLong/SearchGreatOrEqual/SearchGreatOrEqual.md), [SearchLessOrEqual](../../../Data-Collections/CArrayLong/SearchLessOrEqual/SearchLessOrEqual.md), [SearchFirst](../../../Data-Collections/CArrayLong/SearchFirst/SearchFirst.md), [SearchLast](../../../Data-Collections/CArrayLong/SearchLast/SearchLast.md), [SearchLinear](../../../Data-Collections/CArrayLong/SearchLinear/SearchLinear.md) |