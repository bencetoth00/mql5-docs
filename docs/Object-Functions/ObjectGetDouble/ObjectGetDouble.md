# ObjectGetDouble

ObjectGetDouble

The function returns the value of the corresponding object property. The object property must be of the [double](../../Language-Basics/Data-Types/Real-Types-(double,-float)/Real-Types-(double,-float).md) type. There are 2 variants of the function.

1. Immediately returns the property value.

|  |
| --- |
| double  ObjectGetDouble(     long                            chart\_id,          // chart identifier     string                          name,              // object name     ENUM\_OBJECT\_PROPERTY\_DOUBLE     prop\_id,           // property identifier     int                             prop\_modifier=0    // property modifier, if required     ); |

2. Returns true or false, depending on the success of the function. If successful, the property value is placed to a receiving variable passed by reference by the last parameter.

|  |
| --- |
| bool  ObjectGetDouble(     long                            chart\_id,          // chart identifier     string                          name,              // object name     ENUM\_OBJECT\_PROPERTY\_DOUBLE     prop\_id,           // property identifier     int                             prop\_modifier,     // property modifier     double&                         double\_var         // here we accept the property value     ); |

Parameters

chart\_id

[in]  Chart identifier. 0 means the current chart.

name

[in]  Name of the object.

prop\_id

[in]  ID of the object property. The value can be one of the values of the [ENUM\_OBJECT\_PROPERTY\_DOUBLE](../../Constants,-Enumerations-and-Structures/Objects-Constants/Object-Properties/Object-Properties.md#enum_object_property_double) enumeration.

prop\_modifier

[in]  Modifier of the specified property. For the first variant, the default modifier value is equal to 0. Most properties do not require a modifier.  It denotes the number of the level in [Fibonacci tools](../../Constants,-Enumerations-and-Structures/Objects-Constants/Object-Types/Object-Types.md) and in the graphical object Andrew's pitchfork. The numeration of levels starts from zero.

double\_var

[out]  Variable of the double type that received the value of the requested property.

Return Value

Value of the double type for the first calling variant.

For the second variant the function returns true, if this property is maintained and the value has been placed into the double\_var variable, otherwise returns false. To read more about the [error](../../Constants,-Enumerations-and-Structures/Codes-of-Errors-and-Warnings/Runtime-Errors/Runtime-Errors.md) call [GetLastError()](../../Checkup/GetLastError/GetLastError.md).

Note

The function uses a synchronous call, which means that the function waits for the execution of all commands that have been enqueued for this chart prior to its call, that is why this function can be time consuming. This feature should be taken into account when working with a large number of objects on a chart.

 

Example:

|  |
| --- |
| #property copyright "Copyright 2025, MetaQuotes Ltd."  #property link      "https://www.mql5.com"  #property version   "1.00"     #define   OBJ\_NAME   "TestObjectGetDouble"   // Object name  #define   WND        0                       // Chart subwindow  #define   EXT        " (%$)"                 // Format string for displaying price values at levels     //+------------------------------------------------------------------+  //| Script program start function                                    |  //+------------------------------------------------------------------+  void OnStart()    {  //--- current chart ID, the chart symbol, and symbol Digits     long   chart\_id= ChartID();     string symbol  = ChartSymbol(chart\_id);     int    digits  = (int)SymbolInfoInteger(symbol, SYMBOL\_DIGITS);       //--- construct the Fibonacci Levels graphical object at the maximum and minimum prices of the visible chart     if(!CreateFibo(chart\_id))        return;          //--- number of object levels     int total=(int)ObjectGetInteger(chart\_id, OBJ\_NAME, OBJPROP\_LEVELS);     double value =0;     double price0=0;     double price1=0;       //--- anchor point prices     price0=ObjectGetDouble(chart\_id, OBJ\_NAME, OBJPROP\_PRICE, 0);     price1=ObjectGetDouble(chart\_id, OBJ\_NAME, OBJPROP\_PRICE, 1);       //--- in a loop by the number of object levels     for(int i=0; i<total; i++)       {        //--- get the value set for the current level        ResetLastError();        if(!ObjectGetDouble(chart\_id, OBJ\_NAME, OBJPROP\_LEVELVALUE, i, value))          {           Print("ObjectGetDouble() failed. Error ", GetLastError());           return;          }                //--- get the maximum and minimum prices of the object binding and the distance between them in the price value        double max=fmax(price0, price1);        double min=fmin(price0, price1);        double range=max-min;                //--- calculate the price value for the current level of the object        double level\_price=min+range\*value;                //--- set the color for the level so that it is visible on both dark and light backgrounds of the chart        ObjectSetInteger(chart\_id, OBJ\_NAME, OBJPROP\_LEVELCOLOR, i, clrRed);                //--- set a format string for the level so that its price value is displayed along with the level value        string level\_text=ObjectGetString(chart\_id, OBJ\_NAME, OBJPROP\_LEVELTEXT, i);        if(StringFind(level\_text, EXT)<0)          {           level\_text+=EXT;           ObjectSetString(chart\_id, OBJ\_NAME, OBJPROP\_LEVELTEXT, i, level\_text);          }                //--- output the level number and its data - the level value and its price - in the journal        PrintFormat("Fibo level [%d] value: %.3f,  price: %.\*f", i, value, digits, level\_price);       }     /\*     result:     Fibo level [0] value: 0.000,  price: 0.61989     Fibo level [1] value: 0.236,  price: 0.62533     Fibo level [2] value: 0.382,  price: 0.62869     Fibo level [3] value: 0.500,  price: 0.63140     Fibo level [4] value: 0.618,  price: 0.63412     Fibo level [5] value: 1.000,  price: 0.64292     Fibo level [6] value: 1.618,  price: 0.65715     Fibo level [7] value: 2.618,  price: 0.68018     Fibo level [8] value: 4.236,  price: 0.71745     \*/    }  //+------------------------------------------------------------------+  //| Create the Fibo levels graphical object on the specified chart |  //+------------------------------------------------------------------+  bool CreateFibo(const long chart\_id)    {  //--- draw Fibo levels from the highest to the lowest visible price values on the chart and get them     double   price\_high=0, price\_low=0;     datetime time\_high =0, time\_low =0;          if(!GetChartExtremums(chart\_id, price\_high, price\_low, time\_high, time\_low))        return(false);     //--- construct the Fibo Levels object on the found price/time coordinates     if(!ObjectCreate(chart\_id, OBJ\_NAME, OBJ\_FIBO, WND, time\_high, price\_high, time\_low, price\_low))       {        PrintFormat("%s: ObjectCreate() failed. Error %d",\_\_FUNCTION\_\_, GetLastError());        return(false);       }         //--- all is well - update the chart and return 'true'     ChartRedraw();     return(true);    }  //+------------------------------------------------------------------+  //| Return the maximum and minimum prices on the chart and their time|  //+------------------------------------------------------------------+  bool GetChartExtremums(const long chart\_id, double &price\_high, double &price\_low, datetime &time\_high, datetime &time\_low)    {  //--- reset the variables     price\_high=price\_low=0;     time\_high =time\_low =0;  //--- chart symbol     string symbol = ChartSymbol(chart\_id);     //--- calculate the start of the range of copied timeseries based on the number of the first visible bar and the number of bars on the chart     int first = (int)ChartGetInteger(chart\_id, CHART\_FIRST\_VISIBLE\_BAR);     int count = (int)ChartGetInteger(chart\_id, CHART\_VISIBLE\_BARS);     int start = first+1-count;       //--- arrays where timeseries are to be copied     double   array\_high[];     double   array\_low[];     datetime array\_time[];     int      index;       //--- copy three timeseries into arrays in the amount of 'count' and starting from 'start'     ResetLastError();     if(CopySeries(symbol, PERIOD\_CURRENT, start, count, COPY\_RATES\_TIME|COPY\_RATES\_HIGH|COPY\_RATES\_LOW, array\_time, array\_high, array\_low)!=count)       {        PrintFormat("%s: CopySeries() failed. Error %d",\_\_FUNCTION\_\_, GetLastError());        return(false);       }       //--- look for the maximum price index in the array\_high array     index=ArrayMaximum(array\_high);     if(index<0)       {        PrintFormat("%s: ArrayMaximum() failed. Error %d",\_\_FUNCTION\_\_, GetLastError());        return(false);       }  //--- remember the highest price on the visible chart and the time value of the bar this price is located on     price\_high=array\_high[index];     time\_high=array\_time[index];       //--- look for the minimum price index in the array\_low array     index=ArrayMinimum(array\_low);     if(index<0)       {        PrintFormat("%s: ArrayMinimum() failed. Error %d",\_\_FUNCTION\_\_, GetLastError());        return(false);       }  //--- remember the lowest price on the visible chart and the time value of the bar this price is located on     price\_low=array\_low[index];     time\_low=array\_time[index];       //--- all is fine     return(true);    } |
