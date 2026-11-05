# IndicatorParameters

IndicatorParameters

Based on the specified handle, returns the number of input parameters of the indicator, as well as the values and types of the parameters.

|  |
| --- |
| int  IndicatorParameters(     int               indicator\_handle,     // indicator handle     ENUM\_INDICATOR&   indicator\_type,       // a variable for receiving the indicator type     MqlParam&         parameters[]          // an array for receiving parameters     ); |

Parameters

indicator\_handle

[in]  The handle of the indicator, for which you need to know the number of parameters its is calculated on.

indicator\_type

[out]  A variable if the [ENUM\_INDICATOR](../../Constants,-Enumerations-and-Structures/Indicator-Constants/Indicator-Types/Indicator-Types.md) type, into which the indicator type will be written.

parameters[]

[out]  A dynamic array for receiving values of the [MqlParam](../../Constants,-Enumerations-and-Structures/Data-Structures/Indicator-Parameter-Structure/Indicator-Parameter-Structure.md) type, into which the list of indicator parameters will be written. The array size is returned by the IndicatorParameters() function.

Return Value

The number of input parameters of the indicator with the specified handle. In case of an error returns -1. For more details about the error call the [GetLastError()](../../Checkup/GetLastError/GetLastError.md) function.

Example:

|  |
| --- |
| //+------------------------------------------------------------------+  //| Script program start function                                    |  //+------------------------------------------------------------------+  void OnStart()    {     //--- The number of windows on the chart (at least one main window is always present)     int windows=(int)ChartGetInteger(0,CHART\_WINDOWS\_TOTAL);  //--- Go through the chart windows     for(int w=0;w<windows;w++)       {        //--- The number of indicators in this window/subwindow        int total=ChartIndicatorsTotal(0,w);        //--- Take all indicators in the window        for(int i=0;i<total;i++)          {           //--- Get the short name of the indicator           string name=ChartIndicatorName(0,w,i);           //--- Get the indicator handle           int handle=ChartIndicatorGet(0,w,name);           //--- Add to log           PrintFormat("Window=%d,  indicator #%d,  handle=%d",w,i,handle);           //---           MqlParam parameters[];           ENUM\_INDICATOR indicator\_type;           int params=IndicatorParameters(handle,indicator\_type,parameters);           //--- The header of the message           string par\_info="Short name "+name+", type "                           +EnumToString(ENUM\_INDICATOR(indicator\_type))+"\r\n";           //---            for(int p=0;p<params;p++)             {              par\_info+=StringFormat("parameter %d: type=%s, long\_value=%d, double\_value=%G,string\_value=%s\r\n",                                     p,                                     EnumToString((ENUM\_DATATYPE)parameters[p].type),                                     parameters[p].integer\_value,                                     parameters[p].double\_value,                                     parameters[p].string\_value                                     );             }           Print(par\_info);          }        //--- Done for all indicators in the window       }  //---        } |

See also

[ChartIndicatorGet()](../../Chart-Operations/ChartIndicatorGet/ChartIndicatorGet.md)
