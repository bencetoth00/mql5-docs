# FileWriteStruct

FileWriteStruct

The function writes into a bin-file contents of a structure passed as a parameter, starting from the current position of the file pointer.

|  |
| --- |
| uint  FileWriteStruct(     int          file\_handle,       // File handle     const void&  struct\_object,     // link to an object     int          size=-1            // size to be written in bytes     ); |

Parameters

file\_handle

[in]  File descriptor returned by [FileOpen()](../FileOpen/FileOpen.md).

struct\_object

[in] Reference to the object of this structure. The structure should not contain strings, [dynamic arrays](../../Language-Basics/Data-Types/Dynamic-Array-Object/Dynamic-Array-Object.md) or [virtual functions](../../Language-Basics/Object-Oriented-Programming/Virtual-Functions/Virtual-Functions.md).

size=-1

[in] Number of bytes that you want to record. If size is not specified or the specified number of bytes is greater than the size of the structure, the entire structure is written.

Return Value

If successful the function returns the number of bytes written. The file pointer is shifted by the same number of bytes.

Example:

|  |
| --- |
| //+------------------------------------------------------------------+  //|                                          Demo\_FileWiteStruct.mq5 |  //|                        Copyright 2013, MetaQuotes Software Corp. |  //|                                              https://www.mql5.com |  //+------------------------------------------------------------------+  #property copyright "Copyright 2013, MetaQuotes Software Corp."  #property link      "https://www.mql5.com"  #property version   "1.00"  //--- show the window of input parameters when launching the script  #property script\_show\_inputs  //--- parameters for receiving data from the terminal  input string          InpSymbolName="EURUSD";           // currency pair  input ENUM\_TIMEFRAMES InpSymbolPeriod=PERIOD\_H1;        // time frame  input datetime        InpDateStart=D'2013.01.01 00:00'; // data copying start date  //--- parameters for writing data to the file  input string          InpFileName="EURUSD.txt";         // file name  input string          InpDirectoryName="Data";          // directory name  //+------------------------------------------------------------------+  //| Structure for storing candlestick data                           |  //+------------------------------------------------------------------+  struct candlesticks    {     double            open;  // open price     double            close; // close price     double            high;  // high price     double            low;   // low price     datetime          date;  // date    };  //+------------------------------------------------------------------+  //| Script program start function                                    |  //+------------------------------------------------------------------+  void OnStart()    {     datetime     date\_finish=TimeCurrent();     int          size;     datetime     time\_buff[];     double       open\_buff[];     double       close\_buff[];     double       high\_buff[];     double       low\_buff[];     candlesticks cand\_buff[];  //--- reset the error value     ResetLastError();  //--- receive the time of the arrival of the bars from the range     if(CopyTime(InpSymbolName,InpSymbolPeriod,InpDateStart,date\_finish,time\_buff)==-1)       {        PrintFormat("Failed to copy time values. Error code = %d",GetLastError());        return;       }  //--- receive high prices of the bars from the range     if(CopyHigh(InpSymbolName,InpSymbolPeriod,InpDateStart,date\_finish,high\_buff)==-1)       {        PrintFormat("Failed to copy values of high prices. Error code = %d",GetLastError());        return;       }  //--- receive low prices of the bars from the range     if(CopyLow(InpSymbolName,InpSymbolPeriod,InpDateStart,date\_finish,low\_buff)==-1)       {        PrintFormat("Failed to copy values of low prices. Error code = %d",GetLastError());        return;       }  //--- receive open prices of the bars from the range     if(CopyOpen(InpSymbolName,InpSymbolPeriod,InpDateStart,date\_finish,open\_buff)==-1)       {        PrintFormat("Failed to copy values of open prices. Error code = %d",GetLastError());        return;       }  //--- receive close prices of the bars from the range     if(CopyClose(InpSymbolName,InpSymbolPeriod,InpDateStart,date\_finish,close\_buff)==-1)       {        PrintFormat("Failed to copy values of close prices. Error code = %d",GetLastError());        return;       }  //--- define dimension of the arrays     size=ArraySize(time\_buff);  //--- save all data in the structure array     ArrayResize(cand\_buff,size);     for(int i=0;i<size;i++)       {        cand\_buff[i].open=open\_buff[i];        cand\_buff[i].close=close\_buff[i];        cand\_buff[i].high=high\_buff[i];        cand\_buff[i].low=low\_buff[i];        cand\_buff[i].date=time\_buff[i];       }     //--- open the file for writing the structure array to the file (if the file is absent, it will be created automatically)     ResetLastError();     int file\_handle=FileOpen(InpDirectoryName+"//"+InpFileName,FILE\_READ|FILE\_WRITE|FILE\_BIN|FILE\_COMMON);     if(file\_handle!=INVALID\_HANDLE)       {        PrintFormat("%s file is open for writing",InpFileName);        PrintFormat("File path: %s\\Files\\",TerminalInfoString(TERMINAL\_COMMONDATA\_PATH));        //--- prepare the counter of the number of bytes        uint counter=0;        //--- write array values in the loop        for(int i=0;i<size;i++)           counter+=FileWriteStruct(file\_handle,cand\_buff[i]);        PrintFormat("%d bytes of information is written to %s file",InpFileName,counter);        PrintFormat("Total number of bytes: %d \* %d \* %d = %d, %s",size,5,8,size\*5\*8,size\*5\*8==counter ? "Correct" : "Error");        //--- close the file        FileClose(file\_handle);        PrintFormat("Data is written, %s file is closed",InpFileName);       }     else        PrintFormat("Failed to open %s file, Error code = %d",InpFileName,GetLastError());    } |

See also

[Structures and classes](../../Language-Basics/Data-Types/Structures,-Classes-and-Interfaces/Structures,-Classes-and-Interfaces.md)
