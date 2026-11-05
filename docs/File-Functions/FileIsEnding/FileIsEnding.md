# FileIsEnding

FileIsEnding

Defines the end of a file in the process of reading.

|  |
| --- |
| bool  FileIsEnding(     int  file\_handle      // File handle     ); |

Parameters

file\_handle

[in]  File descriptor returned by [FileOpen()](../FileOpen/FileOpen.md).

Return Value

The function returns true if the file end has been reached in the process of reading or moving of the file pointer.

Note

To define the end of the file, the function tries to read the next string from it. If the string does not exist, the function returns true, otherwise it returns false.

Example:

|  |
| --- |
| //--- show the window of input parameters when launching the script  #property script\_show\_inputs  //--- input parameters  input string InpFileName="file.txt";    // file name  input string InpDirectoryName="Data";   // directory name  input int    InpEncodingType=FILE\_ANSI; // ANSI=32 or UNICODE=64  //+------------------------------------------------------------------+  //| Script program start function                                    |  //+------------------------------------------------------------------+  void OnStart()    {  //--- print the path to the file we are going to use     PrintFormat("Working %s\\Files\\ folder",TerminalInfoString(TERMINAL\_DATA\_PATH));  //--- reset the error value     ResetLastError();  //--- open the file for reading (if the file does not exist, the error will occur)     int file\_handle=FileOpen(InpDirectoryName+"//"+InpFileName,FILE\_READ|FILE\_TXT|InpEncodingType);     if(file\_handle!=INVALID\_HANDLE)       {        //--- print the file contents        while(!FileIsEnding(file\_handle))           Print(FileReadString(file\_handle));        //--- close the file        FileClose(file\_handle);       }     else        PrintFormat("Error, code = %d",GetLastError());    } |
