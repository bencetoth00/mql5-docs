# Running MQL5 Program Properties

Running MQL5 Program Properties

To obtain information about the currently running mql5 program, constants from ENUM\_MQL\_INFO\_INTEGER and ENUM\_MQL\_INFO\_STRING are used.

For function [MQLInfoInteger](../../../Checkup/MQLInfoInteger/MQLInfoInteger.md)

ENUM\_MQL\_INFO\_INTEGER

| Identifier | Description | Type |
| --- | --- | --- |
| MQL\_HANDLES\_USED | The current number of active object handles. These include both dynamic (created via [new](../../../Language-Basics/Data-Types/Object-Pointers/Object-Pointers.md)) and non-dynamic objects, global/local variables or class members. The more handles a program uses, the more resources it consumes. | int |
| MQL\_MEMORY\_LIMIT | Maximum possible amount of dynamic memory for MQL5 program in MB | int |
| MQL\_MEMORY\_USED | Memory used by MQL5 program in MB | int |
| MQL\_PROGRAM\_TYPE | Type of the MQL5 program | [ENUM\_PROGRAM\_TYPE](Running-MQL5-Program-Properties.md#enum_program_type) |
| MQL\_DLLS\_ALLOWED | The permission to use DLL for the given running program | bool |
| MQL\_TRADE\_ALLOWED | The [permission to trade](../../../MQL5-programs/Trade-Permission/Trade-Permission.md) for the given running program | bool |
| MQL\_SIGNALS\_ALLOWED | The permission to modify the Signals for the given running program | bool |
| MQL\_DEBUG | Indication that the program is running in the debugging mode | bool |
| MQL\_PROFILER | Indication that the program is running in the code profiling mode | bool |
| MQL\_TESTER | Indication that the program is running in the tester | bool |
| MQL\_FORWARD | Indication that the program is running in the forward testing process | bool |
| MQL\_OPTIMIZATION | Indication that the program is running in the optimization mode | bool |
| MQL\_VISUAL\_MODE | Indication that the program is running in the visual testing mode | bool |
| MQL\_FRAME\_MODE | Indication that the Expert Advisor is running in [gathering optimization result frames mode](../../../Event-Handling/OnTesterPass/OnTesterPass.md) | bool |
| MQL\_LICENSE\_TYPE | Type of license of the EX5 module. The license refers to the EX5 module, from which a request is made using MQLInfoInteger(MQL\_LICENSE\_TYPE). | [ENUM\_LICENSE\_TYPE](Running-MQL5-Program-Properties.md#enum_license_type) |
| MQL\_STARTED\_FROM\_CONFIG | Returns true if a script/EA is launched from the StartUp section of the [configuration file](https://www.metatrader5.com/en/terminal/help/start_advanced/start#configuration_file). This means that the script/EA had been specified in the configuration file the terminal was launched with. | bool |

For function [MQLInfoString](../../../Checkup/MQLInfoString/MQLInfoString.md)

ENUM\_MQL\_INFO\_STRING

| Identifier | Description | Type |
| --- | --- | --- |
| MQL\_PROGRAM\_NAME | Name of the running mql5-program | string |
| MQL5\_PROGRAM\_PATH | Path for the given running program | string |

 

For information about the type of the running program, values of ENUM\_PROGRAM\_TYPE are used.

ENUM\_PROGRAM\_TYPE

| Identifier | Description |
| --- | --- |
| PROGRAM\_SCRIPT | Script |
| PROGRAM\_EXPERT | Expert |
| PROGRAM\_INDICATOR | Indicator |
| PROGRAM\_SERVICE | Service |

 

ENUM\_LICENSE\_TYPE

| Identifier | Description |
| --- | --- |
| LICENSE\_FREE | A free unlimited version |
| LICENSE\_DEMO | A trial version of a paid product from the Market. It works only in the strategy tester |
| LICENSE\_FULL | A purchased licensed version allows at least 5 activations. The number of activations is specified by seller. Seller may increase the allowed number of activations |
| LICENSE\_TIME | A version with a limited term license |

Example:

|  |
| --- |
| ENUM\_PROGRAM\_TYPE mql\_program=(ENUM\_PROGRAM\_TYPE)MQLInfoInteger(MQL\_PROGRAM\_TYPE);     switch(mql\_program)       {        case PROGRAM\_SCRIPT:          {           Print(\_\_FILE\_\_+" is script");           break;          }        case PROGRAM\_EXPERT:          {           Print(\_\_FILE\_\_+" is Expert Advisor");           break;          }        case PROGRAM\_INDICATOR:          {           Print(\_\_FILE\_\_+" is custom indicator");           break;          }        default:Print("MQL5 type value is ",mql\_program);     //---     Print("MQLInfoInteger(MQL\_MEMORY\_LIMIT)=", MQLInfoInteger(MQL\_MEMORY\_LIMIT), " MB");     Print("MQLInfoInteger(MQL\_MEMORY\_USED)=", MQLInfoInteger(MQL\_MEMORY\_USED), " MB");     Print("MQLInfoInteger(MQL\_HANDLES\_USED)=", MQLInfoInteger(MQL\_HANDLES\_USED), " handles"); |
