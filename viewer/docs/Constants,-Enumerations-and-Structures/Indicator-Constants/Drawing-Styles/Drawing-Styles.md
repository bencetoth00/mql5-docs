# Drawing Styles


When creating [a custom indicator](../../../Custom-Indicators/Custom-Indicators.md), you can specify one of 18 types of graphical plotting (as displayed in the main chart window or a chart subwindow), whose values are specified in the ENUM\_DRAW\_TYPE enumeration.

In one custom indicator, it is permissible to use any [indicator building/drawing types](../../../Custom-Indicators/Indicator-Styles-in-Examples/Indicator-Styles-in-Examples.md). Each construction type requires specification of one to five [global arrays](../../../Language-Basics/Variables/Global-Variables/Global-Variables.md) for storing data necessary for drawing. These data arrays must be bound with indicator buffers using the [SetIndexBuffer()](../../../Custom-Indicators/SetIndexBuffer/SetIndexBuffer.md) function. The type of data from [ENUM\_INDEXBUFFER\_TYPE](../Custom-Indicator-Properties/Custom-Indicator-Properties.md#enum_indexbuffer_type_enum) should be specified for each buffer.

Depending on the drawing style, you may need one to four value buffers (marked as INDICATOR\_DATA). If a style admits dynamic alternation of colors (all styles contain COLOR in their names), then you'll need one more buffer of color (indicated type INDICATOR\_COLOR\_INDEX). The color buffers are always bound after value buffers corresponding to the style.

ENUM\_DRAW\_TYPE

| ID | Description | Data buffers | Color buffers |
| --- | --- | --- | --- |
| [DRAW\_NONE](../../../Custom-Indicators/Indicator-Styles-in-Examples/DRAW_NONE/DRAW_NONE.md) | Not drawn | 1 | 0 |
| [DRAW\_LINE](../../../Custom-Indicators/Indicator-Styles-in-Examples/DRAW_LINE/DRAW_LINE.md) | Line | 1 | 0 |
| [DRAW\_SECTION](../../../Custom-Indicators/Indicator-Styles-in-Examples/DRAW_SECTION/DRAW_SECTION.md) | Section | 1 | 0 |
| [DRAW\_HISTOGRAM](../../../Custom-Indicators/Indicator-Styles-in-Examples/DRAW_HISTOGRAM/DRAW_HISTOGRAM.md) | Histogram from the zero line | 1 | 0 |
| [DRAW\_HISTOGRAM2](../../../Custom-Indicators/Indicator-Styles-in-Examples/DRAW_HISTOGRAM2/DRAW_HISTOGRAM2.md) | Histogram of the two indicator buffers | 2 | 0 |
| [DRAW\_ARROW](../../../Custom-Indicators/Indicator-Styles-in-Examples/DRAW_ARROW/DRAW_ARROW.md) | Drawing arrows | 1 | 0 |
| [DRAW\_ZIGZAG](../../../Custom-Indicators/Indicator-Styles-in-Examples/DRAW_ZIGZAG/DRAW_ZIGZAG.md) | Style Zigzag allows vertical section on the bar | 2 | 0 |
| [DRAW\_FILLING](../../../Custom-Indicators/Indicator-Styles-in-Examples/DRAW_FILLING/DRAW_FILLING.md) | Color fill between the two levels | 2 | 0 |
| [DRAW\_BARS](../../../Custom-Indicators/Indicator-Styles-in-Examples/DRAW_BARS/DRAW_BARS.md) | Display as a sequence of bars | 4 | 0 |
| [DRAW\_CANDLES](../../../Custom-Indicators/Indicator-Styles-in-Examples/DRAW_CANDLES/DRAW_CANDLES.md) | Display as a sequence of candlesticks | 4 | 0 |
| [DRAW\_COLOR\_LINE](../../../Custom-Indicators/Indicator-Styles-in-Examples/DRAW_COLOR_LINE/DRAW_COLOR_LINE.md) | Multicolored line | 1 | 1 |
| [DRAW\_COLOR\_SECTION](../../../Custom-Indicators/Indicator-Styles-in-Examples/DRAW_COLOR_SECTION/DRAW_COLOR_SECTION.md) | Multicolored section | 1 | 1 |
| [DRAW\_COLOR\_HISTOGRAM](../../../Custom-Indicators/Indicator-Styles-in-Examples/DRAW_COLOR_HISTOGRAM/DRAW_COLOR_HISTOGRAM.md) | Multicolored histogram from the zero line | 1 | 1 |
| [DRAW\_COLOR\_HISTOGRAM2](../../../Custom-Indicators/Indicator-Styles-in-Examples/DRAW_COLOR_HISTOGRAM2/DRAW_COLOR_HISTOGRAM2.md) | Multicolored histogram of the two indicator buffers | 2 | 1 |
| [DRAW\_COLOR\_ARROW](../../../Custom-Indicators/Indicator-Styles-in-Examples/DRAW_COLOR_ARROW/DRAW_COLOR_ARROW.md) | Drawing multicolored arrows | 1 | 1 |
| [DRAW\_COLOR\_ZIGZAG](../../../Custom-Indicators/Indicator-Styles-in-Examples/DRAW_COLOR_ZIGZAG/DRAW_COLOR_ZIGZAG.md) | Multicolored ZigZag | 2 | 1 |
| [DRAW\_COLOR\_BARS](../../../Custom-Indicators/Indicator-Styles-in-Examples/DRAW_COLOR_BARS/DRAW_COLOR_BARS.md) | Multicolored bars | 4 | 1 |
| [DRAW\_COLOR\_CANDLES](../../../Custom-Indicators/Indicator-Styles-in-Examples/DRAW_COLOR_CANDLES/DRAW_COLOR_CANDLES.md) | Multicolored candlesticks | 4 | 1 |

 

To refine the display of the selected drawing type identifiers listed in ENUM\_PLOT\_PROPERTY are used.

For functions [PlotIndexSetInteger()](../../../Custom-Indicators/PlotIndexSetInteger/PlotIndexSetInteger.md) and [PlotIndexGetInteger()](../../../Custom-Indicators/PlotIndexGetInteger/PlotIndexGetInteger.md)

ENUM\_PLOT\_PROPERTY\_INTEGER

| ID | Description | Property type |
| --- | --- | --- |
| PLOT\_ARROW | Arrow code for style DRAW\_ARROW | uchar |
| PLOT\_ARROW\_SHIFT | Vertical shift of arrows for style DRAW\_ARROW | int |
| PLOT\_DRAW\_BEGIN | Number of initial bars without drawing and values in the DataWindow | int |
| PLOT\_DRAW\_TYPE | Type of graphical construction | [ENUM\_DRAW\_TYPE](Drawing-Styles.md#enum_draw_type) |
| PLOT\_SHOW\_DATA | Sign of display of construction values in the DataWindow | bool |
| PLOT\_SHIFT | Shift of indicator plotting along the time axis in bars | int |
| PLOT\_LINE\_STYLE | Drawing line style | [ENUM\_LINE\_STYLE](Drawing-Styles.md#enum_line_style) |
| PLOT\_LINE\_WIDTH | The thickness of the drawing line | int |
| PLOT\_COLOR\_INDEXES | The number of colors | int |
| PLOT\_LINE\_COLOR | The index of a buffer containing the drawing color | color       modifier = index number of colors |

For the function [PlotIndexSetDouble()](../../../Custom-Indicators/PlotIndexSetDouble/PlotIndexSetDouble.md)

ENUM\_PLOT\_PROPERTY\_DOUBLE

| ID | Description | Property type |
| --- | --- | --- |
| PLOT\_EMPTY\_VALUE | An empty value for plotting, for which there is no drawing | double |

For the function [PlotIndexSetString()](../../../Custom-Indicators/PlotIndexSetString/PlotIndexSetString.md)

ENUM\_PLOT\_PROPERTY\_STRING

| ID | Description | Property type |
| --- | --- | --- |
| PLOT\_LABEL | The name of the indicator graphical series to display in the DataWindow. When working with complex graphical styles requiring several indicator buffers for display, the names for each buffer can be specified using ";" as a separator. Sample code is shown in [DRAW\_CANDLES](../../../Custom-Indicators/Indicator-Styles-in-Examples/DRAW_CANDLES/DRAW_CANDLES.md) | string |

5 styles can be used for drawing lines in custom indicators. They are valid only for the line thickness 0 or 1.

ENUM\_LINE\_STYLE

| ID | Description |
| --- | --- |
| STYLE\_SOLID | Solid line |
| STYLE\_DASH | Broken line |
| STYLE\_DOT | Dotted line |
| STYLE\_DASHDOT | Dash-dot line |
| STYLE\_DASHDOTDOT | Dash - two points |

 

To set the line drawing style and the type of drawing, the [PlotIndexSetInteger()](../../../Custom-Indicators/PlotIndexSetInteger/PlotIndexSetInteger.md) function is used. For the Fibonacci extensions the thickness and drawing style of levels can be indicated using the [ObjectSetInteger()](../../../Object-Functions/ObjectSetInteger/ObjectSetInteger.md) function.

Example:

```cpp
#property indicator_chart_window
#property indicator_buffers 1
#property indicator_plots   1
//--- indicator buffers
double         MABuffer[];
//+------------------------------------------------------------------+
//| Custom indicator initialization function                         |
//+------------------------------------------------------------------+
void OnInit()
  {
//--- Bind the Array to the indicator buffer with index 0
   SetIndexBuffer(0,MABuffer,INDICATOR_DATA);
//--- Set the line drawing
   PlotIndexSetInteger(0,PLOT_DRAW_TYPE,DRAW_LINE);
//--- Set the style line
   PlotIndexSetInteger(0,PLOT_LINE_STYLE,STYLE_DOT);
//--- Set line color
   PlotIndexSetInteger(0,PLOT_LINE_COLOR,clrRed);
//--- Set line thickness
   PlotIndexSetInteger(0,PLOT_LINE_WIDTH,1);
//--- Set labels for the line
   PlotIndexSetString(0,PLOT_LABEL,"Moving Average");
//---
  }
//+------------------------------------------------------------------+
//| Custom indicator iteration function                              |
//+------------------------------------------------------------------+
int OnCalculate(const int rates_total,
                 const int prev_calculated,
                 const datetime &time[],
                 const double &open[],
                 const double &high[],
                 const double &low[],
                 const double &close[],
                 const long &tick_volume[],
                 const long &volume[],
                 const int &spread[])
  {
//---
   for(int i=prev_calculated;i<rates_total;i++)
     {
      MABuffer[i]=close[i];
     }
//--- return value of prev_calculated for next call
   return(rates_total);
  }
```