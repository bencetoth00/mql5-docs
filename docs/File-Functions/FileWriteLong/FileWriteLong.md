# FileWriteLong

FileWriteLong

The function writes the value of the long-type parameter to a bin-file, starting from the current position of the file pointer.

|  |
| --- |
| uint  FileWriteLong(     int   file\_handle,     // File handle     long  value            // Value to be written     ); |

Parameters

file\_handle

[in]  File descriptor returned by [FileOpen()](../FileOpen/FileOpen.md).

value

[in] Value of type long.

Return Value

If successful the function returns the number of bytes written (in this case [sizeof](../../Language-Basics/Operations-and-Expressions/Other-Operations/Other-Operations.md#sizeof)(long)=8). The file pointer is shifted by the same number of bytes.

Example:

|  |
| --- |
| //+------------------------------------------------------------------+  //|                                           Demo\_FileWriteLong.mq5 |  //|                        Copyright 2013, MetaQuotes Software Corp. |  //|                                              https://www.mql5.com |  //+------------------------------------------------------------------+  #property copyright "Copyright 2013, MetaQuotes Software Corp."  #property link      "https://www.mql5.com"  #property version   "1.00"  //--- show the window of input parameters when launching the script  #property script\_show\_inputs  //--- parameters for receiving data from the terminal  input string          InpSymbolName="EURUSD";           // currency pair  input ENUM\_TIMEFRAMES InpSymbolPeriod=PERIOD\_H1;        // time frame  input datetime        InpDateStart=D'2013.01.01 00:00'; // data copying start date  //--- parameters for writing data to the file  input string          InpFileName="Volume.bin"; // file name  input string          InpDirectoryName="Data";  // directory name  //+------------------------------------------------------------------+  //| Script program start function                                    |  //+------------------------------------------------------------------+  void OnStart()    {     datetime date\_finish=TimeCurrent();     long     volume\_buff[];     datetime time\_buff[];     int      size;  //--- reset the error value     ResetLastError();  //--- copy tick volumes for each bar     if(CopyTickVolume(InpSymbolName,InpSymbolPeriod,InpDateStart,date\_finish,volume\_buff)==-1)       {        PrintFormat("Failed to copy values of the tick volume. Error code = %d",GetLastError());        return;       }  //--- copy the time for each bar     if(CopyTime(InpSymbolName,InpSymbolPeriod,InpDateStart,date\_finish,time\_buff)==-1)       {        PrintFormat("Failed to copy time values. Error code = %d",GetLastError());        return;       }  //--- receive the buffer size     size=ArraySize(volume\_buff);  //--- open the file for writing the indicator values (if the file is absent, it will be created automatically)     ResetLastError();     int file\_handle=FileOpen(InpDirectoryName+"//"+InpFileName,FILE\_READ|FILE\_WRITE|FILE\_BIN);     if(file\_handle!=INVALID\_HANDLE)       {        PrintFormat("%s file is available for writing",InpFileName);        PrintFormat("File path: %s\\Files\\",TerminalInfoString(TERMINAL\_DATA\_PATH));        //--- first, write the data sample size        FileWriteLong(file\_handle,(long)size);        //--- write time and volume values to file        for(int i=0;i<size;i++)          {           FileWriteLong(file\_handle,(long)time\_buff[i]);           FileWriteLong(file\_handle,volume\_buff[i]);          }        //--- close the file        FileClose(file\_handle);        PrintFormat("Data is written, %s file is closed",InpFileName);       }     else        PrintFormat("Failed to open %s file, Error code = %d",InpFileName,GetLastError());    } |

See also

[Integer types](../../Language-Basics/Data-Types/Integer-Types/Integer-Types.md), [FileWriteInteger](../FileWriteInteger/FileWriteInteger.md)
