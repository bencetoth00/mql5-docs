# CPositionInfo

CPositionInfo

CPositionInfo is a class for easy access to the open position properties.

Description

CPositionInfo class provides easy access to the open position properties.

Declaration

|  |
| --- |
| class CPositionInfo : public CObject |

Title

|  |
| --- |
| #include <Trade\PositionInfo.mqh> |

|  |
| --- |
| Inheritance hierarchy    [CObject](../../Basic-Class-CObject/Basic-Class-CObject.md)        CPositionInfo |

Class methods by groups

| Access to integer type properties |  |
| --- | --- |
| [Time](Time/Time.md) | Gets the time of position opening |
| [TimeMsc](TimeMsc/TimeMsc.md) | Receives the time of  position opening in milliseconds since 01.01.1970 |
| [TimeUpdate](TimeUpdate/TimeUpdate.md) | Receives the time of position changing in seconds since 01.01.1970 |
| [TimeUpdateMsc](TimeUpdateMsc/TimeUpdateMsc.md) | Receives the time of position changing in milliseconds since 01.01.1970 |
| [PositionType](PositionType/PositionType.md) | Gets the position type |
| [TypeDescription](TypeDescription/TypeDescription.md) | Gets the position type as a string |
| [Magic](Magic/Magic.md) | Gets the ID of expert, that opened the position |
| [Identifier](Identifier/Identifier.md) | Gets the ID of position |
| Access to double type properties |  |
| [Volume](Volume/Volume.md) | Gets the volume of position |
| [PriceOpen](PriceOpen/PriceOpen.md) | Gets the price of position opening |
| [StopLoss](StopLoss/StopLoss.md) | Gets the price of position's Stop Loss |
| [TakeProfit](TakeProfit/TakeProfit.md) | Gets the price of position's Take Profit |
| [PriceCurrent](PriceCurrent/PriceCurrent.md) | Gets the current price by position symbol |
| [Commission](Commission/Commission.md) | Gets the amount of commission by position |
| [Swap](Swap/Swap.md) | Gets the amount of swap by position |
| [Profit](Profit/Profit.md) | Gets the amount of current profit by position |
| Access to text properties |  |
| [Symbol](Symbol/Symbol.md) | Gets the name of position symbol |
| [Comment](Comment/Comment.md) | Gets the comment of the position |
| Access to MQL5 API functions |  |
| [InfoInteger](InfoInteger/InfoInteger.md) | Gets the value of specified integer type property |
| [InfoDouble](InfoDouble/InfoDouble.md) | Gets the value of specified double type property |
| [InfoString](InfoString/InfoString.md) | Gets the value of specified string type property |
| Selection |  |
| [Select](Select/Select.md) | Selects the position |
| [SelectByIndex](SelectByIndex/SelectByIndex.md) | Selects the position by index |
| [SelectByMagic](SelectByMagic/SelectByMagic.md) | Selects a position with the specified symbol name and magic number |
| [SelectByTicket](SelectByTicket/SelectByTicket.md) | Selects the position by ticket |
| State |  |
| [StoreState](StoreState/StoreState.md) | Saves the position parameters |
| [CheckState](CheckState/CheckState.md) | Checks the current parameters against the saved parameters |

|  |
| --- |
| Methods inherited from class CObject  Prev, Prev, Next, Next, [Save](../../Basic-Class-CObject/Save/Save.md), [Load](../../Basic-Class-CObject/Load/Load.md), [Type](../../Basic-Class-CObject/Type/Type.md), [Compare](../../Basic-Class-CObject/Compare/Compare.md) |
