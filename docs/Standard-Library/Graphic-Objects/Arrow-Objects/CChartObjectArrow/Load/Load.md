# Load

Load

Loads object parameters from file.

|  |
| --- |
| virtual bool  Load(     int  file\_handle      // file handle     ) |

Parameters

file\_handle

[in]  handle of file previously opened using the FileOpen(...) function.

Return Value

true - success, false - error.

Example:

|  |
| --- |
| //--- example for CChartObjectArrow::Load    #include <ChartObjects\ChartObjectsArrows.mqh>    //---    void OnStart()      {       int               file\_handle;       CChartObjectArrow arrow;    //--- open file       file\_handle=FileOpen("MyFile.bin",FILE\_READ|FILE\_BIN|FILE\_ANSI);       if(file\_handle>=0)         {          if(!arrow.Load(file\_handle))            {             //--- file load error             printf("File load: Error %d!",GetLastError());             FileClose(file\_handle);             //---             return;            }          FileClose(file\_handle);         }    //--- use arrow    //--- . . .      } |
