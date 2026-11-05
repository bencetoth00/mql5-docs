# Web Colors


The following color constants are defined for the [color](../../../Language-Basics/Data-Types/Integer-Types/Color-Type/Color-Type.md) type:

|  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| clrBlack | clrDarkGreen | clrDarkSlateGray | clrOlive | clrGreen | clrTeal | clrNavy | clrPurple |
| clrMaroon | clrIndigo | clrMidnightBlue | clrDarkBlue | clrDarkOliveGreen | clrSaddleBrown | clrForestGreen | clrOliveDrab |
| clrSeaGreen | clrDarkGoldenrod | clrDarkSlateBlue | clrSienna | clrMediumBlue | clrBrown | clrDarkTurquoise | clrDimGray |
| clrLightSeaGreen | clrDarkViolet | clrFireBrick | clrMediumVioletRed | clrMediumSeaGreen | clrChocolate | clrCrimson | clrSteelBlue |
| clrGoldenrod | clrMediumSpringGreen | clrLawnGreen | clrCadetBlue | clrDarkOrchid | clrYellowGreen | clrLimeGreen | clrOrangeRed |
| clrDarkOrange | clrOrange | clrGold | clrYellow | clrChartreuse | clrLime | clrSpringGreen | clrAqua |
| clrDeepSkyBlue | clrBlue | clrMagenta | clrRed | clrGray | clrSlateGray | clrPeru | clrBlueViolet |
| clrLightSlateGray | clrDeepPink | clrMediumTurquoise | clrDodgerBlue | clrTurquoise | clrRoyalBlue | clrSlateBlue | clrDarkKhaki |
| clrIndianRed | clrMediumOrchid | clrGreenYellow | clrMediumAquamarine | clrDarkSeaGreen | clrTomato | clrRosyBrown | clrOrchid |
| clrMediumPurple | clrPaleVioletRed | clrCoral | clrCornflowerBlue | clrDarkGray | clrSandyBrown | clrMediumSlateBlue | clrTan |
| clrDarkSalmon | clrBurlyWood | clrHotPink | clrSalmon | clrViolet | clrLightCoral | clrSkyBlue | clrLightSalmon |
| clrPlum | clrKhaki | clrLightGreen | clrAquamarine | clrSilver | clrLightSkyBlue | clrLightSteelBlue | clrLightBlue |
| clrPaleGreen | clrThistle | clrPowderBlue | clrPaleGoldenrod | clrPaleTurquoise | clrLightGray | clrWheat | clrNavajoWhite |
| clrMoccasin | clrLightPink | clrGainsboro | clrPeachPuff | clrPink | clrBisque | clrLightGoldenrod | clrBlanchedAlmond |
| clrLemonChiffon | clrBeige | clrAntiqueWhite | clrPapayaWhip | clrCornsilk | clrLightYellow | clrLightCyan | clrLinen |
| clrLavender | clrMistyRose | clrOldLace | clrWhiteSmoke | clrSeashell | clrIvory | clrHoneydew | clrAliceBlue |
| clrLavenderBlush | clrMintCream | clrSnow | clrWhite |  |  |  |  |

Color can be set to an object using the [ObjectSetInteger()](../../../Object-Functions/ObjectGetInteger/ObjectGetInteger.md) function. For setting color to custom indicators the [PlotIndexSetInteger()](../../../Custom-Indicators/PlotIndexSetInteger/PlotIndexSetInteger.md) function is used. For getting color values there are similar functions [ObjectGetInteger()](../../../Object-Functions/ObjectGetInteger/ObjectGetInteger.md) and [PlotIndexGetInteger()](../../../Custom-Indicators/PlotIndexGetInteger/PlotIndexGetInteger.md).

Example:

```cpp
//---- indicator settings
#property indicator_chart_window
#property indicator_buffers 3
#property indicator_plots   3
#property indicator_type1   DRAW_LINE
#property indicator_type2   DRAW_LINE
#property indicator_type3   DRAW_LINE
#property indicator_color1  clrBlue
#property indicator_color2  clrRed
#property indicator_color3  clrLime
```