# FileReadStruct

FileReadStruct

The function reads contents into a structure passed as a parameter from a binary-file, starting with the current position of the file pointer.

|  |
| --- |
| uint  FileReadStruct(     int          file\_handle,        // file handle     const void&  struct\_object,      // target structure to which the contents are read     int          size=-1             // structure size in bytes     ); |

Parameters

file\_handle

[in] File descriptor of an open bin-file.

struct\_object

[out]  The object of this structure. The structure should not contain strings, [dynamic arrays](../../Language-Basics/Data-Types/Dynamic-Array-Object/Dynamic-Array-Object.md) or [virtual functions](../../Language-Basics/Object-Oriented-Programming/Virtual-Functions/Virtual-Functions.md).

size=-1

[in]  Number of bytes that should be read. If size is not specified or the indicated value is greater than the size of the structure, the exact size of the specified structure is used.

Return Value

If successful the function returns the number of bytes read. File pointer is moved by the same number of bytes.

Example (the file obtained after using the example for [FileWriteStruct](../FileWriteStruct/FileWriteStruct.md) function is used here)

|  |
| --- |
| //+------------------------------------------------------------------+  //|                                          Demo\_FileReadStruct.mq5 |  //|                        Copyright 2013, MetaQuotes Software Corp. |  //|                                              https://www.mql5.com |  //+------------------------------------------------------------------+  #property copyright "Copyright 2013, MetaQuotes Software Corp."  #property link      "https://www.mql5.com"  #property version   "1.00"  #property indicator\_separate\_window  #property indicator\_buffers 4  #property indicator\_plots   1  //---- plot Label1  #property indicator\_label1  "Candles"  #property indicator\_type1   DRAW\_CANDLES  #property indicator\_color1  clrOrange  #property indicator\_style1  STYLE\_SOLID  #property indicator\_width1  1  #property indicator\_separate\_window  //--- parameters for receiving data  input string  InpFileName="EURUSD.txt"; // file name  input string  InpDirectoryName="Data";  // directory name  //+------------------------------------------------------------------+  //| Structure for storing candlestick data                           |  //+------------------------------------------------------------------+  struct candlesticks    {     double            open;  // open price     double            close; // close price     double            high;  // high price     double            low;   // low price     datetime          date;  // date    };  //--- indicator buffers  double       open\_buff[];  double       close\_buff[];  double       high\_buff[];  double       low\_buff[];  //--- global variables  candlesticks cand\_buff[];  int          size=0;  int          ind=0;  //+------------------------------------------------------------------+  //| Custom indicator initialization function                         |  //+------------------------------------------------------------------+  int OnInit()    {     int default\_size=100;     ArrayResize(cand\_buff,default\_size);  //--- open the file     ResetLastError();     int file\_handle=FileOpen(InpDirectoryName+"//"+InpFileName,FILE\_READ|FILE\_BIN|FILE\_COMMON);     if(file\_handle!=INVALID\_HANDLE)       {        PrintFormat("%s file is available for reading",InpFileName);        PrintFormat("File path: %s\\Files\\",TerminalInfoString(TERMINAL\_COMMONDATA\_PATH));        //--- read data from the file        while(!FileIsEnding(file\_handle))          {           //--- write data to the array           FileReadStruct(file\_handle,cand\_buff[size]);           size++;           //--- check if the array is overflown           if(size==default\_size)             {              //--- increase the array size              default\_size+=100;              ArrayResize(cand\_buff,default\_size);             }          }        //--- close the file        FileClose(file\_handle);        PrintFormat("Data is read, %s file is closed",InpFileName);       }     else       {        PrintFormat("Failed to open %s file, Error code = %d",InpFileName,GetLastError());        return(INIT\_FAILED);       }  //--- indicator buffers mapping     SetIndexBuffer(0,open\_buff,INDICATOR\_DATA);     SetIndexBuffer(1,high\_buff,INDICATOR\_DATA);     SetIndexBuffer(2,low\_buff,INDICATOR\_DATA);     SetIndexBuffer(3,close\_buff,INDICATOR\_DATA);  //--- empty value     PlotIndexSetDouble(0,PLOT\_EMPTY\_VALUE,0);  //---     return(INIT\_SUCCEEDED);    }  //+------------------------------------------------------------------+  //| Custom indicator iteration function                              |  //+------------------------------------------------------------------+  int OnCalculate(const int rates\_total,                  const int prev\_calculated,                  const datetime &time[],                  const double &open[],                  const double &high[],                  const double &low[],                  const double &close[],                  const long &tick\_volume[],                  const long &volume[],                  const int &spread[])    {     ArraySetAsSeries(time,false);  //--- the loop for the candlesticks that have not been handled yet     for(int i=prev\_calculated;i<rates\_total;i++)       {        //--- 0 by default        open\_buff[i]=0;        close\_buff[i]=0;        high\_buff[i]=0;        low\_buff[i]=0;        //--- check if any data is still present        if(ind<size)          {           for(int j=ind;j<size;j++)             {              //--- if dates coincide, the value from the file is used              if(time[i]==cand\_buff[j].date)                {                 open\_buff[i]=cand\_buff[j].open;                 close\_buff[i]=cand\_buff[j].close;                 high\_buff[i]=cand\_buff[j].high;                 low\_buff[i]=cand\_buff[j].low;                 //--- increase the counter                 ind=j+1;                 break;                }             }          }       }  //--- return value of prev\_calculated for next call     return(rates\_total);    } |

See also

[Structures and classes](../../Language-Basics/Data-Types/Structures,-Classes-and-Interfaces/Structures,-Classes-and-Interfaces.md), [FileWriteStruct](../FileWriteStruct/FileWriteStruct.md)
