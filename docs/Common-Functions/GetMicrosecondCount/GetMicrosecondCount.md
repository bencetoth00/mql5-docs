# GetMicrosecondCount

GetMicrosecondCount

The GetMicrosecondCount() function returns the number of microseconds that have elapsed since the start of MQL5-program.

|  |
| --- |
| ulong  GetMicrosecondCount(); |

Return Value

Value of ulong type.

Example:

|  |
| --- |
| //+------------------------------------------------------------------+  //| Test function                                                    |  //+------------------------------------------------------------------+  void Test()    {     int    res\_int=0;     double res\_double=0;  //---       for(int i=0;i<10000;i++)       {        res\_int+=i\*i;        res\_int++;        res\_double+=i\*i;        res\_double++;       }    }  //+------------------------------------------------------------------+  //| Script program start function                                    |  //+------------------------------------------------------------------+  void OnStart()    {     uint   ui=0,ui\_max=0,ui\_min=INT\_MAX;     ulong  ul=0,ul\_max=0,ul\_min=INT\_MAX;  //--- number of measurements     for(int count=0;count<1000;count++)       {        uint  ui\_res=0;        ulong ul\_res=0;        //---         for(int n=0;n<2;n++)          {           //--- select measurement type           if(n==0) ui=GetTickCount();           else     ul=GetMicrosecondCount();           //--- execute code            Test();           //--- add measurement result (depending on type)           if(n==0) ui\_res+=GetTickCount()-ui;           else     ul\_res+=GetMicrosecondCount()-ul;                   }        //--- calculate minimum and maximum time for both measurements        if(ui\_min>ui\_res) ui\_min=ui\_res;        if(ui\_max<ui\_res) ui\_max=ui\_res;        if(ul\_min>ul\_res) ul\_min=ul\_res;        if(ul\_max<ul\_res) ul\_max=ul\_res;       }  //---     Print("GetTickCount error(msec): ",ui\_max-ui\_min);     Print("GetMicrosecondCount error(msec): ",DoubleToString((ul\_max-ul\_min)/1000.0,2));    } |

See also

[Date and Time](../../Date-and-Time/Date-and-Time.md), [GetTickCount](../GetTickCount/GetTickCount.md), [GetTickCount64](../GetTickCount64/GetTickCount64.md)
