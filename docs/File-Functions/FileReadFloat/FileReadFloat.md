# FileReadFloat

FileReadFloat

Reads the single-precision floating point number (float) from the current position of the binary file.

|  |
| --- |
| float  FileReadFloat(     int  file\_handle    // File handle     ); |

Parameters

file\_handle

[in]  File descriptor returned by [FileOpen()](../FileOpen/FileOpen.md).

Return Value

The value of float type.

Note

For more details about the error, call [GetLastError()](../../Checkup/GetLastError/GetLastError.md).

Example (the file obtained after executing the example for [FileWriteFloat](../FileWriteFloat/FileWriteFloat.md) function is used here)

|  |
| --- |
| //+------------------------------------------------------------------+  //|                                           Demo\_FileReadFloat.mq5 |  //|                        Copyright 2013, MetaQuotes Software Corp. |  //|                                              https://www.mql5.com |  //+------------------------------------------------------------------+  #property copyright "Copyright 2013, MetaQuotes Software Corp."  #property link      "https://www.mql5.com"  #property version   "1.00"  #property indicator\_separate\_window  #property indicator\_buffers 2  #property indicator\_plots   1  //---- plot Label1  #property indicator\_label1  "CloseLine"  #property indicator\_type1   DRAW\_COLOR\_LINE  #property indicator\_color1  clrRed,clrBlue  #property indicator\_style1  STYLE\_SOLID  #property indicator\_width1  2  //--- parameters for data reading  input string InpFileName="Close.bin"; // file name  input string InpDirectoryName="Data"; // directory name  //--- global variables  int      ind=0;  int      size=0;  double   close\_buff[];  datetime time\_buff[];  //--- indicator buffers  double   buff[];  double   color\_buff[];  //+------------------------------------------------------------------+  //| Custom indicator initialization function                         |  //+------------------------------------------------------------------+  int OnInit()    {     int def\_size=100;  //--- allocate memory for the arrays     ArrayResize(close\_buff,def\_size);     ArrayResize(time\_buff,def\_size);  //--- open the file     ResetLastError();     int file\_handle=FileOpen(InpDirectoryName+"//"+InpFileName,FILE\_READ|FILE\_BIN);     if(file\_handle!=INVALID\_HANDLE)       {        PrintFormat("%s file is available for reading",InpFileName);        PrintFormat("File path: %s\\Files\\",TerminalInfoString(TERMINAL\_DATA\_PATH));        //--- read data from the file        while(!FileIsEnding(file\_handle))          {           //--- read time and price values           time\_buff[size]=(datetime)FileReadDouble(file\_handle);           close\_buff[size]=(double)FileReadFloat(file\_handle);           size++;           //--- increase the array sizes if they are overflown           if(size==def\_size)             {              def\_size+=100;              ArrayResize(close\_buff,def\_size);              ArrayResize(time\_buff,def\_size);             }          }        //--- close the file        FileClose(file\_handle);        PrintFormat("Data is read, %s file is closed",InpFileName);       }     else       {        PrintFormat("Failed to open %s file, Error code = %d",InpFileName,GetLastError());        return(INIT\_FAILED);       }  //--- bind the arrays to the indicator buffers     SetIndexBuffer(0,buff,INDICATOR\_DATA);     SetIndexBuffer(1,color\_buff,INDICATOR\_COLOR\_INDEX);  //---- set the indicator values that will not be visible on the chart     PlotIndexSetDouble(0,PLOT\_EMPTY\_VALUE,0);  //---     return(INIT\_SUCCEEDED);    }  //+------------------------------------------------------------------+  //| Custom indicator iteration function                              |  //+------------------------------------------------------------------+  int OnCalculate(const int rates\_total,                  const int prev\_calculated,                  const datetime &time[],                  const double &open[],                  const double &high[],                  const double &low[],                  const double &close[],                  const long &tick\_volume[],                  const long &volume[],                  const int &spread[])    {     ArraySetAsSeries(time,false);  //--- the loop for the bars that have not been handled yet     for(int i=prev\_calculated;i<rates\_total;i++)       {        //--- 0 by default        buff[i]=0;        color\_buff[i]=0; // red color by default        //--- check if any data is still present        if(ind<size)          {           for(int j=ind;j<size;j++)             {              //--- if the dates coincide, the value from the file is used              if(time[i]==time\_buff[j])                {                 //--- receive the price                 buff[i]=close\_buff[j];                 //--- if the current price exceeds the previous one, the color is blue                 if(buff[i-1]>buff[i])                    color\_buff[i]=1;                 //--- increase the counter                 ind=j+1;                 break;                }             }          }       }  //--- return value of prev\_calculated for next call     return(rates\_total);    } |

See also

[Real types (double, float)](../../Language-Basics/Data-Types/Real-Types-(double,-float)/Real-Types-(double,-float).md), [FileReadDouble](../FileReadDouble/FileReadDouble.md), [FileWriteFloat](../FileWriteFloat/FileWriteFloat.md)
