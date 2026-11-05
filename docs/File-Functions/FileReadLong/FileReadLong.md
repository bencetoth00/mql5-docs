# FileReadLong

FileReadLong

The function reads an integer of long type (8 bytes) from the current position of the binary file.

|  |
| --- |
| long  FileReadLong(     int  file\_handle    // File handle     ); |

Parameters

file\_handle

[in]  File descriptor returned by [FileOpen()](../FileOpen/FileOpen.md).

Return Value

The value of long type.

Example (the file obtained during the execution of an example for [FileWriteLong](../FileWriteLong/FileWriteLong.md) function is used here)

|  |
| --- |
| //+------------------------------------------------------------------+  //|                                            Demo\_FileReadLong.mq5 |  //|                        Copyright 2013, MetaQuotes Software Corp. |  //|                                              https://www.mql5.com |  //+------------------------------------------------------------------+  #property copyright "Copyright 2013, MetaQuotes Software Corp."  #property link      "https://www.mql5.com"  #property version   "1.00"  #property indicator\_buffers 1  #property indicator\_plots   1  //---- plot Label1  #property indicator\_label1  "Volume"  #property indicator\_type1   DRAW\_LINE  #property indicator\_color1  clrYellow  #property indicator\_style1  STYLE\_SOLID  #property indicator\_width1  2  #property indicator\_separate\_window  //--- parameters for data reading  input string InpFileName="Volume.bin"; // file name  input string InpDirectoryName="Data";  // directory name  //--- global variables  int      ind=0;  int      size=0;  long     volume\_buff[];  datetime time\_buff[];  //--- indicator buffers  double   buff[];  //+------------------------------------------------------------------+  //| Custom indicator initialization function                         |  //+------------------------------------------------------------------+  int OnInit()    {  //--- open the file     ResetLastError();     int file\_handle=FileOpen(InpDirectoryName+"//"+InpFileName,FILE\_READ|FILE\_BIN);     if(file\_handle!=INVALID\_HANDLE)       {        PrintFormat("%s file is open for writing",InpFileName);        PrintFormat("File path: %s\\Files\\",TerminalInfoString(TERMINAL\_DATA\_PATH));        //--- first, read the amount of data in the file        size=(int)FileReadLong(file\_handle);        //--- allocate memory for the arrays        ArrayResize(volume\_buff,size);        ArrayResize(time\_buff,size);        //--- read data from the file        for(int i=0;i<size;i++)          {           time\_buff[i]=(datetime)FileReadLong(file\_handle);           volume\_buff[i]=FileReadLong(file\_handle);          }        //--- close the file        FileClose(file\_handle);        PrintFormat("Data is read, %s file is closed",InpFileName);       }     else       {        PrintFormat("Failed to open %s file, Error code = %d",InpFileName,GetLastError());        return(INIT\_FAILED);       }  //--- bind the array to the indicator buffer with 0 index     SetIndexBuffer(0,buff,INDICATOR\_DATA);  //---- set the indicator values that will be visible on the chart     PlotIndexSetDouble(0,PLOT\_EMPTY\_VALUE,0);  //---     return(INIT\_SUCCEEDED);    }  //+------------------------------------------------------------------+  //| Custom indicator iteration function                              |  //+------------------------------------------------------------------+  int OnCalculate(const int rates\_total,                  const int prev\_calculated,                  const datetime &time[],                  const double &open[],                  const double &high[],                  const double &low[],                  const double &close[],                  const long &tick\_volume[],                  const long &volume[],                  const int &spread[])    {     ArraySetAsSeries(time,false);  //--- the loop for the bars that have not been handled yet     for(int i=prev\_calculated;i<rates\_total;i++)       {        //--- 0 by default        buff[i]=0;        //--- check if any data is still present        if(ind<size)          {           for(int j=ind;j<size;j++)             {              //--- if dates coincide, the value from the file is used              if(time[i]==time\_buff[j])                {                 buff[i]=(double)volume\_buff[j];                 ind=j+1;                 break;                }             }          }       }  //--- return value of prev\_calculated for next call     return(rates\_total);    } |

See also

[Integer types](../../Language-Basics/Data-Types/Integer-Types/Integer-Types.md), [FileReadInteger](../FileReadInteger/FileReadInteger.md), [FileWriteLong](../FileWriteLong/FileWriteLong.md)
