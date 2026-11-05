# Basic Class CObject


Class CObject is the base class for constructing a MQL5 Standard Library.

### Description

Class CObject allows all its descendants to be part of a linked list. Also, a number of virtual methods for further implementation in descendant classes are identified.

Declaration

```cpp
   class CObject
```

### Title

```cpp
   #include <Object.mqh>
```

|  |
| --- |
| Inheritance hierarchy    CObject  Direct descendants  [CAccountInfo](../Trade-Classes/CAccountInfo/CAccountInfo.md), [CArray](../Data-Collections/CArray/CArray.md), [CChart](../Price-Charts/Price-Charts.md), [CChartObject](../Graphic-Objects/CChartObject/CChartObject.md), [CCurve](../Scientific-Charts/CCurve/CCurve.md), [CDealInfo](../Trade-Classes/CDealInfo/CDealInfo.md), CDictionary\_Obj\_Double, CDictionary\_Obj\_Obj, CDictionary\_String\_Obj, [CExpertBase](../Strategy-Modules/Base-classes-for-Expert-Advisors/CExpertBase/CExpertBase.md), [CFile](../Files/CFile/CFile.md), [CHistoryOrderInfo](../Trade-Classes/CHistoryOrderInfo/CHistoryOrderInfo.md), [CList](../Data-Collections/CList/CList.md), [COrderInfo](../Trade-Classes/COrderInfo/COrderInfo.md), [CPositionInfo](../Trade-Classes/CPositionInfo/CPositionInfo.md), [CString](../Strings/CString/CString.md), [CSymbolInfo](../Trade-Classes/CSymbolInfo/CSymbolInfo.md), [CTerminalInfo](../Trade-Classes/CTerminalInfo/CTerminalInfo.md), [CTrade](../Trade-Classes/CTrade/CTrade.md), [CTreeNode](../Data-Collections/CTreeNode/CTreeNode.md), [CWnd](../Panels-and-Dialogs/CWnd/CWnd.md), ICondition, IExpression, [IMembershipFunction](../Mathematics/Fuzzy-Logic/Membership-functions/IMembershipFunction/IMembershipFunction.md), INamedValue, IParsableRule |

### Class Methods by Groups

| Attributes |  |
| --- | --- |
| [Prev](Prev/Prev.md) | Gets the value of the previous item |
| [Prev](PrevNext/PrevNext.md) | Sets the value of the previous item |
| [Next](Next/Next.md) | Gets the value of the subsequent element |
| [Next](NextSet/NextSet.md) | Sets the next element |
| Compare methods |  |
| virtual [Compare](Compare/Compare.md) | Returns the result of comparison with another object |
| Input/output |  |
| virtual [Save](Save/Save.md) | Writes object to a file |
| virtual [Load](Load/Load.md) | Reads the object from the file |
| virtual [Type](Type/Type.md) | Returns the type of object |