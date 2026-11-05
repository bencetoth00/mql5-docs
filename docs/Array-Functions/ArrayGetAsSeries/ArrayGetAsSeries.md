# ArrayGetAsSeries

ArrayGetAsSeries

It checks direction of an array index.

|  |
| --- |
| bool  ArrayGetAsSeries(     const void&  array[]    // array for checking     ); |

Parameters

array

[in]  Checked array.

Return Value

Returns [true](../../Language-Basics/Data-Types/Integer-Types/Bool-Type/Bool-Type.md), if the specified array has the AS\_SERIES flag set, i.e. access to the array is performed back to front as in timeseries. A [timeseries](../../Timeseries-and-Indicators-Access/Timeseries-and-Indicators-Access.md) differs from a usual array in that the indexing of timeseries elements is performed from its end to beginning (from the newest data to old).

Note

To check whether an array belongs to timeseries, use the [ArrayIsSeries()](../ArrayIsSeries/ArrayIsSeries.md) function. Arrays of price data passed as input parameters into the [OnCalculate()](../../Language-Basics/Functions/Event-Handling-Functions/Event-Handling-Functions.md#oncalculate2) function do not obligatorily have the indexing direction the same as in timeseries. The necessary indexing direction can be set using the [ArraySetAsSeries()](../ArraySetAsSeries/ArraySetAsSeries.md) function.

Example:

|  |
| --- |
| #property description "Indicator calculates absolute values of the difference between"  #property description "Open and Close or High and Low prices displaying them in a separate subwindow"  #property description "as a histrogram."  //--- indicator settings  #property indicator\_separate\_window  #property indicator\_buffers 1  #property indicator\_plots   1  //---- plot  #property indicator\_type1   DRAW\_HISTOGRAM  #property indicator\_style1  STYLE\_SOLID  #property indicator\_width1  3  //--- input parameters  input bool InpAsSeries=true; // Indexing direction in the indicator buffer  input bool InpPrices=true;   // Calculation prices (true - Open,Close; false - High,Low)  //--- indicator buffer  double ExtBuffer[];  //+------------------------------------------------------------------+  //| Calculating indicator values                                     |  //+------------------------------------------------------------------+  void CandleSizeOnBuffer(const int rates\_total,const int prev\_calculated,                          const double &first[],const double &second[],double &buffer[])    {  //--- start variable for calculation of bars     int start=prev\_calculated;  //--- work at the last bar if the indicator values have already been calculated at the previous tick     if(prev\_calculated>0)        start--;  //--- define indexing direction in arrays     bool as\_series\_first=ArrayGetAsSeries(first);     bool as\_series\_second=ArrayGetAsSeries(second);     bool as\_series\_buffer=ArrayGetAsSeries(buffer);  //--- replace indexing direction with direct one if necessary     if(as\_series\_first)        ArraySetAsSeries(first,false);     if(as\_series\_second)        ArraySetAsSeries(second,false);     if(as\_series\_buffer)        ArraySetAsSeries(buffer,false);  //--- calculate indicator values     for(int i=start;i<rates\_total;i++)        buffer[i]=MathAbs(first[i]-second[i]);    }  //+------------------------------------------------------------------+  //| Custom indicator initialization function                         |  //+------------------------------------------------------------------+  int OnInit()    {  //--- bind indicator buffers     SetIndexBuffer(0,ExtBuffer);  //--- set indexing element in the indicator buffer     ArraySetAsSeries(ExtBuffer,InpAsSeries);  //--- check for what prices the indicator is calculated     if(InpPrices)       {        //--- Open and Close prices        PlotIndexSetString(0,PLOT\_LABEL,"BodySize");        //--- set the indicator color        PlotIndexSetInteger(0,PLOT\_LINE\_COLOR,clrOrange);       }     else       {        //--- High and Low prices        PlotIndexSetString(0,PLOT\_LABEL,"ShadowSize");        //--- set the indicator color        PlotIndexSetInteger(0,PLOT\_LINE\_COLOR,clrDodgerBlue);       }  //---     return(INIT\_SUCCEEDED);    }  //+------------------------------------------------------------------+  //| Custom indicator iteration function                              |  //+------------------------------------------------------------------+  int OnCalculate(const int rates\_total,                  const int prev\_calculated,                  const datetime &time[],                  const double &open[],                  const double &high[],                  const double &low[],                  const double &close[],                  const long &tick\_volume[],                  const long &volume[],                  const int &spread[])    {  //--- calculate the indicator according to the flag value     if(InpPrices)        CandleSizeOnBuffer(rates\_total,prev\_calculated,open,close,ExtBuffer);     else        CandleSizeOnBuffer(rates\_total,prev\_calculated,high,low,ExtBuffer);  //--- return value of prev\_calculated for next call     return(rates\_total);    } |

See also

[Access to timeseries](../../Timeseries-and-Indicators-Access/Timeseries-and-Indicators-Access.md), [ArraySetAsSeries](../ArraySetAsSeries/ArraySetAsSeries.md)
