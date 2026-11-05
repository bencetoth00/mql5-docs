# CustomSymbolDelete

CustomSymbolDelete

Deletes a custom symbol with the specified name.

|  |
| --- |
| bool  CustomSymbolDelete(     const string     symbol\_name          // custom symbol name     ); |

Parameters

symbol

[in]  Custom symbol name. It should not match the name of an already existing symbol.

Return Value

true – success, otherwise – false. To get information about the error, call the [GetLastError()](../../Checkup/GetLastError/GetLastError.md) function.

Note

The custom symbol displayed in the Market Watch or the one a chart is opened for cannot be deleted.

 

Example:

|  |
| --- |
| //+------------------------------------------------------------------+  //|                                           CustomSymbolDelete.mq5 |  //|                                  Copyright 2024, MetaQuotes Ltd. |  //|                                             https://www.mql5.com |  //+------------------------------------------------------------------+  #property copyright "Copyright 2024, MetaQuotes Ltd."  #property link      "https://www.mql5.com"  #property version   "1.00"     #define   CUSTOM\_SYMBOL\_NAME     Symbol()+".C"  // custom symbol name  #define   CUSTOM\_SYMBOL\_PATH     "Forex"        // name of the group, in which a symbol is to be created  #define   CUSTOM\_SYMBOL\_ORIGIN   Symbol()       // name of a symbol a custom one is to be based on     //+------------------------------------------------------------------+  //| Script program start function                                    |  //+------------------------------------------------------------------+  void OnStart()    {  //--- if failed to create a custom symbol, inform of that in the journal     if(!CustomSymbolCreate(CUSTOM\_SYMBOL\_NAME, CUSTOM\_SYMBOL\_PATH, CUSTOM\_SYMBOL\_ORIGIN))       {        Print("CustomSymbolCreate() failed. Error ", GetLastError());        return;       }     //--- check the existence of the created symbol and print the result in the journal     bool custom= false;     bool exist = SymbolExist(CUSTOM\_SYMBOL\_NAME, custom);     PrintFormat("Custom symbol '%s' exists: %s", CUSTOM\_SYMBOL\_NAME, (string)exist);       //--- wait two seconds and delete the created symbol with the resulting message in the journal     Sleep(2000);     ResetLastError();     bool deleted = CustomSymbolDelete(CUSTOM\_SYMBOL\_NAME);     Print(deleted ? StringFormat("Custom symbol '%s' removed", CUSTOM\_SYMBOL\_NAME) : StringFormat("CustomSymbolDelete() failed. Error ",GetLastError()));     //--- check the existence of the created symbol and print the result in the journal     exist = SymbolExist(CUSTOM\_SYMBOL\_NAME, custom);     PrintFormat("Custom symbol '%s' exists: %s", CUSTOM\_SYMBOL\_NAME, (string)exist);     /\*     result:     Custom symbol 'EURUSD.C' exists: true     Custom symbol 'EURUSD.C' removed     Custom symbol 'EURUSD.C' exists: false     \*/    } |

 

See also

[SymbolName](../../Market-Info/SymbolName/SymbolName.md), [SymbolSelect](../../Market-Info/SymbolSelect/SymbolSelect.md), [CustomSymbolCreate](../CustomSymbolCreate/CustomSymbolCreate.md)
