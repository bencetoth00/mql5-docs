# Save

Save

Saves parameters of the object in the file.

|  |
| --- |
| virtual bool  Save(     int  file\_handle      // file handle     ) |

Parameters

file\_handle

[in]  Handle of the file previously opened using the function FileOpen (...).

Return Value

true - successfully completed, false - error.

Example:

|  |
| --- |
| //--- example for CChartObject::Save     #include <ChartObjects\ChartObject.mqh>     //---     void OnStart()       {        int          file\_handle;        CChartObject object=new CChartObject;        //--- set object parameters        //--- . . .        //--- open file        file\_handle=FileOpen("MyFile.bin",FILE\_WRITE|FILE\_BIN|FILE\_ANSI);        if(file\_handle>=0)          {           if(!object.Save(file\_handle))             {              //--- file save error              printf("File save: Error %d!",GetLastError());              FileClose(file\_handle);              //---              return;             }           FileClose(file\_handle);          }       } |
