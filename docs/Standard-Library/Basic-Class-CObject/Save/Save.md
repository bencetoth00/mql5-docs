# Save

Save

Saves list element data in a file.

|  |
| --- |
| virtual bool  Save(     int  file\_handle      // File handle     ) |

Parameters

file\_handle

[in]  Handle of the binary file opened earlier using the FileOpen () function

Return Value

true - successfully completed, false - error.

Note

Save(int) method in CObject class always returns 'true' and does not perform any action. If you want to save the data of a derived class in a file, the Save(int) method should be implemented.

Example:

|  |
| --- |
| //--- example for CObject::Save(int)  #include <Object.mqh>  //---  void OnStart()    {     int    file\_handle;     CObject \*object=new CObject;     //---     if(object!=NULL)       {        printf("Object create error");        return;       }     //--- set objects data     //--- . . .     //--- open file     file\_handle=FileOpen("MyFile.bin",FILE\_WRITE|FILE\_BIN|FILE\_ANSI);     if(file\_handle>=0)       {        if(!object.Save(file\_handle))          {           //--- file save error           printf("File save: Error %d!",GetLastError());           delete object;           FileClose(file\_handle);           //---           return;          }        FileClose(file\_handle);       }     delete object;    } |
