# Custom Indicator Properties

# Custom Indicators Properties

The number of indicator buffers that can be used in a custom indicator is unlimited. But for each array, which is designated as the indicator buffer using the [SetIndexBuffer()](../../../Custom-Indicators/SetIndexBuffer/SetIndexBuffer.md) function, it's necessary to specify the data type that it will store. This may be one of the values of the ENUM\_INDEXBUFFER\_TYPE enumeration.

ENUM\_INDEXBUFFER\_TYPE

| ID | Description |
| --- | --- |
| INDICATOR\_DATA | Data to draw |
| INDICATOR\_COLOR\_INDEX | Color |
| INDICATOR\_CALCULATIONS | Auxiliary buffers for intermediate calculations |

A custom indicator has a lot of settings to provide convenient displaying. These settings are made through the assignment of corresponding indicator properties using functions [IndicatorSetDouble()](../../../Custom-Indicators/IndicatorSetDouble/IndicatorSetDouble.md), [IndicatorSetInteger()](../../../Custom-Indicators/IndicatorSetInteger/IndicatorSetInteger.md) and [IndicatorSetString()](../../../Custom-Indicators/IndicatorSetString/IndicatorSetString.md). Identifiers of indicator properties are listed in the ENUM\_CUSTOMIND\_PROPERTY enumeration.

ENUM\_CUSTOMIND\_PROPERTY\_INTEGER

| ID | Description | Property type |
| --- | --- | --- |
| INDICATOR\_DIGITS | Accuracy of drawing of indicator values | int |
| INDICATOR\_HEIGHT | Fixed height of the indicator's window (the preprocessor command [#property indicator\_height](../../../Language-Basics/Preprocessor/Program-Properties-(#property)/Program-Properties-(#property).md)) | int |
| INDICATOR\_LEVELS | Number of levels in the indicator window | int |
| INDICATOR\_LEVELCOLOR | Color of the level line | color                      modifier = level number |
| INDICATOR\_LEVELSTYLE | Style of the level line | [ENUM\_LINE\_STYLE](../Drawing-Styles/Drawing-Styles.md#enum_line_style)  modifier = level number |
| INDICATOR\_LEVELWIDTH | Thickness of the level line | int                         modifier = level number |
| INDICATOR\_FIXED\_MINIMUM | Fixed minimum for the [indicator window](https://www.metatrader5.com/en/terminal/help/charts_analysis/indicators#visualization). The property can only be written by the [IndicatorSetInteger()](../../../Custom-Indicators/IndicatorSetInteger/IndicatorSetInteger.md) function | bool |
| INDICATOR\_FIXED\_MAXIMUM | Fixed maximum for the [indicator window](https://www.metatrader5.com/en/terminal/help/charts_analysis/indicators#visualization). The property can only be written by the [IndicatorSetInteger()](../../../Custom-Indicators/IndicatorSetInteger/IndicatorSetInteger.md) function | bool |

ENUM\_CUSTOMIND\_PROPERTY\_DOUBLE

| ID | Description | Property type |
| --- | --- | --- |
| INDICATOR\_MINIMUM | Minimum of the indicator window | double |
| INDICATOR\_MAXIMUM | Maximum of the indicator window | double |
| INDICATOR\_LEVELVALUE | Level value | double                    modifier = level number |

ENUM\_CUSTOMIND\_PROPERTY\_STRING

| ID | Description | Property type |
| --- | --- | --- |
| INDICATOR\_SHORTNAME | Short indicator name | string |
| INDICATOR\_LEVELTEXT | Level description | string                    modifier = level number |

Examples:

```cpp
//--- indicator settings
#property indicator_separate_window
#property indicator_buffers 4
#property indicator_plots   2
#property indicator_type1   DRAW_LINE
#property indicator_type2   DRAW_LINE
#property indicator_color1  clrLightSeaGreen
#property indicator_color2  clrRed
//--- input parameters
extern int KPeriod=5;
extern int DPeriod=3;
extern int Slowing=3;
//--- indicator buffers
double MainBuffer[];
double SignalBuffer[];
double HighesBuffer[];
double LowesBuffer[];
//+------------------------------------------------------------------+
//| Custom indicator initialization function                         |
//+------------------------------------------------------------------+
void OnInit()
  {
//--- indicator buffers mapping
   SetIndexBuffer(0,MainBuffer,INDICATOR_DATA);
   SetIndexBuffer(1,SignalBuffer,INDICATOR_DATA);
   SetIndexBuffer(2,HighesBuffer,INDICATOR_CALCULATIONS);
   SetIndexBuffer(3,LowesBuffer,INDICATOR_CALCULATIONS);
//--- set accuracy
   IndicatorSetInteger(INDICATOR_DIGITS,2);
//--- set levels
   IndicatorSetInteger(INDICATOR_LEVELS,2);
   IndicatorSetDouble(INDICATOR_LEVELVALUE,0,20);
   IndicatorSetDouble(INDICATOR_LEVELVALUE,1,80);
//--- set maximum and minimum for subwindow
   IndicatorSetDouble(INDICATOR_MINIMUM,0);
   IndicatorSetDouble(INDICATOR_MAXIMUM,100);
//--- sets first bar from which index will be drawn
   PlotIndexSetInteger(0,PLOT_DRAW_BEGIN,KPeriod+Slowing-2);
   PlotIndexSetInteger(1,PLOT_DRAW_BEGIN,KPeriod+Slowing+DPeriod);
//--- set style STYLE_DOT for second line
   PlotIndexSetInteger(1,PLOT_LINE_STYLE,STYLE_DOT);
//--- name for DataWindow and indicator subwindow label
   IndicatorSetString(INDICATOR_SHORTNAME,"Stoch("+KPeriod+","+DPeriod+","+Slowing+")");
   PlotIndexSetString(0,PLOT_LABEL,"Main");
   PlotIndexSetString(1,PLOT_LABEL,"Signal");
//--- sets drawing line to empty value
   PlotIndexSetDouble(0,PLOT_EMPTY_VALUE,0.0);
   PlotIndexSetDouble(1,PLOT_EMPTY_VALUE,0.0);
//--- initialization done
  }
```