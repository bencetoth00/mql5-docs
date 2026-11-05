# FileReadDouble

FileReadDouble

Reads a double-precision floating point number (double) from the current position of the binary file.

|  |
| --- |
| double  FileReadDouble(     int  file\_handle    // File handle     ); |

Parameters

file\_handle

[in]  File descriptor returned by [FileOpen()](../FileOpen/FileOpen.md).

Return Value

The value of double type.

Note

For more details about the error, call [GetLastError()](../../Checkup/GetLastError/GetLastError.md).

Example (the file obtained after executing the example for [FileWriteDouble](../FileWriteDouble/FileWriteDouble.md) function is used here)

|  |
| --- |
| //+------------------------------------------------------------------+  //|                                          Demo\_FileReadDouble.mq5 |  //|                        Copyright 2013, MetaQuotes Software Corp. |  //|                                              https://www.mql5.com |  //+------------------------------------------------------------------+  #property copyright "Copyright 2013, MetaQuotes Software Corp."  #property link      "https://www.mql5.com"  #property version   "1.00"  #property indicator\_chart\_window  #property indicator\_buffers 1  #property indicator\_plots   1  //---- plot Label1  #property indicator\_label1  "MA"  #property indicator\_type1   DRAW\_LINE  #property indicator\_color1  clrGreen  #property indicator\_style1  STYLE\_SOLID  #property indicator\_width1  2  #property indicator\_separate\_window  //--- data reading parameters  input string InpFileName="MA.csv";    // file name  input string InpDirectoryName="Data"; // directory name  //--- global variables  int      ind=0;  int      size=0;  double   ma\_buff[];  datetime time\_buff[];  //--- indicator buffer  double   buff[];  //+------------------------------------------------------------------+  //| Custom indicator initialization function                         |  //+------------------------------------------------------------------+  int OnInit()    {  //--- open the file     ResetLastError();     int file\_handle=FileOpen(InpDirectoryName+"//"+InpFileName,FILE\_READ|FILE\_BIN);     if(file\_handle!=INVALID\_HANDLE)       {        PrintFormat("%s file is available for reading",InpFileName);        PrintFormat("File path: %s\\Files\\",TerminalInfoString(TERMINAL\_DATA\_PATH));        //--- first, read the amount of data in the file        size=(int)FileReadDouble(file\_handle);        //--- allocate memory for the arrays        ArrayResize(ma\_buff,size);        ArrayResize(time\_buff,size);        //--- read data from the file        for(int i=0;i<size;i++)          {           time\_buff[i]=(datetime)FileReadDouble(file\_handle);           ma\_buff[i]=FileReadDouble(file\_handle);          }        //--- close the file        FileClose(file\_handle);        PrintFormat("Data is written, %s file is closed",InpFileName);       }     else       {        PrintFormat("Failed to open %s file, Error code = %d",InpFileName,GetLastError());        return(INIT\_FAILED);       }  //--- bind the array to the indicator buffer with index 0     SetIndexBuffer(0,buff,INDICATOR\_DATA);  //---- set the indicator values that will not be visible on the chart     PlotIndexSetDouble(0,PLOT\_EMPTY\_VALUE,0);  //---     return(INIT\_SUCCEEDED);    }  //+------------------------------------------------------------------+  //| Custom indicator iteration function                              |  //+------------------------------------------------------------------+  int OnCalculate(const int rates\_total,                  const int prev\_calculated,                  const datetime &time[],                  const double &open[],                  const double &high[],                  const double &low[],                  const double &close[],                  const long &tick\_volume[],                  const long &volume[],                  const int &spread[])    {     ArraySetAsSeries(time,false);  //--- the loop for the bars that have not been handled yet     for(int i=prev\_calculated;i<rates\_total;i++)       {        //--- 0 by default        buff[i]=0;        //--- check if any data still exists        if(ind<size)          {           for(int j=ind;j<size;j++)             {              //--- if the dates coincide, the value from the file is used              if(time[i]==time\_buff[j])                {                 buff[i]=ma\_buff[j];                 //--- increase the counter                 ind=j+1;                 break;                }             }          }       }  //--- return value of prev\_calculated for next call     return(rates\_total);    } |

See also

[Real types (double, float)](../../Language-Basics/Data-Types/Real-Types-(double,-float)/Real-Types-(double,-float).md), [StringToDouble](../../Conversion-Functions/StringToDouble/StringToDouble.md), [DoubleToString](../../Conversion-Functions/DoubleToString/DoubleToString.md), [FileWriteDouble](../FileWriteDouble/FileWriteDouble.md)
