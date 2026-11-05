# CHighBuffer

CHighBuffer

CHighBuffer is a class for simplified access to high prices of bars in the history.

Description

CHighBuffer class provides a simplified access to high prices of bars in the history.

Declaration

|  |
| --- |
| class CHighBuffer: public CDoubleBuffer |

Title

|  |
| --- |
| #include <Indicators\TimeSeries.mqh> |

|  |
| --- |
| Inheritance hierarchy    [CObject](../../../Basic-Class-CObject/Basic-Class-CObject.md)        [CArray](../../../Data-Collections/CArray/CArray.md)            [CArrayDouble](../../../Data-Collections/CArrayDouble/CArrayDouble.md)                [CDoubleBuffer](../CDoubleBuffer/CDoubleBuffer.md)                    CHighBuffer |

Class Methods by Groups

| Data Update |  |
| --- | --- |
| virtual [Refresh](Refresh/Refresh.md) | Updates the buffer |
| virtual [RefreshCurrent](RefreshCurrent/RefreshCurrent.md) | Updates the current value |

| Methods inherited from class CObject  Prev, Prev, Next, Next, [Compare](../../../Basic-Class-CObject/Compare/Compare.md) |
| --- |
| Methods inherited from class CArray  [Step](../../../Data-Collections/CArray/Step/Step.md), [Step](../../../Data-Collections/CArray/Step/Step.md), [Total](../../../Data-Collections/CArray/Total/Total.md), [Available](../../../Data-Collections/CArray/Available/Available.md), [Max](../../../Data-Collections/CArray/Max/Max.md), [IsSorted](../../../Data-Collections/CArray/IsSorted/IsSorted.md), [SortMode](../../../Data-Collections/CArray/SortMode/SortMode.md), [Clear](../../../Data-Collections/CArray/Clear/Clear.md), [Sort](../../../Data-Collections/CArray/Sort/Sort.md) |
| Methods inherited from class CArrayDouble  [Delta](../../../Data-Collections/CArrayDouble/Delta/Delta.md), [Type](../../../Data-Collections/CArrayDouble/Type/Type.md), [Save](../../../Data-Collections/CArrayDouble/Save/Save.md), [Load](../../../Data-Collections/CArrayDouble/Load/Load.md), [Reserve](../../../Data-Collections/CArrayDouble/Reserve/Reserve.md), [Resize](../../../Data-Collections/CArrayDouble/Resize/Resize.md), [Shutdown](../../../Data-Collections/CArrayDouble/Shutdown/Shutdown.md), [Add](../../../Data-Collections/CArrayDouble/Add/Add.md), [AddArray](../../../Data-Collections/CArrayDouble/AddArray/AddArray.md), [AddArray](../../../Data-Collections/CArrayDouble/AddArray/AddArray.md), [Insert](../../../Data-Collections/CArrayDouble/Insert/Insert.md), [InsertArray](../../../Data-Collections/CArrayDouble/InsertArray/InsertArray.md), [InsertArray](../../../Data-Collections/CArrayDouble/InsertArray/InsertArray.md), [AssignArray](../../../Data-Collections/CArrayDouble/AssignArray/AssignArray.md), [AssignArray](../../../Data-Collections/CArrayDouble/AssignArray/AssignArray.md), [At](../../../Data-Collections/CArrayDouble/At/At.md), operator, [Minimum](../../../Data-Collections/CArrayDouble/Minimum/Minimum.md), [Maximum](../../../Data-Collections/CArrayDouble/Maximum/Maximum.md), [Update](../../../Data-Collections/CArrayDouble/Update/Update.md), [Shift](../../../Data-Collections/CArrayDouble/Shift/Shift.md), [Delete](../../../Data-Collections/CArrayDouble/Delete/Delete.md), [DeleteRange](../../../Data-Collections/CArrayDouble/DeleteRange/DeleteRange.md), [CompareArray](../../../Data-Collections/CArrayDouble/CompareArray/CompareArray.md), [CompareArray](../../../Data-Collections/CArrayDouble/CompareArray/CompareArray.md), [InsertSort](../../../Data-Collections/CArrayDouble/InsertSort/InsertSort.md), [Search](../../../Data-Collections/CArrayDouble/Search/Search.md), [SearchGreat](../../../Data-Collections/CArrayDouble/SearchGreat/SearchGreat.md), [SearchLess](../../../Data-Collections/CArrayDouble/SearchLess/SearchLess.md), [SearchGreatOrEqual](../../../Data-Collections/CArrayDouble/SearchGreatOrEqual/SearchGreatOrEqual.md), [SearchLessOrEqual](../../../Data-Collections/CArrayDouble/SearchLessOrEqual/SearchLessOrEqual.md), [SearchFirst](../../../Data-Collections/CArrayDouble/SearchFirst/SearchFirst.md), [SearchLast](../../../Data-Collections/CArrayDouble/SearchLast/SearchLast.md), [SearchLinear](../../../Data-Collections/CArrayDouble/SearchLinear/SearchLinear.md) |
| Methods inherited from class CDoubleBuffer  [Size](../CDoubleBuffer/Size/Size.md), [At](../CDoubleBuffer/At/At.md), [SetSymbolPeriod](../CDoubleBuffer/SetSymbolPeriod/SetSymbolPeriod.md) |
