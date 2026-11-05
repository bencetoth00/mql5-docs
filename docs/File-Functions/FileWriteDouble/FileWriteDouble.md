# FileWriteDouble

FileWriteDouble

The function writes the value of a double parameter to a a bin-file, starting from the current position of the file pointer.

|  |
| --- |
| uint  FileWriteDouble(     int     file\_handle,     // File handle     double  value            // Value to write     ); |

Parameters

file\_handle

[in]  File descriptor returned by [FileOpen()](../FileOpen/FileOpen.md).

value

[in]   The value of double type.

Return Value

If successful the function returns the number of bytes written (in this case [sizeof](../../Language-Basics/Operations-and-Expressions/Other-Operations/Other-Operations.md#sizeof)(double)=8). The file pointer is shifted by the same number of bytes.

Example:

|  |
| --- |
| //+------------------------------------------------------------------+  //|                                         Demo\_FileWriteDouble.mq5 |  //|                        Copyright 2013, MetaQuotes Software Corp. |  //|                                              https://www.mql5.com |  //+------------------------------------------------------------------+  #property copyright "Copyright 2013, MetaQuotes Software Corp."  #property link      "https://www.mql5.com"  #property version   "1.00"  //--- show the window of input parameters when launching the script  #property script\_show\_inputs  //--- parameters for receiving data from the terminal  input string             InpSymbolName="EURJPY";           // currency pair  input ENUM\_TIMEFRAMES    InpSymbolPeriod=PERIOD\_M15;       // time frame  input int                InpMAPeriod=10;                   // smoothing period  input int                InpMAShift=0;                     // indicator shift  input ENUM\_MA\_METHOD     InpMAMethod=MODE\_SMA;             // smoothing type  input ENUM\_APPLIED\_PRICE InpAppliedPrice=PRICE\_CLOSE;      // price type  input datetime           InpDateStart=D'2013.01.01 00:00'; // data copying start date  //--- parameters for writing data to the file  input string             InpFileName="MA.csv";    // file name  input string             InpDirectoryName="Data"; // directory name  //+------------------------------------------------------------------+  //| Script program start function                                    |  //+------------------------------------------------------------------+  void OnStart()    {     datetime date\_finish=TimeCurrent();     double   ma\_buff[];     datetime time\_buff[];     int      size;  //--- receive MA indicator handle     ResetLastError();     int ma\_handle=iMA(InpSymbolName,InpSymbolPeriod,InpMAPeriod,InpMAShift,InpMAMethod,InpAppliedPrice);     if(ma\_handle==INVALID\_HANDLE)       {        //--- failed to receive the indicator handle        PrintFormat("Error when receiving indicator handle. Error code = %d",GetLastError());        return;       }  //--- being in the loop until the indicator calculates all its values     while(BarsCalculated(ma\_handle)==-1)        Sleep(20); // a pause to allow the indicator to calculate all its values     PrintFormat("Indicator values starting from %s will be written to the file",TimeToString(InpDateStart));  //--- copy the indicator values     ResetLastError();     if(CopyBuffer(ma\_handle,0,InpDateStart,date\_finish,ma\_buff)==-1)       {        PrintFormat("Failed to copy the indicator values. Error code = %d",GetLastError());        return;       }  //--- copy the time of the appropriate bars' arrival     ResetLastError();     if(CopyTime(InpSymbolName,InpSymbolPeriod,InpDateStart,date\_finish,time\_buff)==-1)       {        PrintFormat("Failed to copy time values. Error code = %d",GetLastError());        return;       }  //--- receive the buffer size     size=ArraySize(ma\_buff);  //--- free the memory occupied by the indicator     IndicatorRelease(ma\_handle);  //--- open the file for writing the indicator values (if the file is absent, it will be created automatically)     ResetLastError();     int file\_handle=FileOpen(InpDirectoryName+"//"+InpFileName,FILE\_READ|FILE\_WRITE|FILE\_BIN);     if(file\_handle!=INVALID\_HANDLE)       {        PrintFormat("%s file is available for writing",InpFileName);        PrintFormat("File path: %s\\Files\\",TerminalInfoString(TERMINAL\_DATA\_PATH));        //--- first, write the size of data sample        FileWriteDouble(file\_handle,(double)size);        //--- write the indicator time and value to the file        for(int i=0;i<size;i++)          {           FileWriteDouble(file\_handle,(double)time\_buff[i]);           FileWriteDouble(file\_handle,ma\_buff[i]);          }        //--- close the file        FileClose(file\_handle);        PrintFormat("Data is written, %s file is closed",InpFileName);       }     else        PrintFormat("Failed to open %s file, Error code = %d",InpFileName,GetLastError());    } |

See also

[Real types (double, float)](../../Language-Basics/Data-Types/Real-Types-(double,-float)/Real-Types-(double,-float).md)
