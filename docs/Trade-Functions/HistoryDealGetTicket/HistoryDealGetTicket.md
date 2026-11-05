# HistoryDealGetTicket

HistoryDealGetTicket

The function selects a deal for further processing and returns the deal ticket in history. Prior to calling HistoryDealGetTicket(), first it is necessary to receive the history of deals and orders using the [HistorySelect()](../HistorySelect/HistorySelect.md) or [HistorySelectByPosition()](../HistorySelectByPosition/HistorySelectByPosition.md) function.

|  |
| --- |
| ulong  HistoryDealGetTicket(     int  index      // ticket deal     ); |

Parameters

index

[in]  Number of a deal in the list of deals

Return Value

Value of the [ulong](../../Language-Basics/Data-Types/Integer-Types/Char,-Short,-Int-and-Long-Types/Char,-Short,-Int-and-Long-Types.md) type. If the function fails, 0 is returned.

Note

Do not confuse [orders](../../Constants,-Enumerations-and-Structures/Trade-Constants/Order-Properties/Order-Properties.md), [deals](../../Constants,-Enumerations-and-Structures/Trade-Constants/Deal-Properties/Deal-Properties.md) and [positions](../../Constants,-Enumerations-and-Structures/Trade-Constants/Position-Properties/Position-Properties.md). Each deal is the result of the execution of an order, each position is the summary result of one or more deals.

Example:

|  |
| --- |
| void OnStart()    {     ulong deal\_ticket;            // deal ticket     ulong order\_ticket;           // ticket of the order the deal was executed on     datetime transaction\_time;    // time of a deal execution      long deal\_type ;              // type of a trade operation     long position\_ID;             // position ID     string deal\_description;      // operation description     double volume;                // operation volume     string symbol;                // symbol of the deal  //--- set the start and end date to request the history of deals     datetime from\_date=0;         // from the very beginning     datetime to\_date=TimeCurrent();// till the current moment  //--- request the history of deals in the specified period     HistorySelect(from\_date,to\_date);  //--- total number in the list of deals     int deals=HistoryDealsTotal();  //--- now process each trade     for(int i=0;i<deals;i++)       {        deal\_ticket=               HistoryDealGetTicket(i);        volume=                    HistoryDealGetDouble(deal\_ticket,DEAL\_VOLUME);        transaction\_time=(datetime)HistoryDealGetInteger(deal\_ticket,DEAL\_TIME);        order\_ticket=              HistoryDealGetInteger(deal\_ticket,DEAL\_ORDER);        deal\_type=                 HistoryDealGetInteger(deal\_ticket,DEAL\_TYPE);        symbol=                    HistoryDealGetString(deal\_ticket,DEAL\_SYMBOL);        position\_ID=               HistoryDealGetInteger(deal\_ticket,DEAL\_POSITION\_ID);        deal\_description=          GetDealDescription(deal\_type,volume,symbol,order\_ticket,position\_ID);        //--- perform fine formatting for the deal number        string print\_index=StringFormat("% 3d",i);        //--- show information on the deal        Print(print\_index+": deal #",deal\_ticket," at ",transaction\_time,deal\_description);       }    }  //+------------------------------------------------------------------+  //| Returns the string description of the operation                  |  //+------------------------------------------------------------------+  string GetDealDescription(long deal\_type,double volume,string symbol,long ticket,long pos\_ID)    {     string descr;  //---     switch(deal\_type)       {        case DEAL\_TYPE\_BALANCE:                  return ("balance");        case DEAL\_TYPE\_CREDIT:                   return ("credit");        case DEAL\_TYPE\_CHARGE:                   return ("charge");        case DEAL\_TYPE\_CORRECTION:               return ("correction");        case DEAL\_TYPE\_BUY:                      descr="buy"; break;        case DEAL\_TYPE\_SELL:                     descr="sell"; break;        case DEAL\_TYPE\_BONUS:                    return ("bonus");        case DEAL\_TYPE\_COMMISSION:               return ("additional commission");        case DEAL\_TYPE\_COMMISSION\_DAILY:         return ("daily commission");        case DEAL\_TYPE\_COMMISSION\_MONTHLY:       return ("monthly commission");        case DEAL\_TYPE\_COMMISSION\_AGENT\_DAILY:   return ("daily agent commission");        case DEAL\_TYPE\_COMMISSION\_AGENT\_MONTHLY: return ("monthly agent commission");        case DEAL\_TYPE\_INTEREST:                 return ("interest rate");        case DEAL\_TYPE\_BUY\_CANCELED:             descr="cancelled buy deal"; break;        case DEAL\_TYPE\_SELL\_CANCELED:            descr="cancelled sell deal"; break;       }     descr=StringFormat("%s %G %s (order #%d, position ID %d)",                        descr,  // current description                        volume, // deal volume                        symbol, // deal symbol                        ticket, // ticket of the order that caused the deal                        pos\_ID  // ID of a position, in which the deal is included                        );     return(descr);  //---    } |
|  |

See also

[HistorySelect()](../HistorySelect/HistorySelect.md), [HistoryDealsTotal()](../HistoryDealsTotal/HistoryDealsTotal.md), [HistoryDealSelect()](../HistoryDealSelect/HistoryDealSelect.md), [Deal Properties](../../Constants,-Enumerations-and-Structures/Trade-Constants/Deal-Properties/Deal-Properties.md)
