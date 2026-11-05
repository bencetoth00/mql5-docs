# OnInit

OnInit

The function is called in indicators and EAs when the [Init](../../MQL5-programs/Client-Terminal-Events/Client-Terminal-Events.md#init) event occurs. It is used to initialize a running MQL5 program. There are two function types.

The version that returns the result

|  |
| --- |
| int  OnInit(void); |

Return Value

[int](../../Language-Basics/Data-Types/Integer-Types/Char,-Short,-Int-and-Long-Types/Char,-Short,-Int-and-Long-Types.md) type value, zero means successful initialization.

When returning [INIT\_FAILED](../../Language-Basics/Functions/Event-Handling-Functions/Event-Handling-Functions.md), the EA is forcibly unloaded from the chart.

When returning [INIT\_FAILED](../../Language-Basics/Functions/Event-Handling-Functions/Event-Handling-Functions.md), the indicator is not unloaded from the chart. The indicator remaining on the chart is non-operational — [event handlers](../Event-Handling.md) are not called in the indicator.

The OnInit() call that returns the execution result is recommended for use since it not only allows for program initialization, but also returns an error code in case of an early program termination.

The version without a result return is left only for compatibility with old codes. It is not recommended for use

|  |
| --- |
| void  OnInit(void); |

Note

The Init event is generated immediately after loading an EA or an indicator. The event is not generated for scripts. The OnInit() function is used to initialize an MQL5 program. If OnInit() has a return value of [int](../../Language-Basics/Data-Types/Integer-Types/Char,-Short,-Int-and-Long-Types/Char,-Short,-Int-and-Long-Types.md#int) type, the non-zero return code means failed initialization and generates the [Deinit](../../MQL5-programs/Client-Terminal-Events/Client-Terminal-Events.md#deinit) event with the [REASON\_INITFAILED](../../Constants,-Enumerations-and-Structures/Named-Constants/Uninitialization-Reason-Codes/Uninitialization-Reason-Codes.md#reason_initfailed) deinitialization reason code.

OnInit() function of void type always means successful initialization and is not recommended for use.

For [optimizing](../../MQL5-programs/Testing-Trading-Strategies/Testing-Trading-Strategies.md) the EA [inputs](../../Language-Basics/Variables/Input-Variables/Input-Variables.md), it is recommended to use values from the [ENUM\_INIT\_RETCODE](https://www.mql5.com/ru/docs/basis/function/events#enum_init_retcode) enumeration as a return code. These values are intended for establishing the optimization process management, including selection of the most suitable [test agents](https://www.mql5.com/ru/docs/runtime/testing#agents). It is possible to request data on agent configuration and resources (number of cores, free memory amount, etc.) using the [TerminalInfoInteger()](https://www.mql5.com/ru/docs/check/terminalinfointeger) function during the EA initialization before launching the test. Based on the obtained data, you can either allow using the test agent or ban it from optimizing the EA.

| ID | Description |
| --- | --- |
| INIT\_SUCCEEDED | Initialization successful, EA test can be continued.  This code means the same as the zero value – the EA initialization in the tester is successful. |
| INIT\_FAILED | Initialization failed. There is no point in continuing the test due to unavoidable errors. For example, it is impossible to create an indicator necessary for the EA operation.  The return of this value means the same as returning the value different from zero – EA initialization in the tester failed. |
| INIT\_PARAMETERS\_INCORRECT | Designed to denote an incorrect set of input parameters by a programmer. In the general optimization table, the result string with this return code is highlighted in red.  A test for such a set of EA inputs is not performed. The agent is ready to receive a new task.  When this value is received, the strategy tester does not pass this task to other agents for repeated execution. |
| INIT\_AGENT\_NOT\_SUITABLE | No program execution errors during initialization. However, for some reasons, the agent is not suitable for conducting a test. For example, there is not enough RAM, no [OpenCL support](../../Working-with-OpenCL/Working-with-OpenCL.md), etc.  After returning this code, the agent no longer receives tasks until the very end of [this optimization](../../MQL5-programs/Testing-Trading-Strategies/Testing-Trading-Strategies.md). |

Using [OnInit()](OnInit.md) returning INIT\_FAILED/INIT\_PARAMETERS\_INCORRECT in the tester have some peculiarities that should be considered when optimizing EAs:

- the set of parameters the OnInit() returned INIT\_PARAMETERS\_INCORRECT for is considered unsuitable for testing and is not used to obtain the next population during [genetic optimization](https://www.metatrader5.com/en/terminal/help/algotrading/optimization_types). Too many "discarded" parameter sets may lead to incorrect results when searching for optimal EA parameters. The search algorithm assumes that the [optimization criterion](https://www.metatrader5.com/en/terminal/help/algotrading/optimization_types#criterion) function is smooth and has no gaps on the entire multitude of input parameters.
- if OnInit() returns INIT\_FAILED, this means that a test cannot be launched, and the EA is unloaded from the agent's memory. The EA is loaded again to perform the next pass with a new set of parameters. Launching the next optimization pass takes much more time as compared to calling TesterStop().

Sample OnInit() function for an EA

|  |
| --- |
| //--- input parameters  input int      ma\_period=20; // moving average period     //--- handle of the indicator used in the EA  int indicator\_handle;     //+------------------------------------------------------------------+  //| Expert initialization function                                   |  //+------------------------------------------------------------------+  int OnInit()    {  //--- check ma\_period validity     if(ma\_period<=0)       {        PrintFormat("Invalid ma\_period input value: %d",ma\_period);        return (INIT\_PARAMETERS\_INCORRECT);       }  //--- during optimization     if(MQLInfoInteger(MQL\_OPTIMIZATION))       {        //--- check available RAM for the agent        int available\_memory\_mb=TerminalInfoInteger(TERMINAL\_MEMORY\_TOTAL);        if(available\_memory\_mb<2000)          {           PrintFormat("Insufficient memory for the test agent: %d MB",                       available\_memory\_mb);           return (INIT\_AGENT\_NOT\_SUITABLE);          }       }  //--- check for the indicator     indicator\_handle=iCustom(\_Symbol,\_Period,"My\_Indicator",ma\_period);     if(indicator\_handle==INVALID\_HANDLE)       {        PrintFormat("Failed to generate My\_Indicator handle. Error code %d",                    GetLastError());        return (INIT\_FAILED);       }  //--- EA initialization successful     return(INIT\_SUCCEEDED);    } |

See also

[OnDeinit](../OnDeinit/OnDeinit.md), [Event handling functions](../../Language-Basics/Functions/Event-Handling-Functions/Event-Handling-Functions.md), [Program running](../../MQL5-programs/Program-Running/Program-Running.md), [Client terminal events](../../MQL5-programs/Client-Terminal-Events/Client-Terminal-Events.md), [Initialization of variables](../../Language-Basics/Variables/Initialization-of-Variables/Initialization-of-Variables.md), [Creating and deleting objects](../../Language-Basics/Variables/Creating-and-Deleting-Objects/Creating-and-Deleting-Objects.md)
