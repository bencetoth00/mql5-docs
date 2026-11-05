# ObjectSetInteger


The function sets the value of the corresponding object property. The object property must be of the [datetime, int, color, bool or char](../../Language-Basics/Data-Types/Integer-Types/Integer-Types.md) type. There are 2 variants of the function.

Setting property value, without modifier

```cpp
bool  ObjectSetInteger(
   long                             chart_id,       // chart identifier
   string                           name,           // object name
   ENUM_OBJECT_PROPERTY_INTEGER     prop_id,        // property
   long                             prop_value      // value
   );
```

Setting a property value indicating the modifier

```cpp
bool  ObjectSetInteger(
   long                             chart_id,       // chart identifier
   string                           name,           // object name
   ENUM_OBJECT_PROPERTY_INTEGER     prop_id,        // property
   int                              prop_modifier,  // modifier
   long                             prop_value      // value
   );
```

Parameters

chart\_id

[in]  Chart identifier. 0 means the current chart.

name

[in]  Name of the object.

prop\_id

[in]  ID of the object property. The value can be one of the values of the [ENUM\_OBJECT\_PROPERTY\_INTEGER](../../Constants,-Enumerations-and-Structures/Objects-Constants/Object-Properties/Object-Properties.md#enum_object_property_integer) enumeration.

prop\_modifier

[in]  Modifier of the specified property.  It denotes the number of the level in [Fibonacci tools](../../Constants,-Enumerations-and-Structures/Objects-Constants/Object-Types/Object-Types.md) and in the graphical object Andrew's pitchfork. The numeration of levels starts from zero.

prop\_value

[in]  The value of the property.

Return Value

The function returns true only if the command to change properties of a graphical object has been sent to a chart successfully. Otherwise it returns false. To read more about the [error](../../Constants,-Enumerations-and-Structures/Codes-of-Errors-and-Warnings/Runtime-Errors/Runtime-Errors.md) call [GetLastError()](../../Checkup/GetLastError/GetLastError.md).

Note

The function uses an asynchronous call, which means that the function does not wait for the execution of the command that has been added to the queue of the specified chart. Instead, it immediately returns control.

To check the command execution result, you can use a function that requests the specified object property. However, you should keep in mind that such functions are added to the end of the queue of that chart, and they wait for the execution result, and can therefore be time consuming. This feature should be taken into account when working with a large number of objects on a chart.

An example of how to create a table of [Web colors](../../Constants,-Enumerations-and-Structures/Objects-Constants/Web-Colors/Web-Colors.md)

```cpp
//+------------------------------------------------------------------+
//|                                               Table of Web Colors|
//|                         Copyright 2011, MetaQuotes Software Corp |
//|                                        https://www.metaquotes.net |
//+------------------------------------------------------------------+
#define X_SIZE 140      // width of an edit object
#define Y_SIZE 33       // height of an edit object
//+------------------------------------------------------------------+
//| Array of web colors                                              |
//+------------------------------------------------------------------+
color ExtClr[140]=
  {
   clrAliceBlue,clrAntiqueWhite,clrAqua,clrAquamarine,clrAzure,clrBeige,clrBisque,clrBlack,clrBlanchedAlmond,
   clrBlue,clrBlueViolet,clrBrown,clrBurlyWood,clrCadetBlue,clrChartreuse,clrChocolate,clrCoral,clrCornflowerBlue,
   clrCornsilk,clrCrimson,clrCyan,clrDarkBlue,clrDarkCyan,clrDarkGoldenrod,clrDarkGray,clrDarkGreen,clrDarkKhaki,
   clrDarkMagenta,clrDarkOliveGreen,clrDarkOrange,clrDarkOrchid,clrDarkRed,clrDarkSalmon,clrDarkSeaGreen,
   clrDarkSlateBlue,clrDarkSlateGray,clrDarkTurquoise,clrDarkViolet,clrDeepPink,clrDeepSkyBlue,clrDimGray,
   clrDodgerBlue,clrFireBrick,clrFloralWhite,clrForestGreen,clrFuchsia,clrGainsboro,clrGhostWhite,clrGold,
   clrGoldenrod,clrGray,clrGreen,clrGreenYellow,clrHoneydew,clrHotPink,clrIndianRed,clrIndigo,clrIvory,clrKhaki,
   clrLavender,clrLavenderBlush,clrLawnGreen,clrLemonChiffon,clrLightBlue,clrLightCoral,clrLightCyan,
   clrLightGoldenrod,clrLightGreen,clrLightGray,clrLightPink,clrLightSalmon,clrLightSeaGreen,clrLightSkyBlue,
   clrLightSlateGray,clrLightSteelBlue,clrLightYellow,clrLime,clrLimeGreen,clrLinen,clrMagenta,clrMaroon,
   clrMediumAquamarine,clrMediumBlue,clrMediumOrchid,clrMediumPurple,clrMediumSeaGreen,clrMediumSlateBlue,
   clrMediumSpringGreen,clrMediumTurquoise,clrMediumVioletRed,clrMidnightBlue,clrMintCream,clrMistyRose,clrMoccasin,
   clrNavajoWhite,clrNavy,clrOldLace,clrOlive,clrOliveDrab,clrOrange,clrOrangeRed,clrOrchid,clrPaleGoldenrod,
   clrPaleGreen,clrPaleTurquoise,clrPaleVioletRed,clrPapayaWhip,clrPeachPuff,clrPeru,clrPink,clrPlum,clrPowderBlue,
   clrPurple,clrRed,clrRosyBrown,clrRoyalBlue,clrSaddleBrown,clrSalmon,clrSandyBrown,clrSeaGreen,clrSeashell,
   clrSienna,clrSilver,clrSkyBlue,clrSlateBlue,clrSlateGray,clrSnow,clrSpringGreen,clrSteelBlue,clrTan,clrTeal,
   clrThistle,clrTomato,clrTurquoise,clrViolet,clrWheat,clrWhite,clrWhiteSmoke,clrYellow,clrYellowGreen
  };
//+------------------------------------------------------------------+
//| Creating and initializing an edit object                         |
//+------------------------------------------------------------------+
void CreateColorBox(int x,int y,color c)
  {
//--- generate a name for a new edit object
   string name="ColorBox_"+(string)x+"_"+(string)y;
//--- create a new edit object
   if(!ObjectCreate(0,name,OBJ_EDIT,0,0,0))
     {
      Print("Cannot create: '",name,"'");
      return;
     }
//--- set coordinates, width and height
   ObjectSetInteger(0,name,OBJPROP_XDISTANCE,x*X_SIZE);
   ObjectSetInteger(0,name,OBJPROP_YDISTANCE,y*Y_SIZE);
   ObjectSetInteger(0,name,OBJPROP_XSIZE,X_SIZE);
   ObjectSetInteger(0,name,OBJPROP_YSIZE,Y_SIZE);
//--- set text color
   if(clrBlack==c) ObjectSetInteger(0,name,OBJPROP_COLOR,clrWhite);
   else            ObjectSetInteger(0,name,OBJPROP_COLOR,clrBlack);
//--- set background color
   ObjectSetInteger(0,name,OBJPROP_BGCOLOR,c);
//--- set text
   ObjectSetString(0,name,OBJPROP_TEXT,(string)c);
  }
//+------------------------------------------------------------------+
//| Script program start function                                    |
//+------------------------------------------------------------------+
void OnStart()
  {
//--- create 7x20 table of colored edit objects
   for(uint i=0;i<140;i++)
      CreateColorBox(i%7,i/7,ExtClr[i]);
  }
```

See also

[Object Types](../../Constants,-Enumerations-and-Structures/Objects-Constants/Object-Types/Object-Types.md), [Object Properties](../../Constants,-Enumerations-and-Structures/Objects-Constants/Object-Properties/Object-Properties.md)