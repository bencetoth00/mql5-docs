# Load

Load

Loads the parameters of the object from the file.

|  |
| --- |
| virtual bool  Load(     int  file\_handle      // file handle     ) |

Parameters

file\_handle

[in]  handle of the file previously opened using the function FileOpen (...).

Return Value

true - successfully completed, false - error.

Example:

|  |
| --- |
| //--- example for CChartObject::Load   #include <ChartObjects\ChartObject.mqh>   //---   void OnStart()    {     int          file\_handle;     CChartObject object;     //--- open file      file\_handle=FileOpen("MyFile.bin",FILE\_READ|FILE\_BIN|FILE\_ANSI);      if(file\_handle>=0)        {         if(!object.Load(file\_handle))           {            //--- file load error            printf("File load: Error %d!",GetLastError());            FileClose(file\_handle);            //---            return;           }         FileClose(file\_handle);        }      //--- use object      //--- . . .     } |
