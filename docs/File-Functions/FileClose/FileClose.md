# FileClose

FileClose

Close the file previously opened by [FileOpen()](../FileOpen/FileOpen.md).

|  |
| --- |
| void  FileClose(     int  file\_handle      // File handle     ); |

Parameters

file\_handle

[in]  File descriptor returned by FileOpen().

Return Value

No value returned.

Example:

|  |
| --- |
| //--- show the window of input parameters when launching the script  #property script\_show\_inputs  //--- input parameters  input string InpFileName="file.txt";    // file name  input string InpDirectoryName="Data";   // directory name  input int    InpEncodingType=FILE\_ANSI; // ANSI=32 or UNICODE=64  //+------------------------------------------------------------------+  //| Script program start function                                    |  //+------------------------------------------------------------------+  void OnStart()    {  //--- print the path to the file we are going to use     PrintFormat("Working %s\\Files\\ folder",TerminalInfoString(TERMINAL\_DATA\_PATH));  //--- reset the error value     ResetLastError();  //--- open the file for reading (if the file does not exist, the error will occur)     int file\_handle=FileOpen(InpDirectoryName+"//"+InpFileName,FILE\_READ|FILE\_TXT|InpEncodingType);     if(file\_handle!=INVALID\_HANDLE)       {        //--- print the file contents        while(!FileIsEnding(file\_handle))           Print(FileReadString(file\_handle));        //--- close the file        FileClose(file\_handle);       }     else        PrintFormat("Error, code = %d",GetLastError());    } |
