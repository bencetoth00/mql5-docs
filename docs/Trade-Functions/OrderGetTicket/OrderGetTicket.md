# OrderGetTicket

OrderGetTicket

Returns ticket of a corresponding order and automatically selects the order for further working with it using functions.

|  |
| --- |
| ulong  OrderGetTicket(     int  index      // Number in the list of orders     ); |

Parameters

index

[in]  Number of an order in the list of current orders.

Return Value

Value of the [ulong](../../Language-Basics/Data-Types/Integer-Types/Char,-Short,-Int-and-Long-Types/Char,-Short,-Int-and-Long-Types.md) type. If the function fails, 0 is returned.

Note

Do not confuse current [pending orders](../../Constants,-Enumerations-and-Structures/Trade-Constants/Order-Properties/Order-Properties.md) with positions, which are also displayed on the "Trade" tab of the "Toolbox" of the client terminal. An order is a request to conduct a [transaction](../../Constants,-Enumerations-and-Structures/Trade-Constants/Trade-Operation-Types/Trade-Operation-Types.md), while a position is a result of one or more [deals](../../Constants,-Enumerations-and-Structures/Trade-Constants/Deal-Properties/Deal-Properties.md).

For the "netting" interpretation of positions ([ACCOUNT\_MARGIN\_MODE\_RETAIL\_NETTING](../../Constants,-Enumerations-and-Structures/Environment-State/Account-Properties/Account-Properties.md#enum_account_info_integer) and [ACCOUNT\_MARGIN\_MODE\_EXCHANGE](../../Constants,-Enumerations-and-Structures/Environment-State/Account-Properties/Account-Properties.md#enum_account_info_integer)), only one [position](../../Constants,-Enumerations-and-Structures/Trade-Constants/Position-Properties/Position-Properties.md) can exist for a [symbol](../../Checkup/Symbol/Symbol.md) at any moment of time. This position is a result of one or more [deals](../../Constants,-Enumerations-and-Structures/Trade-Constants/Deal-Properties/Deal-Properties.md). Do not confuse positions with valid [pending orders](../../Constants,-Enumerations-and-Structures/Trade-Constants/Order-Properties/Order-Properties.md), which are also displayed on the Trading tab of the Toolbox window.

If individual positions are allowed ([ACCOUNT\_MARGIN\_MODE\_RETAIL\_HEDGING](../../Constants,-Enumerations-and-Structures/Environment-State/Account-Properties/Account-Properties.md#enum_account_info_integer)), multiple positions can be open for one symbol.

Function OrderGetTicket() copies data about an order into the program environment, and further calls of [OrderGetDouble()](../OrderGetDouble/OrderGetDouble.md), [OrderGetInteger()](../OrderGetInteger/OrderGetInteger.md), [OrderGetString()](../OrderGetString/OrderGetString.md) return the earlier copied data. This means that the order itself may no longer exist (or its open price, Stop Loss/Take Profit levels or expiration has changed), but data of this order still can be obtained. To ensure receipt of fresh data about an order, it is recommended to call OrderGetTicket() right before referring to them.

Example:

|  |
| --- |
| void OnStart()    {  //--- variables for returning values from order properties     ulong    ticket;     double   open\_price;     double   initial\_volume;     datetime time\_setup;     string   symbol;     string   type;     long     order\_magic;     long     positionID;  //--- number of current pending orders     uint     total=OrdersTotal();  //--- go through orders in a loop     for(uint i=0;i<total;i++)       {        //--- return order ticket by its position in the list        if((ticket=OrderGetTicket(i))>0)          {           //--- return order properties           open\_price    =OrderGetDouble(ORDER\_PRICE\_OPEN);           time\_setup    =(datetime)OrderGetInteger(ORDER\_TIME\_SETUP);           symbol        =OrderGetString(ORDER\_SYMBOL);           order\_magic   =OrderGetInteger(ORDER\_MAGIC);           positionID    =OrderGetInteger(ORDER\_POSITION\_ID);           initial\_volume=OrderGetDouble(ORDER\_VOLUME\_INITIAL);           type          =EnumToString(ENUM\_ORDER\_TYPE(OrderGetInteger(ORDER\_TYPE)));           //--- prepare and show information about the order           printf("#ticket %d %s %G %s at %G was set up at %s",                  ticket,                 // order ticket                  type,                   // type                  initial\_volume,         // placed volume                  symbol,                 // symbol                  open\_price,             // specified open price                  TimeToString(time\_setup)// time of order placing                  );          }       }  //---    } |

See also

[OrdersTotal()](../OrdersTotal/OrdersTotal.md), [OrderSelect()](../OrderSelect/OrderSelect.md), [OrderGetInteger()](../OrderGetInteger/OrderGetInteger.md)
