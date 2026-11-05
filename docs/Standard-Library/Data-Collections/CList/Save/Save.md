# Save

Save

Saves list data in the file.

|  |
| --- |
| virtual bool  Save(     int  file\_handle      // file handle     ) |

Parameters

file\_handle

[in] Handle of the binary file previously opened using the FileOpen () function.

Return Value

true - successfully completed, false - error.

Example:

|  |
| --- |
| //--- example for CList::Save(int)   #include <Arrays\List.mqh>   //---   void OnStart()     {      int    file\_handle;      CList \*list=new CList;      //---      if(list!=NULL)        {         printf("Object create error");         return;        }      //--- add lists elements      //--- . . .      //--- open file      file\_handle=FileOpen("MyFile.bin",FILE\_WRITE|FILE\_BIN|FILE\_ANSI);      if(file\_handle>=0)        {         if(!list.Save(file\_handle))           {            //--- file save error            printf("File save: Error %d!",GetLastError());            delete list;            FileClose(file\_handle);            //---            return;           }         FileClose(file\_handle);        }      //--- delete list      delete list;     } |
