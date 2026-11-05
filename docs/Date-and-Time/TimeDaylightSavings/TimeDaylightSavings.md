# TimeDaylightSavings

TimeDaylightSavings

Returns correction for daylight saving time in seconds, if the switch to summer time has been made. It depends on the time settings of your computer.

|  |
| --- |
| int  TimeDaylightSavings(); |

Return Value

If switch to winter (standard) time has been made, it returns 0.

Example:

|  |
| --- |
| void OnStart()    {  //--- get daylight saving time adjustment in seconds     int sec\_dl=TimeDaylightSavings();       //--- create the text describing the received value     string text=(sec\_dl==0 ? "Standard \"winter\" time is used" :                   StringFormat("Daylight saving time has been switched over. The correction is %d seconds", sec\_dl));       //--- display a description of the daylight saving time adjustment in seconds in the log     Print(text);     /\*     result for "winter" time:     Standard "winter" time is used          result for "summer" time:     Daylight saving time has been switched over. The correction is -3600 seconds     \*/    } |
