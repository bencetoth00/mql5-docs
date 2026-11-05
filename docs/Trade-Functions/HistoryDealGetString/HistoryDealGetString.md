# HistoryDealGetString

HistoryDealGetString

Returns the requested property of a deal. The deal property must be of the string type. There are 2 variants of the function.

1. Immediately returns the property value.

|  |
| --- |
| string  HistoryDealGetString(     ulong                      ticket\_number,     // Ticket     ENUM\_DEAL\_PROPERTY\_STRING  property\_id        // Property identifier     ); |

2. Returns true or false, depending on the success of the function. If successful, the value of the property is placed into a target variable passed by reference by the last parameter.

|  |
| --- |
| bool  HistoryDealGetString(     ulong                      ticket\_number,     // Ticket     ENUM\_DEAL\_PROPERTY\_STRING  property\_id,       // Property identifier     string&                    string\_var         // Here we accept the property value     ); |

Parameters

ticket\_number

[in]  Deal ticket.

property\_id

[in]  Identifier of the deal property. The value can be one of the values of the [ENUM\_DEAL\_PROPERTY\_STRING](../../Constants,-Enumerations-and-Structures/Trade-Constants/Deal-Properties/Deal-Properties.md#enum_deal_property_string) enumeration.

string\_var

[out]  Variable of the string type that accepts the value of the requested property.

Return Value

Value of the [string](../../Language-Basics/Data-Types/String-Type/String-Type.md) type.

Note

Do not confuse [orders](../../Constants,-Enumerations-and-Structures/Trade-Constants/Order-Properties/Order-Properties.md), [deals](../../Constants,-Enumerations-and-Structures/Trade-Constants/Deal-Properties/Deal-Properties.md) and [positions](../../Constants,-Enumerations-and-Structures/Trade-Constants/Position-Properties/Position-Properties.md). Each deal is the result of the execution of an order, each position is the summary result of one or more deals.

Example:

|  |
| --- |
| //+------------------------------------------------------------------+  //| Script program start function                                    |  //+------------------------------------------------------------------+  void OnStart()    {  //--- request deal and order history     if(!HistorySelect(0, TimeCurrent()))       {        Print("HistorySelect() failed. Error ", GetLastError());        return;       }     //--- in a loop by the list of deals in the account history     int total=HistoryDealsTotal();     for(int i=0; i<total; i++)       {        //--- get the ticket of the next deal (the deal is automatically selected to get its properties)        ulong ticket=HistoryDealGetTicket(i);        if(ticket==0)           continue;                //--- get the type and direction of the deal and display the header for the list of real properties of the selected deal        string type=DealTypeDescription((ENUM\_DEAL\_TYPE)HistoryDealGetInteger(ticket, DEAL\_TYPE));        string entry=DealEntryDescription((ENUM\_DEAL\_ENTRY)HistoryDealGetInteger(ticket, DEAL\_ENTRY));        PrintFormat("String properties of an deal %s entry %s #%I64u:", type, entry, ticket);                //--- print all the real properties of the selected deal under the header        HistoryDealPropertiesStringPrint(ticket, 13);       }     /\*     result:     String properties of an deal Buy entry In #2785021084:     Symbol:      EURUSD     Comment:     Test PositionGetString     Extarnal ID:     String properties of an deal Buy entry Out #2497993663:     Symbol:      EURUSD     Comment:     [tp 1.08639]     Extarnal ID:      \*/    }  //+------------------------------------------------------------------+  //| Display string properties of the selected deal in the journal    |  //+------------------------------------------------------------------+  void HistoryDealPropertiesStringPrint(const ulong ticket, const uint header\_width=0)    {     uint   w=0;     string header="";     string value ="";       //--- define the header text and the width of the header field  //--- if the header width is passed to the function equal to zero, then the width will be the size of the header line + 1     header="Symbol:";     w=(header\_width==0 ? header.Length()+1 : header\_width);  //--- get and display the deal symbol with the specified header width in the journal     if(!HistoryDealGetString(ticket, DEAL\_SYMBOL, value))        return;     PrintFormat("%-\*s%-s", w, header, value);       //--- display the deal comment in the journal     header="Comment:";     w=(header\_width==0 ? header.Length()+1 : header\_width);     if(!HistoryDealGetString(ticket, DEAL\_COMMENT, value))        return;     PrintFormat("%-\*s%-s", w, header, value);       //--- display the deal ID in an external trading system      header="Extarnal ID:";     w=(header\_width==0 ? header.Length()+1 : header\_width);     if(!HistoryDealGetString(ticket, DEAL\_EXTERNAL\_ID, value))        return;     PrintFormat("%-\*s%-s", w, header, value);    }  //+------------------------------------------------------------------+  //| Return the deal type description                                 |  //+------------------------------------------------------------------+  string DealTypeDescription(const ENUM\_DEAL\_TYPE type)    {     switch(type)       {        case DEAL\_TYPE\_BUY                     :  return("Buy");        case DEAL\_TYPE\_SELL                    :  return("Sell");        case DEAL\_TYPE\_BALANCE                 :  return("Balance");        case DEAL\_TYPE\_CREDIT                  :  return("Credit");        case DEAL\_TYPE\_CHARGE                  :  return("Additional charge");        case DEAL\_TYPE\_CORRECTION              :  return("Correction");        case DEAL\_TYPE\_BONUS                   :  return("Bonus");        case DEAL\_TYPE\_COMMISSION              :  return("Additional commission");        case DEAL\_TYPE\_COMMISSION\_DAILY        :  return("Daily commission");        case DEAL\_TYPE\_COMMISSION\_MONTHLY      :  return("Monthly commission");        case DEAL\_TYPE\_COMMISSION\_AGENT\_DAILY  :  return("Daily agent commission");        case DEAL\_TYPE\_COMMISSION\_AGENT\_MONTHLY:  return("Monthly agent commission");        case DEAL\_TYPE\_INTEREST                :  return("Interest rate");        case DEAL\_TYPE\_BUY\_CANCELED            :  return("Canceled buy deal");        case DEAL\_TYPE\_SELL\_CANCELED           :  return("Canceled sell deal");        case DEAL\_DIVIDEND                     :  return("Dividend operations");        case DEAL\_DIVIDEND\_FRANKED             :  return("Franked (non-taxable) dividend operations");        case DEAL\_TAX                          :  return("Tax charges");        default                                :  return("Unknown deal type: "+(string)type);       }    }  //+------------------------------------------------------------------+  //| Return position change method                                    |  //+------------------------------------------------------------------+  string DealEntryDescription(const ENUM\_DEAL\_ENTRY entry)    {     switch(entry)       {        case DEAL\_ENTRY\_IN      :  return("In");        case DEAL\_ENTRY\_OUT     :  return("Out");        case DEAL\_ENTRY\_INOUT   :  return("Reverce");        case DEAL\_ENTRY\_OUT\_BY  :  return("Out by");        case DEAL\_ENTRY\_STATE   :  return("Status record");        default                 :  return("Unknown deal entry: "+(string)entry);       }    } |

See also

[HistoryDealsTotal()](../HistoryDealsTotal/HistoryDealsTotal.md), [HistorySelect()](../HistorySelect/HistorySelect.md), [HistoryDealGetTicket()](../HistoryDealGetTicket/HistoryDealGetTicket.md), [Deal Properties](../../Constants,-Enumerations-and-Structures/Trade-Constants/Deal-Properties/Deal-Properties.md)
