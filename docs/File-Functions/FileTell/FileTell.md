# FileTell

FileTell

The file returns the current position of the file pointer of an open file.

|  |
| --- |
| ulong  FileTell(     int  file\_handle    // File handle     ); |

Parameters

file\_handle

[in]  File descriptor returned by [FileOpen()](../FileOpen/FileOpen.md).

Return Value

Current position of the file descriptor in bytes from the beginning of the file.

Note

To obtain information about the [error](FileTell.md) call [GetLastError()](../../Checkup/GetLastError/GetLastError.md).

Example:

|  |
| --- |
| //+------------------------------------------------------------------+  //|                                                Demo\_FileTell.mq5 |  //|                        Copyright 2013, MetaQuotes Software Corp. |  //|                                              https://www.mql5.com |  //+------------------------------------------------------------------+  #property copyright "Copyright 2013, MetaQuotes Software Corp."  #property link      "https://www.mql5.com"  #property version   "1.00"  //--- display the window of input parameters when launching the script  #property script\_show\_inputs  //--- input parameters  input string InpFileName="file.txt";    // file name  input string InpDirectoryName="Data";   // directory name  input int    InpEncodingType=FILE\_ANSI; // ANSI=32 or UNICODE=64  //+------------------------------------------------------------------+  //| Script program start function                                    |  //+------------------------------------------------------------------+  void OnStart()    {  //--- specify the value of the variable for generating random numbers     \_RandomSeed=GetTickCount();  //--- variables for positions of the strings' start points     ulong pos[];     int   size;  //--- reset the error value     ResetLastError();  //--- open the file     int file\_handle=FileOpen(InpDirectoryName+"//"+InpFileName,FILE\_READ|FILE\_TXT|InpEncodingType);     if(file\_handle!=INVALID\_HANDLE)       {        PrintFormat("%s file is available for reading",InpFileName);        //--- receive start position for each string in the file        GetStringPositions(file\_handle,pos);        //--- define the number of strings in the file        size=ArraySize(pos);        if(!size)          {           //--- stop if the file does not have strings           PrintFormat("%s file is empty!",InpFileName);           FileClose(file\_handle);           return;          }        //--- make a random selection of a string number        int ind=MathRand()%size;        //--- shift position to the starting point of the string        FileSeek(file\_handle,pos[ind],SEEK\_SET);        //--- read and print the string with ind number        PrintFormat("String text with %d number: \"%s\"",ind,FileReadString(file\_handle));        //--- close the file        FileClose(file\_handle);        PrintFormat("%s file is closed",InpFileName);       }     else        PrintFormat("Failed to open %s file, Error code = %d",InpFileName,GetLastError());    }  //+-------------------------------------------------------------------------------+  //| The function defines starting points for each of the strings in the file and  |  //| places them in arr array                                                      |  //+-------------------------------------------------------------------------------+  void GetStringPositions(const int handle,ulong &arr[])    {  //--- default array size     int def\_size=127;  //--- allocate memory for the array     ArrayResize(arr,def\_size);  //--- string counter     int i=0;  //--- if this is not the file's end, then there is at least one string     if(!FileIsEnding(handle))       {        arr[i]=FileTell(handle);        i++;       }     else        return; // the file is empty, exit  //--- define the shift in bytes depending on encoding     int shift;     if(FileGetInteger(handle,FILE\_IS\_ANSI))        shift=1;     else        shift=2;  //--- go through the strings in the loop     while(1)       {        //--- read the string        FileReadString(handle);        //--- check for the file end        if(!FileIsEnding(handle))          {           //--- store the next string's position           arr[i]=FileTell(handle)+shift;           i++;           //--- increase the size of the array if it is overflown           if(i==def\_size)             {              def\_size+=def\_size+1;              ArrayResize(arr,def\_size);             }          }        else           break; // end of the file, exit       }  //--- define the actual size of the array     ArrayResize(arr,i);    } |
