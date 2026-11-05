# Positioning Constants


Three identifiers from the ENUM\_CHART\_POSITION list are the possible values of the position parameter for the [ChartNavigate()](../../../Chart-Operations/ChartNavigate/ChartNavigate.md) function.

ENUM\_CHART\_POSITION

| ID | Description |
| --- | --- |
| CHART\_BEGIN | Chart beginning (the oldest prices) |
| CHART\_CURRENT\_POS | Current position |
| CHART\_END | Chart end (the latest prices) |

Example:

```cpp
   long handle=ChartOpen("EURUSD",PERIOD_H12);
   if(handle!=0)
     {
      ChartSetInteger(handle,CHART_AUTOSCROLL,false);
      ChartSetInteger(handle,CHART_SHIFT,true);
      ChartSetInteger(handle,CHART_MODE,CHART_LINE);
      ResetLastError();
      bool res=ChartNavigate(handle,CHART_END,150);
      if(!res) Print("Navigate failed. Error = ",GetLastError());
      ChartRedraw();
     }
```