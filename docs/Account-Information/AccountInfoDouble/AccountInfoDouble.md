# AccountInfoDouble

AccountInfoDouble

Returns the value of the appropriate account property.

|  |
| --- |
| double  AccountInfoDouble(     ENUM\_ACCOUNT\_INFO\_DOUBLE  property\_id      // Property identifier     ); |

Parameters

property\_id

[in]  Property identifier. The value can be one of the values of [ENUM\_ACCOUNT\_INFO\_DOUBLE](../../Constants,-Enumerations-and-Structures/Environment-State/Account-Properties/Account-Properties.md#enum_account_info_double).

Return Value

Value of [double](../../Language-Basics/Data-Types/Real-Types-(double,-float)/Real-Types-(double,-float).md) type.

Example:

|  |
| --- |
| void OnStart()    {  //--- Show all the information available from the function AccountInfoDouble()     printf("ACCOUNT\_BALANCE =  %G",AccountInfoDouble(ACCOUNT\_BALANCE));     printf("ACCOUNT\_CREDIT =  %G",AccountInfoDouble(ACCOUNT\_CREDIT));     printf("ACCOUNT\_PROFIT =  %G",AccountInfoDouble(ACCOUNT\_PROFIT));     printf("ACCOUNT\_EQUITY =  %G",AccountInfoDouble(ACCOUNT\_EQUITY));     printf("ACCOUNT\_MARGIN =  %G",AccountInfoDouble(ACCOUNT\_MARGIN));     printf("ACCOUNT\_MARGIN\_FREE =  %G",AccountInfoDouble(ACCOUNT\_MARGIN\_FREE));     printf("ACCOUNT\_MARGIN\_LEVEL =  %G",AccountInfoDouble(ACCOUNT\_MARGIN\_LEVEL));     printf("ACCOUNT\_MARGIN\_SO\_CALL = %G",AccountInfoDouble(ACCOUNT\_MARGIN\_SO\_CALL));     printf("ACCOUNT\_MARGIN\_SO\_SO = %G",AccountInfoDouble(ACCOUNT\_MARGIN\_SO\_SO));    } |

See also

[SymbolInfoDouble](../../Market-Info/SymbolInfoDouble/SymbolInfoDouble.md), [SymbolInfoString](../../Market-Info/SymbolInfoString/SymbolInfoString.md), [SymbolInfoInteger](../../Market-Info/SymbolInfoInteger/SymbolInfoInteger.md), [PrintFormat](../../Common-Functions/PrintFormat/PrintFormat.md)
