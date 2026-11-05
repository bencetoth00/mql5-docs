# MarketBookAdd


Provides opening of Depth of Market for a selected symbol, and subscribes for receiving notifications of the DOM changes.

```cpp
bool  MarketBookAdd(
   string  symbol      // symbol
   );
```

Parameters

symbol

[in] The name of a symbol, whose Depth of Market is to be used in the Expert Advisor or script.

Return Value

The true value if opened successfully, otherwise false.

Note

Normally, this function must be called from the [OnInit()](../../Event-Handling/OnInit/OnInit.md) function or in the class constructor. To handle incoming alerts, in the Expert Advisor program must contain the function void [OnBookEvent](../../Event-Handling/OnBookEvent/OnBookEvent.md)(string& symbol).

Example:

```cpp
#define   SYMBOL_NAME   "GBPUSD"
//+------------------------------------------------------------------+
//| Script program start function                                    |
//+------------------------------------------------------------------+
void OnStart()
  {
//--- open the market depth for SYMBOL_NAME symbol
   if(!MarketBookAdd(SYMBOL_NAME))
     {
      PrintFormat("MarketBookAdd(%s) failed. Error ", SYMBOL_NAME, GetLastError());
      return;
     }
//--- send the message about successfully opening the market depth to the journal
   PrintFormat("The MarketBook for the '%s' symbol was successfully opened and a subscription to change it was received", SYMBOL_NAME);
//--- wait 2 seconds
   Sleep(2000);
//--- upon completion, unsubscribe from the open market depth
   ResetLastError();
   if(MarketBookRelease(SYMBOL_NAME))
      PrintFormat("MarketBook for the '%s' symbol was successfully closed", SYMBOL_NAME);
   else
      PrintFormat("Error %d occurred when closing MarketBook using the '%s' symbol", GetLastError(), SYMBOL_NAME);
   /*
   result:
   The MarketBook for the 'GBPUSD' symbol was successfully opened and a subscription to change it was received
   MarketBook for the 'GBPUSD' symbol was successfully closed
   */
  }
```

See also

[Structure of Depth of Market](../../Constants,-Enumerations-and-Structures/Data-Structures/Order-Book-Structure/Order-Book-Structure.md), [Structures and Classes](../../Language-Basics/Data-Types/Structures,-Classes-and-Interfaces/Structures,-Classes-and-Interfaces.md)