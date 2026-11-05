# FileWriteFloat

FileWriteFloat

The function writes the value of the float parameter to a bin-file, starting from the current position of the file pointer.

|  |
| --- |
| uint  FileWriteFloat(     int    file\_handle,     // File handle     float  value            // Value to be written     ); |

Parameters

file\_handle

[in]  File descriptor returned by [FileOpen()](../FileOpen/FileOpen.md).

value

[in] The value of float type.

Return Value

If successful the function returns the number of bytes written (in this case [sizeof](../../Language-Basics/Operations-and-Expressions/Other-Operations/Other-Operations.md#sizeof)(float)=4). The file pointer is shifted by the same number of bytes.

Example:

|  |
| --- |
| //+------------------------------------------------------------------+  //|                                          Demo\_FileWriteFloat.mq5 |  //|                        Copyright 2013, MetaQuotes Software Corp. |  //|                                              https://www.mql5.com |  //+------------------------------------------------------------------+  #property copyright "Copyright 2013, MetaQuotes Software Corp."  #property link      "https://www.mql5.com"  #property version   "1.00"  //--- show the window of input parameters when launching the script  #property script\_show\_inputs  //--- parameters for receiving data from the terminal  input string          InpSymbolName="EURUSD";           // currency pair  input ENUM\_TIMEFRAMES InpSymbolPeriod=PERIOD\_M15;       // time frame  input datetime        InpDateStart=D'2013.01.01 00:00'; // data copying start date  //--- parameters for writing data to the file  input string          InpFileName="Close.bin"; // file name  input string          InpDirectoryName="Data"; // directory name  //+------------------------------------------------------------------+  //| Script program start function                                    |  //+------------------------------------------------------------------+  void OnStart()    {     datetime date\_finish=TimeCurrent();     double   close\_buff[];     datetime time\_buff[];     int      size;  //--- reset the error value     ResetLastError();  //--- copy the close price for each bar     if(CopyClose(InpSymbolName,InpSymbolPeriod,InpDateStart,date\_finish,close\_buff)==-1)       {        PrintFormat("Failed to copy close price values. Error code = %d",GetLastError());        return;       }  //--- copy the time for each bar     if(CopyTime(InpSymbolName,InpSymbolPeriod,InpDateStart,date\_finish,time\_buff)==-1)       {        PrintFormat("Failed to copy the time values. Error code = %d",GetLastError());        return;       }  //--- receive the buffer size     size=ArraySize(close\_buff);  //--- open the file for writing the values (if the file is absent, it will be created automatically)     ResetLastError();     int file\_handle=FileOpen(InpDirectoryName+"//"+InpFileName,FILE\_READ|FILE\_WRITE|FILE\_BIN);     if(file\_handle!=INVALID\_HANDLE)       {        PrintFormat("%s file is open for writing",InpFileName);        PrintFormat("File path: %s\\Files\\",TerminalInfoString(TERMINAL\_DATA\_PATH));        //--- write close prices' time and values to the file        for(int i=0;i<size;i++)          {           FileWriteDouble(file\_handle,(double)time\_buff[i]);           FileWriteFloat(file\_handle,(float)close\_buff[i]);          }        //--- close the file        FileClose(file\_handle);        PrintFormat("Data is written, %s file is closed",InpFileName);       }     else        PrintFormat("Failed to open %s file, Error code = %d",InpFileName,GetLastError());    } |

See also

[Real types (double, float)](../../Language-Basics/Data-Types/Real-Types-(double,-float)/Real-Types-(double,-float).md), [FileWriteDouble](../FileWriteDouble/FileWriteDouble.md)
