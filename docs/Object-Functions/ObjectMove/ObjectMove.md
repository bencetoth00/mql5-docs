# ObjectMove

ObjectMove

The function changes coordinates of the specified anchor point of the object.

|  |
| --- |
| bool  ObjectMove(     long      chart\_id,        // chart identifier     string    name,            // object name     int       point\_index,     // anchor point number     datetime  time,            // Time     double    price            // Price     ); |

Parameters

chart\_id

[in]  Chart identifier. 0 means the current chart.

name

[in]  Name of the object.

point\_index

[in]  Index of the anchor point. The number of anchor points depends on the type of object.

time

[in]  Time coordinate of the selected anchor point.

price

[in]  Price coordinate of the selected anchor point.

Return Value

The function returns true if the command has been successfully added to the queue of the specified chart, or false otherwise.

Note

An asynchronous call is always used for ObjectMove(), that is why the function only returns the results of adding the command to a chart queue. In this case, true only means that the command has been successfully enqueued, but the result of its execution is unknown.

To check the command execution result, you can use a function that requests object properties, such as ObjectGetXXX. However, you should keep in mind that such functions are added to the end of the queue of that chart, and they wait for the execution result (due to the synchronous call), and can therefore be time consuming. This feature should be taken into account when working with a large number of objects on a chart.

 

Example:

|  |
| --- |
| #property copyright "Copyright 2025, MetaQuotes Ltd."  #property link      "https://www.mql5.com"  #property version   "1.00"     #define   OBJ\_NAME\_ASK     "TestObjectMoveAsk"  // name of the graphical object for the Ask price  #define   OBJ\_NAME\_BID     "TestObjectMoveBid"  // name of the graphical object for the Bid price  #define   COUNT            100000000            // number of ticks to load history  #define   DELAY            1                    // delay between ticks in ms  //+------------------------------------------------------------------+  //| Script program start function                                    |  //+------------------------------------------------------------------+  void OnStart()    {  //--- current chart ID, the chart symbol, and symbol Digits     long   chart\_id= ChartID();     string symbol  = ChartSymbol(chart\_id);     int    digits  = (int)SymbolInfoInteger(symbol, SYMBOL\_DIGITS);       //--- create two price labels to display the Ask price and Bid price on the chart     if(!CreatePriceLabel(chart\_id, true) || !CreatePriceLabel(chart\_id, false))        return;       //--- array for receiving ticks     MqlTick ticks[]={};       //--- get the number of the next visible bar on the chart and the opening time of this bar in milliseconds     int   first= (int)ChartGetInteger(chart\_id, CHART\_FIRST\_VISIBLE\_BAR)-1;     ulong from = GetTime(symbol, PERIOD\_CURRENT, first)\*1000;       //--- load the tick history into the array     Print("Started collecting ticks...");     if(!GetTicksToArray(symbol, ticks))        return;          //--- reset the tick array and get ticks from the visible range of bars on the chart     ZeroMemory(ticks);     if(CopyTicksRange(symbol, ticks, COPY\_TICKS\_INFO, from)<1)       {        PrintFormat("CopyTicksRange() from date %s failed. Error %d", TimeToString(GetTime(symbol, PERIOD\_CURRENT, first)), GetLastError());        return;       }          Sleep(500);     PrintFormat("Tick ​​visualization started at %s (%I64u), ticks total: %u", TimeToString(GetTime(symbol, PERIOD\_CURRENT, first)), from, ticks.Size());          int count=0;                  // number of ticks processed     int changes=0;                // number of processed price changes     int total=(int)ticks.Size();  // tick array size       //--- in a loop through the tick array     for(int i=0; i<total && !IsStopped(); i++)       {        //--- get a tick from the array and increment the tick counter        MqlTick  tick=ticks[i];        count++;                //--- check the tick Ask and Bid flags        bool ask\_tick=((tick.flags &TICK\_FLAG\_ASK)==TICK\_FLAG\_ASK);         bool bid\_tick=((tick.flags &TICK\_FLAG\_BID)==TICK\_FLAG\_BID);         bool done=false;                //--- if the Ask price changes        if(ask\_tick)          {           if(Move(chart\_id, OBJ\_NAME\_ASK, tick.time, tick.ask))             {              changes++;              done=true;             }          }        //--- if the Bid price changes        if(bid\_tick)          {           if(Move(chart\_id, OBJ\_NAME\_BID, tick.time, tick.bid))             {              changes++;              done=true;             }          }        //--- if any (or both) of the graphical objects have been moved, update the chart        if(done)          {           ChartRedraw(chart\_id);           Sleep(DELAY);          }       }       //--- at the end of the loop, we will report in the journal the number of ticks processed,  //--- wait a couple of seconds, delete the created objects and redraw the chart     PrintFormat("Total ticks completed: %u, Total price changes: %d", count, changes);     Sleep(2000);     if(ObjectsDeleteAll(chart\_id, "TestObjectMove")>0)        ChartRedraw(chart\_id);     /\*     as a result of the script execution, the movement of Ask and Bid prices will be displayed on the visible chart,     starting from the left edge of the chart and to the end of the historical data,     the following data will be displayed in the journal:     Started collecting ticks...     AUDUSD: received 13726794 ticks in 969 ms     Tick ​​visualization started at 2025.01.31 09:00 (1738314000000), ticks total: 44380     Total ticks completed: 44380, Total price changes: 68513     \*/    }  //+------------------------------------------------------------------+  //| Create a "Price label" object                                    |  //+------------------------------------------------------------------+  bool CreatePriceLabel(const long chart\_id, const bool obj\_ask)    {     string obj\_name=(obj\_ask ? OBJ\_NAME\_ASK : OBJ\_NAME\_BID);     ResetLastError();     if(!ObjectCreate(chart\_id, obj\_name, (obj\_ask ? OBJ\_ARROW\_RIGHT\_PRICE : OBJ\_ARROW\_LEFT\_PRICE), 0, 0, 0))       {        PrintFormat("%s: ObjectCreate() failed. Error %d",\_\_FUNCTION\_\_, GetLastError());        return(false);       }     return(ObjectSetInteger(chart\_id, obj\_name, OBJPROP\_COLOR, (obj\_ask ? clrRed : clrBlue)));    }  //+------------------------------------------------------------------+  //| Move the graphical object to the specified price/time coordinates|  //+------------------------------------------------------------------+  bool Move(const long chart\_id, const string obj\_name, const datetime time, const double price)    {     ResetLastError();     if(!ObjectSetInteger(chart\_id, obj\_name, OBJPROP\_TIME, time))       {        PrintFormat("%s: ObjectSetInteger() failed. Error %d",\_\_FUNCTION\_\_, GetLastError());        return(false);       }     if(!ObjectSetDouble(chart\_id, obj\_name, OBJPROP\_PRICE, price))       {        PrintFormat("%s: ObjectSetDouble() failed. Error %d",\_\_FUNCTION\_\_, GetLastError());        return(false);       }     return(true);    }  //+------------------------------------------------------------------+  //| Load ticks into the array                                        |  //+------------------------------------------------------------------+  bool GetTicksToArray(const string symbol, MqlTick &array[])    {     int  attempts=0;     // counter of attempts to obtain tick history     bool success =false; // flag of successful copying of ticks        //--- make 3 attempts to receive ticks     while(attempts<3)        {        //--- measure the start time before receiving the ticks         uint start=GetTickCount();                //--- request the tick history since 1970.01.01 00:00.001 (parameter from=1 ms)         ResetLastError();        int received=CopyTicks(symbol, array, COPY\_TICKS\_ALL, 1, COUNT);         if(received!=-1)           {            //--- display data on the number of ticks and spent time            PrintFormat("%s: received %d ticks in %d ms", symbol, received, GetTickCount()-start);            //--- if the tick history is synchronized, the error code is equal to zero            if(GetLastError()==0)              {               success=true;               break;              }            else               PrintFormat("%s: %s ticks are not synchronized yet, %d ticks received for %d ms. Error=%d",               \_\_FUNCTION\_\_, symbol, received, GetTickCount()-start, GetLastError());           }         //--- count attempts         attempts++;         //--- a one-second pause to wait for the end of synchronization of the tick database        Sleep(1000);        }   //--- receiving the requested ticks from the beginning of the tick history failed in three attempts       if(!success)        {         PrintFormat("Error! Failed to get ticks for symbol %s after three attempts", symbol);         return(false);        }     return(true);    }  //+------------------------------------------------------------------+  //| Return the time by bar index                                     |  //+------------------------------------------------------------------+  datetime GetTime(const string symbol, const ENUM\_TIMEFRAMES timeframe, const int index)    {     datetime array[1]={};     ResetLastError();     if(CopyTime(symbol, timeframe, index, 1, array)!=1)        PrintFormat("%s: CopyTime() failed. Error %d",\_\_FUNCTION\_\_, GetLastError());     return(array[0]);    } |
