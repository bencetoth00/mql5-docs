# FileReadString

FileReadString

The function reads a string from the current position of a file pointer in a file.

|  |
| --- |
| string  FileReadString(     int  file\_handle,     // File handle     int  length=-1        // Length of the string     ); |

Parameters

file\_handle

[in]  File descriptor returned by [FileOpen()](../FileOpen/FileOpen.md).

length=-1

[in]  Number of characters to read.

Return Value

Line read (string).

Note

When reading from a bin-file. the length of a string to read must be specified. When reading from a txt-file the string length is not required, and the string will be read from the current position to the line feed character "\r\n". When reading from a csv-file, the string length isn't required also, the string will be read from the current position till the nearest delimiter or till the text string end character.

If the file is opened with FILE\_ANSI [flag](../../Constants,-Enumerations-and-Structures/Input-Output-Constants/File-Opening-Flags/File-Opening-Flags.md), then the line read is converted to Unicode.

Example (the file obtained after executing the example for [FileWriteInteger](../FileWriteInteger/FileWriteInteger.md) function is used here)

|  |
| --- |
| //--- display the window of input parameters when launching the script  #property script\_show\_inputs  //--- parameters for data reading  input string InpFileName="Trend.bin"; // file name  input string InpDirectoryName="Data"; // directory name  //+------------------------------------------------------------------+  //| Script program start function                                    |  //+------------------------------------------------------------------+  void OnStart()    {  //--- open the file     ResetLastError();     int file\_handle=FileOpen(InpDirectoryName+"//"+InpFileName,FILE\_READ|FILE\_BIN|FILE\_ANSI);     if(file\_handle!=INVALID\_HANDLE)       {        PrintFormat("%s file is available for reading",InpFileName);        PrintFormat("File path: %s\\Files\\",TerminalInfoString(TERMINAL\_DATA\_PATH));        //--- additional variables        int    str\_size;        string str;        //--- read data from the file        while(!FileIsEnding(file\_handle))          {           //--- find out how many symbols are used for writing the time           str\_size=FileReadInteger(file\_handle,INT\_VALUE);           //--- read the string           str=FileReadString(file\_handle,str\_size);           //--- print the string           PrintFormat(str);          }        //--- close the file        FileClose(file\_handle);        PrintFormat("Data is read, %s file is closed",InpFileName);       }     else        PrintFormat("Failed to open %s file, Error code = %d",InpFileName,GetLastError());    } |

See also

[String Type](../../Language-Basics/Data-Types/String-Type/String-Type.md), [Conversion Functions](../../Conversion-Functions/Conversion-Functions.md), [FileWriteInteger](../FileWriteInteger/FileWriteInteger.md)
