# FileGetInteger

FileGetInteger

Gets an integer property of a file. There are two variants of the function.

1. Get a property by the handle of a file.

|  |
| --- |
| long  FileGetInteger(     int                         file\_handle,   // File handle     ENUM\_FILE\_PROPERTY\_INTEGER  property\_id    // Property ID     ); |

2. Get a property by the file name.

|  |
| --- |
| long  FileGetInteger(     const string                file\_name,            // File name     ENUM\_FILE\_PROPERTY\_INTEGER  property\_id,          // Property ID     bool                        common\_folder=false   // The file is viewed in a local folder (false)     );                                                // or a common folder of all terminals (true) |

Parameters

file\_handle

[in]  File descriptor returned by [FileOpen()](../FileOpen/FileOpen.md).

file\_name

[in]  File name.

property\_id

[in]  File property ID. The value can be one of the values of the [ENUM\_FILE\_PROPERTY\_INTEGER](../../Constants,-Enumerations-and-Structures/Input-Output-Constants/File-Properties/File-Properties.md) enumeration. If the second variant of the function is used, you can receive only the values of the [following properties](../../Constants,-Enumerations-and-Structures/Input-Output-Constants/File-Properties/File-Properties.md#filegetinteger_limitation): FILE\_EXISTS, FILE\_CREATE\_DATE, FILE\_MODIFY\_DATE, FILE\_ACCESS\_DATE and FILE\_SIZE.

common\_folder=false

[in]  Points to the file location. If the parameter is false, terminal data folder is viewed. Otherwise it is assumed that the file is in the shared folder of all terminals \Terminal\Common\Files ([FILE\_COMMON](../../Constants,-Enumerations-and-Structures/Input-Output-Constants/File-Opening-Flags/File-Opening-Flags.md)).

Return Value

The value of the property. In case of an error, -1 is returned. To get an error code use the [GetLastError()](../../Checkup/GetLastError/GetLastError.md) function.

If a folder is specified when getting properties by the name, the function will have error 5018 (ERR\_MQL\_FILE\_IS\_DIRECTORY) in any case, though the return value will be correct.

Note

The function always changes the error code. In case of successful completion the error code is reset to NULL.

Example:

|  |
| --- |
| //--- display the window of input parameters when launching the script  #property script\_show\_inputs  //--- input parameters  input string InpFileName="data.csv";  input string InpDirectoryName="SomeFolder";  //+------------------------------------------------------------------+  //| Script program start function                                    |  //+------------------------------------------------------------------+  void OnStart()    {     string path=InpDirectoryName+"//"+InpFileName;     long   l=0;  //--- open the file     ResetLastError();     int handle=FileOpen(path,FILE\_READ|FILE\_CSV);     if(handle!=INVALID\_HANDLE)       {        //--- print all information about the file        Print(InpFileName," file info:");        FileInfo(handle,FILE\_EXISTS,l,"bool");        FileInfo(handle,FILE\_CREATE\_DATE,l,"date");        FileInfo(handle,FILE\_MODIFY\_DATE,l,"date");        FileInfo(handle,FILE\_ACCESS\_DATE,l,"date");        FileInfo(handle,FILE\_SIZE,l,"other");        FileInfo(handle,FILE\_POSITION,l,"other");        FileInfo(handle,FILE\_END,l,"bool");        FileInfo(handle,FILE\_IS\_COMMON,l,"bool");        FileInfo(handle,FILE\_IS\_TEXT,l,"bool");        FileInfo(handle,FILE\_IS\_BINARY,l,"bool");        FileInfo(handle,FILE\_IS\_CSV,l,"bool");        FileInfo(handle,FILE\_IS\_ANSI,l,"bool");        FileInfo(handle,FILE\_IS\_READABLE,l,"bool");        FileInfo(handle,FILE\_IS\_WRITABLE,l,"bool");        //--- close the file        FileClose(handle);       }     else        PrintFormat("%s file is not opened, ErrorCode = %d",InpFileName,GetLastError());    }  //+------------------------------------------------------------------+  //| Display the value of the file property                           |  //+------------------------------------------------------------------+  void FileInfo(const int handle,const ENUM\_FILE\_PROPERTY\_INTEGER id,                long l,const string type)    {  //--- receive the property value     ResetLastError();     if((l=FileGetInteger(handle,id))!=-1)       {        //--- the value received, display it in the correct format        if(!StringCompare(type,"bool"))           Print(EnumToString(id)," = ",l ? "true" : "false");        if(!StringCompare(type,"date"))           Print(EnumToString(id)," = ",(datetime)l);        if(!StringCompare(type,"other"))           Print(EnumToString(id)," = ",l);       }     else        Print("Error, Code = ",GetLastError());    } |

See also

[File Operations](../File-Functions.md), [File Properties](../../Constants,-Enumerations-and-Structures/Input-Output-Constants/File-Properties/File-Properties.md)
