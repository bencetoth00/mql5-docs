# PositionGetString

PositionGetString

The function returns the requested property of an open position, pre-selected using [PositionGetSymbol](../PositionGetSymbol/PositionGetSymbol.md) or [PositionSelect](../PositionSelect/PositionSelect.md). The position property should be of the string type. There are 2 variants of the function.

1. Immediately returns the property value.

|  |
| --- |
| string  PositionGetString(     ENUM\_POSITION\_PROPERTY\_STRING  property\_id      // Property identifier     ); |

2. Returns true or false, depending on the success of the function execution. If successful, the value of the property is placed in a receiving variables passed by reference by the last parameter.

|  |
| --- |
| bool  PositionGetString(     ENUM\_POSITION\_PROPERTY\_STRING  property\_id,     // Property identifier     string&                        string\_var       // Here we accept the property value     ); |

Parameters

property\_id

[in]  Identifier of a position property. The value can be one of the values of the [ENUM\_POSITION\_PROPERTY\_STRING](../../Constants,-Enumerations-and-Structures/Trade-Constants/Position-Properties/Position-Properties.md#enum_position_property_string) enumeration.

string\_var

[out]  Variable of the string type accepting the value of the requested property.

Return Value

Value of the [string](../../Language-Basics/Data-Types/String-Type/String-Type.md) type. If the function fails, an empty string is returned.

Note

For the "netting" interpretation of positions ([ACCOUNT\_MARGIN\_MODE\_RETAIL\_NETTING](../../Constants,-Enumerations-and-Structures/Environment-State/Account-Properties/Account-Properties.md#enum_account_info_integer) and [ACCOUNT\_MARGIN\_MODE\_EXCHANGE](../../Constants,-Enumerations-and-Structures/Environment-State/Account-Properties/Account-Properties.md#enum_account_info_integer)), only one [position](../../Constants,-Enumerations-and-Structures/Trade-Constants/Position-Properties/Position-Properties.md) can exist for a [symbol](../../Checkup/Symbol/Symbol.md) at any moment of time. This position is a result of one or more [deals](../../Constants,-Enumerations-and-Structures/Trade-Constants/Deal-Properties/Deal-Properties.md). Do not confuse positions with valid [pending orders](../../Constants,-Enumerations-and-Structures/Trade-Constants/Order-Properties/Order-Properties.md), which are also displayed on the Trading tab of the Toolbox window.

If individual positions are allowed ([ACCOUNT\_MARGIN\_MODE\_RETAIL\_HEDGING](../../Constants,-Enumerations-and-Structures/Environment-State/Account-Properties/Account-Properties.md#enum_account_info_integer)), multiple positions can be open for one symbol.

To ensure receipt of fresh data about a position, it is recommended to call [PositionSelect()](../PositionSelect/PositionSelect.md) right before referring to them.

Example:

|  |
| --- |
| //+------------------------------------------------------------------+  //| Script program start function                                    |  //+------------------------------------------------------------------+  void OnStart()    {  //--- in a loop by all account positions     int total=PositionsTotal();     for(int i=0; i<total; i++)       {        //--- get the ticket of the next position by automatically selecting a position to access its properties        ulong ticket=PositionGetTicket(i);        if(ticket==0)           continue;                //--- get the position type and display the header for the list of position string properties        string type=(PositionGetInteger(POSITION\_TYPE)==POSITION\_TYPE ? "Buy" : "Sell");        PrintFormat("String properties of an open position %s #%I64u:", type, ticket);                //--- print all the string properties of the selected position under the header        PositionPropertiesStringPrint(15);       }     /\*     result:     String properties of an open position Buy #2810798881:     Symbol:        EURUSD     Comment:       Test PositionGetString     External ID:        \*/    }  //+------------------------------------------------------------------+  //| Display string properties of the selected position in the journal|  //+------------------------------------------------------------------+  void PositionPropertiesStringPrint(const uint header\_width=0)    {     uint   w=0;     string header="";     string value="";       //--- define the header text and the width of the header field  //--- if the header width is passed to the function equal to zero, then the width will be the size of the header line + 1     header="Symbol:";     w=(header\_width==0 ? header.Length()+1 : header\_width);  //--- get and display the position symbol with the specified header width in the journal     if(!PositionGetString(POSITION\_SYMBOL, value))        return;     PrintFormat("%-\*s%-s", w, header, value);       //--- display the position comment in the journal     header="Comment:";     w=(header\_width==0 ? header.Length()+1 : header\_width);     if(!PositionGetString(POSITION\_COMMENT, value))        return;     PrintFormat("%-\*s%-s", w, header, value);       //--- display the position ID in an external system in the journal      header="External ID:";     w=(header\_width==0 ? header.Length()+1 : header\_width);     if(!PositionGetString(POSITION\_EXTERNAL\_ID, value))        return;     PrintFormat("%-\*s%-s", w, header, value);    } |

See also

[PositionGetSymbol()](../PositionGetSymbol/PositionGetSymbol.md), [PositionSelect()](../PositionSelect/PositionSelect.md), [Position Properties](../../Constants,-Enumerations-and-Structures/Trade-Constants/Position-Properties/Position-Properties.md)
