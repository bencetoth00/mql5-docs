# CAccountInfo

CAccountInfo

CAccountInfo is a class for easy access to the currently opened trade account properties.

Description

CAccountInfo class provides easy access to the currently opened trade account properties.

Declaration

|  |
| --- |
| class CAccountInfo : public CObject |

Title

|  |
| --- |
| #include <Trade\AccountInfo.mqh> |

|  |
| --- |
| Inheritance hierarchy    [CObject](../../Basic-Class-CObject/Basic-Class-CObject.md)        CAccountInfo |

Class methods by groups

| Access to integer type properties |  |
| --- | --- |
| [Login](Login/Login.md) | Gets the account number |
| [TradeMode](TradeMode/TradeMode.md) | Gets the trade mode |
| [TradeModeDescription](TradeModeDescription/TradeModeDescription.md) | Gets the trade mode as a string |
| [Leverage](Leverage/Leverage.md) | Gets the amount of given leverage |
| [StopoutMode](StopoutMode/StopoutMode.md) | Gets the mode of stop out setting |
| [StopoutModeDescription](StopoutModeDescription/StopoutModeDescription.md) | Gets the mode of stop out setting as a string |
| [TradeAllowed](TradeAllowed/TradeAllowed.md) | Gets the flag of trade allowance |
| [TradeExpert](TradeExpert/TradeExpert.md) | Gets the flag of automated trade allowance |
| [LimitOrders](LimitOrders/LimitOrders.md) | Gets the maximal number of allowed pending orders |
| [MarginMode](MarginMode/MarginMode.md) | Gets margin calculation mode |
| [MarginModeDescription](MarginModeDescription/MarginModeDescription.md) | Gets margin calculation mode as a string |
| Access to double type properties |  |
| [Balance](Balance/Balance.md) | Gets the balance of account |
| [Credit](Credit/Credit.md) | Gets the amount of given credit |
| [Profit](Profit/Profit.md) | Gets the amount of current profit on account |
| [Equity](Equity/Equity.md) | Gets the amount of current equity on account |
| [Margin](Margin/Margin.md) | Gets the amount of reserved margin |
| [FreeMargin](FreeMargin/FreeMargin.md) | Gets the amount of free margin |
| [MarginLevel](MarginLevel/MarginLevel.md) | Gets the level of margin |
| [MarginCall](MarginCall/MarginCall.md) | Gets the level of margin for deposit |
| [MarginStopOut](MarginStopOut/MarginStopOut.md) | Gets the level of margin for Stop Out |
| Access to text properties |  |
| [Name](Name/Name.md) | Gets the client name |
| [Server](Server/Server.md) | Gets the trade server name |
| [Currency](Currency/Currency.md) | Gets the deposit currency name |
| [Company](Company/Company.md) | Gets the company name that serves an account |
| Access to MQL5 API functions |  |
| [InfoInteger](InfoInteger/InfoInteger.md) | Gets the value of specified integer type property |
| [InfoDouble](InfoDouble/InfoDouble.md) | Gets the value of specified double type property |
| [InfoString](InfoString/InfoString.md) | Gets the value of specified string type property |
| Additional methods |  |
| [OrderProfitCheck](OrderProfitCheck/OrderProfitCheck.md) | Gets the evaluated profit based on the parameters passed |
| [MarginCheck](MarginCheck/MarginCheck.md) | Gets the amount of margin required to execute trade operation |
| [FreeMarginCheck](FreeMarginCheck/FreeMarginCheck.md) | Gets the amount of free margin left after execution of trade operation |
| [MaxLotCheck](MaxLotCheck/MaxLotCheck.md) | Gets the maximal possible volume of trade operation |

|  |
| --- |
| Methods inherited from class CObject  Prev, Prev, Next, Next, [Save](../../Basic-Class-CObject/Save/Save.md), [Load](../../Basic-Class-CObject/Load/Load.md), [Type](../../Basic-Class-CObject/Type/Type.md), [Compare](../../Basic-Class-CObject/Compare/Compare.md) |
