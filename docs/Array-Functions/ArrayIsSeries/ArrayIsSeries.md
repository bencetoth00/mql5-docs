# ArrayIsSeries

ArrayIsSeries

The function checks whether an array is a timeseries.

|  |
| --- |
| bool  ArrayIsSeries(     const void&  array[]    // checked array     ); |

Parameters

array[]

[in]  Checked array.

Return Value

It returns true, if a checked array is an array timeseries, otherwise it returns false. Arrays passed as a parameter to the [OnCalculate()](../../Language-Basics/Functions/Event-Handling-Functions/Event-Handling-Functions.md#oncalculate2) function must be checked for the order of accessing the array elements by [ArrayGetAsSeries()](../ArrayGetAsSeries/ArrayGetAsSeries.md).

Example:

|  |
| --- |
| #property indicator\_chart\_window  #property indicator\_buffers 1  #property indicator\_plots   1  //---- plot Label1  #property indicator\_label1  "Label1"  #property indicator\_type1   DRAW\_LINE  #property indicator\_color1  clrRed  #property indicator\_style1  STYLE\_SOLID  #property indicator\_width1  1  //--- indicator buffers  double         Label1Buffer[];  //+------------------------------------------------------------------+  //| Custom indicator initialization function                         |  //+------------------------------------------------------------------+  void OnInit()    {  //--- indicator buffers mapping     SetIndexBuffer(0,Label1Buffer,INDICATOR\_DATA);  //---    }  //+------------------------------------------------------------------+  //| Custom indicator iteration function                              |  //+------------------------------------------------------------------+  int OnCalculate(const int rates\_total,                  const int prev\_calculated,                  const datetime &time[],                  const double &open[],                  const double &high[],                  const double &low[],                  const double &close[],                  const long &tick\_volume[],                  const long &volume[],                  const int &spread[])    {  //---     if(ArrayIsSeries(open))        Print("open[] is timeseries");     else        Print("open[] is not timeseries!!!");  //--- return value of prev\_calculated for next call     return(rates\_total);    } |

See also

[Access to timeseries and indicators](../../Timeseries-and-Indicators-Access/Timeseries-and-Indicators-Access.md)
