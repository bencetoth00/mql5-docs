# AccountInfoString


Returns the value of the appropriate account property.

```cpp
string  AccountInfoString(
   ENUM_ACCOUNT_INFO_STRING  property_id      // Property identifier
   );
```

Parameters

property\_id

[in]  Property identifier. The value can be one of the values of [ENUM\_ACCOUNT\_INFO\_STRING](../../Constants,-Enumerations-and-Structures/Environment-State/Account-Properties/Account-Properties.md#enum_account_info_string).

Return Value

Value of [string](../../Language-Basics/Data-Types/String-Type/String-Type.md) type.

Example:

```cpp
void OnStart()
  {
//--- Show all the information available from the function AccountInfoString()
   Print("The name of the broker = ",AccountInfoString(ACCOUNT_COMPANY));
   Print("Deposit currency = ",AccountInfoString(ACCOUNT_CURRENCY));
   Print("Client name = ",AccountInfoString(ACCOUNT_NAME));
   Print("The name of the trade server = ",AccountInfoString(ACCOUNT_SERVER));
  }
```

See also

[Account Information](../../Constants,-Enumerations-and-Structures/Environment-State/Account-Properties/Account-Properties.md)