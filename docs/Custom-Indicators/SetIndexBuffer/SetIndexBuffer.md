# SetIndexBuffer

SetIndexBuffer

The function binds a specified indicator buffer with one-dimensional dynamic array of the [double](../../Language-Basics/Data-Types/Real-Types-(double,-float)/Real-Types-(double,-float).md) type.

|  |
| --- |
| bool  SetIndexBuffer(     int                    index,         // buffer index     double                 buffer[],      // array     ENUM\_INDEXBUFFER\_TYPE  data\_type      // what will be stored     ); |

Parameters

index

[in] Number of the indicator buffer. The numbering starts with 0. The number must be less than the value declared in [#property indicator\_buffers](../../Language-Basics/Preprocessor/Program-Properties-(#property)/Program-Properties-(#property).md).

buffer[]

[in]  An array declared in the custom indicator program.

data\_type

[in] Type of data stored in the indicator array. By default it is [INDICATOR\_DATA](../../Constants,-Enumerations-and-Structures/Indicator-Constants/Custom-Indicator-Properties/Custom-Indicator-Properties.md#enum_indexbuffer_type_enum) (values of the calculated indicator). It may also take the value of [INDICATOR\_COLOR\_INDEX](../../Constants,-Enumerations-and-Structures/Indicator-Constants/Custom-Indicator-Properties/Custom-Indicator-Properties.md#enum_indexbuffer_type_enum); in this case this buffer is used for storing color indexes for the previous indicator buffer. You can specify up to 64 [colors](../../Constants,-Enumerations-and-Structures/Objects-Constants/Web-Colors/Web-Colors.md) in the [#property indicator\_colorN](../../Language-Basics/Preprocessor/Program-Properties-(#property)/Program-Properties-(#property).md) line. The [INDICATOR\_CALCULATIONS](../../Constants,-Enumerations-and-Structures/Indicator-Constants/Custom-Indicator-Properties/Custom-Indicator-Properties.md#enum_indexbuffer_type_enum) value means that the buffer is used in intermediate calculations of the indicator and is not intended for drawing.

Return Value

If successful, returns [true](../../Language-Basics/Data-Types/Integer-Types/Bool-Type/Bool-Type.md), otherwise - [false](../../Language-Basics/Data-Types/Integer-Types/Bool-Type/Bool-Type.md).

Note

After binding, the dynamic array buffer[] will be indexed as in common arrays, even if the indexing of [timeseries](../../Timeseries-and-Indicators-Access/Timeseries-and-Indicators-Access.md) is pre-installed for the bound array. If you want to change the order of access to elements of the indicator array, use the [ArraySetAsSeries()](../../Array-Functions/ArraySetAsSeries/ArraySetAsSeries.md) function after binding the array using the SetIndexBuffer() function. Please note that you can't change the size for dynamic arrays set as indicator buffers by the function [SetIndexBuffer()](SetIndexBuffer.md). For indicator buffers, all operations of size changes are performed by the executing sub-system of the terminal.

Example:

|  |
| --- |
| //+------------------------------------------------------------------+  //|                                              TestCopyBuffer1.mq5 |  //|                        Copyright 2009, MetaQuotes Software Corp. |  //|                                              https://www.mql5.com |  //+------------------------------------------------------------------+  #property copyright "2009, MetaQuotes Software Corp."  #property link      "https://www.mql5.com"  #property version   "1.00"     #property indicator\_separate\_window  #property indicator\_buffers 1  #property indicator\_plots   1  //---- plot MA  #property indicator\_label1  "MA"  #property indicator\_type1   DRAW\_LINE  #property indicator\_color1  clrRed  #property indicator\_style1  STYLE\_SOLID  #property indicator\_width1  1  //--- input parameters  input bool               AsSeries=true;  input int                period=15;  input ENUM\_MA\_METHOD     smootMode=MODE\_EMA;  input ENUM\_APPLIED\_PRICE price=PRICE\_CLOSE;  input int                shift=0;  //--- indicator buffers  double                   MABuffer[];  int                      ma\_handle;  //+------------------------------------------------------------------+  //| Custom indicator initialization function                         |  //+------------------------------------------------------------------+  int OnInit()    {  //--- indicator buffers mapping     if(AsSeries) ArraySetAsSeries(MABuffer,true);     Print("Indicator buffer is timeseries = ",ArrayGetAsSeries(MABuffer));     SetIndexBuffer(0,MABuffer,INDICATOR\_DATA);     Print("Indicator buffer after SetIndexBuffer() is timeseries = ",           ArrayGetAsSeries(MABuffer));       //--- change the order of accessing elements of the indicator buffer     ArraySetAsSeries(MABuffer,AsSeries);          IndicatorSetString(INDICATOR\_SHORTNAME,"MA("+period+")"+AsSeries);  //---     ma\_handle=iMA(Symbol(),0,period,shift,smootMode,price);     return(INIT\_SUCCEEDED);    }  //+------------------------------------------------------------------+  //| Custom indicator iteration function                              |  //+------------------------------------------------------------------+  int OnCalculate(const int rates\_total,                  const int prev\_calculated,                  const datetime &time[],                  const double &open[],                  const double &high[],                  const double &low[],                  const double &close[],                  const long &tick\_volume[],                  const long &volume[],                  const int &spread[])    {  //--- Copy the values of the moving average in the buffer MABuffer     int copied=CopyBuffer(ma\_handle,0,0,rates\_total,MABuffer);        Print("MABuffer[0] = ",MABuffer[0]);// Depending on the value AsSeries                                        // Will receive a very old value                                        // Or for the current unfinished bar     //--- return value of prev\_calculated for next call     return(rates\_total);    }  //+------------------------------------------------------------------+ |

See also

[Custom Indicator Properties](../../Constants,-Enumerations-and-Structures/Indicator-Constants/Custom-Indicator-Properties/Custom-Indicator-Properties.md), [Access to timeseries and indicators](../../Timeseries-and-Indicators-Access/Timeseries-and-Indicators-Access.md)
