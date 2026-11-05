# FileFindClose

FileFindClose

The function closes the search handle.

|  |
| --- |
| void  FileFindClose(     long  search\_handle      //  Search handle     ); |

Parameters

search\_handle

[in]  Search handle, retrieved by [FileFindFirst()](../FileFindFirst/FileFindFirst.md).

Return Value

No value returned.

Note

Function must be called to free up system resources.

Example:

|  |
| --- |
| //--- display the window of input parameters when launching the script  #property script\_show\_inputs  //--- filter  input string InpFilter="\*";  //+------------------------------------------------------------------+  //| Script program start function                                    |  //+------------------------------------------------------------------+  void OnStart()    {     string file\_name;     int    i=1;  //--- receive search handle in local folder's root     long search\_handle=FileFindFirst(InpFilter,file\_name);  //--- check if FileFindFirst() function executed successfully     if(search\_handle!=INVALID\_HANDLE)       {        //--- check if the passed strings are file or directory names in the loop        do          {           ResetLastError();           //--- if this is a file, the function will return true, if it is a directory, the function will generate error 5018           FileIsExist(file\_name);           PrintFormat("%d : %s name = %s",i,GetLastError()==5018 ? "Directory" : "File",file\_name);           i++;          }        while(FileFindNext(search\_handle,file\_name));        //--- close search handle        FileFindClose(search\_handle);       }     else        Print("Files not found!");    } |

See also

[FileFindFirst](../FileFindFirst/FileFindFirst.md), [FileFindNext](../FileFindNext/FileFindNext.md)
