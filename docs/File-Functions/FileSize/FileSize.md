# FileSize

FileSize

The function returns the file size in bytes.

|  |
| --- |
| ulong  FileSize(     int  file\_handle    // File handle     ); |

Parameters

file\_handle

[in]  File descriptor returned by [FileOpen()](../FileOpen/FileOpen.md).

Return Value

The value of type int.

Note

To obtain information about the [error](../../Constants,-Enumerations-and-Structures/Codes-of-Errors-and-Warnings/Runtime-Errors/Runtime-Errors.md) call [GetLastError()](../../Checkup/GetLastError/GetLastError.md).

Example:

|  |
| --- |
| //--- show the window of input parameters when launching the script  #property script\_show\_inputs  //--- input parameters  input ulong  InpThresholdSize=20;        // file threshold size in kilobytes  input string InpBigFolderName="big";     // folder for large files  input string InpSmallFolderName="small"; // folder for small files  //+------------------------------------------------------------------+  //| Script program start function                                    |  //+------------------------------------------------------------------+  void OnStart()    {     string   file\_name;      // variable for storing file names     string   filter="\*.csv"; // filter for searching the files     ulong    file\_size=0;    // file size in bytes     int      size=0;         // number of files  //--- print the path to the file we are going to work with     PrintFormat("Working in %s\\Files\\ folder",TerminalInfoString(TERMINAL\_COMMONDATA\_PATH));  //--- receive the search handle in common folder's root of all terminals     long search\_handle=FileFindFirst(filter,file\_name,FILE\_COMMON);  //--- check if FileFindFirst() has been executed successfully     if(search\_handle!=INVALID\_HANDLE)       {        //--- move files in the loop according to their size        do          {           //--- open the file           ResetLastError();           int file\_handle=FileOpen(file\_name,FILE\_READ|FILE\_CSV|FILE\_COMMON);           if(file\_handle!=INVALID\_HANDLE)             {              //--- receive the file size              file\_size=FileSize(file\_handle);              //--- close the file              FileClose(file\_handle);             }           else             {              PrintFormat("Failed to open %s file, Error code = %d",file\_name,GetLastError());              continue;             }           //--- print the file size           PrintFormat("Size of %s file is equal to %d bytes",file\_name,file\_size);           //--- define the path for moving the file           string path;           if(file\_size>InpThresholdSize\*1024)              path=InpBigFolderName+"//"+file\_name;           else              path=InpSmallFolderName+"//"+file\_name;           //--- move the file           ResetLastError();           if(FileMove(file\_name,FILE\_COMMON,path,FILE\_REWRITE|FILE\_COMMON))              PrintFormat("%s file is moved",file\_name);           else              PrintFormat("Error, code = %d",GetLastError());          }        while(FileFindNext(search\_handle,file\_name));        //--- close the search handle        FileFindClose(search\_handle);       }     else        Print("Files not found!");    } |
