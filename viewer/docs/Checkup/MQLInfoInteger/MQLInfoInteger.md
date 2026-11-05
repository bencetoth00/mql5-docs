# MQLInfoInteger


Returns the value of a corresponding property of a running mql5 program.

```cpp
int  MQLInfoInteger(
   int  property_id      // identifier of a property
   );
```

Parameters

property\_id

[in] Identifier of a property. Can be one of values of the [ENUM\_MQL\_INFO\_INTEGER](../../Constants,-Enumerations-and-Structures/Environment-State/Running-MQL5-Program-Properties/Running-MQL5-Program-Properties.md#enum_mql_info_integer) enumeration.

Return Value

Value of int type.

Example:

```cpp
//+------------------------------------------------------------------+
//| Script program start function                                    |
//+------------------------------------------------------------------+
void OnStart()
  {
//--- get the values of available and consumed memory for the MQL program
   int limit = MQLInfoInteger(MQL_MEMORY_LIMIT);   // maximum possible amount of dynamic memory for MQL5 program in MB
   int used  = MQLInfoInteger(MQL_MEMORY_USED);    // memory size used by MQL5 program in MB
//--- send the received values to the journal
   PrintFormat("Maximum possible amount of dynamic memory for MQL5 program: %d Mb\n"+
               "Memory used by MQL5 program: %d Mb", limit, used);
   /*
   result
   Maximum possible amount of dynamic memory for MQL5 program: 8388608 Mb
   Memory used by MQL5 program: 2 Mb
   */
  }
```