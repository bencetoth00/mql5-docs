# ObjectCreate


The function creates an object with the specified name, type, and the initial coordinates in the specified chart subwindow. During creation up to 30 coordinates can be specified.

```cpp
bool  ObjectCreate(
   long         chart_id,      // chart identifier
   string       name,          // object name
   ENUM_OBJECT  type,          // object type
   sub_window   nwin,          // window index
   datetime     time1,         // time of the first anchor point
   double       price1,        // price of the first anchor point
   ...
   datetime     timeN=0,       // time of the N-th anchor point
   double       priceN=0,      // price of the N-th anchor point
   ...
   datetime     time30=0,      // time of the 30th anchor point
   double       price30=0      // price of the 30th anchor point
   );
```

Parameters

chart\_id

[in]  Chart identifier. 0 means the current chart.

name

[in]  Name of the object. The name must be unique within a chart, including its subwindows.

type

[in]  Object type. The value can be one of the values of the [ENUM\_OBJECT](../../Constants,-Enumerations-and-Structures/Objects-Constants/Object-Types/Object-Types.md) enumeration.

sub\_window

[in]  Number of the chart subwindow. 0 means the main chart window. The specified subwindow must exist, otherwise the function returns false.

time1

[in]  The time coordinate of the first anchor.

price1

[in]  The price coordinate of the first anchor point.

timeN=0

[in]  The time coordinate of the N-th anchor point.

priceN=0

[in]  The price coordinate of the N-th anchor point.

time30=0

[in]  The time coordinate of the thirtieth anchor point.

price30=0

[in]  The price coordinate of the thirtieth anchor point.

Return Value

The function returns true if the command has been successfully added to the queue of the specified chart, or false otherwise. If an object has already been created, an attempt is made to change its coordinates.

Note

An asynchronous call is always used for ObjectCreate(), that is why the function only returns the results of adding the command to a chart queue. In this case, true only means that the command has been successfully enqueued, but the result of its execution is unknown.

To check the command execution result, you can use the [ObjectFind()](../ObjectFind/ObjectFind.md) function or any other function that requests object properties, such as ObjectGetXXX. However, you should keep in mind that such functions are added to the end of the queue of that chart, and they wait for the execution result (due to the synchronous call), and can therefore be time consuming. This feature should be taken into account when working with a large number of objects on a chart.

An object name should not exceed 63 characters.

The numbering of the chart subwindows (if there are subwindows with indicators in the chart) starts with 1. The main chart window of the chart is and always has index 0.

The large number of anchor points (up to 30) is implemented for future use. At the same time, the limit of 30 possible anchor points for graphical objects is determined by the limit on the number of parameters (not more than 64) that can be used when calling a function.

When an object is renamed, two events are formed simultaneously. These events can be handled in an Expert Advisor or indicator by the [OnChartEvent()](../../Event-Handling/OnChartEvent/OnChartEvent.md) function:

- an event of deletion of an object with the old name;
- an event of creation of an object with a new name.

There is a certain number of anchor points that must be specified when creating each [object type](../../Constants,-Enumerations-and-Structures/Objects-Constants/Object-Types/Object-Types.md):

