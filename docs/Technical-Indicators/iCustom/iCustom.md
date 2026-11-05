# iCustom

iCustom

The function returns the handle of a specified custom indicator.

|  |
| --- |
| int  iCustom(     string           symbol,     // symbol name     ENUM\_TIMEFRAMES  period,     // period     string           name        // folder/custom\_indicator\_name     ...                          // list of indicator input parameters     ); |

Parameters

symbol

[in] The symbol name of the security, the data of which should be used to calculate the indicator. The [NULL](../../Language-Basics/Data-Types/Void-Type-and-NULL-Constant/Void-Type-and-NULL-Constant.md) value means the current symbol.

period

[in] The value of the period can be one of the [ENUM\_TIMEFRAMES](../../Constants,-Enumerations-and-Structures/Chart-Constants/Chart-Timeframes/Chart-Timeframes.md) values, 0 means the current timeframe.

name

[in]  Custom indicator name. If the name starts with the reverse slash '\', the EX5 indicator file is searched for relative to the MQL5 root directory. So, for a call of iCustom(Symbol(), Period(), "\FirstIndicator"...), the indicator will be loaded as MQL5\FirstIndicator.ex5. If the file is not found at this path, error 4802 (ERR\_INDICATOR\_CANNOT\_CREATE) is returned.

If the path does not start with '\', the indicator is searched and downloaded as follows:

- First, the indicator EX5 file is searched for in the folder where the EX5 file of the calling program is located. For example, the CrossMA.EX5 EA is located in MQL5\Experts\MyExperts and contains the iCustom call (Symbol(), Period(), "SecondIndicator"...). In this case, the indicator is searched for in MQL5\Experts\MyExperts\SecondIndicator.ex5.
- If the indicator is not found in the same directory, the search is performed relative to the MQL5\Indicators indicator root directory. In other words, the search for the MQL5\Indicators\SecondIndicator.ex5 file is performed. If the indicator is still not found, the function returns [INVALID\_HANDLE](../../Constants,-Enumerations-and-Structures/Named-Constants/Other-Constants/Other-Constants.md) and the error 4802 (ERR\_INDICATOR\_CANNOT\_CREATE) is triggered.

If the path to the indicator is set in the subdirectory (for example, MyIndicators\ThirdIndicator), the search is first performed in the calling program folder (the EA is located in MQL5\Experts\MyExperts) in MQL5\Experts\MyExperts\MyIndicators\ThirdIndicator.ex5. If unsuccessful, the search for the MQL5\Indicators\MyIndicators\ThirdIndicator.ex5 file is performed. Make sure to use the double reverse slash '\\' as a separator in the path, for example iCustom(Symbol(), Period(), "MyIndicators\\ThirdIndicator"...)

...

[in] [input-parameters](../../Language-Basics/Variables/Input-Variables/Input-Variables.md) of a custom indicator, separated by commas. Type and order of parameters must match. If there is no parameters specified, then [default values](../../Language-Basics/Functions/Functions.md#default_value) will be used.

Return Value

Returns the handle of a specified technical indicator,  in case of failure returns [INVALID\_HANDLE](../../Constants,-Enumerations-and-Structures/Named-Constants/Other-Constants/Other-Constants.md). The computer memory can be freed from an indicator that is no more utilized, using the [IndicatorRelease()](../../Timeseries-and-Indicators-Access/IndicatorRelease/IndicatorRelease.md) function, to which the indicator handle is passed.

Note

A custom indicator must be compiled (with extension EX5) and located in the directory MQL5/Indicators of the client terminal or its subdirectory.

Indicators that require testing are defined automatically from the call of the iCustom() function, if the corresponding parameter is set through a [constant string](../../Language-Basics/Data-Types/String-Type/String-Type.md). For all other cases (use of the [IndicatorCreate()](../../Timeseries-and-Indicators-Access/IndicatorCreate/IndicatorCreate.md) function or use of a non-constant string in the parameter that sets the indicator name) the property [#property tester\_indicator](../../Language-Basics/Preprocessor/Program-Properties-(#property)/Program-Properties-(#property).md) is required:

|  |
| --- |
| #property tester\_indicator "indicator\_name.ex5" |

If [the first call form](../../Event-Handling/OnCalculate/OnCalculate.md) is used in the indicator, then at the custom indicator start you can additionally indicate data for calculation in its "Parameters" tab. If the "Apply to" parameter is not selected explicitly, the default calculation is based on the values of "Close" prices.

![Selecting timeseries to calculate an indicator](../../assets/applyto.png "Selecting timeseries to calculate an indicator")

When you call a custom indicator from mql5-program, the Applied\_Price parameter or a handle of another indicator should be passed last, after all input variables of the custom indicator.

See also

[Program Properties](../../Language-Basics/Preprocessor/Program-Properties-(#property)/Program-Properties-(#property).md), [Timeseries and Indicators Access](../../Timeseries-and-Indicators-Access/Timeseries-and-Indicators-Access.md),[IndicatorCreate()](../../Timeseries-and-Indicators-Access/IndicatorCreate/IndicatorCreate.md), [IndicatorRelease()](../../Timeseries-and-Indicators-Access/IndicatorRelease/IndicatorRelease.md)

Example:

|  |
| --- |
| #property indicator\_separate\_window  #property indicator\_buffers 1  #property indicator\_plots   1  //---- plot Label1  #property indicator\_label1  "Label1"  #property indicator\_type1   DRAW\_LINE  #property indicator\_color1  clrRed  #property indicator\_style1  STYLE\_SOLID  #property indicator\_width1  1  //--- input parameters  input int MA\_Period=21;  input int MA\_Shift=0;  input ENUM\_MA\_METHOD MA\_Method=MODE\_SMA;  //--- indicator buffers  double         Label1Buffer[];  //--- Handle of the Custom Moving Average.mq5 custom indicator  int MA\_handle;  //+------------------------------------------------------------------+  //| Custom indicator initialization function                         |  //+------------------------------------------------------------------+  int OnInit()    {  //--- indicator buffers mapping     SetIndexBuffer(0,Label1Buffer,INDICATOR\_DATA);     ResetLastError();     MA\_handle=iCustom(NULL,0,"Examples\\Custom Moving Average",                       MA\_Period,                       MA\_Shift,                       MA\_Method,                       PRICE\_CLOSE // using the close prices                       );     Print("MA\_handle = ",MA\_handle,"  error = ",GetLastError());  //---     return(INIT\_SUCCEEDED);    }  //+------------------------------------------------------------------+  //| Custom indicator iteration function                              |  //+------------------------------------------------------------------+  int OnCalculate(const int rates\_total,                  const int prev\_calculated,                  const datetime &time[],                  const double &open[],                  const double &high[],                  const double &low[],                  const double &close[],                  const long &tick\_volume[],                  const long &volume[],                  const int &spread[])    {  //--- Copy the values of the indicator Custom Moving Average to our indicator buffer     int copy=CopyBuffer(MA\_handle,0,0,rates\_total,Label1Buffer);     Print("copy = ",copy,"    rates\_total = ",rates\_total);  //--- If our attempt has failed - Report this     if(copy<=0)        Print("An attempt to get the values if Custom Moving Average has failed");  //--- return value of prev\_calculated for next call     return(rates\_total);    }  //+------------------------------------------------------------------+ |
