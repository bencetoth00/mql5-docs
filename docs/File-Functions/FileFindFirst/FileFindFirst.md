# FileFindFirst

FileFindFirst

The function starts the search of files or subdirectories in a directory in accordance with the specified filter.

|  |
| --- |
| long  FileFindFirst(     const string   file\_filter,          // String - search filter     string&        returned\_filename,    // Name of the file or subdirectory found     int            common\_flag=0         // Defines the search     ); |

Parameters

file\_filter

[in]  Search filter. A subdirectory (or sequence of nested subdirectories) relative to the \Files directory, in which files should be searched for, can be specified in the filter.

returned\_filename

[out]  The returned parameter, where, in case of success, the name of the first found file or subdirectory is placed. Only the file name is returned (including the extension), the directories and subdirectories are not included no matter if they are specified or not in the search filter.

common\_flag

[in] [Flag](../../Constants,-Enumerations-and-Structures/Input-Output-Constants/File-Opening-Flags/File-Opening-Flags.md) determining the location of the file. If common\_flag = FILE\_COMMON, then the file is located in a shared folder for all client terminals \Terminal\Common\Files. Otherwise, the file is located in a local folder.

Return Value

Returns handle of the object searched, which should be used for further sorting of files and subdirectories by the [FileFindNext()](../FileFindNext/FileFindNext.md) function, or [INVALID\_HANDLE](../../Constants,-Enumerations-and-Structures/Named-Constants/Other-Constants/Other-Constants.md) when there is no file and subdirectory corresponding to the filter (in the particular case - when the directory is empty). After searching, the handle must be closed using the [FileFindClose()](../FileFindClose/FileFindClose.md) function.

Note

For security reasons, work with files is strictly controlled in the MQL5 language. Files with which file operations are conducted using MQL5 means, cannot be outside the file sandbox.

Example:

|  |
| --- |
| //--- display the window of input parameters when launching the script  #property script\_show\_inputs  //--- filter  input string InpFilter="Dir1\\\*";  //+------------------------------------------------------------------+  //| Script program start function                                    |  //+------------------------------------------------------------------+  void OnStart()    {     string file\_name;     string int\_dir="";     int    i=1,pos=0,last\_pos=-1;  //--- search for the last backslash     while(!IsStopped())       {        pos=StringFind(InpFilter,"\\",pos+1);        if(pos>=0)           last\_pos=pos;        else           break;       }  //--- the filter contains the folder name     if(last\_pos>=0)        int\_dir=StringSubstr(InpFilter,0,last\_pos+1);  //--- get the search handle in the root of the local folder     long search\_handle=FileFindFirst(InpFilter,file\_name);  //--- check if the FileFindFirst() is executed successfully     if(search\_handle!=INVALID\_HANDLE)       {        //--- in a loop, check if the passed strings are the names of files or directories        do          {           ResetLastError();           //--- if it's a file, the function returns true, and if it's a directory, it returns error ERR\_FILE\_IS\_DIRECTORY           FileIsExist(int\_dir+file\_name);           PrintFormat("%d : %s name = %s",i,GetLastError()==ERR\_FILE\_IS\_DIRECTORY ? "Directory" : "File",file\_name);           i++;          }        while(FileFindNext(search\_handle,file\_name));        //--- close the search handle        FileFindClose(search\_handle);       }     else        Print("Files not found!");    } |

See also

[FileFindNext](../FileFindNext/FileFindNext.md), [FileFindClose](../FileFindClose/FileFindClose.md)