| ID | Description | Anchor Points |
| --- | --- | --- |
| [OBJ\_VLINE](../../Constants,-Enumerations-and-Structures/Objects-Constants/Object-Types/OBJ_VLINE/OBJ_VLINE.md) | Vertical Line | One anchor point. Actually only the time coordinate is used. |
| [OBJ\_HLINE](../../Constants,-Enumerations-and-Structures/Objects-Constants/Object-Types/OBJ_HLINE/OBJ_HLINE.md) | Horizontal Line | One anchor point. Actually only the price coordinate is used. |
| [OBJ\_TREND](../../Constants,-Enumerations-and-Structures/Objects-Constants/Object-Types/OBJ_TREND/OBJ_TREND.md) | Trend Line | Two anchor points. |
| [OBJ\_TRENDBYANGLE](../../Constants,-Enumerations-and-Structures/Objects-Constants/Object-Types/OBJ_TRENDBYANGLE/OBJ_TRENDBYANGLE.md) | Trend Line By Angle | Two anchor points. |
| [OBJ\_CYCLES](../../Constants,-Enumerations-and-Structures/Objects-Constants/Object-Types/OBJ_CYCLES/OBJ_CYCLES.md) | Cycle Lines | Two anchor points. |
| [OBJ\_ARROWED\_LINE](../../Constants,-Enumerations-and-Structures/Objects-Constants/Object-Types/OBJ_ARROWED_LINE/OBJ_ARROWED_LINE.md) | Arrowed Line | Two anchor points. |
| [OBJ\_CHANNEL](../../Constants,-Enumerations-and-Structures/Objects-Constants/Object-Types/OBJ_CHANNEL/OBJ_CHANNEL.md) | Equidistant Channel | Three anchor points. |
| [OBJ\_STDDEVCHANNEL](../../Constants,-Enumerations-and-Structures/Objects-Constants/Object-Types/OBJ_STDDEVCHANNEL/OBJ_STDDEVCHANNEL.md) | Standard Deviation Channel | Two anchor points. |
| [OBJ\_REGRESSION](../../Constants,-Enumerations-and-Structures/Objects-Constants/Object-Types/OBJ_REGRESSION/OBJ_REGRESSION.md) | Linear Regression Channel | Two anchor points. |
| [OBJ\_PITCHFORK](../../Constants,-Enumerations-and-Structures/Objects-Constants/Object-Types/OBJ_PITCHFORK/OBJ_PITCHFORK.md) | Andrews’ Pitchfork | Three anchor points. |
| [OBJ\_GANNLINE](../../Constants,-Enumerations-and-Structures/Objects-Constants/Object-Types/OBJ_GANNLINE/OBJ_GANNLINE.md) | Gann Line | Two anchor points. |
| [OBJ\_GANNFAN](../../Constants,-Enumerations-and-Structures/Objects-Constants/Object-Types/OBJ_GANNFAN/OBJ_GANNFAN.md) | Gann Fan | Two anchor points. |
| [OBJ\_GANNGRID](../../Constants,-Enumerations-and-Structures/Objects-Constants/Object-Types/OBJ_GANNGRID/OBJ_GANNGRID.md) | Gann Grid | Two anchor points. |
| [OBJ\_FIBO](../../Constants,-Enumerations-and-Structures/Objects-Constants/Object-Types/OBJ_FIBO/OBJ_FIBO.md) | Fibonacci Retracement | Two anchor points. |
| [OBJ\_FIBOTIMES](../../Constants,-Enumerations-and-Structures/Objects-Constants/Object-Types/OBJ_FIBOTIMES/OBJ_FIBOTIMES.md) | Fibonacci Time Zones | Two anchor points. |
| [OBJ\_FIBOFAN](../../Constants,-Enumerations-and-Structures/Objects-Constants/Object-Types/OBJ_FIBOFAN/OBJ_FIBOFAN.md) | Fibonacci Fan | Two anchor points. |
| [OBJ\_FIBOARC](../../Constants,-Enumerations-and-Structures/Objects-Constants/Object-Types/OBJ_FIBOARC/OBJ_FIBOARC.md) | Fibonacci Arcs | Two anchor points. |
| [OBJ\_FIBOCHANNEL](../../Constants,-Enumerations-and-Structures/Objects-Constants/Object-Types/OBJ_FIBOCHANNEL/OBJ_FIBOCHANNEL.md) | Fibonacci Channel | Three anchor points. |
| [OBJ\_EXPANSION](../../Constants,-Enumerations-and-Structures/Objects-Constants/Object-Types/OBJ_EXPANSION/OBJ_EXPANSION.md) | Fibonacci Expansion | Three anchor points. |
| [OBJ\_ELLIOTWAVE5](../../Constants,-Enumerations-and-Structures/Objects-Constants/Object-Types/OBJ_ELLIOTWAVE5/OBJ_ELLIOTWAVE5.md) | Elliott Motive Wave | Five anchor points. |
| [OBJ\_ELLIOTWAVE3](../../Constants,-Enumerations-and-Structures/Objects-Constants/Object-Types/OBJ_ELLIOTWAVE3/OBJ_ELLIOTWAVE3.md) | Elliott Correction Wave | Three anchor points. |
| [OBJ\_RECTANGLE](../../Constants,-Enumerations-and-Structures/Objects-Constants/Object-Types/OBJ_RECTANGLE/OBJ_RECTANGLE.md) | Rectangle | Two anchor points. |
| [OBJ\_TRIANGLE](../../Constants,-Enumerations-and-Structures/Objects-Constants/Object-Types/OBJ_TRIANGLE/OBJ_TRIANGLE.md) | Triangle | Three anchor points. |
| [OBJ\_ELLIPSE](../../Constants,-Enumerations-and-Structures/Objects-Constants/Object-Types/OBJ_ELLIPSE/OBJ_ELLIPSE.md) | Ellipse | Three anchor points. |
| [OBJ\_ARROW\_THUMB\_UP](../../Constants,-Enumerations-and-Structures/Objects-Constants/Object-Types/OBJ_ARROW_THUMB_UP/OBJ_ARROW_THUMB_UP.md) | Thumbs Up | One anchor point. |
| [OBJ\_ARROW\_THUMB\_DOWN](../../Constants,-Enumerations-and-Structures/Objects-Constants/Object-Types/OBJ_ARROW_THUMB_DOWN/OBJ_ARROW_THUMB_DOWN.md) | Thumbs Down | One anchor point. |
| [OBJ\_ARROW\_UP](../../Constants,-Enumerations-and-Structures/Objects-Constants/Object-Types/OBJ_ARROW_UP/OBJ_ARROW_UP.md) | Arrow Up | One anchor point. |
| [OBJ\_ARROW\_DOWN](../../Constants,-Enumerations-and-Structures/Objects-Constants/Object-Types/OBJ_ARROW_DOWN/OBJ_ARROW_DOWN.md) | Arrow Down | One anchor point. |
| [OBJ\_ARROW\_STOP](../../Constants,-Enumerations-and-Structures/Objects-Constants/Object-Types/OBJ_ARROW_STOP/OBJ_ARROW_STOP.md) | Stop Sign | One anchor point. |
| [OBJ\_ARROW\_CHECK](../../Constants,-Enumerations-and-Structures/Objects-Constants/Object-Types/OBJ_ARROW_CHECK/OBJ_ARROW_CHECK.md) | Check Sign | One anchor point. |
| [OBJ\_ARROW\_LEFT\_PRICE](../../Constants,-Enumerations-and-Structures/Objects-Constants/Object-Types/OBJ_ARROW_LEFT_PRICE/OBJ_ARROW_LEFT_PRICE.md) | Left Price Label | One anchor point. |
| [OBJ\_ARROW\_RIGHT\_PRICE](../../Constants,-Enumerations-and-Structures/Objects-Constants/Object-Types/OBJ_ARROW_RIGHT_PRICE/OBJ_ARROW_RIGHT_PRICE.md) | Right Price Label | One anchor point. |
| [OBJ\_ARROW\_BUY](../../Constants,-Enumerations-and-Structures/Objects-Constants/Object-Types/OBJ_ARROW_BUY/OBJ_ARROW_BUY.md) | Buy Sign | One anchor point. |
| [OBJ\_ARROW\_SELL](../../Constants,-Enumerations-and-Structures/Objects-Constants/Object-Types/OBJ_ARROW_SELL/OBJ_ARROW_SELL.md) | Sell Sign | One anchor point. |
| [OBJ\_ARROW](../../Constants,-Enumerations-and-Structures/Objects-Constants/Object-Types/OBJ_ARROW/OBJ_ARROW.md) | Arrow | One anchor point. |
| [OBJ\_TEXT](../../Constants,-Enumerations-and-Structures/Objects-Constants/Object-Types/OBJ_TEXT/OBJ_TEXT.md) | Text | One anchor point. |
| [OBJ\_LABEL](../../Constants,-Enumerations-and-Structures/Objects-Constants/Object-Types/OBJ_LABEL/OBJ_LABEL.md) | Label | Position is set using the [OBJPROP\_XDISTANCE](../../Constants,-Enumerations-and-Structures/Objects-Constants/Object-Properties/Object-Properties.md#enum_object_property_integer) and [OBJPROP\_YDISTANCE](../../Constants,-Enumerations-and-Structures/Objects-Constants/Object-Properties/Object-Properties.md#enum_object_property_integer) properties. |
| [OBJ\_BUTTON](../../Constants,-Enumerations-and-Structures/Objects-Constants/Object-Types/OBJ_BUTTON/OBJ_BUTTON.md) | Button | Position is set using the [OBJPROP\_XDISTANCE](../../Constants,-Enumerations-and-Structures/Objects-Constants/Object-Properties/Object-Properties.md#enum_object_property_integer) and [OBJPROP\_YDISTANCE](../../Constants,-Enumerations-and-Structures/Objects-Constants/Object-Properties/Object-Properties.md#enum_object_property_integer) properties. |
| [OBJ\_CHART](../../Constants,-Enumerations-and-Structures/Objects-Constants/Object-Types/OBJ_CHART/OBJ_CHART.md) | Chart | Position is set using the [OBJPROP\_XDISTANCE](../../Constants,-Enumerations-and-Structures/Objects-Constants/Object-Properties/Object-Properties.md#enum_object_property_integer) and [OBJPROP\_YDISTANCE](../../Constants,-Enumerations-and-Structures/Objects-Constants/Object-Properties/Object-Properties.md#enum_object_property_integer) properties. |
| [OBJ\_BITMAP](../../Constants,-Enumerations-and-Structures/Objects-Constants/Object-Types/OBJ_BITMAP/OBJ_BITMAP.md) | Bitmap | One anchor point. |
| [OBJ\_BITMAP\_LABEL](../../Constants,-Enumerations-and-Structures/Objects-Constants/Object-Types/OBJ_BITMAP_LABEL/OBJ_BITMAP_LABEL.md) | Bitmap Label | Position is set using the [OBJPROP\_XDISTANCE](../../Constants,-Enumerations-and-Structures/Objects-Constants/Object-Properties/Object-Properties.md#enum_object_property_integer) and [OBJPROP\_YDISTANCE](../../Constants,-Enumerations-and-Structures/Objects-Constants/Object-Properties/Object-Properties.md#enum_object_property_integer) properties. |
| [OBJ\_EDIT](../../Constants,-Enumerations-and-Structures/Objects-Constants/Object-Types/OBJ_EDIT/OBJ_EDIT.md) | Edit | Position is set using the [OBJPROP\_XDISTANCE](../../Constants,-Enumerations-and-Structures/Objects-Constants/Object-Properties/Object-Properties.md#enum_object_property_integer) and [OBJPROP\_YDISTANCE](../../Constants,-Enumerations-and-Structures/Objects-Constants/Object-Properties/Object-Properties.md#enum_object_property_integer) properties. |
| [OBJ\_EVENT](../../Constants,-Enumerations-and-Structures/Objects-Constants/Object-Types/OBJ_EVENT/OBJ_EVENT.md) | The "Event" object corresponding to an event in the economic calendar | One anchor point. Actually only the time coordinate is used. |
| [OBJ\_RECTANGLE\_LABEL](../../Constants,-Enumerations-and-Structures/Objects-Constants/Object-Types/OBJ_RECTANGLE_LABEL/OBJ_RECTANGLE_LABEL.md) | The "Rectangle label" object for creating and designing the custom graphical interface. | Position is set using the [OBJPROP\_XDISTANCE](../../Constants,-Enumerations-and-Structures/Objects-Constants/Object-Properties/Object-Properties.md#enum_object_property_integer) and [OBJPROP\_YDISTANCE](../../Constants,-Enumerations-and-Structures/Objects-Constants/Object-Properties/Object-Properties.md#enum_object_property_integer) properties. |

 

Example:

```cpp
#property copyright "Copyright 2025, MetaQuotes Ltd."
#property link      "https://www.mql5.com"
#property version   "1.00"
#property script_show_inputs
#define   OBJ_NAME   "TestObjectCreate"            // object name
#define   OBJ_X      40                            // object X coordinate
#define   OBJ_Y      40                            // object Y coordinate
#define   OBJ_WIDTH  300                           // object width
#define   OBJ_HEIGHT 200                           // object height
#define   WND        0                             // chart subwindow
input ENUM_OBJECT InpObjectToCreate =  OBJ_VLINE;  /* Object type to create   */ // object type to plot on the chart
struct SPoint                                      // anchor point structure
  {
   double   price;
   datetime time;
  };
SPoint   ExtAnchorPoints[5];                       // array of graphical object anchor points
long     ExtChartID;                               // ID
//+------------------------------------------------------------------+
//| Script program start function                                    |
//+------------------------------------------------------------------+
void OnStart()
  {
//--- check the number of available bars
   int bars=Bars(_Symbol,_Period);
   if(bars<7)
     {
      PrintFormat("The number of available bars (%d) is not enough to create some graphical objects",bars);
      return;
     }
//--- current chart ID
   ExtChartID=ChartID();
//--- delete the previously created object
   ObjectDelete(ExtChartID, OBJ_NAME);
//--- set five anchor points (time/price)
   SetAnchorPointsData();
//--- price/time of anchor points
   datetime tm0=ExtAnchorPoints[0].time;
   double   pr0=ExtAnchorPoints[0].price;
   datetime tm1=ExtAnchorPoints[1].time;
   double   pr1=ExtAnchorPoints[1].price;
   datetime tm2=ExtAnchorPoints[2].time;
   double   pr2=ExtAnchorPoints[2].price;
   datetime tm3=ExtAnchorPoints[3].time;
   double   pr3=ExtAnchorPoints[3].price;
   datetime tm4=ExtAnchorPoints[4].time;
   double   pr4=ExtAnchorPoints[4].price;
//--- if the object successfully created, set its remaining parameters:
   if(ObjectCreate(ExtChartID,OBJ_NAME,InpObjectToCreate,WND,tm0,pr0,tm1,pr1,tm2,pr2,tm3,pr3,tm4,pr4))
     {
      //--- make the object selectable and select it
      ObjectSetInteger(ExtChartID, OBJ_NAME, OBJPROP_SELECTABLE, true);
      ObjectSetInteger(ExtChartID, OBJ_NAME, OBJPROP_SELECTED, true);
      //--- for objects positioned by chart coordinates
      ENUM_OBJECT obj=InpObjectToCreate;
      if(obj==OBJ_LABEL || obj==OBJ_BUTTON || obj==OBJ_CHART || obj==OBJ_BITMAP_LABEL || obj==OBJ_EDIT || obj==OBJ_RECTANGLE_LABEL)
        {
         //--- set the object coordinates
         ObjectSetInteger(ExtChartID,OBJ_NAME,OBJPROP_XDISTANCE,OBJ_X);
         ObjectSetInteger(ExtChartID,OBJ_NAME,OBJPROP_YDISTANCE,OBJ_Y);
         //--- set the object size
         ObjectSetInteger(ExtChartID,OBJ_NAME,OBJPROP_XSIZE,OBJ_WIDTH);
         ObjectSetInteger(ExtChartID,OBJ_NAME,OBJPROP_YSIZE,OBJ_HEIGHT);
        }
      //--- update the chart to show the changes
      ChartRedraw(ExtChartID);
     }
  }
//+------------------------------------------------------------------+
//| Fill the array of object anchor points                           |
//+------------------------------------------------------------------+
void SetAnchorPointsData(void)
  {
//--- left anchor point bar (with index 0)
   int bar_first=(int)ChartGetInteger(ExtChartID,CHART_FIRST_VISIBLE_BAR)-1;
//--- set the price/time of the first anchor point (with index 0)
   ExtAnchorPoints[0].price=iOpen(_Symbol,_Period,bar_first);
   ExtAnchorPoints[0].time =iTime(_Symbol,_Period,bar_first);
//--- set the price/time of anchor points with indices 1 - 3
   int distance=(int)round(bar_first/4);  // distance in bars between anchor points
   for(int i=1;i<4;i++)
     {
      ExtAnchorPoints[i].price=iOpen(_Symbol,_Period,bar_first-i*distance);
      ExtAnchorPoints[i].time =iTime(_Symbol,_Period,bar_first-i*distance);
     }
//--- set the price/time of the last anchor point (with index 4)
   ExtAnchorPoints[4].price=iOpen(_Symbol,_Period,1);
   ExtAnchorPoints[4].time =iTime(_Symbol,_Period,1);
  }
```