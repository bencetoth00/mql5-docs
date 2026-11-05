# Load

Load

Loads data array from the file.

|  |
| --- |
| virtual bool  Load(     int  file\_handle      // file handle     ) |

Parameters

file\_handle

[in]  Handle of the binary file previously opened using the FileOpen(...) function.

Return Value

true – successfully completed, false - error.

Example:

|  |
| --- |
| //--- example for CArrayShort::Load(int)  #include <Arrays\ArrayShort.mqh>  //---  void OnStart()    {     int          file\_handle;     CArrayShort \*array=new CArrayShort;     //---     if(array!=NULL)       {        printf("Object create error");        return;       }     //--- open file     file\_handle=FileOpen("MyFile.bin",FILE\_READ|FILE\_BIN|FILE\_ANSI);     if(file\_handle>=0)       {        if(!array.Load(file\_handle))          {           //--- file load error           printf("File load: Error %d!",GetLastError());           delete array;           FileClose(file\_handle);           //---           return;          }        FileClose(file\_handle);       }     //--- use arrays elements     for(int i=0;i<array.Total();i++)       {        printf("Element[%d] = %d",i,array.At(i));       }     delete array;    } |
