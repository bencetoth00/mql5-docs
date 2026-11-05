# FileWriteInteger

FileWriteInteger

The function writes the value of the int parameter to a bin-file, starting from the current position of the file pointer.

|  |
| --- |
| uint  FileWriteInteger(     int  file\_handle,        // File handle     int  value,              // Value to be written     int  size=INT\_VALUE      // Size in bytes     ); |

Parameters

file\_handle

[in]  File descriptor returned by [FileOpen()](../FileOpen/FileOpen.md).

value

[in] Integer value.

size=INT\_VALUE

[in] Number of bytes (up to 4 inclusive), that should be written. The corresponding constants are provided: CHAR\_VALUE=1, SHORT\_VALUE=2 and INT\_VALUE=4, so the function can write the integer value of char, uchar, short, ushort, int, or uint type.

Return Value

If successful the function returns the number of bytes written. The file pointer is shifted by the same number of bytes.

Example:

|  |
| --- |
| //+------------------------------------------------------------------+  //|                                        Demo\_FileWriteInteger.mq5 |  //|                        Copyright 2013, MetaQuotes Software Corp. |  //|                                              https://www.mql5.com |  //+------------------------------------------------------------------+  #property copyright "Copyright 2013, MetaQuotes Software Corp."  #property link      "https://www.mql5.com"  #property version   "1.00"  //--- show the window of input parameters when launching the script  #property script\_show\_inputs  //--- parameters for receiving data from the terminal  input string             InpSymbolName="EURUSD";           // currency pair  input ENUM\_TIMEFRAMES    InpSymbolPeriod=PERIOD\_H1;        // time frame  input datetime           InpDateStart=D'2013.01.01 00:00'; // data copying start date  //--- parameters for writing data to the file  input string             InpFileName="Trend.bin"; // file name  input string             InpDirectoryName="Data"; // directory name  //+------------------------------------------------------------------+  //| Script program start function                                    |  //+------------------------------------------------------------------+  void OnStart()    {     datetime date\_finish=TimeCurrent();     double   close\_buff[];     datetime time\_buff[];     int      size;  //--- reset the error value     ResetLastError();  //--- copy the close price for each bar     if(CopyClose(InpSymbolName,InpSymbolPeriod,InpDateStart,date\_finish,close\_buff)==-1)       {        PrintFormat("Failed to copy the values of close prices. Error code = %d",GetLastError());        return;       }  //--- copy the time for each bar     if(CopyTime(InpSymbolName,InpSymbolPeriod,InpDateStart,date\_finish,time\_buff)==-1)       {        PrintFormat("Failed to copy time values. Error code = %d",GetLastError());        return;       }  //--- receive the buffer size     size=ArraySize(close\_buff);  //--- open the file for writing the values (if the file is absent, it will be created automatically)     ResetLastError();     int file\_handle=FileOpen(InpDirectoryName+"//"+InpFileName,FILE\_READ|FILE\_WRITE|FILE\_BIN);     if(file\_handle!=INVALID\_HANDLE)       {        PrintFormat("%s file is available for writing",InpFileName);        PrintFormat("File path: %s\\Files\\",TerminalInfoString(TERMINAL\_DATA\_PATH));        //---         int   up\_down=0; // trend flag        int   arr\_size;  // arr array size        uchar arr[];     // uchar type array        //--- write time values to the file        for(int i=0;i<size-1;i++)          {           //--- compare close prices of the current and next bars           if(close\_buff[i]<=close\_buff[i+1])             {              if(up\_down!=1)                {                 //--- write date value to the file using FileWriteInteger                 StringToCharArray(TimeToString(time\_buff[i]),arr);                 arr\_size=ArraySize(arr);                 //--- first, write the number of symbols in the array                 FileWriteInteger(file\_handle,arr\_size,INT\_VALUE);                 //--- write the symbols                 for(int j=0;j<arr\_size;j++)                    FileWriteInteger(file\_handle,arr[j],CHAR\_VALUE);                 //--- change the trend flag                 up\_down=1;                }             }           else             {              if(up\_down!=-1)                {                 //--- write the date value to the file using FileWriteInteger                 StringToCharArray(TimeToString(time\_buff[i]),arr);                 arr\_size=ArraySize(arr);                 //--- first, write the number of symbols in the array                 FileWriteInteger(file\_handle,arr\_size,INT\_VALUE);                 //--- write the symbols                 for(int j=0;j<arr\_size;j++)                    FileWriteInteger(file\_handle,arr[j],CHAR\_VALUE);                 //--- change the trend flag                 up\_down=-1;                }             }          }        //--- close the file        FileClose(file\_handle);        PrintFormat("Data is written, %s file is closed",InpFileName);       }     else        PrintFormat("Failed to open %s file, Error code = %d",InpFileName,GetLastError());    } |

See also

[IntegerToString](../../Conversion-Functions/IntegerToString/IntegerToString.md), [StringToInteger](../../Conversion-Functions/StringToInteger/StringToInteger.md), [Integer types](../../Language-Basics/Data-Types/Integer-Types/Integer-Types.md)
