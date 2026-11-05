# AccountInfoDouble


Returns the value of the appropriate account property.

```cpp
double  AccountInfoDouble(
   ENUM_ACCOUNT_INFO_DOUBLE  property_id      // Property identifier
   );
```

Parameters

property\_id

[in]  Property identifier. The value can be one of the values of [ENUM\_ACCOUNT\_INFO\_DOUBLE](../../Constants,-Enumerations-and-Structures/Environment-State/Account-Properties/Account-Properties.md#enum_account_info_double).

Return Value

Value of [double](../../Language-Basics/Data-Types/Real-Types-(double,-float)/Real-Types-(double,-float).md) type.

Example:

```cpp
void OnStart()
  {
//--- Show all the information available from the function AccountInfoDouble()
   printf("ACCOUNT_BALANCE =  %G",AccountInfoDouble(ACCOUNT_BALANCE));
   printf("ACCOUNT_CREDIT =  %G",AccountInfoDouble(ACCOUNT_CREDIT));
   printf("ACCOUNT_PROFIT =  %G",AccountInfoDouble(ACCOUNT_PROFIT));
   printf("ACCOUNT_EQUITY =  %G",AccountInfoDouble(ACCOUNT_EQUITY));
   printf("ACCOUNT_MARGIN =  %G",AccountInfoDouble(ACCOUNT_MARGIN));
   printf("ACCOUNT_MARGIN_FREE =  %G",AccountInfoDouble(ACCOUNT_MARGIN_FREE));
   printf("ACCOUNT_MARGIN_LEVEL =  %G",AccountInfoDouble(ACCOUNT_MARGIN_LEVEL));
   printf("ACCOUNT_MARGIN_SO_CALL = %G",AccountInfoDouble(ACCOUNT_MARGIN_SO_CALL));
   printf("ACCOUNT_MARGIN_SO_SO = %G",AccountInfoDouble(ACCOUNT_MARGIN_SO_SO));
  }
```

See also

[SymbolInfoDouble](../../Market-Info/SymbolInfoDouble/SymbolInfoDouble.md), [SymbolInfoString](../../Market-Info/SymbolInfoString/SymbolInfoString.md), [SymbolInfoInteger](../../Market-Info/SymbolInfoInteger/SymbolInfoInteger.md), [PrintFormat](../../Common-Functions/PrintFormat/PrintFormat.md)