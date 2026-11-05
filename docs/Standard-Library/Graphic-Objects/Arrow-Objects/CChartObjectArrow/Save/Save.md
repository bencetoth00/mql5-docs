# Save

Save

Saves object parameters to file.

|  |
| --- |
| virtual bool  Save(     int  file\_handle      // file handle     ) |

Parameters

file\_handle

[in]  handle of file opened previously using the FileOpen(...) function.

Return Value

true - successful, false - error.

Example:

|  |
| --- |
| //--- example for CChartObjectArrow::Save    #include <ChartObjects\ChartObjectsArrows.mqh>    //---    void OnStart()      {       int               file\_handle;       CChartObjectArrow arrow;    //--- set object parameters       double price=SymbolInfoDouble(Symbol(),SYMBOL\_BID);       if(!arrow.Create(0,"Arrow",0,TimeCurrent(),price,181))         {          //--- arrow create error          printf("Arrow create: Error %d!",GetLastError());          //---          return;         }       //--- open file       file\_handle=FileOpen("MyFile.bin",FILE\_WRITE|FILE\_BIN|FILE\_ANSI);       if(file\_handle>=0)         {          if(!arrow.Save(file\_handle))            {             //--- file save error             printf("File save: Error %d!",GetLastError());             FileClose(file\_handle);             //---             return;            }          FileClose(file\_handle);         }      } |
