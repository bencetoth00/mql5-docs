# Chart Corner

# The Chart Corner to Which an Object Is Attached

There is a number of [graphical objects](../Object-Types/Object-Types.md) for which you can set a chart corner, relative to which the coordinates are specified in pixels. These are the following types of objects (in brackets object type identifiers are specified):

- Label (OBJ\_LABEL);
- Button (OBJ\_BUTTON);
- Bitmap Label (OBJ\_BITMAP\_LABEL);
- Edit (OBJ\_EDIT).

- Rectangle Label (OBJ\_RECTANGLE\_LABEL);

| Object | ID | X/Y | Width/Height | Date/Price | [OBJPROP\_CORNER](../Object-Properties/Object-Properties.md#enum_object_property_integer) | [OBJPROP\_ANCHOR](../Object-Properties/Object-Properties.md#enum_object_property_integer) | [OBJPROP\_ANGLE](../Object-Properties/Object-Properties.md#enum_object_property_double) |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Text | [OBJ\_TEXT](../Object-Types/OBJ_TEXT/OBJ_TEXT.md) | — | — | Yes | — | Yes | Yes |
| Label | [OBJ\_LABEL](../Object-Types/OBJ_LABEL/OBJ_LABEL.md) | Yes | Yes (read only) | — | Yes | Yes | Yes |
| Button | [OBJ\_BUTTON](../Object-Types/OBJ_BUTTON/OBJ_BUTTON.md) | Yes | Yes | — | Yes | — | — |
| Bitmap | [OBJ\_BITMAP](../Object-Types/OBJ_BITMAP/OBJ_BITMAP.md) | — | Yes (read only) | Yes | — | Yes | — |
| Bitmap Label | [OBJ\_BITMAP\_LABEL](../Object-Types/OBJ_BITMAP_LABEL/OBJ_BITMAP_LABEL.md) | Yes | Yes (read only) | — | Yes | Yes | — |
| Edit | [OBJ\_EDIT](../Object-Types/OBJ_EDIT/OBJ_EDIT.md) | Yes | Yes | — | Yes | — | — |
| Rectangle Label | [OBJ\_RECTANGLE\_LABEL](../Object-Types/OBJ_RECTANGLE_LABEL/OBJ_RECTANGLE_LABEL.md) | Yes | Yes | — | Yes | — | — |

The following designations are used in the table:

- X/Y – coordinates of anchor points specified in pixels relative to a chart corner;
- Width/Height – objects have width and height. For "read only", the width and height values are calculated only once the object is rendered on chart;
- Date/Price – anchor point coordinates are specified using the date and price values;
- OBJPROP\_CORNER – defines the chart corner relative to which the anchor point coordinates are specified. Can be one of the 4 values of the [ENUM\_BASE\_CORNER](Chart-Corner.md#enum_base_corner) enumeration;
- OBJPROP\_ANCHOR – defines the anchor point in object itself and can be one of the 9 values of the [ENUM\_ANCHOR\_POINT](../Methods-of-Object-Binding/Methods-of-Object-Binding.md#enum_anchor_point) enumeration. Coordinates in pixels are specified from this very point to selected chart corner;
- OBJPROP\_ANGLE – defines the object rotation angle counterclockwise.

In order to specify the chart corner, from which X and Y coordinates will be measured in pixels, use [ObjectSetInteger](../../../Object-Functions/ObjectSetInteger/ObjectSetInteger.md)(chartID, name, [OBJPROP\_CORNER](../Object-Properties/Object-Properties.md), chart\_corner), where:

- chartID - chart identifier;
- name –  name of a graphical object;
- OBJPROP\_CORNER – property ID to specify the corner for binding;
- chart\_corner – the desired chart corner, can be one of the values of the ENUM\_BASE\_CORNER enumeration.

ENUM\_BASE\_CORNER

| ID | Description |
| --- | --- |
| CORNER\_LEFT\_UPPER | Center of coordinates is in the upper left corner of the chart |
| CORNER\_LEFT\_LOWER | Center of coordinates is in the lower left corner of the chart |
| CORNER\_RIGHT\_LOWER | Center of coordinates is in the lower right corner of the chart |
| CORNER\_RIGHT\_UPPER | Center of coordinates is in the upper right corner of the chart |

Example:

```cpp
void CreateLabel(long   chart_id,
                 string name,
                 int    chart_corner,
                 int    anchor_point,
                 string text_label,
                 int    x_ord,
                 int    y_ord)
  {
//---
   if(ObjectCreate(chart_id,name,OBJ_LABEL,0,0,0))
     {
      ObjectSetInteger(chart_id,name,OBJPROP_CORNER,chart_corner);
      ObjectSetInteger(chart_id,name,OBJPROP_ANCHOR,anchor_point);
      ObjectSetInteger(chart_id,name,OBJPROP_XDISTANCE,x_ord);
      ObjectSetInteger(chart_id,name,OBJPROP_YDISTANCE,y_ord);
      ObjectSetString(chart_id,name,OBJPROP_TEXT,text_label);
     }
   else
      Print("Failed to create the object OBJ_LABEL ",name,", Error code = ", GetLastError());
  }
//+------------------------------------------------------------------+
//| Script program start function                                    |
//+------------------------------------------------------------------+
void OnStart()
  {
//---
   int height=(int)ChartGetInteger(0,CHART_HEIGHT_IN_PIXELS,0);
   int width=(int)ChartGetInteger(0,CHART_WIDTH_IN_PIXELS,0);
   string arrows[4]={"LEFT_UPPER","RIGHT_UPPER","RIGHT_LOWER","LEFT_LOWER"};
   CreateLabel(0,arrows[0],CORNER_LEFT_UPPER,ANCHOR_LEFT_UPPER,arrows[0],50,50);
   CreateLabel(0,arrows[1],CORNER_RIGHT_UPPER,ANCHOR_RIGHT_UPPER,arrows[1],50,50);
   CreateLabel(0,arrows[2],CORNER_RIGHT_LOWER,ANCHOR_RIGHT_LOWER,arrows[2],50,50);
   CreateLabel(0,arrows[3],CORNER_LEFT_LOWER,ANCHOR_LEFT_LOWER,arrows[3],50,50);
  }
```