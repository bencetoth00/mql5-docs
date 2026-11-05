# Load

Load

Loads list element data from a file.

|  |
| --- |
| virtual bool  Load(     int  file\_handle      // file handle     ) |

Parameters

file\_handle

[in]  Handle of the binary file opened earlier using the FileOpen() function.

Return Value

true – successfully completed, false - error.

Note

Load(int) method in the CObject class always returns 'true' and does not perform any action. If you want to load the data of a derived class from a file, the Load(int) method should be implemented.

Example:

|  |
| --- |
| //--- example for CObject::Load(int)  #include <Object.mqh>  //---  void OnStart()    {     int    file\_handle;     CObject \*object=new CObject;     //---     if(object!=NULL)       {        printf("Object create error");        return;       }     //--- open file     file\_handle=FileOpen("MyFile.bin",FILE\_READ|FILE\_BIN|FILE\_ANSI);     if(file\_handle>=0)       {        if(!object.Load(file\_handle))          {           //--- file load error           printf("File load: Error %d!",GetLastError());           delete object;           FileClose(file\_handle);           //---           return;          }        FileClose(file\_handle);       }     //--- use object      //--- . . .     delete object;    } |
