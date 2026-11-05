# OnDeinit

OnDeinit

The function is called in indicators and EAs when the [Deinit](../../MQL5-programs/Client-Terminal-Events/Client-Terminal-Events.md#deinit) event occurs. It is used to deinitialize a running MQL5 program.

|  |
| --- |
| void  OnDeinit(     const int  reason         // deinitialization reason code     ); |

Parameters

reason

[in]  Deinitialization reason code.

Return Value

No return value

Note

Deinit event is generated for EAs and indicators in the following cases:

- before a re-initialization due to the change of a symbol or a chart period the mql5 program is attached to;
- before a re-initialization due to the change of the [inputs](../../Language-Basics/Variables/Input-Variables/Input-Variables.md);
- before unloading an mql5 program.

The reason parameter may have the following values:

| Constant | Value | Description |
| --- | --- | --- |
| REASON\_PROGRAM | 0 | The EA has stopped working calling the [ExpertRemove()](../../Common-Functions/ExpertRemove/ExpertRemove.md) function |
| REASON\_REMOVE | 1 | Program removed from a chart |
| REASON\_RECOMPILE | 2 | Program recompiled |
| REASON\_CHARTCHANGE | 3 | A symbol or a chart period is changed |
| REASON\_CHARTCLOSE | 4 | Chart closed |
| REASON\_PARAMETERS | 5 | Inputs changed by a user |
| REASON\_ACCOUNT | 6 | Another account has been activated or reconnection to the trade server has occurred due to changes in the account settings |
| REASON\_TEMPLATE | 7 | Another chart template applied |
| REASON\_INITFAILED | 8 | The [OnInit()](../OnInit/OnInit.md) handler returned a non-zero value |
| REASON\_CLOSE | 9 | Terminal closed |

[EA](../../index.md#expert) deinitialization reason codes can be received by the [UninitializeReason()](../../Checkup/UninitializeReason/UninitializeReason.md) function or from the predefined [\_UninitReason](../../Predefined-Variables/_UninitReason/_UninitReason.md) variable.

Sample OnInit() and OnDeinit() functions for the EA

|  |
| --- |
| input int fake\_parameter=3;      // useless parameter  //+------------------------------------------------------------------+  //| Expert initialization function                                   |  //+------------------------------------------------------------------+  int OnInit()    {  //--- Get the number of a build where the program is compiled     Print(\_\_FUNCTION\_\_," Build #",\_\_MQLBUILD\_\_);  //--- Reset reason code can also be obtained in OnInit()     Print(\_\_FUNCTION\_\_," Deinitialization reason code can be received during the EA reset");  //--- The first way to get a deinitialization reason code     Print(\_\_FUNCTION\_\_," \_UninitReason = ",getUninitReasonText(\_UninitReason));  //--- The second way to get a deinitialization reason code       Print(\_\_FUNCTION\_\_," UninitializeReason() = ",getUninitReasonText(UninitializeReason()));  //---     return(INIT\_SUCCEEDED);    }  //+------------------------------------------------------------------+  //| Expert deinitialization function                                 |  //+------------------------------------------------------------------+  void OnDeinit(const int reason)    {  //--- The first way to get a deinitialization reason code     Print(\_\_FUNCTION\_\_," Deinitialization reason code = ",reason);  //--- The second way to get a deinitialization reason code     Print(\_\_FUNCTION\_\_," \_UninitReason = ",getUninitReasonText(\_UninitReason));  //--- The third way to get a deinitialization reason code       Print(\_\_FUNCTION\_\_," UninitializeReason() = ",getUninitReasonText(UninitializeReason()));    }  //+------------------------------------------------------------------+  //| Return a textual description of the deinitialization reason code |  //+------------------------------------------------------------------+  string getUninitReasonText(int reasonCode)    {     string text="";  //---     switch(reasonCode)       {        case REASON\_ACCOUNT:           text="Account was changed";break;        case REASON\_CHARTCHANGE:           text="Symbol or timeframe was changed";break;        case REASON\_CHARTCLOSE:           text="Chart was closed";break;        case REASON\_PARAMETERS:           text="Input-parameter was changed";break;        case REASON\_RECOMPILE:           text="Program "+\_\_FILE\_\_+" was recompiled";break;        case REASON\_REMOVE:           text="Program "+\_\_FILE\_\_+" was removed from chart";break;        case REASON\_TEMPLATE:           text="New template was applied to chart";break;        default:text="Another reason";       }  //---     return text;    } |

See also

[OnInit](../OnInit/OnInit.md), [Event handling functions](../../Language-Basics/Functions/Event-Handling-Functions/Event-Handling-Functions.md), [Program running](../../MQL5-programs/Program-Running/Program-Running.md), [Client terminal events](../../MQL5-programs/Client-Terminal-Events/Client-Terminal-Events.md), [Uninitialization reason codes](../../Constants,-Enumerations-and-Structures/Named-Constants/Uninitialization-Reason-Codes/Uninitialization-Reason-Codes.md), [Visibility scope and lifetime of variables](../../Language-Basics/Variables/Visibility-Scope-and-Lifetime-of-Variables/Visibility-Scope-and-Lifetime-of-Variables.md), [Creating and deleting objects](../../Language-Basics/Variables/Creating-and-Deleting-Objects/Creating-and-Deleting-Objects.md)
