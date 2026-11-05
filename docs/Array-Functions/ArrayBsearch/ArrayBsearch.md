# ArrayBsearch

ArrayBsearch

Searches for a specified value in a multidimensional numeric array [sorted](../ArraySort/ArraySort.md) ascending. Search is performed through the elements of the first dimension.

For searching in an array of double type

|  |
| --- |
| int  ArrayBsearch(     const double&    array[],   // array for search     double           value      // what is searched for     ); |

For searching in an array of float type

|  |
| --- |
| int  ArrayBsearch(     const float&    array[],   // array for search     float           value      // what is searched for     ); |

For searching in an array of long type

|  |
| --- |
| int  ArrayBsearch(     const long&    array[],   // array for search     long           value      // what is searched for     ); |

For searching in an array of int type

|  |
| --- |
| int  ArrayBsearch(     const int&    array[],   // array for search     int           value      // what is searched for     ); |

For searching in an array of short type

|  |
| --- |
| int  ArrayBsearch(     const short&    array[],   // array for search     short           value      // what is searched for     ); |

For searching in an array of char type

|  |
| --- |
| int  ArrayBsearch(     const char&    array[],   // array for search     char           value      // what is searched for     ); |

Parameters

array[]

[in]  Numeric array for search.

value

[in]  Value for search.

Return Value

The function returns index of a found element. If the wanted value isn't found, the function returns the index of an element nearest in value.

Note

Binary search processes only sorted arrays. To sort numeric arrays use the [ArraySort()](../ArraySort/ArraySort.md) function.

Example:

|  |
| --- |
| #property description "Script based on RSI indicator data displays"  #property description "how often the market was in"  #property description "overbought and oversold areas in the specified time interval."  //--- display the window of input parameters when launching the script  #property script\_show\_inputs  //--- input parameters  input int                InpMAPeriod=14;                    // Moving average period  input ENUM\_APPLIED\_PRICE InpAppliedPrice=PRICE\_CLOSE;       // Price type  input double             InpOversoldValue=30.0;             // Oversold level  input double             InpOverboughtValue=70.0;           // Overbought level  input datetime           InpDateStart=D'2012.01.01 00:00';  // Analysis start date  input datetime           InpDateFinish=D'2013.01.01 00:00'; // Analysis finish date  //+------------------------------------------------------------------+  //| Script program start function                                    |  //+------------------------------------------------------------------+  void OnStart()    {     double rsi\_buff[]; // array of the indicator values     int    size=0;     // array size  //--- receive RSI indicator handle     ResetLastError();     int rsi\_handle=iRSI(Symbol(),Period(),InpMAPeriod,InpAppliedPrice);     if(rsi\_handle==INVALID\_HANDLE)       {        //--- failed to receive the indicator handle        PrintFormat("Indicator handle receiving error. Error code = %d",GetLastError());        return;       }  //--- being in the loop, until the indicator calculates all its values     while(BarsCalculated(rsi\_handle)==-1)       {        //--- exit if the indicator has forcedly completed the script's operation        if(IsStopped())           return;        //--- a pause to allow the indicator to calculate all its values        Sleep(10);       }  //--- copy the indicator values for a certain period of time     ResetLastError();     if(CopyBuffer(rsi\_handle,0,InpDateStart,InpDateFinish,rsi\_buff)==-1)       {        PrintFormat("Failed to copy the indicator values. Error code = %d",GetLastError());        return;       }  //--- receive the array size     size=ArraySize(rsi\_buff);  //--- sort out the array     ArraySort(rsi\_buff);  //--- find out the time (in percentage terms) the market was in the oversold area     double ovs=(double)ArrayBsearch(rsi\_buff,InpOversoldValue)\*100/(double)size;  //--- find out the time (in percentage terms) the market was in the overbought area     double ovb=(double)(size-ArrayBsearch(rsi\_buff,InpOverboughtValue))\*100/(double)size;  //--- form the strings for displaying the data     string str="From "+TimeToString(InpDateStart,TIME\_DATE)+" to "                +TimeToString(InpDateFinish,TIME\_DATE)+" the market was:";     string str\_ovb="in overbought area "+DoubleToString(ovb,2)+"% of time";     string str\_ovs="in oversold area "+DoubleToString(ovs,2)+"% of time";  //--- display the data on the chart     CreateLabel("top",5,60,str,clrDodgerBlue);     CreateLabel("overbought",5,35,str\_ovb,clrDodgerBlue);     CreateLabel("oversold",5,10,str\_ovs,clrDodgerBlue);  //--- redraw the chart     ChartRedraw(0);  //--- pause     Sleep(10000);    }  //+------------------------------------------------------------------+  //| Display comment in the bottom left corner of the chart           |  //+------------------------------------------------------------------+  void CreateLabel(const string name,const int x,const int y,                   const string str,const color clr)    {  //--- create the label     ObjectCreate(0,name,OBJ\_LABEL,0,0,0);  //--- bind the label to the bottom left corner     ObjectSetInteger(0,name,OBJPROP\_CORNER,CORNER\_LEFT\_LOWER);  //--- change position of the anchor point     ObjectSetInteger(0,name,OBJPROP\_ANCHOR,ANCHOR\_LEFT\_LOWER);  //--- distance from the anchor point in X-direction     ObjectSetInteger(0,name,OBJPROP\_XDISTANCE,x);  //--- distance from the anchor point in Y-direction     ObjectSetInteger(0,name,OBJPROP\_YDISTANCE,y);  //--- label text     ObjectSetString(0,name,OBJPROP\_TEXT,str);  //--- text color     ObjectSetInteger(0,name,OBJPROP\_COLOR,clr);  //--- text size     ObjectSetInteger(0,name,OBJPROP\_FONTSIZE,12);    } |
