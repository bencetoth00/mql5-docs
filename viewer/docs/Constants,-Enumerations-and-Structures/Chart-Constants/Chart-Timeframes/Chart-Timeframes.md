# Chart Timeframes


All predefined timeframes of charts have unique identifiers. The PERIOD\_CURRENT identifier means the current period of a chart, at which a mql5-program is running.

ENUM\_TIMEFRAMES

| ID | Description |
| --- | --- |
| PERIOD\_CURRENT | Current timeframe |
| PERIOD\_M1 | 1 minute |
| PERIOD\_M2 | 2 minutes |
| PERIOD\_M3 | 3 minutes |
| PERIOD\_M4 | 4 minutes |
| PERIOD\_M5 | 5 minutes |
| PERIOD\_M6 | 6 minutes |
| PERIOD\_M10 | 10 minutes |
| PERIOD\_M12 | 12 minutes |
| PERIOD\_M15 | 15 minutes |
| PERIOD\_M20 | 20 minutes |
| PERIOD\_M30 | 30 minutes |
| PERIOD\_H1 | 1 hour |
| PERIOD\_H2 | 2 hours |
| PERIOD\_H3 | 3 hours |
| PERIOD\_H4 | 4 hours |
| PERIOD\_H6 | 6 hours |
| PERIOD\_H8 | 8 hours |
| PERIOD\_H12 | 12 hours |
| PERIOD\_D1 | 1 day |
| PERIOD\_W1 | 1 week |
| PERIOD\_MN1 | 1 month |

Example:

```cpp
   string chart_name="test_Object_Chart";
   Print("Let's try to create a Chart object with the name ",chart_name);
//--- If such an object does not exist - create it
   if(ObjectFind(0,chart_name)<0)ObjectCreate(0,chart_name,OBJ_CHART,0,0,0,0,0);
//--- Define symbol
   ObjectSetString(0,chart_name,OBJPROP_SYMBOL,"EURUSD");
//--- Set X coordinate of the anchor point
   ObjectSetInteger(0,chart_name,OBJPROP_XDISTANCE,100);
//--- Set Y coordinate of the anchor point
   ObjectSetInteger(0,chart_name,OBJPROP_YDISTANCE,100);
//--- Set the width of chart
   ObjectSetInteger(0,chart_name,OBJPROP_XSIZE,400);
//--- Set the height
   ObjectSetInteger(0,chart_name,OBJPROP_YSIZE,300);
//--- Set the timeframe
   ObjectSetInteger(0,chart_name,OBJPROP_PERIOD,PERIOD_D1);
//--- Set scale (from 0 to 5)
   ObjectSetDouble(0,chart_name,OBJPROP_SCALE,4);
//--- Disable selection by a mouse
   ObjectSetInteger(0,chart_name,OBJPROP_SELECTABLE,false);
```

 

### Timeseries identifiers

The identifiers of timeseries are used in the [iHighest()](../../../Timeseries-and-Indicators-Access/iHighest/iHighest.md) and [iLowest()](../../../Timeseries-and-Indicators-Access/iLowest/iLowest.md) functions. They can be equal to a value the enumeration

ENUM\_SERIESMODE

| Identifier | Description |
| --- | --- |
| MODE\_OPEN | Opening price |
| MODE\_LOW | Low price |
| MODE\_HIGH | High price |
| MODE\_CLOSE | Close price |
| MODE\_VOLUME | Tick volume |
| MODE\_REAL\_VOLUME | Real volume |
| MODE\_SPREAD | Spread |

See also

[PeriodSeconds](../../../Common-Functions/PeriodSeconds/PeriodSeconds.md), [Period](../../../Checkup/Period/Period.md), [Date and Time](../../../Date-and-Time/Date-and-Time.md), [Visibility of objects](../../Objects-Constants/Visibility-of-Objects/Visibility-of-Objects.md)