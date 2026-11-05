# AccountInfoString

AccountInfoString

Returns the value of the appropriate account property.

|  |
| --- |
| string  AccountInfoString(     ENUM\_ACCOUNT\_INFO\_STRING  property\_id      // Property identifier     ); |

Parameters

property\_id

[in]  Property identifier. The value can be one of the values of [ENUM\_ACCOUNT\_INFO\_STRING](../../Constants,-Enumerations-and-Structures/Environment-State/Account-Properties/Account-Properties.md#enum_account_info_string).

Return Value

Value of [string](../../Language-Basics/Data-Types/String-Type/String-Type.md) type.

Example:

|  |
| --- |
| void OnStart()    {  //--- Show all the information available from the function AccountInfoString()     Print("The name of the broker = ",AccountInfoString(ACCOUNT\_COMPANY));     Print("Deposit currency = ",AccountInfoString(ACCOUNT\_CURRENCY));     Print("Client name = ",AccountInfoString(ACCOUNT\_NAME));     Print("The name of the trade server = ",AccountInfoString(ACCOUNT\_SERVER));    } |

See also

[Account Information](../../Constants,-Enumerations-and-Structures/Environment-State/Account-Properties/Account-Properties.md)
