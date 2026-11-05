# IndicatorSetString

IndicatorSetString

The function sets the value of the corresponding indicator property. Indicator property must be of the string type. There are two variants of the function.

Call with specifying the property identifier.

|  |
| --- |
| bool  IndicatorSetString(     int     prop\_id,           // identifier     string  prop\_value         // value to be set     ); |

Call with specifying the property identifier and modifier.

|  |
| --- |
| bool  IndicatorSetString(     int     prop\_id,           // identifier     int     prop\_modifier,     // modifier     string  prop\_value         // value to be set     ) |

Parameters

prop\_id

[in]  Identifier of the indicator property. The value can be one of the values of the [ENUM\_CUSTOMIND\_PROPERTY\_STRING](../../Constants,-Enumerations-and-Structures/Indicator-Constants/Custom-Indicator-Properties/Custom-Indicator-Properties.md#enum_customind_property_string) enumeration.

prop\_modifier

[in]  Modifier of the specified property. Only level properties require a modifier.

prop\_value

[in]  Value of property.

Return Value

In case of successful execution, returns true, otherwise - false.

Note

Numbering of properties (modifiers) starts from 1 (one) when using the #property directive, while the function uses numbering from 0 (zero). In case the level number is set incorrectly, [indicator display](../../Constants,-Enumerations-and-Structures/Indicator-Constants/Drawing-Styles/Drawing-Styles.md) can differ from the intended one.

For example, in order to set description of the first horizontal line use zeroth index:

- IndicatorSetString(INDICATOR\_LEVELTEXT, 0, "First Level") - index 0 is used to set text description of the first level.

Example: indicator that sets text labels to the indicator horizontal lines.

![Example of using the IndicatorSetString() function](../../assets/indicatorsetstring.png "Example of using the IndicatorSetString() function")

|  |
| --- |
| #property indicator\_separate\_window  #property indicator\_minimum 0  #property indicator\_maximum 100  //--- display three horizontal levels in a separate indicator window  #property indicator\_level1 30  #property indicator\_level2 50  #property indicator\_level3 70  //--- set color of horizontal levels  #property indicator\_levelcolor clrRed  //--- set style of horizontal levels  #property indicator\_levelstyle STYLE\_SOLID  //+------------------------------------------------------------------+  //| Custom indicator initialization function                         |  //+------------------------------------------------------------------+  int OnInit()    {  //--- set descriptions of horizontal levels     IndicatorSetString(INDICATOR\_LEVELTEXT,0,"First Level (index 0)");     IndicatorSetString(INDICATOR\_LEVELTEXT,1,"Second Level (index 1)");     IndicatorSetString(INDICATOR\_LEVELTEXT,2,"Third Level (index 2)");  //--- set the short name for indicator     IndicatorSetString(INDICATOR\_SHORTNAME,"IndicatorSetString() Demo");  //---     return(INIT\_SUCCEEDED);    }  //+------------------------------------------------------------------+  //| Custom indicator iteration function                              |  //+------------------------------------------------------------------+  int OnCalculate(const int rates\_total,                  const int prev\_calculated,                  const datetime &time[],                  const double &open[],                  const double &high[],                  const double &low[],                  const double &close[],                  const long &tick\_volume[],                  const long &volume[],                  const int &spread[])    {  //---       //--- return value of prev\_calculated for next call     return(rates\_total);    } |

See also

[Custom Indicator Properties](../../Constants,-Enumerations-and-Structures/Indicator-Constants/Custom-Indicator-Properties/Custom-Indicator-Properties.md), [Program Properties (#property)](../../Language-Basics/Preprocessor/Program-Properties-(#property)/Program-Properties-(#property).md)
