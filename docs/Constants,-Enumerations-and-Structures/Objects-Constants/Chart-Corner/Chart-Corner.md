# Chart Corner

The Chart Corner to Which an Object Is Attached

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

|  |
| --- |
| void CreateLabel(long   chart\_id,                   string name,                   int    chart\_corner,                   int    anchor\_point,                   string text\_label,                   int    x\_ord,                   int    y\_ord)    {  //---     if(ObjectCreate(chart\_id,name,OBJ\_LABEL,0,0,0))       {        ObjectSetInteger(chart\_id,name,OBJPROP\_CORNER,chart\_corner);        ObjectSetInteger(chart\_id,name,OBJPROP\_ANCHOR,anchor\_point);        ObjectSetInteger(chart\_id,name,OBJPROP\_XDISTANCE,x\_ord);        ObjectSetInteger(chart\_id,name,OBJPROP\_YDISTANCE,y\_ord);        ObjectSetString(chart\_id,name,OBJPROP\_TEXT,text\_label);       }     else        Print("Failed to create the object OBJ\_LABEL ",name,", Error code = ", GetLastError());    }  //+------------------------------------------------------------------+  //| Script program start function                                    |  //+------------------------------------------------------------------+  void OnStart()    {  //---     int height=(int)ChartGetInteger(0,CHART\_HEIGHT\_IN\_PIXELS,0);     int width=(int)ChartGetInteger(0,CHART\_WIDTH\_IN\_PIXELS,0);     string arrows[4]={"LEFT\_UPPER","RIGHT\_UPPER","RIGHT\_LOWER","LEFT\_LOWER"};     CreateLabel(0,arrows[0],CORNER\_LEFT\_UPPER,ANCHOR\_LEFT\_UPPER,arrows[0],50,50);     CreateLabel(0,arrows[1],CORNER\_RIGHT\_UPPER,ANCHOR\_RIGHT\_UPPER,arrows[1],50,50);     CreateLabel(0,arrows[2],CORNER\_RIGHT\_LOWER,ANCHOR\_RIGHT\_LOWER,arrows[2],50,50);     CreateLabel(0,arrows[3],CORNER\_LEFT\_LOWER,ANCHOR\_LEFT\_LOWER,arrows[3],50,50);    } |
