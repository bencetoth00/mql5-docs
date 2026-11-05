# CSpreadBuffer

CSpreadBuffer

CSpreadBuffer is a class for simplified access to spreads of the bars in the history.

Description

The CSpreadBuffer class provides a simplified access to spreads of the bars in the history.

Declaration

|  |
| --- |
| class CSpreadBuffer: public CArrayInt |

Title

|  |
| --- |
| #include <Indicators\TimeSeries.mqh> |

|  |
| --- |
| Inheritance hierarchy    [CObject](../../../Basic-Class-CObject/Basic-Class-CObject.md)        [CArray](../../../Data-Collections/CArray/CArray.md)            [CArrayInt](../../../Data-Collections/CArrayInt/CArrayInt.md)                CSpreadBuffer |

Class Methods by Groups

| Attributes |  |
| --- | --- |
| [Size](Size/Size.md) | Sets buffer size |
| Settings |  |
| [SetSymbolPeriod](SetSymbolPeriod/SetSymbolPeriod.md) | Sets symbol and period |
| Data Access |  |
| [At](At/At.md) | Gets the buffer element |
| Data Update |  |
| virtual [Refresh](Refresh/Refresh.md) | Updates the buffer |
| virtual [RefreshCurrent](RefreshCurrent/RefreshCurrent.md) | Updates the current value |

| Methods inherited from class CObject  Prev, Prev, Next, Next, [Compare](../../../Basic-Class-CObject/Compare/Compare.md) |
| --- |
| Methods inherited from class CArray  [Step](../../../Data-Collections/CArray/Step/Step.md), [Step](../../../Data-Collections/CArray/Step/Step.md), [Total](../../../Data-Collections/CArray/Total/Total.md), [Available](../../../Data-Collections/CArray/Available/Available.md), [Max](../../../Data-Collections/CArray/Max/Max.md), [IsSorted](../../../Data-Collections/CArray/IsSorted/IsSorted.md), [SortMode](../../../Data-Collections/CArray/SortMode/SortMode.md), [Clear](../../../Data-Collections/CArray/Clear/Clear.md), [Sort](../../../Data-Collections/CArray/Sort/Sort.md) |
| Methods inherited from class CArrayInt  [Type](../../../Data-Collections/CArrayInt/Type/Type.md), [Save](../../../Data-Collections/CArrayInt/Save/Save.md), [Load](../../../Data-Collections/CArrayInt/Load/Load.md), [Reserve](../../../Data-Collections/CArrayInt/Reserve/Reserve.md), [Resize](../../../Data-Collections/CArrayInt/Resize/Resize.md), [Shutdown](../../../Data-Collections/CArrayInt/Shutdown/Shutdown.md), [Add](../../../Data-Collections/CArrayInt/Add/Add.md), [AddArray](../../../Data-Collections/CArrayInt/AddArray/AddArray.md), [AddArray](../../../Data-Collections/CArrayInt/AddArray/AddArray.md), [Insert](../../../Data-Collections/CArrayInt/Insert/Insert.md), [InsertArray](../../../Data-Collections/CArrayInt/InsertArray/InsertArray.md), [InsertArray](../../../Data-Collections/CArrayInt/InsertArray/InsertArray.md), [AssignArray](../../../Data-Collections/CArrayInt/AssignArray/AssignArray.md), [AssignArray](../../../Data-Collections/CArrayInt/AssignArray/AssignArray.md), [At](../../../Data-Collections/CArrayInt/At/At.md), operator, Minimum, Maximum, [Update](../../../Data-Collections/CArrayInt/Update/Update.md), [Shift](../../../Data-Collections/CArrayInt/Shift/Shift.md), [Delete](../../../Data-Collections/CArrayInt/Delete/Delete.md), [DeleteRange](../../../Data-Collections/CArrayInt/DeleteRange/DeleteRange.md), [CompareArray](../../../Data-Collections/CArrayInt/CompareArray/CompareArray.md), [CompareArray](../../../Data-Collections/CArrayInt/CompareArray/CompareArray.md), [InsertSort](../../../Data-Collections/CArrayInt/InsertSort/InsertSort.md), [Search](../../../Data-Collections/CArrayInt/Search/Search.md), [SearchGreat](../../../Data-Collections/CArrayInt/SearchGreat/SearchGreat.md), [SearchLess](../../../Data-Collections/CArrayInt/SearchLess/SearchLess.md), [SearchGreatOrEqual](../../../Data-Collections/CArrayInt/SearchGreatOrEqual/SearchGreatOrEqual.md), [SearchLessOrEqual](../../../Data-Collections/CArrayInt/SearchLessOrEqual/SearchLessOrEqual.md), [SearchFirst](../../../Data-Collections/CArrayInt/SearchFirst/SearchFirst.md), [SearchLast](../../../Data-Collections/CArrayInt/SearchLast/SearchLast.md), [SearchLinear](../../../Data-Collections/CArrayInt/SearchLinear/SearchLinear.md) |
