# Positioning Constants

Positioning Constants

Three identifiers from the ENUM\_CHART\_POSITION list are the possible values of the position parameter for the [ChartNavigate()](../../../Chart-Operations/ChartNavigate/ChartNavigate.md) function.

ENUM\_CHART\_POSITION

| ID | Description |
| --- | --- |
| CHART\_BEGIN | Chart beginning (the oldest prices) |
| CHART\_CURRENT\_POS | Current position |
| CHART\_END | Chart end (the latest prices) |

Example:

|  |
| --- |
| long handle=ChartOpen("EURUSD",PERIOD\_H12);     if(handle!=0)       {        ChartSetInteger(handle,CHART\_AUTOSCROLL,false);        ChartSetInteger(handle,CHART\_SHIFT,true);        ChartSetInteger(handle,CHART\_MODE,CHART\_LINE);        ResetLastError();        bool res=ChartNavigate(handle,CHART\_END,150);        if(!res) Print("Navigate failed. Error = ",GetLastError());        ChartRedraw();       } |
