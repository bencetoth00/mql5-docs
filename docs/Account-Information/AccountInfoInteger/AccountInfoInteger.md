# AccountInfoInteger

AccountInfoInteger

Returns the value of the appropriate account property.

|  |
| --- |
| long  AccountInfoInteger(     ENUM\_ACCOUNT\_INFO\_INTEGER  property\_id      // Identifier of the property     ); |

Parameters

property\_id

[in]  Property identifier. The value can be one of the values of [ENUM\_ACCOUNT\_INFO\_INTEGER](../../Constants,-Enumerations-and-Structures/Environment-State/Account-Properties/Account-Properties.md#enum_account_info_integer).

Return Value

Value of [long](../../Language-Basics/Data-Types/Integer-Types/Char,-Short,-Int-and-Long-Types/Char,-Short,-Int-and-Long-Types.md) type.

Note

The property must be of [bool](../../Language-Basics/Data-Types/Integer-Types/Bool-Type/Bool-Type.md), [int](../../Language-Basics/Data-Types/Integer-Types/Char,-Short,-Int-and-Long-Types/Char,-Short,-Int-and-Long-Types.md) or [long](../../Language-Basics/Data-Types/Integer-Types/Char,-Short,-Int-and-Long-Types/Char,-Short,-Int-and-Long-Types.md) type.

Example:

|  |
| --- |
| void OnStart()    {  //--- Show all the information available from the function AccountInfoInteger()     printf("ACCOUNT\_LOGIN =  %d",AccountInfoInteger(ACCOUNT\_LOGIN));     printf("ACCOUNT\_LEVERAGE =  %d",AccountInfoInteger(ACCOUNT\_LEVERAGE));     bool thisAccountTradeAllowed=AccountInfoInteger(ACCOUNT\_TRADE\_ALLOWED);     bool EATradeAllowed=AccountInfoInteger(ACCOUNT\_TRADE\_EXPERT);     ENUM\_ACCOUNT\_TRADE\_MODE tradeMode=(ENUM\_ACCOUNT\_TRADE\_MODE)AccountInfoInteger(ACCOUNT\_TRADE\_MODE);     ENUM\_ACCOUNT\_STOPOUT\_MODE stopOutMode=(ENUM\_ACCOUNT\_STOPOUT\_MODE)AccountInfoInteger(ACCOUNT\_MARGIN\_SO\_MODE);     //--- Inform about the possibility to perform a trade operation     if(thisAccountTradeAllowed)        Print("Trade for this account is permitted");     else        Print("Trade for this account is prohibited!");     //--- Find out if it is possible to trade on this account by Expert Advisors     if(EATradeAllowed)        Print("Trade by Expert Advisors is permitted for this account");     else        Print("Trade by Expert Advisors is prohibited for this account!");     //--- Find out the account type     switch(tradeMode)       {        case(ACCOUNT\_TRADE\_MODE\_DEMO):           Print("This is a demo account");           break;        case(ACCOUNT\_TRADE\_MODE\_CONTEST):           Print("This is a competition account");           break;        default:Print("This is a real account!");       }     //--- Find out the StopOut level setting mode     switch(stopOutMode)       {        case(ACCOUNT\_STOPOUT\_MODE\_PERCENT):           Print("The StopOut level is specified percentage");           break;        default:Print("The StopOut level is specified in monetary terms");       }    } |

See also

[Account Information](../../Constants,-Enumerations-and-Structures/Environment-State/Account-Properties/Account-Properties.md)
