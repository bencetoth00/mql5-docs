# PositionGetDouble

PositionGetDouble

The function returns the requested property of an open position, pre-selected using [PositionGetSymbol](../PositionGetSymbol/PositionGetSymbol.md) or [PositionSelect](../PositionSelect/PositionSelect.md). The position property must be of the double type. There are 2 variants of the function.

1. Immediately returns the property value.

|  |
| --- |
| double  PositionGetDouble(     ENUM\_POSITION\_PROPERTY\_DOUBLE  property\_id      // Property identifier     ); |

2. Returns true or false, depending on the success of the function execution. If successful, the value of the property is placed in a receiving variable passed by reference by the last parameter.

|  |
| --- |
| bool  PositionGetDouble(     ENUM\_POSITION\_PROPERTY\_DOUBLE  property\_id,     // Property identifier     double&                        double\_var       // Here we accept the property value     ); |

Parameters

property\_id

[in]  Identifier of a position property. The value can be one of the values of the [ENUM\_POSITION\_PROPERTY\_DOUBLE](../../Constants,-Enumerations-and-Structures/Trade-Constants/Position-Properties/Position-Properties.md#enum_position_property_double) enumeration.

double\_var

[out]  Variable of the double type, accepting the value of the requested property.

Return Value

Value of the [double](../../Language-Basics/Data-Types/Real-Types-(double,-float)/Real-Types-(double,-float).md) type. If the function fails, 0 is returned.

Note

For the "netting" interpretation of positions ([ACCOUNT\_MARGIN\_MODE\_RETAIL\_NETTING](../../Constants,-Enumerations-and-Structures/Environment-State/Account-Properties/Account-Properties.md#enum_account_info_integer) and [ACCOUNT\_MARGIN\_MODE\_EXCHANGE](../../Constants,-Enumerations-and-Structures/Environment-State/Account-Properties/Account-Properties.md#enum_account_info_integer)), only one [position](../../Constants,-Enumerations-and-Structures/Trade-Constants/Position-Properties/Position-Properties.md) can exist for a [symbol](../../Checkup/Symbol/Symbol.md) at any moment of time. This position is a result of one or more [deals](../../Constants,-Enumerations-and-Structures/Trade-Constants/Deal-Properties/Deal-Properties.md). Do not confuse positions with valid [pending orders](../../Constants,-Enumerations-and-Structures/Trade-Constants/Order-Properties/Order-Properties.md), which are also displayed on the Trading tab of the Toolbox window.

If individual positions are allowed ([ACCOUNT\_MARGIN\_MODE\_RETAIL\_HEDGING](../../Constants,-Enumerations-and-Structures/Environment-State/Account-Properties/Account-Properties.md#enum_account_info_integer)), multiple positions can be open for one symbol.

To ensure receipt of fresh data about a position, it is recommended to call [PositionSelect()](../PositionSelect/PositionSelect.md) right before referring to them.

Example:

|  |
| --- |
| //+------------------------------------------------------------------+  //| Script program start function                                    |  //+------------------------------------------------------------------+  void OnStart()    {  //--- in a loop by all account positions     int total=PositionsTotal();     for(int i=0; i<total; i++)       {        //--- get the ticket of the next position by automatically selecting a position to access its properties        ulong ticket=PositionGetTicket(i);        if(ticket==0)           continue;                //--- get the position type and display the header for the list of position real properties        string type=(PositionGetInteger(POSITION\_TYPE)==POSITION\_TYPE ? "Buy" : "Sell");        PrintFormat("Double properties of an open position %s #%I64u:", type, ticket);                //--- print all the real properties of the selected position under the header        PositionPropertiesDoublePrint(15);       }     /\*     result:     Double properties of an open position Buy #2807075208:     Volume:        1.00     Price open:    1.10516     StopLoss:      0.00000     TakeProfit:    0.00000     Price current: 1.10518     Swap:          0.00     Profit:        2.00 USD     \*/    }  //+------------------------------------------------------------------+  //| Display real properties of the selected position in the journal  |  //+------------------------------------------------------------------+  void PositionPropertiesDoublePrint(const uint header\_width=0)    {     uint   w=0;     string header="";     double value=0;       //--- get the account currency, position symbol and the number of decimal places for the symbol     string currency=AccountInfoString(ACCOUNT\_CURRENCY);     string symbol  =PositionGetString(POSITION\_SYMBOL);     int    digits  =(int)SymbolInfoInteger(symbol, SYMBOL\_DIGITS);       //--- define the header text and the width of the header field  //--- if the header width is passed to the function equal to zero, then the width will be the size of the header line + 1     header="Volume:";     w=(header\_width==0 ? header.Length()+1 : header\_width);  //--- get and display the position volume with the specified header width in the journal     if(!PositionGetDouble(POSITION\_VOLUME, value))        return;     PrintFormat("%-\*s%-.2f", w, header, value);       //--- display the position price value in the journal     header="Price open:";     w=(header\_width==0 ? header.Length()+1 : header\_width);     if(!PositionGetDouble(POSITION\_PRICE\_OPEN, value))        return;     PrintFormat("%-\*s%-.\*f", w, header, digits, value);       //--- display the StopLoss value in the journal     header="StopLoss:";     w=(header\_width==0 ? header.Length()+1 : header\_width);     if(!PositionGetDouble(POSITION\_SL, value))        return;     PrintFormat("%-\*s%-.\*f", w, header, digits, value);       //--- display the TakeProfit value in the journal     header="TakeProfit:";     w=(header\_width==0 ? header.Length()+1 : header\_width);     if(!PositionGetDouble(POSITION\_TP, value))        return;     PrintFormat("%-\*s%-.\*f", w, header, digits, value);     //--- display the 'Price current' value in the journal     header="Price current:";     w=(header\_width==0 ? header.Length()+1 : header\_width);     if(!PositionGetDouble(POSITION\_PRICE\_CURRENT, value))        return;     PrintFormat("%-\*s%-.\*f", w, header, digits, value);     //--- display the accumulated swap value in the journal     header="Swap:";     w=(header\_width==0 ? header.Length()+1 : header\_width);     if(!PositionGetDouble(POSITION\_SWAP, value))        return;     PrintFormat("%-\*s%-.2f", w, header, value);     //--- display the current profit value to the journal     header="Profit:";     w=(header\_width==0 ? header.Length()+1 : header\_width);     if(!PositionGetDouble(POSITION\_PROFIT, value))        return;     PrintFormat("%-\*s%-.2f %s", w, header, value, currency);    } |

See also

[PositionGetSymbol()](../PositionGetSymbol/PositionGetSymbol.md), [PositionSelect()](../PositionSelect/PositionSelect.md), [Position Properties](../../Constants,-Enumerations-and-Structures/Trade-Constants/Position-Properties/Position-Properties.md)
