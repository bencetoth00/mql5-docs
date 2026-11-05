# ChartRedraw

ChartRedraw

This function calls a forced redrawing of a specified chart.

|  |
| --- |
| void  ChartRedraw(     long  chart\_id=0      // Chart ID     ); |

Parameters

chart\_id=0

[in]  Chart ID. 0 means the current chart.

Note

Usually it is used after changing the [object properties](../../Constants,-Enumerations-and-Structures/Objects-Constants/Object-Properties/Object-Properties.md).

Example:

|  |
| --- |
| #define   WIDTH      50    // rectangle width in bars     //+------------------------------------------------------------------+  //| Script program start function                                    |  //+------------------------------------------------------------------+  void OnStart()    {  //--- get the current chart ID and set the graphical object name     long   chart\_id = ChartID();     string obj\_name = MQLInfoString(MQL\_PROGRAM\_NAME)+"\_RectLabel";       //--- get two rectangle time coordinates     datetime time1  = iTime(\_Symbol, \_Period, WIDTH);     datetime time2  = iTime(\_Symbol, \_Period, 0);     if(time1==0 || time2==0)       {        Print("Error getting time ", GetLastError());        return;       }     //--- get the maximum and minimum prices in the range of the rectangle width     double price1 = HighestHigh(\_Symbol, \_Period, 0, WIDTH);     double price2 = LowestLow(\_Symbol, \_Period, 0, WIDTH);     if(price1==EMPTY\_VALUE || price2==EMPTY\_VALUE)        return;     //--- create a rectangle object     Print("Create a wheat-colored rectangle");     if(!ObjectCreate(chart\_id, obj\_name, OBJ\_RECTANGLE, 0, time1, price1, time2, price2))       {        Print("ObjectCreate() failed. Error ", GetLastError());        return;       }     //--- fill the rectangle with the original color     ObjectSetInteger(chart\_id, obj\_name, OBJPROP\_FILL, true);     ObjectSetInteger(chart\_id, obj\_name, OBJPROP\_BACK, true);     ObjectSetInteger(chart\_id, obj\_name, OBJPROP\_COLOR, clrWheat);     ChartRedraw();       //--- wait a second, fill the rectangle with the DodgerBlue color and update the chart     Sleep(1000);     Print("Change color to DodgerBlue");     ObjectSetInteger(chart\_id, obj\_name, OBJPROP\_COLOR, clrDodgerBlue);     ChartRedraw();       //--- wait a second, fill the rectangle with the LimeGreen color and update the chart     Sleep(1000);     Print("Change color to LimeGreen");     ObjectSetInteger(chart\_id, obj\_name, OBJPROP\_COLOR, clrLimeGreen);     ChartRedraw();       //--- wait a second, fill the rectangle with the OrangeRed color and update the chart     Sleep(1000);     Print("Change color to OrangeRed");     ObjectSetInteger(chart\_id, obj\_name, OBJPROP\_COLOR, clrOrangeRed);     ChartRedraw();       //--- wait a second, fill the rectangle with the Wheat color and update the chart     Sleep(1000);     Print("Reset color to original");     ObjectSetInteger(chart\_id, obj\_name, OBJPROP\_COLOR, clrWheat);     ChartRedraw();       //--- after three seconds, remove the object from the chart     Sleep(3000);     Print("Delete the rectangle");     ObjectDelete(chart\_id, obj\_name);    }  //+------------------------------------------------------------------+  //| Return the maximum High in the specified range of bars           |  //+------------------------------------------------------------------+  double HighestHigh(const string symbol, const ENUM\_TIMEFRAMES timeframe, const uint start, const uint count)    {     ResetLastError();     int index=iHighest(symbol, timeframe, MODE\_HIGH, count, start);     if(index==-1)       {        PrintFormat("%s: iHighest() failed. Error %d",\_\_FUNCTION\_\_, GetLastError());        return(EMPTY\_VALUE);       }     GetLastError();     double price=iHigh(symbol, timeframe, index);     if(price==0)       {        PrintFormat("%s: iHigh() failed. Error %d",\_\_FUNCTION\_\_, GetLastError());        return(EMPTY\_VALUE);       }     return(price);    }  //+------------------------------------------------------------------+  //| Return the minimum Low in the specified range of bars            |  //+------------------------------------------------------------------+  double LowestLow(const string symbol, const ENUM\_TIMEFRAMES timeframe, const uint start, const uint count)    {     ResetLastError();     int index=iLowest(symbol, timeframe, MODE\_LOW, count, start);     if(index==-1)       {        PrintFormat("%s: iLowest() failed. Error %d",\_\_FUNCTION\_\_, GetLastError());        return(EMPTY\_VALUE);       }     GetLastError();     double price=iLow(symbol, timeframe, index);     if(price==0)       {        PrintFormat("%s: iLow() failed. Error %d",\_\_FUNCTION\_\_, GetLastError());        return(EMPTY\_VALUE);       }     return(price);    } |

See also

[Objects functions](../../Object-Functions/Object-Functions.md)
