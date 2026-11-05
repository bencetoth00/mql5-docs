# FileSave

FileSave

Writes to a binary file all elements of an array passed as a parameter. The function allows you to quickly write arrays of numeric types or simple structures as one string.

|  |
| --- |
| bool  FileSave(     const string  file\_name,         // File name     void&         buffer[],          // An array of numeric types or simple structures     int           common\_flag=0      // A file flag, by default files are written to <data\_folder>\MQL5\Files\     ); |

Parameters

file\_name

[in]  The name of the file, to the data array will be written.

buffer

[in]  An array of numeric types or [simple structures](../../Language-Basics/Data-Types/Structures,-Classes-and-Interfaces/Structures,-Classes-and-Interfaces.md#simple_structure).

common\_flag=0

[in] [A file flag](../../Constants,-Enumerations-and-Structures/Input-Output-Constants/File-Opening-Flags/File-Opening-Flags.md) indicating the operation mode. If the parameter is not specified, the file will be written to the subfolder MQL5\Files (or to <testing\_agent\_directory>\MQL5\Files in case of testing).

Return Value

In case of failure returns false.

Example:

|  |
| --- |
| //+------------------------------------------------------------------+  //|                                                Demo\_FileSave.mq5 |  //|                        Copyright 2016, MetaQuotes Software Corp. |  //|                                             https://www.mql5.com |  //+------------------------------------------------------------------+  #property copyright "Copyright 2000-2024, MetaQuotes Ltd."  #property link      "https://www.mql5.com"  #property version   "1.00"  #property script\_show\_inputs  //--- input parameters  input int      ticks\_to\_save=1000; // Number of ticks  //+------------------------------------------------------------------+  //| Script program start function                                    |  //+------------------------------------------------------------------+  void OnStart()    {     string  filename=\_Symbol+"\_ticks.bin";     MqlTick ticks[];  u//---     int copied=CopyTicks(\_Symbol,ticks,COPY\_TICKS\_ALL,0,ticks\_to\_save);     if(copied!=-1)       {        PrintFormat(" CopyTicks(%s) copied %d ticks",\_Symbol,copied);        //--- If the tick history is synchronized, the error code is equal to zero        if(!GetLastError()==0)           PrintFormat("%s: Ticks are not synchronized, error=%d",\_Symbol,copied,\_LastError);        //---  Writing ticks to a file        if(!FileSave(filename,ticks,FILE\_COMMON))           PrintFormat("FileSave() failed, error=%d",GetLastError());       }     else        PrintFormat("Failed CopyTicks(%s), Error=",\_Symbol,GetLastError());  //--- Now reading the ticks back to the file     ArrayFree(ticks);     long count=FileLoad(filename,ticks,FILE\_COMMON);     if(count!=-1)       {        Print("Time\tBid\tAsk\tLast\tVolume\tms\tflags");        for(int i=0;i<count;i++)          {           PrintFormat("%s.%03I64u:\t%G\t%G\t%G\t%I64u\t0x%04x",           TimeToString(ticks[i].time,TIME\_DATE|TIME\_SECONDS),ticks[i].time\_msc%1000,           ticks[i].bid,ticks[i].ask,ticks[i].last,ticks[i].volume,ticks[i].flags);          }       }    } |

See also

[Structures and Classes](../../Language-Basics/Data-Types/Structures,-Classes-and-Interfaces/Structures,-Classes-and-Interfaces.md), [FileWriteArray](../FileWriteArray/FileWriteArray.md), [FileWriteStruct](../FileWriteStruct/FileWriteStruct.md), [FileLoad](../FileLoad/FileLoad.md), [FileWrite](../FileWrite/FileWrite.md)
