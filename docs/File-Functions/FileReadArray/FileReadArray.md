# FileReadArray

FileReadArray

Reads from a file of BIN type arrays of any type except string (may be an array of structures, not containing strings, and dynamic arrays).

|  |
| --- |
| uint  FileReadArray(     int    file\_handle,               // File handle     void&  array[],                   // Array to record     int    start=0,                   // start array position to write     int    count=WHOLE\_ARRAY          // count to read     ); |

Parameters

file\_handle

[in]  File descriptor returned by [FileOpen()](../FileOpen/FileOpen.md).

array[]

[out] An array where the data will be loaded.

start=0

[in]  Start position to read from the array.

count=WHOLE\_ARRAY

[in]  Number of elements to read. By default, reads the entire array (count=[WHOLE\_ARRAY](../../Constants,-Enumerations-and-Structures/Named-Constants/Other-Constants/Other-Constants.md)).

Return Value

Number of elements read.

Note

String array can be read only from the file of TXT type. If necessary, the function tries to increase the size of the array.

Example (the file obtained after execution of the example for [FileWriteArray](../FileWriteArray/FileWriteArray.md) function is used here)

|  |
| --- |
| //--- display the window of input parameters when launching the script  #property script\_show\_inputs  //--- input parameters  input string InpFileName="data.bin";  input string InpDirectoryName="SomeFolder";  //+------------------------------------------------------------------+  //| Structure for storing price data                                 |  //+------------------------------------------------------------------+  struct prices    {     datetime          date; // date     double            bid;  // bid price     double            ask;  // ask price    };  //+------------------------------------------------------------------+  //| Script program start function                                    |  //+------------------------------------------------------------------+  void OnStart()    {  //--- structure array     prices arr[];  //--- file path     string path=InpDirectoryName+"//"+InpFileName;  //--- open the file     ResetLastError();     int file\_handle=FileOpen(path,FILE\_READ|FILE\_BIN);     if(file\_handle!=INVALID\_HANDLE)       {        //--- read all data from the file to the array        FileReadArray(file\_handle,arr);        //--- receive the array size        int size=ArraySize(arr);        //--- print data from the array        for(int i=0;i<size;i++)           Print("Date = ",arr[i].date," Bid = ",arr[i].bid," Ask = ",arr[i].ask);        Print("Total data = ",size);        //--- close the file        FileClose(file\_handle);       }     else        Print("File open failed, error ",GetLastError());    } |

See also

[Variables](../../Language-Basics/Variables/Variables.md#array_define), [FileWriteArray](../FileWriteArray/FileWriteArray.md)
