# CustomSymbolCreate


Creates a custom symbol with the specified name in the specified group.

```cpp
bool  CustomSymbolCreate(
   const string     symbol_name,         // custom symbol name
   const string     symbol_path="",      // name of a group a symbol is to be created in
   const string     symbol_origin=NULL   // name of a symbol used as a basis to create a custom symbol
   );
```

Parameters

symbol\_name

[in]  Custom symbol name. It should not contain groups or subgroups the symbol is located in.

symbol\_path=""

[in]  The group name a symbol is located in.

symbol\_origin=NULL

[in]  Name of a symbol the [properties](../../Constants,-Enumerations-and-Structures/Environment-State/Symbol-Properties/Symbol-Properties.md) of a created custom symbol are to be copied from. After creating a custom symbol, any property value can be changed to a necessary one using the appropriate functions.

Return Value

true – success, otherwise – false. To get information about the error, call the [GetLastError()](../../Checkup/GetLastError/GetLastError.md) function.

Note

All custom symbols are created in the special Custom section. If a group name is not specified (the symbol\_path parameter in the CustomSymbolCreate function contains an empty string or NULL), a custom symbol is generated in the Custom section root. Here we can draw an analogy with the file system, where groups and subgroups can be viewed as folders and subfolders

The symbol and group names may only contain Latin letters without punctuation, spaces or special characters (may only contain ".", "\_", "&" and "#"). It is not recommended to use characters <, >, :, ", /, |, ?, \*.

The custom symbol name should be unique regardless of a group name it is created in. If a symbol with the same name already exists, the CustomSymbolCreate() function returns 'false', while the subsequent [GetLastError()](../../Checkup/GetLastError/GetLastError.md) call returns the error 5300 (ERR\_NOT\_CUSTOM\_SYMBOL) or 5304 (ERR\_CUSTOM\_SYMBOL\_EXIST).

The length of the symbol name should not exceed 31 characters. Otherwise, CustomSymbolCreate() returns 'false' and the error 5302 – ERR\_CUSTOM\_SYMBOL\_NAME\_LONG is activated.

The symbol\_path parameter can be set in two ways:

- only a group name without a name of the custom symbol, for example – "CFD\\Metals". It is best to use this option to avoid errors.
- or <group> name + groups separator "\\"+<custom symbol name>, for example – "CFD\\Metals\\Platinum". In this case, the group name should end with the exact name of the custom symbol. In case of a mismatch, the custom symbol is still created, but not in the intended group. For example, if symbol\_path="CFD\\Metals\\Platinum" and symbol\_name="platinum" (register error), then a custom symbol named "platinum" is created in the "Custom\CFD\Metals\Platinum" group. The SymbolInfoGetString("platinum",SYMBOL\_PATH) function returns the "Custom\CFD\Metals\Platinum\platinum" value.

 

Note that the [SYMBOL\_PATH](../../Constants,-Enumerations-and-Structures/Environment-State/Symbol-Properties/Symbol-Properties.md#enum_symbol_info_string) property returns the path with the symbol name at the end. Therefore, it cannot be copied without changes if you want to create a custom symbol in the exact same group. In this case, it is necessary to cut the symbol name in order not to get the result described above.

If a non-existent symbol is set as the symbol\_origin parameter, then the custom symbol is created empty as if the symbol\_origin parameter is not set. The error 4301 – ERR\_MARKET\_UNKNOWN\_SYMBOL is activated in that case.

The symbol\_path parameter length should not exceed 127 characters considering "Custom\\", "\\" groups separators and the symbol name if it is specified at the end.

 

Example:

```cpp
//+------------------------------------------------------------------+
//|                                           CustomSymbolCreate.mq5 |
//|                                  Copyright 2024, MetaQuotes Ltd. |
//|                                             https://www.mql5.com |
//+------------------------------------------------------------------+
#property copyright "Copyright 2024, MetaQuotes Ltd."
#property link      "https://www.mql5.com"
#property version   "1.00"
#define   CUSTOM_SYMBOL_NAME     Symbol()+".C"  // custom symbol name
#define   CUSTOM_SYMBOL_PATH     "Forex"        // name of the group, in which a symbol is to be created
#define   CUSTOM_SYMBOL_ORIGIN   Symbol()       // name of a symbol a custom one is to be based on
//+------------------------------------------------------------------+
//| Script program start function                                    |
//+------------------------------------------------------------------+
void OnStart()
  {
//--- if failed to create a custom symbol, inform of that in the journal
   if(!CustomSymbolCreate(CUSTOM_SYMBOL_NAME, CUSTOM_SYMBOL_PATH, CUSTOM_SYMBOL_ORIGIN))
     {
      Print("CustomSymbolCreate() failed. Error ", GetLastError());
      return;
     }
//--- check the existence of the created symbol and get the group it was created in
   bool   custom= false;
   bool   exist = SymbolExist(CUSTOM_SYMBOL_NAME, custom);
   string path  = SymbolInfoString(CUSTOM_SYMBOL_NAME, SYMBOL_PATH);
//--- print the result of creating the symbol and the name of the group (specified and obtained from the symbol properties) in the journal
   PrintFormat("Custom symbol '%s' created\n"+
               "Symbol '%s' is exist: %s\n"+
               "Symbol '%s' is custom: %s\n"+
               "Path specified in the settings: '%s'\n"+
               "Path returned from the 'SYMBOL_PATH' property: '%s'",
               CUSTOM_SYMBOL_NAME,
               CUSTOM_SYMBOL_NAME, (string)exist,
               CUSTOM_SYMBOL_NAME, (string)custom,
               CUSTOM_SYMBOL_PATH,
               path);
//--- wait two seconds and delete the created symbol with the resulting message in the journal
   Sleep(2000);
   ResetLastError();
   bool deleted = CustomSymbolDelete(CUSTOM_SYMBOL_NAME);
   Print(deleted ? StringFormat("Custom symbol '%s' removed", CUSTOM_SYMBOL_NAME) : StringFormat("CustomSymbolDelete() failed. Error ",GetLastError()));
   /*
   result:
   Custom symbol 'EURUSD.C' created
   Symbol 'EURUSD.C' is exist: true
   Symbol 'EURUSD.C' is custom: true
   Path specified in the settings: 'Forex'
   Path returned from the 'SYMBOL_PATH' property: 'Custom\Forex\EURUSD.C'
   Custom symbol 'EURUSD.C' removed
   */
  }
```

 

See also

[SymbolName](../../Market-Info/SymbolName/SymbolName.md), [SymbolSelect](../../Market-Info/SymbolSelect/SymbolSelect.md), [CustomSymbolDelete](../CustomSymbolDelete/CustomSymbolDelete.md)