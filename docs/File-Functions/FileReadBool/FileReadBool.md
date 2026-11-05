# FileReadBool

FileReadBool

Reads from the file of CSV type string from the current position to a delimiter (or till the end of the text line) and converts the read string to a bool type value.

|  |
| --- |
| bool  FileReadBool(     int  file\_handle    // File handle     ); |

Parameters

file\_handle

[in]  File descriptor returned by [FileOpen()](../FileOpen/FileOpen.md).

Return Value

Line read may be set to "true", "false" or the symbolic representation of integers "0" or "1". A nonzero value is converted to a logical true. The function returns the converted value.

Example (the file obtained after executing the example for [FileWrite](../FileWrite/FileWrite.md) function is used here)

|  |
| --- |
| //+------------------------------------------------------------------+  //|                                            Demo\_FileReadBool.mq5 |  //|                        Copyright 2013, MetaQuotes Software Corp. |  //|                                              https://www.mql5.com |  //+------------------------------------------------------------------+  #property copyright "Copyright 2013, MetaQuotes Software Corp."  #property link      "https://www.mql5.com"  #property version   "1.00"  #property indicator\_chart\_window  #property indicator\_buffers 2  #property indicator\_plots   2  //---- plot Label1  #property indicator\_label1  "UpSignal"  #property indicator\_type1   DRAW\_ARROW  #property indicator\_color1  clrRed  #property indicator\_style1  STYLE\_SOLID  #property indicator\_width1  4  //---- plot Label2  #property indicator\_label2  "DownSignal"  #property indicator\_type2   DRAW\_ARROW  #property indicator\_color2  clrRed  #property indicator\_style2  STYLE\_SOLID  #property indicator\_width2  4  //--- parameters for data reading  input string InpFileName="MACD.csv";  // file name  input string InpDirectoryName="Data"; // directory name  //--- global variables  int      ind=0;       // index  double   upbuff[];    // indicator buffers of up arrows  double   downbuff[];  // indicator buffer of down arrows  bool     sign\_buff[]; // signal array (true - buy, false - sell)  datetime time\_buff[]; // array of signals' arrival time  int      size=0;      // size of signal arrays  //+------------------------------------------------------------------+  //| Custom indicator initialization function                         |  //+------------------------------------------------------------------+  int OnInit()    {  //--- open the file     ResetLastError();     int file\_handle=FileOpen(InpDirectoryName+"//"+InpFileName,FILE\_READ|FILE\_CSV);     if(file\_handle!=INVALID\_HANDLE)       {        PrintFormat("%s file is open for reading",InpFileName);        //--- first, read the number of signals        size=(int)FileReadNumber(file\_handle);        //--- allocate memory for the arrays        ArrayResize(sign\_buff,size);        ArrayResize(time\_buff,size);        //--- read data from the file        for(int i=0;i<size;i++)          {           //--- signal time           time\_buff[i]=FileReadDatetime(file\_handle);           //--- signal value           sign\_buff[i]=FileReadBool(file\_handle);          }        //--- close the file        FileClose(file\_handle);       }     else       {        PrintFormat("Failed to open %s file, Error code = %d",InpFileName,GetLastError());        return(INIT\_FAILED);       }  //--- binding the arrays     SetIndexBuffer(0,upbuff,INDICATOR\_DATA);     SetIndexBuffer(1,downbuff,INDICATOR\_DATA);  //--- set the symbol code for drawing in PLOT\_ARROW     PlotIndexSetInteger(0,PLOT\_ARROW,241);     PlotIndexSetInteger(1,PLOT\_ARROW,242);  //---- set the indicator values that will not be seen on the chart     PlotIndexSetDouble(0,PLOT\_EMPTY\_VALUE,0);     PlotIndexSetDouble(1,PLOT\_EMPTY\_VALUE,0);  //---     return(INIT\_SUCCEEDED);    }  //+------------------------------------------------------------------+  //| Custom indicator iteration function                              |  //+------------------------------------------------------------------+  int OnCalculate(const int rates\_total,                  const int prev\_calculated,                  const datetime &time[],                  const double &open[],                  const double &high[],                  const double &low[],                  const double &close[],                  const long &tick\_volume[],                  const long &volume[],                  const int &spread[])    {     ArraySetAsSeries(time,false);     ArraySetAsSeries(low,false);     ArraySetAsSeries(high,false);  //--- the loop for the bars that have not been handled yet     for(int i=prev\_calculated;i<rates\_total;i++)       {        //--- 0 by default        upbuff[i]=0;        downbuff[i]=0;        //--- check if any data is still present        if(ind<size)          {           for(int j=ind;j<size;j++)             {              //--- if dates coincide, use the value from the file              if(time[i]==time\_buff[j])                {                 //--- draw the arrow according to the signal                 if(sign\_buff[j])                    upbuff[i]=high[i];                 else                    downbuff[i]=low[i];                 //--- increase the counter                 ind=j+1;                 break;                }             }          }       }  //--- return value of prev\_calculated for next call     return(rates\_total);    } |

See also

[Type bool](../../Language-Basics/Data-Types/Integer-Types/Bool-Type/Bool-Type.md), [FileWrite](../FileWrite/FileWrite.md)
