# TimeToString

TimeToString

Converting a value containing time in seconds elapsed since 01.01.1970 into a string of "yyyy.mm.dd hh:mi" format.

|  |
| --- |
| string  TimeToString(     datetime  value,                           // number     int       mode=TIME\_DATE|TIME\_MINUTES      // output format     ); |

Parameters

value

[in]  Time in seconds from 00:00 1970/01/01.

mode=TIME\_DATE|TIME\_MINUTES

[in] Additional data input mode. Can be one or combined flag:   
TIME\_DATE gets result as "yyyy.mm.dd",   
TIME\_MINUTES gets result as "hh:mi",   
TIME\_SECONDS gets results as "hh:mi:ss".

Return Value

String.

 

Example:

|  |
| --- |
| datetime ExtBarTimeOpen;     //+------------------------------------------------------------------+  //| Custom indicator initialization function                         |  //+------------------------------------------------------------------+  int OnInit()    {  //--- set the timer to one second     EventSetTimer(1);  //---     return(INIT\_SUCCEEDED);    }  //+------------------------------------------------------------------+  //| Custom indicator deinitialization function                       |  //+------------------------------------------------------------------+  void OnDeinit(const int reason)    {     Comment("");    }  //+------------------------------------------------------------------+  //| Custom indicator iteration function                              |  //+------------------------------------------------------------------+  int OnCalculate(const int rates\_total,                  const int prev\_calculated,                  const datetime &time[],                  const double &open[],                  const double &high[],                  const double &low[],                  const double &close[],                  const long &tick\_volume[],                  const long &volume[],                  const int &spread[])    {  //--- get the current bar opening time     ExtBarTimeOpen=time[rates\_total-1];  //--- return value of prev\_calculated for next call     return(rates\_total);    }  //+------------------------------------------------------------------+  //| Timer function                                                   |  //+------------------------------------------------------------------+  void OnTimer()    {  //--- set the previous bar opening time     static datetime bar\_open\_time=ExtBarTimeOpen;  //--- count the number of seconds passed since the bar opened     static int seconds=int(TimeCurrent()-ExtBarTimeOpen);  //--- if the previous opening time is not equal to the current one, then this is a new bar  //--- write the new opening time as the previous one and set the seconds to zero     if(bar\_open\_time!=ExtBarTimeOpen)       {        bar\_open\_time=ExtBarTimeOpen;        seconds=0;       }  //--- increase and adjust the number of seconds passed since the bar opened     seconds++;     if(seconds>PeriodSeconds(PERIOD\_CURRENT))        seconds=0;  //--- bar opening time as yyyy.mm.dd hh:mi     string bar\_time\_open=TimeToString(ExtBarTimeOpen);  //--- current time as yyyy.mm.dd hh:mi:ss     string time\_current=TimeToString(TimeCurrent(),TIME\_DATE|TIME\_MINUTES|TIME\_SECONDS);  //--- number of seconds left until a new bar opens     int    sec\_left=PeriodSeconds(PERIOD\_CURRENT)-seconds;  //--- amount of time remaining until the current bar closes as hh:mm:ss     string time\_left=TimeToString(sec\_left,TIME\_MINUTES|TIME\_SECONDS);  //--- create the output string     string txt=StringFormat("Opening time of the current bar: %s\n"+                             "Time Current: %s\n"+                             "Seconds have passed since the bar opened: %d\n"+                             "Approximately seconds left before bar closes: %d\n"+                             "Time remaining until bar closes: %s",bar\_time\_open,time\_current,seconds,sec\_left,time\_left);  //--- display the bar open time and the current time,  //--- the number of seconds passed since the current bar opened and remaining until it closes and  //--- the time remaining until the current bar closes in the comment     Comment(txt);     /\*     result on M1:     Opening time of the current bar: 2024.02.22 18:06     Time Current: 2024.02.22 18:06:24     Seconds have passed since the bar opened: 25     Approximately seconds left before bar closes: 35     Time remaining until bar closes: 00:00:35        result on M5:     Opening time of the current bar: 2024.02.22 18:05     Time Current: 2024.02.22 18:07:28     Seconds have passed since the bar opened: 149     Approximately seconds left before bar closes: 151     Time remaining until bar closes: 00:02:31        result on H1:     Opening time of the current bar: 2024.02.22 18:00     Time Current: 2024.02.22 18:08:13     Seconds have passed since the bar opened: 494     Approximately seconds left before bar closes: 3106     Time remaining until bar closes: 00:51:46          result on D1:     Opening time of the current bar: 2024.02.22 00:00     Time Current: 2024.02.22 18:11:01     Seconds have passed since the bar opened: 65462     Approximately seconds left before bar closes: 20938     Time remaining until bar closes: 05:48:58     \*/    } |

See also

[StringToTime](../StringToTime/StringToTime.md), [TimeToStruct](../../Date-and-Time/TimeToStruct/TimeToStruct.md)
