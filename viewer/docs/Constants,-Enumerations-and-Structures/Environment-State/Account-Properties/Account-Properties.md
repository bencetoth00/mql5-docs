# Account Properties


To obtain information about the current account there are several functions: [AccountInfoInteger()](../../../Account-Information/AccountInfoInteger/AccountInfoInteger.md), [AccountInfoDouble()](../../../Account-Information/AccountInfoDouble/AccountInfoDouble.md) and [AccountInfoString()](../../../Account-Information/AccountInfoString/AccountInfoString.md). The function parameter values can accept values from the corresponding ENUM\_ACCOUNT\_INFO enumerations.

For the function [AccountInfoInteger()](../../../Account-Information/AccountInfoInteger/AccountInfoInteger.md)

ENUM\_ACCOUNT\_INFO\_INTEGER

| Identifier | Description | Type |
| --- | --- | --- |
| ACCOUNT\_LOGIN | Account number | long |
| ACCOUNT\_TRADE\_MODE | Account trade mode | [ENUM\_ACCOUNT\_TRADE\_MODE](Account-Properties.md#enum_account_trade_mode) |
| ACCOUNT\_LEVERAGE | Account leverage | long |
| ACCOUNT\_LIMIT\_ORDERS | Maximum allowed number of active pending orders | int |
| ACCOUNT\_MARGIN\_SO\_MODE | Mode for setting the minimal allowed margin | [ENUM\_ACCOUNT\_STOPOUT\_MODE](Account-Properties.md#enum_account_stopout_mode) |
| ACCOUNT\_TRADE\_ALLOWED | [Allowed trade](../../../MQL5-programs/Trade-Permission/Trade-Permission.md) for the current account | bool |
| ACCOUNT\_TRADE\_EXPERT | [Allowed trade](../../../MQL5-programs/Trade-Permission/Trade-Permission.md) for an Expert Advisor | bool |
| ACCOUNT\_MARGIN\_MODE | Margin calculation mode | [ENUM\_ACCOUNT\_MARGIN\_MODE](Account-Properties.md#enum_account_margin_mode) |
| ACCOUNT\_CURRENCY\_DIGITS | The number of decimal places in the account currency, which are required for an accurate display of trading results | int |
| ACCOUNT\_FIFO\_CLOSE | An indication showing that positions can only be closed by FIFO rule. If the property value is set to true, then each symbol positions will be closed in the same order, in which they are opened, starting with the oldest one. In case of an attempt to close positions in a different order, the trader will receive an appropriate error.     For accounts with the non-hedging position accounting mode ([ACCOUNT\_MARGIN\_MODE](Account-Properties.md#enum_account_info_integer)!=[ACCOUNT\_MARGIN\_MODE\_RETAIL\_HEDGING](Account-Properties.md#enum_account_margin_mode)), the property value is always false. | bool |
| ACCOUNT\_HEDGE\_ALLOWED | Allowed opposite positions on a single symbol | bool |

For the function [AccountInfoDouble()](../../../Account-Information/AccountInfoDouble/AccountInfoDouble.md)

ENUM\_ACCOUNT\_INFO\_DOUBLE

| Identifier | Description | Type |
| --- | --- | --- |
| ACCOUNT\_BALANCE | Account balance in the deposit currency | double |
| ACCOUNT\_CREDIT | Account credit in the deposit currency | double |
| ACCOUNT\_PROFIT | Current profit of an account in the deposit currency | double |
| ACCOUNT\_EQUITY | Account equity in the deposit currency | double |
| ACCOUNT\_MARGIN | Account margin used in the deposit currency | double |
| ACCOUNT\_MARGIN\_FREE | Free margin of an account in the deposit currency | double |
| ACCOUNT\_MARGIN\_LEVEL | Account margin level in percents | double |
| ACCOUNT\_MARGIN\_SO\_CALL | Margin call level. Depending on the set ACCOUNT\_MARGIN\_SO\_MODE is expressed in percents or in the deposit currency | double |
| ACCOUNT\_MARGIN\_SO\_SO | Margin stop out level. Depending on the set ACCOUNT\_MARGIN\_SO\_MODE is expressed in percents or in the deposit currency | double |
| ACCOUNT\_MARGIN\_INITIAL | Initial margin. The amount reserved on an account to cover the margin of all pending orders | double |
| ACCOUNT\_MARGIN\_MAINTENANCE | Maintenance margin. The minimum equity reserved on an account to cover the minimum amount of all open positions | double |
| ACCOUNT\_ASSETS | The current assets of an account | double |
| ACCOUNT\_LIABILITIES | The current liabilities on an account | double |
| ACCOUNT\_COMMISSION\_BLOCKED | The current blocked commission amount on an account | double |

For function [AccountInfoString()](../../../Account-Information/AccountInfoString/AccountInfoString.md)

ENUM\_ACCOUNT\_INFO\_STRING

| Identifier | Description | Type |
| --- | --- | --- |
| ACCOUNT\_NAME | Client name | string |
| ACCOUNT\_SERVER | Trade server name | string |
| ACCOUNT\_CURRENCY | Account currency | string |
| ACCOUNT\_COMPANY | Name of a company that serves the account | string |

There are several types of accounts that can be opened on a trade server. The type of account on which an MQL5 program is running can be found out using the ENUM\_ACCOUNT\_TRADE\_MODE enumeration.

ENUM\_ACCOUNT\_TRADE\_MODE

| Identifier | Description |
| --- | --- |
| ACCOUNT\_TRADE\_MODE\_DEMO | Demo account |
| ACCOUNT\_TRADE\_MODE\_CONTEST | Contest account |
| ACCOUNT\_TRADE\_MODE\_REAL | Real account |

In case equity is not enough for maintaining open positions, the Stop Out situation, i.e. forced closing occurs. The minimum margin level at which Stop Out occurs can be set in percentage or in monetary terms. To find out the mode set for the account use the ENUM\_ACCOUNT\_STOPOUT\_MODE enumeration.

ENUM\_ACCOUNT\_STOPOUT\_MODE

| Identifier | Description |
| --- | --- |
| ACCOUNT\_STOPOUT\_MODE\_PERCENT | Account stop out mode in percents |
| ACCOUNT\_STOPOUT\_MODE\_MONEY | Account stop out mode in money |

ENUM\_ACCOUNT\_MARGIN\_MODE

| Identifier | Description |
| --- | --- |
| ACCOUNT\_MARGIN\_MODE\_RETAIL\_NETTING | Used for the OTC markets to interpret positions in the "netting" mode (only one position can exist for one symbol). The margin is calculated based on the symbol type ([SYMBOL\_TRADE\_CALC\_MODE](../Symbol-Properties/Symbol-Properties.md#enum_symbol_info_integer)). |
| ACCOUNT\_MARGIN\_MODE\_EXCHANGE | Used for the exchange markets. Margin is calculated based on the discounts specified in symbol settings. Discounts are set by the broker, but not less than the values set by the exchange. |
| ACCOUNT\_MARGIN\_MODE\_RETAIL\_HEDGING | Used for the exchange markets where individual positions are possible (hedging, multiple positions can exist for one symbol). The margin is calculated based on the symbol type ([SYMBOL\_TRADE\_CALC\_MODE](../Symbol-Properties/Symbol-Properties.md#enum_symbol_info_integer)) taking into account the hedged margin ([SYMBOL\_MARGIN\_HEDGED](../Symbol-Properties/Symbol-Properties.md#enum_symbol_info_double)). |

An example of the script that outputs a brief account information.

```cpp
//+------------------------------------------------------------------+
//| Script program start function                                    |
//+------------------------------------------------------------------+
void OnStart()
  {
//--- Name of the company
   string company=AccountInfoString(ACCOUNT_COMPANY);
//--- Name of the client
   string name=AccountInfoString(ACCOUNT_NAME);
//--- Account number
   long login=AccountInfoInteger(ACCOUNT_LOGIN);
//--- Name of the server
   string server=AccountInfoString(ACCOUNT_SERVER);
//--- Account currency
   string currency=AccountInfoString(ACCOUNT_CURRENCY);
//--- Demo, contest or real account
   ENUM_ACCOUNT_TRADE_MODE account_type=(ENUM_ACCOUNT_TRADE_MODE)AccountInfoInteger(ACCOUNT_TRADE_MODE);
//--- Now transform the value of  the enumeration into an understandable form
   string trade_mode;
   switch(account_type)
     {
      case  ACCOUNT_TRADE_MODE_DEMO:
         trade_mode="demo";
         break;
      case  ACCOUNT_TRADE_MODE_CONTEST:
         trade_mode="contest";
         break;
      default:
         trade_mode="real";
         break;
     }
//--- Stop Out is set in percentage or money
   ENUM_ACCOUNT_STOPOUT_MODE stop_out_mode=(ENUM_ACCOUNT_STOPOUT_MODE)AccountInfoInteger(ACCOUNT_MARGIN_SO_MODE);
//--- Get the value of the levels when Margin Call and Stop Out occur
   double margin_call=AccountInfoDouble(ACCOUNT_MARGIN_SO_CALL);
   double stop_out=AccountInfoDouble(ACCOUNT_MARGIN_SO_SO);
//--- Show brief account information
   PrintFormat("The account of the client '%s' #%d %s opened in '%s' on the server '%s'",
               name,login,trade_mode,company,server);
   PrintFormat("Account currency - %s, MarginCall and StopOut levels are set in %s",
               currency,(stop_out_mode==ACCOUNT_STOPOUT_MODE_PERCENT)?"percentage":" money");
   PrintFormat("MarginCall=%G, StopOut=%G",margin_call,stop_out);
  }
```