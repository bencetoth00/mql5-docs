# IndicatorRelease

IndicatorRelease

The function removes an indicator handle and releases the calculation block of the indicator, if it's not used by anyone else.

|  |
| --- |
| bool  IndicatorRelease(     int       indicator\_handle     // indicator handle     ); |

Return Value

Returns true in case of success, otherwise returns false.

Note

The function allows removing an indicator handle, if it's no longer needed, thus saving memory. The handle is removed immediately, the calculation block is deleted in some time (if it's not called anymore).

When working in the [strategy tester](../../MQL5-programs/Testing-Trading-Strategies/Testing-Trading-Strategies.md#alert_etc), the IndicatorRelease() function is not executed.

Example:

|  |
| --- |
| //+------------------------------------------------------------------+  //|                                        Test\_IndicatorRelease.mq5 |  //|                        Copyright 2010, MetaQuotes Software Corp. |  //|                                             https://www.mql5.com |  //+------------------------------------------------------------------+  #property copyright "2010, MetaQuotes Software Corp."  #property link      "https://www.mql5.com"  #property version   "1.00"  //--- input parameters  input int                MA\_Period=15;  input int                MA\_shift=0;  input ENUM\_MA\_METHOD     MA\_smooth=MODE\_SMA;  input ENUM\_APPLIED\_PRICE price=PRICE\_CLOSE;  //--- will store indicator handle  int MA\_handle=INVALID\_HANDLE;  //+------------------------------------------------------------------+  //| Expert initialization function                                   |  //+------------------------------------------------------------------+  int OnInit()    {  //--- create indicator handle     MA\_handle=iMA(Symbol(),0,MA\_Period,MA\_shift,MA\_smooth,PRICE\_CLOSE);  //--- delete global variable     if(GlobalVariableCheck("MA\_value"))        GlobalVariableDel("MA\_value");  //---     return(INIT\_SUCCEEDED);    }  //+------------------------------------------------------------------+  //| Expert tick function                                             |  //+------------------------------------------------------------------+  void OnTick()    {  //--- if the global variable value does not exist     if(!GlobalVariableCheck("MA\_value"))       {        //--- obtain the indicator value in the last two bars        if(MA\_handle!=INVALID\_HANDLE)          {           //--- dynamic array for the indicator values           double values[];           if(CopyBuffer(MA\_handle,0,0,2,values)==2 && values[0]!=EMPTY\_VALUE)             {              //--- remember in the global variable value on the last but one bar              if(GlobalVariableSet("MA\_value",values[0]))                {                 //--- free the handle of the indicator                 if(!IndicatorRelease(MA\_handle))                    Print("IndicatorRelease() failed. Error ",GetLastError());                 else MA\_handle=INVALID\_HANDLE;                }              else                 Print("GlobalVariableSet failed. Error ",GetLastError());             }          }       }  //---    } |
