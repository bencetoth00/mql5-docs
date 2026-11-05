# TerminalClose

TerminalClose

The function commands the terminal to complete operation.

|  |
| --- |
| bool  TerminalClose(     int ret\_code      // closing code of the client terminal     ); |

Parameters

ret\_code

[in]  Return code, returned by the process of the client terminal at the operation completion.

Return Value

The function returns true on success, otherwise  - false.

Note

The TerminalClose() function does not stop the terminal immediately, it just commands the terminal to complete its operation.

The code of an Expert Advisor that called TerminalClose() must have all arrangements for the immediate completion (e.g. all previously opened files must be closed in the normal mode). Call of this function must be followed by the [return operator](../../Language-Basics/Operators/Return-Operator/Return-Operator.md).

The ret\_code parameter allows indicating the necessary return code for analyzing reasons of the program termination of the terminal operation when starting it from the command prompt.

Example:

|  |
| --- |
| //--- input parameters  input int  tiks\_before=500; // number of ticks till termination  input int  pips\_to\_go=15;   // distance in pips   input int  seconds\_st=50;   // number of seconds given to the Expert Advisor  //--- globals  datetime   launch\_time;  int        tick\_counter=0;  //+------------------------------------------------------------------+  //| Expert deinitialization function                                 |  //+------------------------------------------------------------------+  void OnDeinit(const int reason)    {  //---     Print(\_\_FUNCTION\_\_," reason code = ",reason);     Comment("");    }  //+------------------------------------------------------------------+  //| Expert tick function                                             |  //+------------------------------------------------------------------+  void OnTick()    {     static double first\_bid=0.0;     MqlTick       tick;     double        distance;  //---     SymbolInfoTick(\_Symbol,tick);     tick\_counter++;     if(first\_bid==0.0)       {        launch\_time=tick.time;        first\_bid=tick.bid;        Print("first\_bid =",first\_bid);        return;       }  //--- price distance in pips     distance=(tick.bid-first\_bid)/\_Point;  //--- show a notification to track the EA operation     string comm="From the moment of start:\r\n\x25CF elapsed seconds: "+                 IntegerToString(tick.time-launch\_time)+" ;"+                 "\r\n\x25CF ticks received: "+(string)tick\_counter+" ;"+                 "\r\n\x25CF price went in points: "+StringFormat("%G",distance);     Comment(comm);  //--- section for checking condition to close the terminal     if(tick\_counter>=tiks\_before)        TerminalClose(0);    // exit by tick counter     if(distance>pips\_to\_go)        TerminalClose(1);    // go up by the number of pips equal to pips\_to\_go     if(distance<-pips\_to\_go)        TerminalClose(-1);   // go down by the number of pips equal to pips\_to\_go     if(tick.time-launch\_time>seconds\_st)        TerminalClose(100);  // termination by timeout  //---    } |

See also

[Program running](../../MQL5-programs/Program-Running/Program-Running.md), [Execution errors](../../MQL5-programs/Runtime-Errors/Runtime-Errors.md), [Reasons for deinitialization](../../Constants,-Enumerations-and-Structures/Named-Constants/Uninitialization-Reason-Codes/Uninitialization-Reason-Codes.md)
