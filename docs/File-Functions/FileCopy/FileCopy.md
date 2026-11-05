# FileCopy

FileCopy

The function copies the original file from a local or shared folder to another file.

|  |
| --- |
| bool  FileCopy(     const string  src\_file\_name,     // Name of a source file     int           common\_flag,       // Location     const string  dst\_file\_name,     // Name of the destination file     int           mode\_flags         // Access mode     ); |

Parameters

src\_file\_name

[in]  File name to copy.

common\_flag

[in] [Flag](../../Constants,-Enumerations-and-Structures/Input-Output-Constants/File-Opening-Flags/File-Opening-Flags.md) determining the location of the file. If common\_flag = FILE\_COMMON, then the file is located in a shared folder for all client terminals \Terminal\Common\Files. Otherwise, the file is located in a local folder (for example, common\_flag=0).

dst\_file\_name

[in]  Result file name.

mode\_flags

[in] [Access flags](../../Constants,-Enumerations-and-Structures/Input-Output-Constants/File-Opening-Flags/File-Opening-Flags.md). The parameter can contain only 2 flags: FILE\_REWRITE and/or FILE\_COMMON - other flags are ignored. If the file already exists, and the FILE\_REWRITE flag hasn't been specified, then the file will not be rewritten, and the function will return false.

Return Value

In case of failure the function returns false.

Note

For security reasons, work with files is strictly controlled in the MQL5 language. Files with which file operations are conducted using MQL5 means, cannot be outside the file sandbox.

If the new file already exists, the copy will be made depending on the availability of the FILE\_REWRITE flag in the mode\_flags parameter.

Example:

|  |
| --- |
| //--- display the window of input parameters when launching the script  #property script\_show\_inputs  //--- input parameters  input string InpSrc="source.txt";       // source  input string InpDst="destination.txt";  // copy  input int    InpEncodingType=FILE\_ANSI; // ANSI=32 or UNICODE=64  //+------------------------------------------------------------------+  //| Script program start function                                    |  //+------------------------------------------------------------------+  void OnStart()    {  //--- display the source contents (it must exist)     if(!FileDisplay(InpSrc))        return;  //--- check if the copy file already exists (may not be created)     if(!FileDisplay(InpDst))       {        //--- the copy file does not exist, copying without FILE\_REWRITE flag (correct copying)        if(FileCopy(InpSrc,0,InpDst,0))           Print("File is copied!");        else           Print("File is not copied!");       }     else       {        //--- the copy file already exists, try to copy without FILE\_REWRITE flag (incorrect copying)        if(FileCopy(InpSrc,0,InpDst,0))           Print("File is copied!");        else           Print("File is not copied!");        //--- InpDst file's contents remains the same        FileDisplay(InpDst);        //--- copy once more with FILE\_REWRITE flag (correct copying if the file exists)        if(FileCopy(InpSrc,0,InpDst,FILE\_REWRITE))           Print("File is copied!");        else           Print("File is not copied!");       }  //--- receive InpSrc file copy     FileDisplay(InpDst);    }  //+------------------------------------------------------------------+  //| Read the file contents                                           |  //+------------------------------------------------------------------+  bool FileDisplay(const string file\_name)    {  //--- reset the error value     ResetLastError();  //--- open the file     int file\_handle=FileOpen(file\_name,FILE\_READ|FILE\_TXT|InpEncodingType);     if(file\_handle!=INVALID\_HANDLE)       {        //--- display the file contents in the loop        Print("+---------------------+");        PrintFormat("File name = %s",file\_name);        while(!FileIsEnding(file\_handle))           Print(FileReadString(file\_handle));        Print("+---------------------+");        //--- close the file        FileClose(file\_handle);        return(true);       }  //--- failed to open the file     PrintFormat("%s is not opened, error = %d",file\_name,GetLastError());     return(false);    } |
