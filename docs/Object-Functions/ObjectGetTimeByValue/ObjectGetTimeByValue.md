# ObjectGetTimeByValue

ObjectGetTimeByValue

The function returns the time value for the specified price value of the specified object.

|  |
| --- |
| datetime  ObjectGetTimeByValue(     long    chart\_id,     // chart identifier     string  name,         // object name     double  value,        // Price     int     line\_id       // Line number     ); |

Parameters

chart\_id

[in]  Chart identifier. 0 means the current chart.

name

[in]  Name of the object.

value

[in]  Price value.

line\_id

[in]  Line identifier.

Return Value

The time value for the specified price value of the specified object.

Note

The function uses a synchronous call, which means that the function waits for the execution of all commands that have been enqueued for this chart prior to its call, that is why this function can be time consuming. This feature should be taken into account when working with a large number of objects on a chart.

An object can have several values in one price coordinate, therefore it is necessary to specify the line number. This function applies only to the following objects:

- Trendline (OBJ\_TREND)
- Trendline by angle (OBJ\_TRENDBYANGLE)
- Gann line (OBJ\_GANNLINE)
- Equidistant channel (OBJ\_CHANNEL) - 2 lines
- Linear regression channel (OBJ\_REGRESSION) - 3 lines
- Standard deviation channel (OBJ\_STDDEVCHANNEL) - 3 lines
- Arrowed line (OBJ\_ARROWED\_LINE)

 

Example:

|  |
| --- |
| #property copyright "Copyright 2025, MetaQuotes Ltd."  #property link      "https://www.mql5.com"  #property version   "1.00"     #define   OBJ\_NAME   "TestObjectGetTimeByValue" // graphical object name  #define   STEP       100                        // price step     //+------------------------------------------------------------------+  //| Script program start function                                    |  //+------------------------------------------------------------------+  void OnStart()    {  //--- ID, symbol     long   chart\_id=ChartID();     string chart\_symbol=ChartSymbol(chart\_id);       //--- get the Point value of the chart symbol     double point=SymbolInfoDouble(chart\_symbol, SYMBOL\_POINT);     if(point==0)       {        PrintFormat("Failed to get the Point value of the \"%s\" symbol. Error %d", chart\_symbol, GetLastError());        return;       }         //--- build an equidistant channel from the High of the left visible bar to the Low of the right one     if(!CreateChannel(chart\_id))        return;       //--- chart maximum and minimum, chart symbol Digits     double chart\_max=ChartGetDouble(chart\_id, CHART\_PRICE\_MAX);     double chart\_min=ChartGetDouble(chart\_id, CHART\_PRICE\_MIN);     int    digits=(int)SymbolInfoInteger(chart\_symbol, SYMBOL\_DIGITS);     //--- while the calculated price is greater than the minimum price value of the chart,  //--- go in a loop through the chart prices with STEP and get the time value  //--- for the calculated price value of each line of the equidistant channel.  //--- output the received time for each line to the journal     int index=0;     double price=chart\_max;     do       {        price=chart\_max-STEP\*index\*point;        datetime time0=ObjectGetTimeByValue(chart\_id, OBJ\_NAME, price, 0);        datetime time1=ObjectGetTimeByValue(chart\_id, OBJ\_NAME, price, 1);        string   time0\_str=(time0>0 ? TimeToString(time0) : "No value at this price");        string   time1\_str=(time1>0 ? TimeToString(time1) : "No value at this price");        string   idx=StringFormat("%02d", index);        PrintFormat("[%s] For price %.\*f the time value at line 0: %s, at line 1: %s", idx, digits, price, time0\_str, time1\_str);        index++;       }     while(!IsStopped() && price>=chart\_min);       //--- wait 5 seconds and clean up     Sleep(5000);     ObjectDelete(chart\_id, OBJ\_NAME);     ChartRedraw(chart\_id);     /\*     result:     [00] For price 1.26110 the time value at line 0: No value at this price,  at line 1: No value at this price     [01] For price 1.26010 the time value at line 0: 2024.12.30 17:00, at line 1: No value at this price     [02] For price 1.25910 the time value at line 0: 2024.12.30 22:30, at line 1: No value at this price     [03] For price 1.25810 the time value at line 0: 2024.12.31 04:00, at line 1: 2024.12.30 16:30     [04] For price 1.25710 the time value at line 0: 2024.12.31 10:00, at line 1: 2024.12.30 22:00     [05] For price 1.25610 the time value at line 0: 2024.12.31 15:30, at line 1: 2024.12.31 03:30     [06] For price 1.25510 the time value at line 0: 2024.12.31 21:00, at line 1: 2024.12.31 09:00     [07] For price 1.25410 the time value at line 0: 2025.01.02 03:30, at line 1: 2024.12.31 14:30     [08] For price 1.25310 the time value at line 0: No value at this price, at line 1: 2024.12.31 20:30     [09] For price 1.25210 the time value at line 0: No value at this price, at line 1: 2025.01.02 03:00     [10] For price 1.25110 the time value at line 0: No value at this price, at line 1: No value at this price     [11] For price 1.25010 the time value at line 0: No value at this price, at line 1: No value at this price     [12] For price 1.24910 the time value at line 0: No value at this price, at line 1: No value at this price     [13] For price 1.24810 the time value at line 0: No value at this price, at line 1: No value at this price     \*/    }  //+--------------------------------------------------------------------------------------------+  //| Construct an equidistant channel from the High of the left bar to the Low of the right bar |  //+--------------------------------------------------------------------------------------------+  bool CreateChannel(const long chart\_id=0)    {     long     bar1  =0, bar2  =0, visible=0;     datetime time1 =0, time2 =0;     double   price1=0, price2=0;     //--- get the first bar of the chart visible on the left     ResetLastError();     if(!ChartGetInteger(chart\_id, CHART\_FIRST\_VISIBLE\_BAR, 0, bar1))       {        PrintFormat("%s: ChartGetInteger() failed. Error %d",\_\_FUNCTION\_\_, GetLastError());        return(false);       }  //--- number of visible bars on the chart     if(!ChartGetInteger(chart\_id, CHART\_VISIBLE\_BARS, 0, visible))       {        PrintFormat("%s: ChartGetInteger() failed. Error %d",\_\_FUNCTION\_\_, GetLastError());        return(false);       }     //--- adjust the obtained values and calculate the index of the first bar visible on the right     bar1-=1;     visible-=2;     bar2=bar1-visible;       //--- chart symbol     string symbol=ChartSymbol(chart\_id);       //--- get the time of the first bar visible on the left of the chart     ResetLastError();     datetime time\_array[1];     if(CopyTime(symbol, PERIOD\_CURRENT, (int)bar1, 1, time\_array)!=1)       {        PrintFormat("%s: CopyTime() failed. Error %d",\_\_FUNCTION\_\_, GetLastError());        return(false);       }     time1=time\_array[0];       //--- get the time of the first bar of the chart visible on the right     if(CopyTime(symbol, PERIOD\_CURRENT, (int)bar2, 1, time\_array)!=1)       {        PrintFormat("%s: CopyTime() failed. Error %d",\_\_FUNCTION\_\_, GetLastError());        return(false);       }     time2=time\_array[0];       //--- get the High price of the first bar visible on the left of the chart     double price\_array[];     if(CopyHigh(symbol, PERIOD\_CURRENT, (int)bar1, 1, price\_array)!=1)       {        PrintFormat("%s: CopyHigh() failed. Error %d",\_\_FUNCTION\_\_, GetLastError());        return(false);       }     price1=price\_array[0];       //--- get the Low price of the first bar visible on the right of the chart     if(CopyLow(symbol, PERIOD\_CURRENT, (int)bar2, 1, price\_array)!=1)       {        PrintFormat("%s: CopyLow() failed. Error %d",\_\_FUNCTION\_\_, GetLastError());        return(false);       }     price2=price\_array[0];       //--- calculate the price range of the chart in points  //--- for an equidistant channel, the distance of the second line will be 1/3 of the price range     double range=price1-price2;     double distance=range\*0.3;       //--- at the calculated coordinates, create a graphical object - an equidistant channel     if(!ObjectCreate(chart\_id, OBJ\_NAME, OBJ\_CHANNEL, 0, time1, price1, time2, price2, time1, price1-distance))       {        PrintFormat("%s: ObjectCreate() failed. Error %d",\_\_FUNCTION\_\_, GetLastError());        return(false);       }         //--- update the chart and return 'true'     ChartRedraw(chart\_id);     return(true);    } |

   
See also

[Object Types](../../Constants,-Enumerations-and-Structures/Objects-Constants/Object-Types/Object-Types.md)
