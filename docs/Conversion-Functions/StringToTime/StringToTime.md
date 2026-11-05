# StringToTime

StringToTime

Transforms the string containing time and/or date in the "yyyy.mm.dd [hh:mi]" format into the datetime type number.

|  |
| --- |
| datetime  StringToTime(     const string  time\_string      // date string     ); |

Parameters

time\_string

[in]  String in one of the specified formats:

- "yyyy.mm.dd [hh:mi]"
- "yyyy.mm.dd [hh:mi:ss]"
- "yyyymmdd [hh:mi:ss]"
- "yyyymmdd [hhmiss]"
- "yyyy/mm/dd [hh:mi:ss]"
- "yyyy-mm-dd [hh:mi:ss]"

Return Value

[datetime](../../Language-Basics/Data-Types/Integer-Types/Datetime-Type/Datetime-Type.md) type value containing the number of seconds elapsed since 01.01.1970.

Note

Any sequence of space and tabulation characters between date and time is considered to be a single space to avoid additional processing of the time\_string before calling StringToTime().

 

Example:

|  |
| --- |
| //--- input parameters  input group    "The date can be entered in any of the formats:"  input group    "yyyy.mm.dd [hh:mi], yyyy.mm.dd [hh:mi:ss]"  input group    "yyyymmdd [hh:mi:ss], yyyymmdd [hhmiss]"  input group    "yyyy/mm/dd [hh:mi:ss], yyyy-mm-dd [hh:mi:ss]"  input string   InpDateStr;    // Please enter the date here as a string     //+------------------------------------------------------------------+  //| Script program start function                                    |  //+------------------------------------------------------------------+  void OnStart()    {  //--- convert the time entered in the inputs as a string into a datetime value     datetime time=StringToTime(InpDateStr);  //--- display the entered string and the obtained time in the journal     PrintFormat("Date entered as a string in the form '%s' is converted to datetime in the form '%s'",                 InpDateStr, TimeToString(time, TIME\_DATE|TIME\_MINUTES|TIME\_SECONDS));  //--- create a vertical line on the received date-time and shift the chart to this location     if(CreateVLine(time))        ChartNavigateToTime(time);     /\*     result:     Date entered as a string in the form '' is converted to datetime in the form '1970.01.01 00:00:00'     Date entered as a string in the form '2024' is converted to datetime in the form '2024.02.24 20:24:00'     Date entered as a string in the form '202400' is converted to datetime in the form '2024.02.24 20:24:00'     Date entered as a string in the form '20240000' is converted to datetime in the form '2024.02.24 00:00:00'     Date entered as a string in the form '2024022410' is converted to datetime in the form '2030.09.06 00:00:00'     Date entered as a string in the form '20240224 10' is converted to datetime in the form '2024.02.24 10:00:00'     Date entered as a string in the form '20240224 01' is converted to datetime in the form '2024.02.24 01:00:00'     Date entered as a string in the form '20240224 0030' is converted to datetime in the form '2024.02.24 23:00:00'     Date entered as a string in the form '20240224 0100' is converted to datetime in the form '2024.02.24 01:00:00'     \*/    }  //+------------------------------------------------------------------+  //| Create a vertical line object                                    |  //+------------------------------------------------------------------+  bool CreateVLine(const datetime line\_time)    {     ResetLastError();        string name=MQLInfoString(MQL\_PROGRAM\_NAME)+"\_VLINE";     if(!ObjectCreate(0, name, OBJ\_VLINE, 0, line\_time, 0))       {        Print("ObjectCreate() failed. Error code: ", GetLastError());        return(false);       }     ObjectSetInteger(0, name, OBJPROP\_STYLE, STYLE\_DOT);     ObjectSetInteger(0, name, OBJPROP\_SELECTABLE, true);        return(true);    }  //+------------------------------------------------------------------+  //| Shift the chart to the specified bar opening time                |  //+------------------------------------------------------------------+  bool ChartNavigateToTime(const datetime time)    {     ChartSetInteger(0, CHART\_AUTOSCROLL, false);     ResetLastError();        int bar=iBarShift(\_Symbol, PERIOD\_CURRENT, time);     if(bar<0)       {        PrintFormat("%s: iBarShift() failed. Error code: %d", \_\_FUNCTION\_\_, GetLastError());        return(false);       }        long first=0;     if(!ChartGetInteger(0, CHART\_FIRST\_VISIBLE\_BAR, 0, first))       {        PrintFormat("%s: ChartGetInteger() failed. Error code: %d", \_\_FUNCTION\_\_, GetLastError());        return(false);       }        return(ChartNavigate(0, CHART\_CURRENT\_POS, (int)first-bar));    } |

See also

[TimeToString](../TimeToString/TimeToString.md), [TimeToStruct](../../Date-and-Time/TimeToStruct/TimeToStruct.md)
