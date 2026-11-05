# IndicatorSetDouble

IndicatorSetDouble

The function sets the value of the corresponding indicator property. Indicator property must be of the double type. There are two variants of the function.

Call with specifying the property identifier.

|  |
| --- |
| bool  IndicatorSetDouble(     int     prop\_id,           // identifier     double  prop\_value         // value to be set     ); |

Call with specifying the property identifier and modifier.

|  |
| --- |
| bool  IndicatorSetDouble(     int     prop\_id,           // identifier     int     prop\_modifier,     // modifier     double  prop\_value         // value to be set     ) |

Parameters

prop\_id

[in]  Identifier of the indicator property. The value can be one of the values of the [ENUM\_CUSTOMIND\_PROPERTY\_DOUBLE](../../Constants,-Enumerations-and-Structures/Indicator-Constants/Custom-Indicator-Properties/Custom-Indicator-Properties.md#enum_customind_property_double) enumeration.

prop\_modifier

[in]  Modifier of the specified property. Only level properties require a modifier. Numbering of levels starts from 0. It means that in order to set property for the second level you need to specify 1 (1 less than when using [compiler directive](../../Language-Basics/Preprocessor/Program-Properties-(#property)/Program-Properties-(#property).md)).

prop\_value

[in]  Value of property.

Return Value

In case of successful execution, returns true, otherwise - false.

Note

Numbering of properties (modifiers) starts from 1 (one) when using the #property directive, while the function uses numbering from 0 (zero). In case the level number is set incorrectly, [indicator display](../../Constants,-Enumerations-and-Structures/Indicator-Constants/Drawing-Styles/Drawing-Styles.md) can differ from the intended one.

For example, the first level value for the indicator in a separate subwindow can be set in two ways:

- property indicator\_level1  50 - the value of 1 is used for specifying the level number,
- IndicatorSetDouble(INDICATOR\_LEVELVALUE, 0, 50) - 0 is used for specifying the first level.

Example: indicator that turns upside down the maximum and minimum values ​​of the indicator window and values ​​of levels on which the horizontal lines are placed.

![Example of using the IndicatorSetDouble() function](../../assets/indicatorsetdouble.png "Example of using the IndicatorSetDouble() function")

|  |
| --- |
| #property indicator\_separate\_window  //--- set the maximum and minimum values ​​for the indicator window  #property indicator\_minimum  0  #property indicator\_maximum  100  //--- display three horizontal levels in a separate indicator window  #property indicator\_level1 25  #property indicator\_level2 50  #property indicator\_level3 75  //--- set thickness of horizontal levels  #property indicator\_levelwidth 1  //--- set style of horizontal levels  #property indicator\_levelstyle STYLE\_DOT  //+------------------------------------------------------------------+  //| Custom indicator initialization function                         |  //+------------------------------------------------------------------+  int OnInit()    {  //--- set descriptions of horizontal levels     IndicatorSetString(INDICATOR\_LEVELTEXT,0,"First Level (index 0)");     IndicatorSetString(INDICATOR\_LEVELTEXT,1,"Second Level (index 1)");     IndicatorSetString(INDICATOR\_LEVELTEXT,2,"Third Level (index 2)");  //--- set the short name for indicator     IndicatorSetString(INDICATOR\_SHORTNAME,"IndicatorSetDouble() Demo");  //--- set color for each level     IndicatorSetInteger(INDICATOR\_LEVELCOLOR,0,clrBlue);     IndicatorSetInteger(INDICATOR\_LEVELCOLOR,1,clrGreen);     IndicatorSetInteger(INDICATOR\_LEVELCOLOR,2,clrRed);  //---     return(INIT\_SUCCEEDED);    }  //+------------------------------------------------------------------+  //| Custom indicator iteration function                              |  //+------------------------------------------------------------------+  int OnCalculate(const int rates\_total,                  const int prev\_calculated,                  const datetime &time[],                  const double &open[],                  const double &high[],                  const double &low[],                  const double &close[],                  const long &tick\_volume[],                  const long &volume[],                  const int &spread[])    {     static int tick\_counter=0;     static double level1=25,level2=50,level3=75;     static double max=100,min=0, shift=100;  //--- calculate ticks     tick\_counter++;  //--- turn levels upside down on every 10th tick     if(tick\_counter%10==0)       {        //--- invert sign for the level values        level1=-level1;        level2=-level2;        level3=-level3;        //--- invert sign for the maximum and minimum values        max-=shift;        min-=shift;        //--- invert the shift value        shift=-shift;        //--- set new level values        IndicatorSetDouble(INDICATOR\_LEVELVALUE,0,level1);        IndicatorSetDouble(INDICATOR\_LEVELVALUE,1,level2);        IndicatorSetDouble(INDICATOR\_LEVELVALUE,2,level3);        //--- set new values of maximum and minimum in the indicator window        Print("Set up max = ",max,",   min = ",min);        IndicatorSetDouble(INDICATOR\_MAXIMUM,max);        IndicatorSetDouble(INDICATOR\_MINIMUM,min);       }  //--- return value of prev\_calculated for next call     return(rates\_total);    } |

See also

[Indicator Styles in Examples](../Indicator-Styles-in-Examples/Indicator-Styles-in-Examples.md), [Connection between Indicator Properties and Functions](../Connection-between-Indicator-Properties-and-Functions/Connection-between-Indicator-Properties-and-Functions.md), [Drawing Styles](../../Constants,-Enumerations-and-Structures/Indicator-Constants/Drawing-Styles/Drawing-Styles.md)
