# Uninitialization Reason Codes

Uninitialization Reason Codes

Uninitialization reason [codes](../../../index.md#expert) are returned by the [UninitializeReason()](../../../Checkup/UninitializeReason/UninitializeReason.md) function. The possible values are the following:

| Constant | Value | Description |
| --- | --- | --- |
| REASON\_PROGRAM | 0 | Expert Advisor terminated its operation by calling the [ExpertRemove()](../../../Common-Functions/ExpertRemove/ExpertRemove.md) function |
| REASON\_REMOVE | 1 | Program has been deleted from the chart |
| REASON\_RECOMPILE | 2 | Program has been recompiled |
| REASON\_CHARTCHANGE | 3 | Symbol or chart period has been changed |
| REASON\_CHARTCLOSE | 4 | Chart has been closed |
| REASON\_PARAMETERS | 5 | Input parameters have been changed by a user |
| REASON\_ACCOUNT | 6 | Another account has been activated or reconnection to the trade server has occurred due to changes in the account settings |
| REASON\_TEMPLATE | 7 | A new template has been applied |
| REASON\_INITFAILED | 8 | This value means that [OnInit()](../../../Event-Handling/OnInit/OnInit.md) handler has returned a nonzero value |
| REASON\_CLOSE | 9 | Terminal has been closed |

The uninitialization reason code is also passed as a parameter of the predetermined function [OnDeinit](../../../Event-Handling/OnDeinit/OnDeinit.md)(const int reason).

Example:

|  |
| --- |
| //+------------------------------------------------------------------+  //| get text description                                             |  //+------------------------------------------------------------------+  string getUninitReasonText(int reasonCode)    {     string text="";  //---     switch(reasonCode)       {        case REASON\_ACCOUNT:           text="Account was changed";break;        case REASON\_CHARTCHANGE:           text="Symbol or timeframe was changed";break;        case REASON\_CHARTCLOSE:           text="Chart was closed";break;        case REASON\_PARAMETERS:           text="Input-parameter was changed";break;        case REASON\_RECOMPILE:           text="Program "+\_\_FILE\_\_+" was recompiled";break;        case REASON\_REMOVE:           text="Program "+\_\_FILE\_\_+" was removed from chart";break;        case REASON\_TEMPLATE:           text="New template was applied to chart";break;        default:text="Another reason";       }  //---     return text;    }  //+------------------------------------------------------------------+  //| Expert deinitialization function                                 |  //+------------------------------------------------------------------+  void OnDeinit(const int reason)    {  //--- The first way to get the uninitialization reason code     Print(\_\_FUNCTION\_\_,"\_Uninitalization reason code = ",reason);  //--- The second way to get the uninitialization reason code     Print(\_\_FUNCTION\_\_,"\_UninitReason = ",getUninitReasonText(\_UninitReason));    } |
