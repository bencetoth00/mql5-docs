# HistoryDealGetDouble

HistoryDealGetDouble

Returns the requested property of a deal. The deal property must be of the double type. There are 2 variants of the function.

1. Immediately returns the property value.

|  |
| --- |
| double  HistoryDealGetDouble(     ulong                      ticket\_number,     // Ticket     ENUM\_DEAL\_PROPERTY\_DOUBLE  property\_id        // Property identifier     ); |

2. Returns true or false, depending on the success of the function. If successful, the value of the property is placed into a target variable passed by reference by the last parameter.

|  |
| --- |
| bool  HistoryDealGetDouble(     ulong                      ticket\_number,     // Ticket     ENUM\_DEAL\_PROPERTY\_DOUBLE  property\_id,       // Property identifier     double&                    double\_var         // Here we accept the property value     ); |

Parameters

ticket\_number

[in]  Deal ticket.

property\_id

[in]  Identifier of a deal property. The value can be one of the values of the [ENUM\_DEAL\_PROPERTY\_DOUBLE](../../Constants,-Enumerations-and-Structures/Trade-Constants/Deal-Properties/Deal-Properties.md#enum_deal_property_double) enumeration.

double\_var

[out]  Variable of the double type that accepts the value of the requested property.

Return Value

Value of the [double](../../Language-Basics/Data-Types/Real-Types-(double,-float)/Real-Types-(double,-float).md) type.

Note

Do not confuse [orders](../../Constants,-Enumerations-and-Structures/Trade-Constants/Order-Properties/Order-Properties.md), [deals](../../Constants,-Enumerations-and-Structures/Trade-Constants/Deal-Properties/Deal-Properties.md) and [positions](../../Constants,-Enumerations-and-Structures/Trade-Constants/Position-Properties/Position-Properties.md). Each deal is the result of the execution of an order, each position is the summary result of one or more deals.

Example:

|  |
| --- |
| //+------------------------------------------------------------------+  //| Script program start function                                    |  //+------------------------------------------------------------------+  void OnStart()    {  //--- request deal and order history     if(!HistorySelect(0, TimeCurrent()))       {        Print("HistorySelect() failed. Error ", GetLastError());        return;       }     //--- in a loop by the list of deals in the account history     int total=HistoryDealsTotal();     for(int i=0; i<total; i++)       {        //--- get the ticket of the next deal (the deal is automatically selected to get its properties)        ulong ticket=HistoryDealGetTicket(i);        if(ticket==0)           continue;                //--- get the type and direction of the deal and display the header for the list of real properties of the selected deal        string type=DealTypeDescription((ENUM\_DEAL\_TYPE)HistoryDealGetInteger(ticket, DEAL\_TYPE));        string entry=DealEntryDescription((ENUM\_DEAL\_ENTRY)HistoryDealGetInteger(ticket, DEAL\_ENTRY));        PrintFormat("Double properties of an deal %s entry %s #%I64u:", type, entry, ticket);                //--- print all the real properties of the selected deal under the header        HistoryDealPropertiesDoublePrint(ticket, 12);       }     /\*     real:     Double properties of an deal Buy entry In #2785070622:     Volume:     0.50     Price:      1.10480     Commission: 0.00     Swap:       0.00     Profit:     0.00 USD     Fee:        0.00     StopLoss:   0.00000     TakeProfit: 0.00000     Double properties of an deal Sell entry Out #2785071538:     Volume:     0.50     Price:      1.10491     Commission: 0.00     Swap:       0.00     Profit:     5.50 USD     Fee:        0.00     StopLoss:   0.00000     TakeProfit: 0.00000     \*/    }  //+------------------------------------------------------------------+  //| Display real properties of the selected deal in the journal      |  //+------------------------------------------------------------------+  void HistoryDealPropertiesDoublePrint(const ulong ticket, const uint header\_width=0)    {     uint   w=0;     string header="";     double value=0;       //--- get the deal symbol, profit currency and the number of decimal places for the symbol     string symbol  = HistoryDealGetString(ticket, DEAL\_SYMBOL);     string currency= SymbolInfoString(symbol, SYMBOL\_CURRENCY\_PROFIT);     int    digits  = (int)SymbolInfoInteger(symbol, SYMBOL\_DIGITS);       //--- define the header text and the width of the header field  //--- if the header width is passed to the function equal to zero, then the width will be the size of the header line + 1     header="Volume:";     w=(header\_width==0 ? header.Length()+1 : header\_width);  //--- get and display the deal volume with the specified header width in the journal     if(!HistoryDealGetDouble(ticket, DEAL\_VOLUME, value))        return;     PrintFormat("%-\*s%-.2f", w, header, value);       //--- display the deal price in the journal     header="Price:";     w=(header\_width==0 ? header.Length()+1 : header\_width);     if(!HistoryDealGetDouble(ticket, DEAL\_PRICE, value))        return;     PrintFormat("%-\*s%-.\*f", w, header, digits, value);       //--- display the deal commission in the journal     header="Commission:";     w=(header\_width==0 ? header.Length()+1 : header\_width);     if(!HistoryDealGetDouble(ticket, DEAL\_COMMISSION, value))        return;     PrintFormat("%-\*s%-.2f", w, header, value);       //--- display the accumulated swap in the journal when closing     header="Swap:";     w=(header\_width==0 ? header.Length()+1 : header\_width);     if(!HistoryDealGetDouble(ticket, DEAL\_SWAP, value))        return;     PrintFormat("%-\*s%-.2f", w, header, value);       //--- display the deal financial result in the journal     header="Profit:";     w=(header\_width==0 ? header.Length()+1 : header\_width);     if(!HistoryDealGetDouble(ticket, DEAL\_PROFIT, value))        return;     PrintFormat("%-\*s%-.2f %s", w, header, value, currency);       //--- display the deal fee in the journal     header="Fee:";     w=(header\_width==0 ? header.Length()+1 : header\_width);     if(!HistoryDealGetDouble(ticket, DEAL\_FEE, value))        return;     PrintFormat("%-\*s%-.2f", w, header, value);       //--- display the StopLoss level in the journal     header="StopLoss:";     w=(header\_width==0 ? header.Length()+1 : header\_width);     if(!HistoryDealGetDouble(ticket, DEAL\_SL, value))        return;     PrintFormat("%-\*s%-.\*f", w, header, digits, value);     //--- display the TakeProfit level in the journal     header="TakeProfit:";     w=(header\_width==0 ? header.Length()+1 : header\_width);     if(!HistoryDealGetDouble(ticket, DEAL\_TP, value))        return;     PrintFormat("%-\*s%-.\*f", w, header, digits, value);    }  //+------------------------------------------------------------------+  //| Return the deal type description                                 |  //+------------------------------------------------------------------+  string DealTypeDescription(const ENUM\_DEAL\_TYPE type)    {     switch(type)       {        case DEAL\_TYPE\_BUY                     :  return("Buy");        case DEAL\_TYPE\_SELL                    :  return("Sell");        case DEAL\_TYPE\_BALANCE                 :  return("Balance");        case DEAL\_TYPE\_CREDIT                  :  return("Credit");        case DEAL\_TYPE\_CHARGE                  :  return("Additional charge");        case DEAL\_TYPE\_CORRECTION              :  return("Correction");        case DEAL\_TYPE\_BONUS                   :  return("Bonus");        case DEAL\_TYPE\_COMMISSION              :  return("Additional commission");        case DEAL\_TYPE\_COMMISSION\_DAILY        :  return("Daily commission");        case DEAL\_TYPE\_COMMISSION\_MONTHLY      :  return("Monthly commission");        case DEAL\_TYPE\_COMMISSION\_AGENT\_DAILY  :  return("Daily agent commission");        case DEAL\_TYPE\_COMMISSION\_AGENT\_MONTHLY:  return("Monthly agent commission");        case DEAL\_TYPE\_INTEREST                :  return("Interest rate");        case DEAL\_TYPE\_BUY\_CANCELED            :  return("Canceled buy deal");        case DEAL\_TYPE\_SELL\_CANCELED           :  return("Canceled sell deal");        case DEAL\_DIVIDEND                     :  return("Dividend operations");        case DEAL\_DIVIDEND\_FRANKED             :  return("Franked (non-taxable) dividend operations");        case DEAL\_TAX                          :  return("Tax charges");        default                                :  return("Unknown deal type: "+(string)type);       }    }  //+------------------------------------------------------------------+  //| Return position change method                                    |  //+------------------------------------------------------------------+  string DealEntryDescription(const ENUM\_DEAL\_ENTRY entry)    {     switch(entry)       {        case DEAL\_ENTRY\_IN      :  return("In");        case DEAL\_ENTRY\_OUT     :  return("Out");        case DEAL\_ENTRY\_INOUT   :  return("Reverce");        case DEAL\_ENTRY\_OUT\_BY  :  return("Out by");        case DEAL\_ENTRY\_STATE   :  return("Status record");        default                 :  return("Unknown deal entry: "+(string)entry);       }    } |

See also

[HistorySelect()](../HistorySelect/HistorySelect.md), [HistoryDealsTotal()](../HistoryDealsTotal/HistoryDealsTotal.md), [HistoryDealGetTicket()](../HistoryDealGetTicket/HistoryDealGetTicket.md), [Deal Properties](../../Constants,-Enumerations-and-Structures/Trade-Constants/Deal-Properties/Deal-Properties.md)
