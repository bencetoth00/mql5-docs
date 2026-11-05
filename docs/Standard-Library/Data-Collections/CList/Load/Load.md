# Load

Load

Loads list data from the file.

|  |
| --- |
| virtual bool  Load(     int  file\_handle      // file handle     ) |

Parameters

file\_handle

[in] Handle of the binary file previously opened using the FileOpen () function.

Return Value

true - successfully completed, false - error.

Note

When reading list elements from the file, the [CList::CreateElement(int)](../CreateElement/CreateElement.md) method is called to create each element.

Example:

|  |
| --- |
| //--- example for CLoad::Load(int)   #include <Arrays\List.mqh>   //---   void OnStart()     {      int    file\_handle;      CList \*list=new CList;      //---      if(list!=NULL)        {         printf("Object create error");         return;        }      //--- open file      file\_handle=FileOpen("MyFile.bin",FILE\_READ|FILE\_BIN|FILE\_ANSI);      if(file\_handle>=0)        {         if(!list.Load(file\_handle))           {            //--- file load error            printf("File load: Error %d!",GetLastError());            delete list;            FileClose(file\_handle);            //---            return;           }         FileClose(file\_handle);        }      //--- use list elements      //--- . . .      //--- delete list      delete list;     } |
