# CDealInfo


CDealInfo is a class for easy access to the deal properties.

### Description

CDealInfo class provides access to the deal properties.

### Declaration

```cpp
   class CDealInfo : public CObject
```

### Title

```cpp
   #include <Trade\DealInfo.mqh>
```

|  |
| --- |
| Inheritance hierarchy    [CObject](../../Basic-Class-CObject/Basic-Class-CObject.md)        CDealInfo |

### Class methods by groups

| Access to integer type properties |  |
| --- | --- |
| [Order](Order/Order.md) | Gets the order by which the deal is executed |
| [Time](Time/Time.md) | Gets the time of deal execution |
| [TimeMsc](TimeMsc/TimeMsc.md) | Receives the time of a deal execution in milliseconds since 01.01.1970 |
| [DealType](DealType/DealType.md) | Gets the deal type |
| [TypeDescription](TypeDescription/TypeDescription.md) | Gets the deal type as a string |
| [Entry](Entry/Entry.md) | Gets the deal direction |
| [EntryDescription](EntryDescription/EntryDescription.md) | Gets the deal direction as a string |
| [Magic](Magic/Magic.md) | Gets the ID of expert, that executed the deal |
| [PositionId](PositionId/PositionId.md) | Gets the ID of position, in which the deal was involved |
| Access to double type properties |  |
| [Volume](Volume/Volume.md) | Gets the volume of deal |
| [Price](Price/Price.md) | Gets the deal price |
| [Commision](Commision/Commision.md) | Gets the amount of commission of the deal |
| [Swap](Swap/Swap.md) | Gets the amount of swap when position is closed |
| [Profit](Profit/Profit.md) | Gets the financial result of deal |
| Access to text properties |  |
| [Symbol](Symbol/Symbol.md) | Gets the name of deal symbol |
| [Comment](Comment/Comment.md) | Gets the deal comment |
| Access to MQL5 API functions |  |
| [InfoInteger](InfoInteger/InfoInteger.md) | Gets the value of specified integer type property |
| [InfoDouble](InfoDouble/InfoDouble.md) | Gets the value of specified double type property |
| [InfoString](InfoString/InfoString.md) | Gets value of specified string type property |
| Selection |  |
| [Ticket](Ticket/Ticket.md) | Gets ticket/selects the deal |
| [SelectByIndex](SelectByIndex/SelectByIndex.md) | Selects the deal by index |

|  |
| --- |
| Methods inherited from class CObject  Prev, Prev, Next, Next, [Save](../../Basic-Class-CObject/Save/Save.md), [Load](../../Basic-Class-CObject/Load/Load.md), [Type](../../Basic-Class-CObject/Type/Type.md), [Compare](../../Basic-Class-CObject/Compare/Compare.md) |