# FileWrite

FileWrite

The function is intended for writing of data into a CSV file, delimiter being inserted automatically unless it is equal to 0. After writing into the file, the line end character "\r\n" will be added.

|  |
| --- |
| uint  FileWrite(     int  file\_handle,   // File handle     ...                 // List of recorded parameters     ); |

Parameters

file\_handle

[in]  File descriptor returned by [FileOpen()](../FileOpen/FileOpen.md).

...

[in] The list of parameters separated by commas, to write to the file. The number of written parameters can be up to 63.

Return Value

Number of bytes written.

Note

Numbers will be converted into a text at output (see the Print() function). Data of the double type are output with the accuracy of 16 digits after the decimal point, and the data can be displayed either in traditional or in scientific format - depending on which format will be the most compact. The data of the float type are shown with 5 digits after the decimal point. To output real numbers with different precision or in a clearly specified format, use [DoubleToString()](../../Conversion-Functions/DoubleToString/DoubleToString.md).

Numbers of the bool type are displayed as "true" or "false" strings. Numbers of the datetime type are displayed as "YYYY.MM.DD HH:MI:SS".

Example:

|  |
| --- |
| //+------------------------------------------------------------------+  //|                                               Demo\_FileWrite.mq5 |  //|                        Copyright 2013, MetaQuotes Software Corp. |  //|                                              https://www.mql5.com |  //+------------------------------------------------------------------+  #property copyright "Copyright 2013, MetaQuotes Software Corp."  #property link      "https://www.mql5.com"  #property version   "1.00"  //--- show the window of input parameters when launching the script  #property script\_show\_inputs  //--- parameters for receiving data from the terminal  input string             InpSymbolName="EURUSD";           // currency pair  input ENUM\_TIMEFRAMES    InpSymbolPeriod=PERIOD\_H1;        // time frame  input int                InpFastEMAPeriod=12;              // fast EMA period  input int                InpSlowEMAPeriod=26;              // slow EMA period  input int                InpSignalPeriod=9;                // difference averaging period  input ENUM\_APPLIED\_PRICE InpAppliedPrice=PRICE\_CLOSE;      // price type  input datetime           InpDateStart=D'2012.01.01 00:00'; // data copying start date  //--- parameters for writing data to file  input string             InpFileName="MACD.csv";  // file name  input string             InpDirectoryName="Data"; // directory name  //+------------------------------------------------------------------+  //| Script program start function                                    |  //+------------------------------------------------------------------+  void OnStart()    {     datetime date\_finish; // data copying end date     bool     sign\_buff[]; // signal array (true - buy, false - sell)     datetime time\_buff[]; // array of signals' arrival time     int      sign\_size=0; // signal array size     double   macd\_buff[]; // array of indicator values     datetime date\_buff[]; // array of indicator dates     int      macd\_size=0; // size of indicator arrays  //--- end time is the current time     date\_finish=TimeCurrent();  //--- receive MACD indicator handle     ResetLastError();     int macd\_handle=iMACD(InpSymbolName,InpSymbolPeriod,InpFastEMAPeriod,InpSlowEMAPeriod,InpSignalPeriod,InpAppliedPrice);     if(macd\_handle==INVALID\_HANDLE)       {        //--- failed to receive indicator handle        PrintFormat("Error when receiving indicator handle. Error code = %d",GetLastError());        return;       }  //--- being in the loop until the indicator calculates all its values     while(BarsCalculated(macd\_handle)==-1)        Sleep(10); // pause to allow the indicator to calculate all its values  //--- copy the indicator values for a certain period of time     ResetLastError();     if(CopyBuffer(macd\_handle,0,InpDateStart,date\_finish,macd\_buff)==-1)       {        PrintFormat("Failed to copy indicator values. Error code = %d",GetLastError());        return;       }  //--- copy the appropriate time for the indicator values     ResetLastError();     if(CopyTime(InpSymbolName,InpSymbolPeriod,InpDateStart,date\_finish,date\_buff)==-1)       {        PrintFormat("Failed to copy time values. Error code = %d",GetLastError());        return;       }  //--- free the memory occupied by the indicator     IndicatorRelease(macd\_handle);  //--- receive the buffer size     macd\_size=ArraySize(macd\_buff);  //--- analyze the data and save the indicator signals to the arrays     ArrayResize(sign\_buff,macd\_size-1);     ArrayResize(time\_buff,macd\_size-1);     for(int i=1;i<macd\_size;i++)       {        //--- buy signal        if(macd\_buff[i-1]<0 && macd\_buff[i]>=0)          {           sign\_buff[sign\_size]=true;           time\_buff[sign\_size]=date\_buff[i];           sign\_size++;          }        //--- sell signal        if(macd\_buff[i-1]>0 && macd\_buff[i]<=0)          {           sign\_buff[sign\_size]=false;           time\_buff[sign\_size]=date\_buff[i];           sign\_size++;          }       }  //--- open the file for writing the indicator values (if the file is absent, it will be created automatically)     ResetLastError();     int file\_handle=FileOpen(InpDirectoryName+"//"+InpFileName,FILE\_READ|FILE\_WRITE|FILE\_CSV);     if(file\_handle!=INVALID\_HANDLE)       {        PrintFormat("%s file is available for writing",InpFileName);        PrintFormat("File path: %s\\Files\\",TerminalInfoString(TERMINAL\_DATA\_PATH));        //--- first, write the number of signals        FileWrite(file\_handle,sign\_size);        //--- write the time and values of signals to the file        for(int i=0;i<sign\_size;i++)           FileWrite(file\_handle,time\_buff[i],sign\_buff[i]);        //--- close the file        FileClose(file\_handle);        PrintFormat("Data is written, %s file is closed",InpFileName);       }     else        PrintFormat("Failed to open %s file, Error code = %d",InpFileName,GetLastError());    } |

See also

[Comment](../../Common-Functions/Comment/Comment.md), [Print](../../Common-Functions/Print/Print.md), [StringFormat](../../Conversion-Functions/StringFormat/StringFormat.md)
