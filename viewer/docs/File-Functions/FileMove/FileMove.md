# FileMove


Moves a file from a local or shared folder to another folder.

```cpp
bool  FileMove(
   const string  src_file_name,    // File name for the move operation
   int           common_flag,      // Location
   const string  dst_file_name,    // Name of the destination file
   int           mode_flags        // Access mode
   );
```

Parameters

src\_file\_name

[in]  File name to move/rename.

common\_flag

[in] [Flag](../../Constants,-Enumerations-and-Structures/Input-Output-Constants/File-Opening-Flags/File-Opening-Flags.md) determining the location of the file. If common\_flag = FILE\_COMMON, then the file is located in a shared folder for all client terminals \Terminal\Common\Files. Otherwise, the file is located in a local folder (common\_flag=0).

dst\_file\_name

[in]  File name after operation

mode\_flags

[in] [Access flags](../../Constants,-Enumerations-and-Structures/Input-Output-Constants/File-Opening-Flags/File-Opening-Flags.md). The parameter can contain only 2 flags: FILE\_REWRITE and/or FILE\_COMMON - other flags are ignored. If the file already exists and the FILE\_REWRITE flag isn't specified, the file will not be rewritten, and the function will return false.

Return Value

In case of failure the function returns false.

Note

For security reasons, work with files is strictly controlled in the MQL5 language. Files with which file operations are conducted using MQL5 means, cannot be outside the file sandbox.

If the new file already exists, the copy will be made depending on the availability of the FILE\_REWRITE flag in the mode\_flags parameter.

Example:

```cpp
//--- display the window of input parameters when launching the script
#property script_show_inputs
//--- input parameters
input string InpSrcName="data.txt";
input string InpDstName="newdata.txt";
input string InpSrcDirectory="SomeFolder";
input string InpDstDirectory="OtherFolder";
//+------------------------------------------------------------------+
//| Script program start function                                    |
//+------------------------------------------------------------------+
void OnStart()
  {
   string local=TerminalInfoString(TERMINAL_DATA_PATH);
   string common=TerminalInfoString(TERMINAL_COMMONDATA_PATH);
//--- receive file paths
   string src_path;
   string dst_path;
   StringConcatenate(src_path,InpSrcDirectory,"//",InpSrcName);
   StringConcatenate(dst_path,InpDstDirectory,"//",InpDstName);
//--- check if the source file exists (if not - exit)
   if(FileIsExist(src_path))
      PrintFormat("%s file exists in the %s\\Files\\%s folder",InpSrcName,local,InpSrcDirectory);
   else
     {
      PrintFormat("Error, %s source file not found",InpSrcName);
      return;
     }
//--- check if the result file already exists
   if(FileIsExist(dst_path,FILE_COMMON))
     {
      PrintFormat("%s file exists in the %s\\Files\\%s folder",InpDstName,common,InpDstDirectory);
      //--- file exists, moving should be performed with FILE_REWRITE flag
      ResetLastError();
      if(FileMove(src_path,0,dst_path,FILE_COMMON|FILE_REWRITE))
         PrintFormat("%s file moved",InpSrcName);
      else
         PrintFormat("Error! Code = %d",GetLastError());
     }
   else
     {
      PrintFormat("%s file does not exist in the %s\\Files\\%s folder",InpDstName,common,InpDstDirectory);
      //--- the file does not exist, moving should be performed without FILE_REWRITE flag
      ResetLastError();
      if(FileMove(src_path,0,dst_path,FILE_COMMON))
         PrintFormat("%s file moved",InpSrcName);
      else
         PrintFormat("Error! Code = %d",GetLastError());
     }
//--- the file is moved; let's check it out
   if(FileIsExist(dst_path,FILE_COMMON) && !FileIsExist(src_path,0))
      Print("Success!");
   else
      Print("Error!");
  }
```

See also

[FileIsExist](../FileIsExist/FileIsExist.md)