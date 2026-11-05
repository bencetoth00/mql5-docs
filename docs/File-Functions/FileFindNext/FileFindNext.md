# FileFindNext

FileFindNext

The function continues the search started by [FileFindFirst()](../FileFindFirst/FileFindFirst.md).

|  |
| --- |
| bool  FileFindNext(     long      search\_handle,         // Search handle     string&   returned\_filename      // Name of the file or subdirectory found     ); |

Parameters

search\_handle

[in]  Search handle, retrieved by [FileFindFirst()](../FileFindFirst/FileFindFirst.md).

returned\_filename

[out] The name of the next file or subdirectory found. Only the file name is returned (including the extension), the directories and subdirectories are not included no matter if they are specified or not in the search filter.

Return Value

If successful returns true, otherwise false.

Example:

|  |
| --- |
| //--- display the window of input parameters when launching the script  #property script\_show\_inputs  //--- filter  input string InpFilter="\*";  //+------------------------------------------------------------------+  //| Script program start function                                    |  //+------------------------------------------------------------------+  void OnStart()    {     string file\_name;     int    i=1;  //--- receive search handle in local folder's root     long search\_handle=FileFindFirst(InpFilter,file\_name);  //--- check if FileFindFirst() function executed successfully     if(search\_handle!=INVALID\_HANDLE)       {        //--- check if the passed strings are file or directory names in the loop        do          {           ResetLastError();           //--- if this is a file, the function will return true, if it is a directory, the function will generate error ERR\_FILE\_IS\_DIRECTORY           FileIsExist(file\_name);           PrintFormat("%d : %s name = %s",i,GetLastError()==ERR\_FILE\_IS\_DIRECTORY ? "Directory" : "File",file\_name);           i++;          }        while(FileFindNext(search\_handle,file\_name));        //--- close search handle        FileFindClose(search\_handle);       }     else        Print("Files not found!");    } |

See also

[FileFindFirst](../FileFindFirst/FileFindFirst.md), [FileFindClose](../FileFindClose/FileFindClose.md)
