# Save

Save

Saves data array in the file.

|  |
| --- |
| virtual bool  Save(     int  file\_handle      // file handle     ) |

Parameters

file\_handle

[in] Handle of the binary file previously opened using the FileOpen(...) function.

Return Value

true – successfully completed, false - error.

Example:

|  |
| --- |
| //--- example for CArrayDouble::Save(int)  #include <Arrays\ArrayDouble.mqh>  //---  void OnStart()    {     int           file\_handle;     CArrayDouble \*array=new CArrayDouble;     //---     if(array!=NULL)       {        printf("Object create error");        return;       }     //--- add 100 arrays elements     for(int i=0;i<100;i++)       {        array.Add(i);       }     //--- open file     file\_handle=FileOpen("MyFile.bin",FILE\_WRITE|FILE\_BIN|FILE\_ANSI);     if(file\_handle>=0)       {        if(!array.Save(file\_handle))          {           //--- file save error           printf("File save: Error %d!",GetLastError());           delete array;           FileClose(file\_handle);           //---           return;          }        FileClose(file\_handle);       }     //--- delete array     delete array;    } |
