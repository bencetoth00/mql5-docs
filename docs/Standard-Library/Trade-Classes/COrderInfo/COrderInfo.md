# COrderInfo

COrderInfo

COrderInfo is a class for easy access to the pending order properties.

Description

COrderInfo class provides access to the pending order properties.

Declaration

|  |
| --- |
| class COrderInfo : public CObject |

Title

|  |
| --- |
| #include <Trade\OrderInfo.mqh> |

|  |
| --- |
| Inheritance hierarchy    [CObject](../../Basic-Class-CObject/Basic-Class-CObject.md)        COrderInfo |

Class methods by groups

| Access to integer type properties |  |
| --- | --- |
| [Ticket](Ticket/Ticket.md) | Gets the ticket of an order, previously selected for access |
| [TimeSetup](TimeSetup/TimeSetup.md) | Gets the time of order placement |
| [TimeSetupMsc](TimeSetupMsc/TimeSetupMsc.md) | Receives the time of placing an order in milliseconds since 01.01.1970 |
| [OrderType](OrderType/OrderType.md) | Gets the order type |
| [OrderTypeDescription](TypeDescription/TypeDescription.md) | Gets the order type as a string |
| [State](State/State.md) | Gets the order state |
| [StateDescription](StateDescription/StateDescription.md) | Gets the order state as a string |
| [TimeExpiration](TimeExpiration/TimeExpiration.md) | Gets the time of order expiration |
| [TimeDone](TimeDone/TimeDone.md) | Gets the time of order execution or cancellation |
| [TimeDoneMsc](TimeDoneMsc/TimeDoneMsc.md) | Receives order execution or cancellation time in milliseconds since 01.01.1970 |
| [TypeFilling](TypeFilling/TypeFilling.md) | Gets the type of order execution by remainder |
| [TypeFillingDescription](TypeFillingDescription/TypeFillingDescription.md) | Gets the type of order execution by remainder as a string |
| [TypeTime](TypeTime/TypeTime.md) | Gets the type of order at the time of the expiration |
| [TypeTimeDescription](TypeTimeDescription/TypeTimeDescription.md) | Gets the order type by expiration time as a string |
| [Magic](Magic/Magic.md) | Gets the ID of expert that placed the order |
| [PositionId](PositionId/PositionId.md) | Gets the ID of position |
| Access to double type properties |  |
| [VolumeInitial](VolumeInitial/VolumeInitial.md) | Gets the initial volume of order |
| [VolumeCurrent](VolumeCurrent/VolumeCurrent.md) | Gets the unfilled volume of order |
| [PriceOpen](PriceOpen/PriceOpen.md) | Gets the order price |
| [StopLoss](StopLoss/StopLoss.md) | Gets the order's Stop Loss |
| [TakeProfit](TakeProfit/TakeProfit.md) | Gets the order's Take Profit |
| [PriceCurrent](PriceCurrent/PriceCurrent.md) | Gets the current price by order symbol |
| [PriceStopLimit](PriceStopLimit/PriceStopLimit.md) | Gets the price of a Limit order |
| Access to text properties |  |
| [Symbol](Symbol/Symbol.md) | Gets the name of order symbol |
| [Comment](Comment/Comment.md) | Gets the order comment |
| Access to MQL5 API functions |  |
| [InfoInteger](InfoInteger/InfoInteger.md) | Gets the value of specified integer type property |
| [InfoDouble](InfoDouble/InfoDouble.md) | Gets the value of specified double type property |
| [InfoString](InfoString/InfoString.md) | Gets value of specified string type property |
| State |  |
| [StoreState](StoreState/StoreState.md) | Saves the order parameters |
| [CheckState](CheckState/CheckState.md) | Checks the current parameters against the saved parameters |
| Selection |  |
| [Select](Select/Select.md) | Selects an order by ticket for further access to its properties |
| [SelectByIndex](SelectByIndex/SelectByIndex.md) | Selects an order by index for further access to its properties |

|  |
| --- |
| Methods inherited from class CObject  Prev, Prev, Next, Next, [Save](../../Basic-Class-CObject/Save/Save.md), [Load](../../Basic-Class-CObject/Load/Load.md), [Type](../../Basic-Class-CObject/Type/Type.md), [Compare](../../Basic-Class-CObject/Compare/Compare.md) |
