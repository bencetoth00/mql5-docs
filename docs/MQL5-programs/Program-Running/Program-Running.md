# Program Running

Program Running

Each script, each service and each Expert Advisor runs in its own separate thread. All indicators calculated on one symbol, even if they are attached to different charts, work in the same thread. Thus, all indicators on one symbol share the resources of one thread.

All other actions associated with a symbol, like processing of ticks and history synchronization, are also consistently performed in the same thread with indicators. This means that if an infinite action is performed in an indicator, all other events associated with its symbol will never be performed.

When running an Expert Advisor, make sure that it has an actual [trading environment](../../Market-Info/Market-Info.md) and can [access the history](../../Timeseries-and-Indicators-Access/Organizing-Data-Access/Organizing-Data-Access.md) of the required symbol and period, and [synchronize](../../Timeseries-and-Indicators-Access/Organizing-Data-Access/Organizing-Data-Access.md#synchronized) data between the terminal and the server. For all these procedures, the terminal provides a start delay of no more than 5 seconds, after which the Expert Advisor will be started with available data. Therefore, in case there is no connection to the server, this may lead to a delay in the start of an Expert Advisor.

The below table contains a brief summary of MQL5 programs:

| Program | Running | Note |
| --- | --- | --- |
| Service | A separate thread, the number of threads for services is equal to the number of services | A looped service cannot break running of other programs |
| Script | A separate thread, the number of threads for scripts is equal to the number of scripts | A looped script cannot break running of other programs |
| Expert Advisor | A separate thread, the number of threads for Expert Advisors is equal to the number of Expert Advisors | A looped Expert Advisor cannot break running of other programs |
| Indicator | One thread for all indicators on a symbol. The number of threads is equal to the number of symbols with indicators | An infinite loop in one indicator will stop all other indicators on this symbol |

Right after a program is attached to a chart, it is uploaded to the client terminal memory, as well as global variable are [initialized](../../Language-Basics/Variables/Initialization-of-Variables/Initialization-of-Variables.md). If some global variable of the class type has a [constructor](../../Language-Basics/Data-Types/Structures,-Classes-and-Interfaces/Structures,-Classes-and-Interfaces.md#constructor), this constructor will be called during initialization of [global variables](../../Language-Basics/Variables/Global-Variables/Global-Variables.md).

After that the program is waiting for an [event](../Client-Terminal-Events/Client-Terminal-Events.md) from the client terminal. Each mql5-program should have at least one [event-handler](../../Language-Basics/Functions/Event-Handling-Functions/Event-Handling-Functions.md), otherwise the loaded program will not be executed. Event handlers have  predefined names, parameters and return types.

| Type | Function name | Parameters | Application | Comment |
| --- | --- | --- | --- | --- |
| int | [OnInit](../../Event-Handling/OnInit/OnInit.md) | none | Expert Advisors and indicators | [Init](../Client-Terminal-Events/Client-Terminal-Events.md#init) event handler. It allows to use the void return type. |
| void | [OnDeinit](../../Event-Handling/OnDeinit/OnDeinit.md) | const int reason | Expert Advisors and indicators | [Deinit](../Client-Terminal-Events/Client-Terminal-Events.md#deinit) event handler. |
| void | [OnStart](../../Event-Handling/OnStart/OnStart.md) | none | scripts and services | [Start](../Client-Terminal-Events/Client-Terminal-Events.md#start) event handler. |
| int | [OnCalculate](../../Language-Basics/Functions/Event-Handling-Functions/Event-Handling-Functions.md#oncalculate2) | const int rates\_total,  const int prev\_calculated,  const datetime &Time[],  const double &Open[],  const double &High[],  const double &Low[],  const double &Close[],  const long &TickVolume[],  const long &Volume[],  const int &Spread[] | indicators | Calculate event handler for all prices. |
| int | [OnCalculate](../../Event-Handling/OnCalculate/OnCalculate.md) | const int rates\_total,  const int prev\_calculated,  const int begin,  const double &price[] | indicators | [Calculate](../Client-Terminal-Events/Client-Terminal-Events.md#calculate) event handler on the single data array.  Indicator cannot have two event handlers simultaneously.  In this case the only one event handler will work on the data array. |
| void | [OnTick](../../Event-Handling/OnTick/OnTick.md) | none | Expert Advisors | [NewTick](../Client-Terminal-Events/Client-Terminal-Events.md#newtick) event handler. While the event of a new tick receipt is being processed, no other events of this type are received. |
| void | [OnTimer](../../Event-Handling/OnTimer/OnTimer.md) | none | Expert Advisors and indicators | [Timer](../Client-Terminal-Events/Client-Terminal-Events.md#timer) event handler. |
| void | [OnTrade](../../Event-Handling/OnTrade/OnTrade.md) | none | Expert Advisors | [Trade](../Client-Terminal-Events/Client-Terminal-Events.md#trade) event handler. |
| double | [OnTester](../../Event-Handling/OnTester/OnTester.md) | none | Expert Advisors | [Tester](../Client-Terminal-Events/Client-Terminal-Events.md#tester) event handler. |
| void | [OnChartEvent](../../Event-Handling/OnChartEvent/OnChartEvent.md) | const int id,  const long &lparam,  const double &dparam,  const string &sparam | Expert Advisors and indicators | [ChartEvent](../Client-Terminal-Events/Client-Terminal-Events.md#chartevent) event handler. |
| void | [OnBookEvent](../../Event-Handling/OnBookEvent/OnBookEvent.md) | const string &symbol\_name | Expert Advisors and indicators | [BookEvent](../Client-Terminal-Events/Client-Terminal-Events.md#bookevent) event handler. |

A client terminal sends new events to the corresponding open charts. Events can also be generated by charts ([chart events](../../Event-Handling/OnChartEvent/OnChartEvent.md)) or mql5-programs ([custom events](../../Working-with-Events/EventChartCustom/EventChartCustom.md)). Generation of events of creation or deletion of graphical objects on a chart can be enabled or disabled by setting [CHART\_EVENT\_OBJECT\_CREATE](../../Constants,-Enumerations-and-Structures/Chart-Constants/Chart-Properties/Chart-Properties.md#enum_chart_property_integer) and [CHART\_EVENT\_OBJECT\_DELETE](../../Constants,-Enumerations-and-Structures/Chart-Constants/Chart-Properties/Chart-Properties.md#enum_chart_property_integer) chart properties. Each MQL5 program and each chart has its own queue of events, where all new incoming events are added.

A program receives only events from the chart it runs on. All events are processed one after another in the order they are received. If a queue already has a [NewTick](../Client-Terminal-Events/Client-Terminal-Events.md#newtick) event, or this event is currently being processed, then the new NewTick event is not placed in the queue of the MQL5 program. Similarly, if [ChartEvent](../Client-Terminal-Events/Client-Terminal-Events.md#chartevent) is already enqueued, or this event is being processed, no new event of this kind is enqueued. The timer events are handled the same way – if the [Timer](../Client-Terminal-Events/Client-Terminal-Events.md#timer) event is in the queue or being handled, the new timer event is not enqueued.

Event queues have a limited but sufficient size, so that the queue overflow for well written programs is unlikely. In case of queue overflow, new events are discarded without queuing.

It is strongly recommended not to use infinite loops to handle events. Possible exceptions are scripts and services handling a single [Start](../Client-Terminal-Events/Client-Terminal-Events.md#start) event.

[Libraries](../../index.md#library) do not handle any events.

 

Functions prohibited in Indicators and Expert Advisors

Indicators, scripts and Expert Advisors are executable programs written in MQL5. They are designed for different types of tasks. Therefore there are some restrictions on the use of certain functions, depending on the [type of program](../../Constants,-Enumerations-and-Structures/Environment-State/Running-MQL5-Program-Properties/Running-MQL5-Program-Properties.md#enum_program_type). The following functions are prohibited in indicators:

- [OrderCalcMargin()](../../Trade-Functions/OrderCalcMargin/OrderCalcMargin.md);
- [OrderCalcProfit()](../../Trade-Functions/OrderCalcProfit/OrderCalcProfit.md);
- [OrderCheck()](../../Trade-Functions/OrderCheck/OrderCheck.md);
- [OrderSend()](../../Trade-Functions/OrderSend/OrderSend.md);
- [SendFTP()](../../Network-Functions/SendFTP/SendFTP.md);
- [Sleep()](../../Common-Functions/Sleep/Sleep.md);
- [ExpertRemove()](../../Common-Functions/ExpertRemove/ExpertRemove.md);
- [MessageBox()](../../Common-Functions/MessageBox/MessageBox.md).

 

All functions designed for indicators are prohibited in Expert Advisors and scripts:

- [SetIndexBuffer()](../../Custom-Indicators/SetIndexBuffer/SetIndexBuffer.md);
- [IndicatorSetDouble()](../../Custom-Indicators/IndicatorSetDouble/IndicatorSetDouble.md);
- [IndicatorSetInteger()](../../Custom-Indicators/IndicatorSetInteger/IndicatorSetInteger.md);
- [IndicatorSetString()](../../Custom-Indicators/IndicatorSetString/IndicatorSetString.md);
- [PlotIndexSetDouble()](../../Custom-Indicators/PlotIndexSetDouble/PlotIndexSetDouble.md);
- [PlotIndexSetInteger()](../../Custom-Indicators/PlotIndexSetInteger/PlotIndexSetInteger.md);
- [PlotIndexSetString()](../../Custom-Indicators/PlotIndexSetString/PlotIndexSetString.md);
- [PlotIndexGetInteger](../../Custom-Indicators/PlotIndexGetInteger/PlotIndexGetInteger.md).

The library is not an independent program and is executed in the context of the MQL5 program that has called it: script, indicator or Expert Advisor. Accordingly, the above restrictions apply to the called library.

 

Functions prohibited in services

Services do not accept any events, as they are not bound to a chart.  The following functions are prohibited in services:

[ExpertRemove()](../../Common-Functions/ExpertRemove/ExpertRemove.md);

[EventSetMillisecondTimer()](../../Working-with-Events/EventSetMillisecondTimer/EventSetMillisecondTimer.md);

[EventSetTimer()](../../Working-with-Events/EventSetTimer/EventSetTimer.md);

[EventKillTimer()](../../Working-with-Events/EventKillTimer/EventKillTimer.md);

[SetIndexBuffer()](../../Custom-Indicators/SetIndexBuffer/SetIndexBuffer.md);

[IndicatorSetDouble()](../../Custom-Indicators/IndicatorSetDouble/IndicatorSetDouble.md);

[IndicatorSetInteger()](../../Custom-Indicators/IndicatorSetInteger/IndicatorSetInteger.md);

[IndicatorSetString()](../../Custom-Indicators/IndicatorSetString/IndicatorSetString.md);

[PlotIndexSetDouble()](../../Custom-Indicators/PlotIndexSetDouble/PlotIndexSetDouble.md);

[PlotIndexSetInteger()](../../Custom-Indicators/PlotIndexSetInteger/PlotIndexSetInteger.md);

[PlotIndexSetString()](../../Custom-Indicators/PlotIndexSetString/PlotIndexSetString.md);

[PlotIndexGetInteger()](../../Custom-Indicators/PlotIndexGetInteger/PlotIndexGetInteger.md);

 

Loading and Unloading of Indicators

Indicators are loaded in the following cases:

- an indicator is attached to a chart;
- terminal start (if the indicator was attached to the chart prior to the shutdown of the terminal);
- loading of a template (if the indicator attached to a chart is specified in the template);
- change of a profile (if the indicator is attached to one of the profile charts);
- change of a symbol and/or timeframe of a chart, to which the indicator is attached;

- change of the account to which the terminal is connected;

- after the successful recompilation of an indicator (if the indicator was attached to a chart);
- change of [input parameters](../../Language-Basics/Variables/Input-Variables/Input-Variables.md) of the indicator.

 

Indicators are unloaded in the following cases:

- when detaching an indicator from a chart;
- terminal shutdown (if the indicator was attached to a chart);
- loading of a template (if an indicator is attached to a chart);
- closing of a chart, to which the indicator was attached;
- change of a profile (if the indicator is attached to one of charts of the changed profile);
- change of a symbol and/or timeframe of a chart, to which the indicator is attached;
- change of the account to which the terminal is connected;

- change of [input parameters](../../Language-Basics/Variables/Input-Variables/Input-Variables.md) of the indicator.

 

Loading and Unloading of Expert Advisors

Expert Advisors are loaded in the following cases:

- when attaching an Expert Advisor to a chart;
- terminal start (if the Expert Advisor was attached to the chart prior to the shutdown of the terminal);
- loading of a template (if the Expert Advisor attached to the chart is specified in the template);
- change of a profile (if the Expert Advisor is attached to the one of the profile charts);
- connection to an account, even if the account number is the same (if the Expert Advisor was attached to the chart before the authorization of the terminal on the server).

Expert Advisors are unloaded in the following cases:

- when detaching an Expert Advisor from a chart;
- if a new Expert Advisor is attached to a chart, if another Expert Advisor has been attached already, this Expert Advisor is unloaded.
- terminal shutdown (if the Expert Advisor was attached to a chart);
- loading of a template (if an Expert Advisor is attached to the chart);
- close of a chart, to which the Expert Advisor is attached.
- change of a profile (if the Expert Advisor is attached to one of charts of the changed profile);

- change of the account to which the terminal is connected (if the Expert Advisor was attached to the chart before the authorization of the terminal on the server);

- calling the [ExpertRemove()](../../Common-Functions/ExpertRemove/ExpertRemove.md) function.

In case the symbol or timeframe of a chart, to which the Expert Advisor is attached, changes, Expert Advisors are not loaded or unloaded. In this case client terminal subsequently calls [OnDeinit()](../../Event-Handling/OnDeinit/OnDeinit.md) handlers on the old symbol/timeframe and [OnInit()](../../Event-Handling/OnInit/OnInit.md) on the new symbol/timeframe (if they are such), values of global variables and [static variables](../../Language-Basics/Variables/Static-Variables/Static-Variables.md) are not reset. All events, which have been received for the Expert Advisor before the initialization is completed ([OnInit()](../../Event-Handling/OnInit/OnInit.md) function) are skipped.

 

Loading and Unloading of Scripts

Scripts are loaded immediately after they are attached to a chart and unloaded immediately after they complete their operation. OnInit() and OnDeinit() are not called for scripts.

When a program is unloaded (deleted from a chart) the client terminal performs deinitialization of [global](../../Language-Basics/Variables/Global-Variables/Global-Variables.md) variables and deletes the events queue. In this case deinitialization means reset of all the [string-](../../Language-Basics/Data-Types/String-Type/String-Type.md)type variables, deallocation of [dynamical array objects](../../Language-Basics/Data-Types/Dynamic-Array-Object/Dynamic-Array-Object.md) and call of their [destructors](../../Language-Basics/Data-Types/Structures,-Classes-and-Interfaces/Structures,-Classes-and-Interfaces.md#destructor) if they are available.

 

Loading and Unloading services

Services are loaded right after starting the terminal if they were launched at the moment of the terminal shutdown. Services are unloaded immediately after completing their work.

Services have a single OnStart() handler, in which you can implement an endless data receiving and handling loop, for example creating and updating custom symbols using the network functions.

Unlike Expert Advisors, indicators and scripts, services are not bound to a specific chart, therefore a separate mechanism is provided to launch them.  A new service instance is created in the Navigator using the "Add Service" command. A service instance can be launched, stopped and removed using the appropriate instance menu. To manage all instances, use the service menu.

 

For a better understanding of the Expert Advisor operation we recommend to compile the code of the following Expert Advisor and perform actions of load/unload, template change, symbol change, timeframe change etc:

Example:

|  |
| --- |
| //+------------------------------------------------------------------+  //|                                                   TestExpert.mq5 |  //|                        Copyright 2009, MetaQuotes Software Corp. |  //|                                              https://www.mql5.com |  //+------------------------------------------------------------------+  #property copyright "2009, MetaQuotes Software Corp."  #property link      "https://www.mql5.com"  #property version   "1.00"     class CTestClass    {  public:       CTestClass() { Print("CTestClass constructor"); }     ~CTestClass() { Print("CTestClass destructor"); }    };  CTestClass global;  //+------------------------------------------------------------------+  //| Expert initialization function                                   |  //+------------------------------------------------------------------+  int OnInit()    {  //---     Print("Initialization");  //---     return(INIT\_SUCCEEDED);    }  //+------------------------------------------------------------------+  //| Expert deinitialization function                                 |  //+------------------------------------------------------------------+  void OnDeinit(const int reason)    {  //---     Print("Deinitialization with reason",reason);    }  //+------------------------------------------------------------------+  //| Expert tick function                                             |  //+------------------------------------------------------------------+  void OnTick()    {  //---       }  //+------------------------------------------------------------------+ |

See also

[Client terminal events](../Client-Terminal-Events/Client-Terminal-Events.md), [Event handlers](../../Language-Basics/Functions/Event-Handling-Functions/Event-Handling-Functions.md)
