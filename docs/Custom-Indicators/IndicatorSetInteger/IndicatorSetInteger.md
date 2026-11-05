# IndicatorSetInteger

IndicatorSetInteger

The function sets the value of the corresponding indicator property. Indicator property must be of the int or color type. There are two variants of the function.

Call with specifying the property identifier.

|  |
| --- |
| bool  IndicatorSetInteger(     int  prop\_id,           // identifier     int  prop\_value         // value to be set     ); |

Call with specifying the property identifier and modifier.

|  |
| --- |
| bool  IndicatorSetInteger(     int  prop\_id,           // identifier     int  prop\_modifier,     // modifier     int  prop\_value         // value to be set     ) |

Parameters

prop\_id

[in]  Identifier of the indicator property. The value can be one of the values of the [ENUM\_CUSTOMIND\_PROPERTY\_INTEGER](../../Constants,-Enumerations-and-Structures/Indicator-Constants/Custom-Indicator-Properties/Custom-Indicator-Properties.md#enum_customind_property_integer) enumeration.

prop\_modifier

[in]  Modifier of the specified property. Only level properties require a modifier.

prop\_value

[in]  Value of property.

Return Value

In case of successful execution, returns true, otherwise - false.

Note

Numbering of properties (modifiers) starts from 1 (one) when using the #property directive, while the function uses numbering from 0 (zero). In case the level number is set incorrectly, [indicator display](../../Constants,-Enumerations-and-Structures/Indicator-Constants/Drawing-Styles/Drawing-Styles.md) can differ from the intended one.

For example, in order to set thickness of the first horizontal line use zeroth index:

- IndicatorSetInteger(INDICATOR\_LEVELWIDTH, 0, 5) - index 0 is used to set thickness of the first level.

Example: indicator that sets color, style and thickness of the indicator horizontal lines.

![Example of using the IndicatorSetInteger() function](../../assets/indicatorsetinteger.png "Example of using the IndicatorSetInteger() function")

|  |
| --- |
| #property indicator\_separate\_window  #property indicator\_minimum 0  #property indicator\_maximum 100  //--- display three horizontal levels in a separate indicator window  #property indicator\_level1 20  #property indicator\_level2 50  #property indicator\_level3 80  //--- set thickness of horizontal levels  #property indicator\_levelwidth 5  //--- set color of horizontal levels  #property indicator\_levelcolor clrAliceBlue  //--- set style of horizontal levels  #property indicator\_levelstyle STYLE\_DOT  //+------------------------------------------------------------------+  //| Custom indicator initialization function                         |  //+------------------------------------------------------------------+  int OnInit()    {  //--- set descriptions of horizontal levels     IndicatorSetString(INDICATOR\_LEVELTEXT,0,"First Level (index 0)");     IndicatorSetString(INDICATOR\_LEVELTEXT,1,"Second Level (index 1)");     IndicatorSetString(INDICATOR\_LEVELTEXT,2,"Third Level (index 2)");  //--- set the short name for indicator     IndicatorSetString(INDICATOR\_SHORTNAME,"IndicatorSetInteger() Demo");     return(INIT\_SUCCEEDED);    }  //+------------------------------------------------------------------+  //| Custom indicator iteration function                              |  //+------------------------------------------------------------------+  int OnCalculate(const int rates\_total,                  const int prev\_calculated,                  const datetime &time[],                  const double &open[],                  const double &high[],                  const double &low[],                  const double &close[],                  const long &tick\_volume[],                  const long &volume[],                  const int &spread[])    {     static int tick\_counter=0;  //--- calculate ticks     tick\_counter++;  //--- and calculate colors of horizontal levels depending on the tick counter     ChangeLevelColor(0,tick\_counter,3,6,10); // three last parameters are switching the color     ChangeLevelColor(1,tick\_counter,3,6,8);     ChangeLevelColor(2,tick\_counter,4,7,9);  //--- modify style of horizontal levels     ChangeLevelStyle(0,tick\_counter);     ChangeLevelStyle(1,tick\_counter+5);     ChangeLevelStyle(2,tick\_counter+15);  //--- get width as the remainder of integer division of the ticks number by 5     int width=tick\_counter%5;  //--- iterate over all horizontal levels and set thickness     for(int l=0;l<3;l++)        IndicatorSetInteger(INDICATOR\_LEVELWIDTH,l,width+1);  //--- return value of prev\_calculated for next call     return(rates\_total);    }  //+------------------------------------------------------------------+  //| Set color of horizontal line in the separate indicator window    |  //+------------------------------------------------------------------+  void ChangeLevelColor(int level,      // number of horizontal line                        int tick\_number,// dividend, number to get the remainder of division                        int f\_trigger,  // first divisor of color switching                        int s\_trigger,  // second divisor of color switching                        int t\_trigger)  // third divisor of color switching    {     static color colors[3]={clrRed,clrBlue,clrGreen};  //--- index of color from the colors[] array     int index=-1;  //--- calculate the number of color from the colors[] array to paint horizontal line     if(tick\_number%f\_trigger==0)        index=0;   // if tick\_number is divided by f\_trigger without the remainder     if(tick\_number%s\_trigger==0)        index=1;   // if tick\_number is divided by s\_trigger without the remainder     if(tick\_number%t\_trigger==0)        index=2;   // if tick\_number is divided by t\_trigger without the remainder  //--- if color is defined, set it           if(index!=-1)        IndicatorSetInteger(INDICATOR\_LEVELCOLOR,level,colors[index]);  //---    }  //+------------------------------------------------------------------+  //| Set style of horizontal line in the separate indicator window    |  //+------------------------------------------------------------------+  void ChangeLevelStyle(int level,     // number of horizontal line                        int tick\_number// number to get the remainder of division                        )    {  //--- array to store styles     static ENUM\_LINE\_STYLE styles[5]=       {STYLE\_SOLID,STYLE\_DASH,STYLE\_DOT,STYLE\_DASHDOT,STYLE\_DASHDOTDOT};  //--- index of style from the styles[] array     int index=-1;  //--- calculate the number from the styles[] array to set style of horizontal line     if(tick\_number%50==0)        index=5;   // if tick\_number is divided by 50 without the remainder, then style is STYLE\_DASHDOTDOT     if(tick\_number%40==0)        index=4;   // ... style is STYLE\_DASHDOT     if(tick\_number%30==0)        index=3;   // ... STYLE\_DOT     if(tick\_number%20==0)        index=2;   // ... STYLE\_DASH     if(tick\_number%10==0)        index=1;   // ... STYLE\_SOLID  //--- if style is defined, set it           if(index!=-1)        IndicatorSetInteger(INDICATOR\_LEVELSTYLE,level,styles[index]);    } |

See also

[Custom Indicator Properties](../../Constants,-Enumerations-and-Structures/Indicator-Constants/Custom-Indicator-Properties/Custom-Indicator-Properties.md), [Program Properties (#property)](../../Language-Basics/Preprocessor/Program-Properties-(#property)/Program-Properties-(#property).md),  [Drawing Styles](../../Constants,-Enumerations-and-Structures/Indicator-Constants/Drawing-Styles/Drawing-Styles.md)
