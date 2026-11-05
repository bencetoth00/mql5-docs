# CustomSymbolSetString

CustomSymbolSetString

Sets the string type property value for a custom symbol.

|  |
| --- |
| bool  CustomSymbolSetString(     const string              symbol\_name,      // symbol name     ENUM\_SYMBOL\_INFO\_STRING   property\_id,      // property ID     string                    property\_value    // property value     ); |

Parameters

symbol\_name

[in]  Custom symbol name.

property\_id

[in]  Symbol property ID. The value can be one of the values of the [ENUM\_SYMBOL\_INFO\_STRING](../../Constants,-Enumerations-and-Structures/Environment-State/Symbol-Properties/Symbol-Properties.md#enum_symbol_info_string) enumeration.

property\_value

[in]  A string type variable containing the property value.

Return Value

true – success, otherwise – false. To get information about the error, call the [GetLastError()](../../Checkup/GetLastError/GetLastError.md) function.

Note

The minute and tick history of the custom symbol is completely removed if the SYMBOL\_FORMULA property (setting the equation for the custom symbol price construction) is changed in the symbol specification. After deleting the custom symbol history, the terminal attempts to create a new history using the new equation. The same happens when the custom symbol equation is changed manually.

 

Example:

|  |
| --- |
| //+------------------------------------------------------------------+  //|                                        CustomSymbolSetString.mq5 |  //|                                  Copyright 2024, MetaQuotes Ltd. |  //|                                             https://www.mql5.com |  //+------------------------------------------------------------------+  #property copyright "Copyright 2024, MetaQuotes Ltd."  #property link      "https://www.mql5.com"  #property version   "1.00"     #define   CUSTOM\_SYMBOL\_NAME     Symbol()+".C"  // custom symbol name  #define   CUSTOM\_SYMBOL\_PATH     "Forex"        // name of the group, in which a symbol is to be created  #define   CUSTOM\_SYMBOL\_ORIGIN   Symbol()       // name of a symbol a custom one is to be based on     //+------------------------------------------------------------------+  //| Script program start function                                    |  //+------------------------------------------------------------------+  void OnStart()    {  //--- get the error code when creating a custom symbol     int create=CreateCustomSymbol(CUSTOM\_SYMBOL\_NAME, CUSTOM\_SYMBOL\_PATH, CUSTOM\_SYMBOL\_ORIGIN);       //--- if the error code is not 0 (successful symbol creation) and not 5304 (symbol has already been created) - leave     if(create!=0 && create!=5304)        return;          //--- get and print in the journal the properties of the symbol the custom one is based on  //--- (minimum volume, maximum volume, minimum volume change step for deal execution)     string origin\_basis    = SymbolInfoString(CUSTOM\_SYMBOL\_ORIGIN, SYMBOL\_BASIS);     string origin\_category = SymbolInfoString(CUSTOM\_SYMBOL\_ORIGIN, SYMBOL\_CATEGORY);     string origin\_formula  = SymbolInfoString(CUSTOM\_SYMBOL\_ORIGIN, SYMBOL\_FORMULA);          PrintFormat("The '%s' symbol from which the custom '%s' was created:\n"+                 "  Basis: %s\n  Category: %s\n  Formula: %s",                 CUSTOM\_SYMBOL\_ORIGIN, CUSTOM\_SYMBOL\_NAME,                 origin\_basis, origin\_category, origin\_formula);       //--- set other values for the custom symbol properties     ResetLastError();     bool res=true;     res &=CustomSymbolSetString(CUSTOM\_SYMBOL\_NAME, SYMBOL\_BASIS, CUSTOM\_SYMBOL\_ORIGIN);     res &=CustomSymbolSetString(CUSTOM\_SYMBOL\_NAME, SYMBOL\_CATEGORY, "FX");     res &=CustomSymbolSetString(CUSTOM\_SYMBOL\_NAME, SYMBOL\_FORMULA, ("1.0 / "+CUSTOM\_SYMBOL\_ORIGIN));     //--- if there was an error when setting any of the properties, display an appropriate message in the journal     if(!res)        Print("CustomSymbolSetString() failed. Error ", GetLastError());       //--- get and print in the journal the modified custom symbol properties  //--- (minimum volume, maximum volume, minimum volume change step for deal execution)     string custom\_basis    = SymbolInfoString(CUSTOM\_SYMBOL\_NAME, SYMBOL\_BASIS);     string custom\_category = SymbolInfoString(CUSTOM\_SYMBOL\_NAME, SYMBOL\_CATEGORY);     string custom\_formula  = SymbolInfoString(CUSTOM\_SYMBOL\_NAME, SYMBOL\_FORMULA);          PrintFormat("Custom symbol '%s' based on '%s':\n"+                 "  Basis: %s\n  Category: %s\n  Formula: %s",                 CUSTOM\_SYMBOL\_ORIGIN, CUSTOM\_SYMBOL\_NAME,                 custom\_basis, custom\_category, custom\_formula);       //--- display a hint about the script termination keys on the chart comment     Comment(StringFormat("Press 'Esc' to exit or 'Del' to delete the '%s' symbol and exit", CUSTOM\_SYMBOL\_NAME));     //--- wait for pressing the Esc or Del keys to exit in an endless loop     while(!IsStopped() && TerminalInfoInteger(TERMINAL\_KEYSTATE\_ESCAPE)==0)       {        Sleep(16);        //--- when pressing Del, delete the created custom symbol        if(TerminalInfoInteger(TERMINAL\_KEYSTATE\_DELETE)<0)          {           if(DeleteCustomSymbol(CUSTOM\_SYMBOL\_NAME))              PrintFormat("Custom symbol '%s' deleted successfully", CUSTOM\_SYMBOL\_NAME);           break;          }       }  //--- clear the chart before exiting     Comment("");     /\*     result:     The 'EURUSD' symbol from which the custom 'EURUSD.C' was created:       Basis:        Category:        Formula:      Custom symbol 'EURUSD' based on 'EURUSD.C':       Basis: EURUSD       Category: FX       Formula: 1.0 / EURUSD     \*/    }  //+------------------------------------------------------------------+  //| Create a custom symbol, return an error code                     |  //+------------------------------------------------------------------+  int CreateCustomSymbol(const string symbol\_name, const string symbol\_path, const string symbol\_origin=NULL)    {  //--- define the name of a symbol a custom one is to be based on     string origin=(symbol\_origin==NULL ? Symbol() : symbol\_origin);       //--- if failed to create a custom symbol and this is not error 5304, report this in the journal     ResetLastError();     int error=0;     if(!CustomSymbolCreate(symbol\_name, symbol\_path, origin))       {        error=GetLastError();        if(error!=5304)           PrintFormat("CustomSymbolCreate(%s, %s, %s) failed. Error %d", symbol\_name, symbol\_path, origin, error);       }  //--- successful     return(error);    }  //+------------------------------------------------------------------+  //| Remove a custom symbol                                           |  //+------------------------------------------------------------------+  bool DeleteCustomSymbol(const string symbol\_name)    {  //--- hide the symbol from the Market Watch window     ResetLastError();     if(!SymbolSelect(symbol\_name, false))       {        PrintFormat("SymbolSelect(%s, false) failed. Error %d", GetLastError());        return(false);       }          //--- if failed to delete a custom symbol, report this in the journal and return 'false'     ResetLastError();     if(!CustomSymbolDelete(symbol\_name))       {        PrintFormat("CustomSymbolDelete(%s) failed. Error %d", symbol\_name, GetLastError());        return(false);       }  //--- successful     return(true);    } |

 

See also

[SymbolInfoString](../../Market-Info/SymbolInfoString/SymbolInfoString.md)
