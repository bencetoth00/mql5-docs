# FileIsExist

FileIsExist

Checks the existence of a file.

|  |
| --- |
| bool  FileIsExist(     const string  file\_name,       // File name     int           common\_flag=0    // Search area     ); |

Parameters

file\_name

[in]  The name of the file being checked

common\_flag=0

[in] [Flag](../../Constants,-Enumerations-and-Structures/Input-Output-Constants/File-Opening-Flags/File-Opening-Flags.md) determining the location of the file. If common\_flag = FILE\_COMMON, then the file is located in a shared folder for all client terminals \Terminal\Common\Files. Otherwise, the file is located in a local folder.

Return Value

Returns true, if the specified file exists.

Note

Checked file can turn out to be a subdirectory. In this case, FileIsExist() function will return false, while error 5018 will be logged in \_LastError variable - "This is a directory, not a file" (see example for [FileFindFirst](../FileFindFirst/FileFindFirst.md) function).

For security reasons, work with files is strictly controlled in the MQL5 language. Files with which file operations are conducted using MQL5 means, cannot be outside the file sandbox.

If common\_flag = FILE\_COMMON, then the function looks for the file in a shared folder for all client terminals \Terminal\Common\Files, otherwise the function looks for a file in a local folder (MQL5\Files or MQL5\Tester\Files in the case of testing).

Example:

|  |
| --- |
| //--- show the window of input parameters when launching the script  #property script\_show\_inputs  //--- date for old files  input datetime InpFilesDate=D'2013.01.01 00:00';  //+------------------------------------------------------------------+  //| Script program start function                                    |  //+------------------------------------------------------------------+  void OnStart()    {     string   file\_name;      // variable for storing file names     string   filter="\*.txt"; // filter for searching the files     datetime create\_date;    // file creation date     string   files[];        // list of file names     int      def\_size=25;    // array size by default     int      size=0;         // number of files  //--- allocate memory for the array     ArrayResize(files,def\_size);  //--- receive the search handle in the local folder's root     long search\_handle=FileFindFirst(filter,file\_name);  //--- check if FileFindFirst() executed successfully     if(search\_handle!=INVALID\_HANDLE)       {        //--- searching files in the loop        do          {           files[size]=file\_name;           //--- increase the array size           size++;           if(size==def\_size)             {              def\_size+=25;              ArrayResize(files,def\_size);             }           //--- reset the error value           ResetLastError();           //--- receive the file creation date           create\_date=(datetime)FileGetInteger(file\_name,FILE\_CREATE\_DATE,false);           //--- check if the file is old           if(create\_date<InpFilesDate)             {              PrintFormat("%s file deleted!",file\_name);              //--- delete the old file              FileDelete(file\_name);             }          }        while(FileFindNext(search\_handle,file\_name));        //--- close the search handle        FileFindClose(search\_handle);       }     else       {        Print("Files not found!");        return;       }  //--- check what files have remained     PrintFormat("Results:");     for(int i=0;i<size;i++)       {        if(FileIsExist(files[i]))           PrintFormat("%s file exists!",files[i]);        else           PrintFormat("%s file deleted!",files[i]);       }    } |

See also

[FileFindFirst](../FileFindFirst/FileFindFirst.md)
