# PositionGetInteger

PositionGetInteger

The function returns the requested property of an open position, pre-selected using [PositionGetSymbol](../PositionGetSymbol/PositionGetSymbol.md) or [PositionSelect](../PositionSelect/PositionSelect.md). The position property should be of datetime, int type. There are 2 variants of the function.

1. Immediately returns the property value.

|  |
| --- |
| long  PositionGetInteger(     ENUM\_POSITION\_PROPERTY\_INTEGER  property\_id      // Property identifier     ); |

2. Returns true or false, depending on the success of the function execution. If successful, the value of the property is placed in a receiving variables passed by reference by the last parameter.

|  |
| --- |
| bool  PositionGetInteger(     ENUM\_POSITION\_PROPERTY\_INTEGER  property\_id,     // Property identifier     long&                           long\_var         // Here we accept the property value     ); |

Parameters

property\_id

[in]  Identifier of a position property. The value can be one of the values of the [ENUM\_POSITION\_PROPERTY\_INTEGER](../../Constants,-Enumerations-and-Structures/Trade-Constants/Position-Properties/Position-Properties.md#enum_position_property_integer) enumeration.

long\_var

[out]  Variable of the long type accepting the value of the requested property.

Return Value

Value of the [long](../../Language-Basics/Data-Types/Integer-Types/Char,-Short,-Int-and-Long-Types/Char,-Short,-Int-and-Long-Types.md#long) type. If the function fails, 0 is returned.

Note

For the "netting" interpretation of positions ([ACCOUNT\_MARGIN\_MODE\_RETAIL\_NETTING](../../Constants,-Enumerations-and-Structures/Environment-State/Account-Properties/Account-Properties.md#enum_account_info_integer) and [ACCOUNT\_MARGIN\_MODE\_EXCHANGE](../../Constants,-Enumerations-and-Structures/Environment-State/Account-Properties/Account-Properties.md#enum_account_info_integer)), only one [position](../../Constants,-Enumerations-and-Structures/Trade-Constants/Position-Properties/Position-Properties.md) can exist for a [symbol](../../Checkup/Symbol/Symbol.md) at any moment of time. This position is a result of one or more [deals](../../Constants,-Enumerations-and-Structures/Trade-Constants/Deal-Properties/Deal-Properties.md). Do not confuse positions with valid [pending orders](../../Constants,-Enumerations-and-Structures/Trade-Constants/Order-Properties/Order-Properties.md), which are also displayed on the Trading tab of the Toolbox window.

If individual positions are allowed ([ACCOUNT\_MARGIN\_MODE\_RETAIL\_HEDGING](../../Constants,-Enumerations-and-Structures/Environment-State/Account-Properties/Account-Properties.md#enum_account_info_integer)), multiple positions can be open for one symbol.

To ensure receipt of fresh data about a position, it is recommended to call [PositionSelect()](../PositionSelect/PositionSelect.md) right before referring to them.

Example:

|  |
| --- |
| //+------------------------------------------------------------------+  //| Trade function                                                   |  //+------------------------------------------------------------------+  void OnTrade()    {  //--- check if a position is present and display the time of its changing     if(PositionSelect(\_Symbol))       {       //--- receive position ID for further work        ulong position\_ID=PositionGetInteger(POSITION\_IDENTIFIER);        Print(\_Symbol," position #",position\_ID);  //--- receive the time of position forming in milliseconds since 01.01.1970        long create\_time\_msc=PositionGetInteger(POSITION\_TIME\_MSC);        PrintFormat("Position #%d  POSITION\_TIME\_MSC = %i64 milliseconds => %s",position\_ID,                    create\_time\_msc,TimeToString(create\_time\_msc/1000));  //--- receive the time of the position's last change in seconds since 01.01.1970        long update\_time\_sec=PositionGetInteger(POSITION\_TIME\_UPDATE);        PrintFormat("Position #%d  POSITION\_TIME\_UPDATE = %i64 seconds => %s",                    position\_ID,update\_time\_sec,TimeToString(update\_time\_sec));  //--- receive the time of the position's last change in milliseconds since 01.01.1970        long update\_time\_msc=PositionGetInteger(POSITION\_TIME\_UPDATE\_MSC);        PrintFormat("Position #%d  POSITION\_TIME\_UPDATE\_MSC = %i64 milliseconds => %s",                    position\_ID,update\_time\_msc,TimeToString(update\_time\_msc/1000));       }  //---    } |

See also

[PositionGetSymbol()](../PositionGetSymbol/PositionGetSymbol.md), [PositionSelect()](../PositionSelect/PositionSelect.md), [Position Properties](../../Constants,-Enumerations-and-Structures/Trade-Constants/Position-Properties/Position-Properties.md)
