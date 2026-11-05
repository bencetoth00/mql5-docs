# FileWriteString

FileWriteString

The function writes the value of a string-type parameter into a BIN, CSV or TXT file starting from the current position of the file pointer. When writing to a CSV or TXT file: if there is a symbol in the string '\n' (LF) without previous character '\r' (CR), then before '\n' the missing '\r' is added.

|  |
| --- |
| uint  FileWriteString(     int           file\_handle,    // File handle     const string  text\_string,    // string to write     int           length=-1       // number of symbols     ); |

Parameters

file\_handle

[in]  File descriptor returned by [FileOpen()](../FileOpen/FileOpen.md).

text\_string

[in]  String.

length=-1

[in] The number of characters that you want to write. This option is needed for writing a string into a BIN file. If the size is not specified, then the entire string without the trailer 0 is written. If you specify a size smaller than the length of the string, then a part of the string without the trailer 0 is written. If you specify a size greater than the length of the string, the string is filled by the appropriate number of zeros. For files of CSV and TXT type, this parameter is ignored and the string is written entirely.

Return Value

If successful the function returns the number of bytes written. The file pointer is shifted by the same number of bytes.

Note

Note that when writing to a file opened by the FILE\_UNICODE [flag](../../Constants,-Enumerations-and-Structures/Input-Output-Constants/File-Opening-Flags/File-Opening-Flags.md) (or without a flag FILE\_ANSI), then the number of bytes written will be twice as large as the number of string characters written. When recording to a file opened with the FILE\_ANSI flag, the number of bytes written will coincide with the number of string characters written.

Example:

|  |
| --- |
| //+------------------------------------------------------------------+  //|                                         Demo\_FileWriteString.mq5 |  //|                        Copyright 2013, MetaQuotes Software Corp. |  //|                                              https://www.mql5.com |  //+------------------------------------------------------------------+  #property copyright "Copyright 2013, MetaQuotes Software Corp."  #property link      "https://www.mql5.com"  #property version   "1.00"  //--- show the window of input parameters when launching the script  #property script\_show\_inputs  //--- parameters for receiving data from the terminal  input string             InpSymbolName="EURUSD";           // currency pair  input ENUM\_TIMEFRAMES    InpSymbolPeriod=PERIOD\_H1;        // time frame  input int                InpMAPeriod=14;                   // MA period  input ENUM\_APPLIED\_PRICE InpAppliedPrice=PRICE\_CLOSE;      // price type  input datetime           InpDateStart=D'2013.01.01 00:00'; // data copying start date  //--- parameters for writing data to the file  input string             InpFileName="RSI.csv";   // file name  input string             InpDirectoryName="Data"; // directory name  //+------------------------------------------------------------------+  //| Script program start function                                    |  //+------------------------------------------------------------------+  void OnStart()    {     datetime date\_finish; // data copying end date     double   rsi\_buff[];  // array of indicator values     datetime date\_buff[]; // array of the indicator dates     int      rsi\_size=0;  // size of the indicator arrays  //--- end time is the current one     date\_finish=TimeCurrent();  //--- receive RSI indicator handle     ResetLastError();     int rsi\_handle=iRSI(InpSymbolName,InpSymbolPeriod,InpMAPeriod,InpAppliedPrice);     if(rsi\_handle==INVALID\_HANDLE)       {        //--- failed to receive the indicator handle        PrintFormat("Error when receiving indicator handle. Error code = %d",GetLastError());        return;       }  //--- being in the loop, until the indicator calculates all its values     while(BarsCalculated(rsi\_handle)==-1)        Sleep(10); // a pause to allow the indicator to calculate all its values  //--- copy the indicator values for a certain period of time     ResetLastError();     if(CopyBuffer(rsi\_handle,0,InpDateStart,date\_finish,rsi\_buff)==-1)       {        PrintFormat("Failed to copy indicator values. Error code = %d",GetLastError());        return;       }  //--- copy the appropriate time for the indicator values     ResetLastError();     if(CopyTime(InpSymbolName,InpSymbolPeriod,InpDateStart,date\_finish,date\_buff)==-1)       {        PrintFormat("Failed to copy time values. Error code = %d",GetLastError());        return;       }  //--- free the memory occupied by the indicator     IndicatorRelease(rsi\_handle);  //--- receive the buffer size     rsi\_size=ArraySize(rsi\_buff);  //--- open the file for writing the indicator values (if the file is absent, it will be created automatically)     ResetLastError();     int file\_handle=FileOpen(InpDirectoryName+"//"+InpFileName,FILE\_READ|FILE\_WRITE|FILE\_CSV|FILE\_ANSI);     if(file\_handle!=INVALID\_HANDLE)       {        PrintFormat("%s file is available for writing",InpFileName);        PrintFormat("File path: %s\\Files\\",TerminalInfoString(TERMINAL\_DATA\_PATH));        //--- prepare additional variables        string str="";        bool   is\_formed=false;        //--- write dates of forming overbought and oversold areas        for(int i=0;i<rsi\_size;i++)          {           //--- check the indicator values           if(rsi\_buff[i]>=70 || rsi\_buff[i]<=30)             {              //--- if the value is the first one in this area              if(!is\_formed)                {                 //--- add the value and the date                 str=(string)rsi\_buff[i]+"\t"+(string)date\_buff[i];                 is\_formed=true;                }              else                 str+="\t"+(string)rsi\_buff[i]+"\t"+(string)date\_buff[i];              //--- move to the next loop iteration              continue;             }           //--- check the flag           if(is\_formed)             {              //--- the string is formed, write it to the file              FileWriteString(file\_handle,str+"\r\n");              is\_formed=false;             }          }        //--- close the file        FileClose(file\_handle);        PrintFormat("Data is written, %s file is closed",InpFileName);       }     else        PrintFormat("Failed to open %s file, Error code = %d",InpFileName,GetLastError());    } |

See also

[String Type](../../Language-Basics/Data-Types/String-Type/String-Type.md), [StringFormat](../../Conversion-Functions/StringFormat/StringFormat.md)
