# Object Properties

Object Properties

Graphical objects can have various properties depending on the object type. Values of object properties are set up and received by corresponding [functions for working with graphical objects](../../../Object-Functions/Object-Functions.md).

All objects used in technical analysis are bound to the time and price coordinates: trendline, channels, Fibonacci tools, etc. But there is a number of auxiliary objects intended to improve the user interface that are bound to the always visible part of a chart (main chart windows or indicator subwindows):

| Object | ID | X/Y | Width/Height | Date/Price | [OBJPROP\_CORNER](Object-Properties.md#enum_object_property_integer) | [OBJPROP\_ANCHOR](Object-Properties.md#enum_object_property_integer) | [OBJPROP\_ANGLE](Object-Properties.md#enum_object_property_double) |
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
- OBJPROP\_CORNER – defines the chart corner relative to which the anchor point coordinates are specified. Can be one of the 4 values of the [ENUM\_BASE\_CORNER](../Chart-Corner/Chart-Corner.md#enum_base_corner) enumeration;
- OBJPROP\_ANCHOR – defines the anchor point in object itself and can be one of the 9 values of the [ENUM\_ANCHOR\_POINT](../Methods-of-Object-Binding/Methods-of-Object-Binding.md#enum_anchor_point) enumeration. Coordinates in pixels are specified from this very point to selected chart corner;
- OBJPROP\_ANGLE – defines the object rotation angle counterclockwise.

The functions defining the properties of graphical objects, as well as [ObjectCreate()](../../../Object-Functions/ObjectCreate/ObjectCreate.md) and [ObjectMove()](../../../Object-Functions/ObjectMove/ObjectMove.md) operations for creating and moving objects along the chart are actually used for sending commands to the chart. If these functions are executed successfully, the command is included in the common queue of the chart events. Visual changes in the properties of graphical objects are implemented when handling the queue of the chart events.

Thus, do not expect an immediate visual update of graphical objects after calling these functions. Generally, the graphical objects on the chart are updated automatically by the terminal following the change events - a new quote arrival, resizing the chart window, etc. Use [ChartRedraw()](../../../Chart-Operations/ChartRedraw/ChartRedraw.md) function to forcefully update the graphical objects.

For functions [ObjectSetInteger()](../../../Object-Functions/ObjectSetInteger/ObjectSetInteger.md) and [ObjectGetInteger()](../../../Object-Functions/ObjectGetInteger/ObjectGetInteger.md)

ENUM\_OBJECT\_PROPERTY\_INTEGER

| Identifier | Description | Property Type |
| --- | --- | --- |
| OBJPROP\_COLOR | Color | color |
| OBJPROP\_STYLE | Style | [ENUM\_LINE\_STYLE](../../Indicator-Constants/Drawing-Styles/Drawing-Styles.md#enum_line_style) |
| OBJPROP\_WIDTH | Line thickness | int |
| OBJPROP\_BACK | Object in the background | bool |
| OBJPROP\_ZORDER | Priority of a graphical object for receiving events of clicking on a chart ([CHARTEVENT\_CLICK](../../Chart-Constants/Types-of-Chart-Events/Types-of-Chart-Events.md)). The default zero value is set when creating an object; the priority can be increased if necessary. When objects are placed one atop another, only one of them with the highest priority will receive the CHARTEVENT\_CLICK event. | long |
| OBJPROP\_FILL | Fill an object with color (for OBJ\_RECTANGLE, OBJ\_TRIANGLE, OBJ\_ELLIPSE, OBJ\_CHANNEL, OBJ\_STDDEVCHANNEL, OBJ\_REGRESSION) | bool |
| OBJPROP\_HIDDEN | Disable the display of a graphical object in the client terminal [object list](https://www.metatrader5.com/en/terminal/help/charts_advanced/charts_objects_list#objects) called by the Charts \ Objects \ Object List command. This prevents accidental deletion of MQL5 program service objects by a user. In addition to hiding the object from the list, the property disables the ability to delete it using the Charts \ Objects \ Delete Last command.     The value of 'true' hides the object. By default, hidden objects are those that display calendar events and trading history, as well as those [created from an MQL5 program](../../../Object-Functions/ObjectCreate/ObjectCreate.md). Click "List all" to see them in the object list and access their properties. | bool |
| OBJPROP\_SELECTED | Object is selected | bool |
| OBJPROP\_READONLY | Ability to edit text in the Edit object | bool |
| OBJPROP\_TYPE | Object type | [ENUM\_OBJECT](../Object-Types/Object-Types.md)   r/o |
| OBJPROP\_TIME | Time coordinate | datetime   modifier=number of anchor point |
| OBJPROP\_SELECTABLE | Object availability | bool |
| OBJPROP\_CREATETIME | Time of object creation | datetime    r/o |
| OBJPROP\_LEVELS | Number of levels | int |
| OBJPROP\_LEVELCOLOR | Color of the line-level | color   modifier=level number |
| OBJPROP\_LEVELSTYLE | Style of the line-level | [ENUM\_LINE\_STYLE](../../Indicator-Constants/Drawing-Styles/Drawing-Styles.md#enum_line_style) modifier=level number |
| OBJPROP\_LEVELWIDTH | Thickness of the line-level | int      modifier=level number |
| OBJPROP\_ALIGN | Horizontal text alignment in the "Edit" object (OBJ\_EDIT) | [ENUM\_ALIGN\_MODE](Object-Properties.md#enum_align_mode) |
| OBJPROP\_FONTSIZE | Font size | int |
| OBJPROP\_RAY\_LEFT | Ray goes to the left | bool |
| OBJPROP\_RAY\_RIGHT | Ray goes to the right | bool |
| OBJPROP\_RAY | A vertical line goes through all the windows of a chart | bool |
| OBJPROP\_ELLIPSE | Showing the full ellipse of the Fibonacci Arc object ([OBJ\_FIBOARC](../Object-Types/Object-Types.md)) | bool |
| OBJPROP\_ARROWCODE | Arrow code for the Arrow object | uchar |
| OBJPROP\_TIMEFRAMES | Visibility of an object at timeframes | set of flags [flags](../Visibility-of-Objects/Visibility-of-Objects.md) |
| OBJPROP\_ANCHOR | Location of the anchor point of a graphical object | [ENUM\_ARROW\_ANCHOR](../Methods-of-Object-Binding/Methods-of-Object-Binding.md#enum_arrow_anchor) (for OBJ\_ARROW),  [ENUM\_ANCHOR\_POINT](../Methods-of-Object-Binding/Methods-of-Object-Binding.md) (for OBJ\_LABEL, OBJ\_BITMAP\_LABEL and OBJ\_TEXT) |
| OBJPROP\_XDISTANCE | The distance in pixels along the X axis from the binding corner (see [note](Object-Properties.md#distance_fixedsize)) | int |
| OBJPROP\_YDISTANCE | The distance in pixels along the Y axis from the binding corner (see [note](Object-Properties.md#distance_fixedsize)) | int |
| OBJPROP\_DIRECTION | Trend of the Gann object | [ENUM\_GANN\_DIRECTION](../Gann-Objects/Gann-Objects.md) |
| OBJPROP\_DEGREE | Level of the Elliott Wave Marking | [ENUM\_ELLIOT\_WAVE\_DEGREE](../Levels-of-Elliott-Wave/Levels-of-Elliott-Wave.md) |
| OBJPROP\_DRAWLINES | Displaying lines for marking the Elliott Wave | bool |
| OBJPROP\_STATE | Button state (pressed / depressed) | bool |
| OBJPROP\_CHART\_ID | ID of the "Chart" object ([OBJ\_CHART](../Object-Types/Object-Types.md)). It allows working with the properties of this object like with a normal chart using the functions described in [Chart Operations](../../../Chart-Operations/Chart-Operations.md), but there some [exceptions](Object-Properties.md#objprop_chart_id_exception). | long   r/o |
| OBJPROP\_XSIZE | The object's width along the X axis in pixels. Specified for  OBJ\_LABEL (read only), OBJ\_BUTTON, OBJ\_CHART, OBJ\_BITMAP, OBJ\_BITMAP\_LABEL, OBJ\_EDIT, OBJ\_RECTANGLE\_LABEL objects. | int |
| OBJPROP\_YSIZE | The object's height along the Y axis in pixels. Specified for  OBJ\_LABEL (read only), OBJ\_BUTTON, OBJ\_CHART, OBJ\_BITMAP, OBJ\_BITMAP\_LABEL, OBJ\_EDIT, OBJ\_RECTANGLE\_LABEL objects. | int |
| OBJPROP\_XOFFSET | The X coordinate of the upper left corner of the [rectangular visible area](Object-Properties.md#visual_rectangle) in the graphical objects "Bitmap Label" and "Bitmap" (OBJ\_BITMAP\_LABEL and OBJ\_BITMAP). The value is set in pixels relative to the upper left corner of the original image. | int |
| OBJPROP\_YOFFSET | The Y coordinate of the upper left corner of the [rectangular visible area](Object-Properties.md#visual_rectangle) in the graphical objects "Bitmap Label" and "Bitmap" (OBJ\_BITMAP\_LABEL and OBJ\_BITMAP). The value is set in pixels relative to the upper left corner of the original image. | int |
| OBJPROP\_PERIOD | Timeframe for the Chart object | [ENUM\_TIMEFRAMES](../../Chart-Constants/Chart-Timeframes/Chart-Timeframes.md) |
| OBJPROP\_DATE\_SCALE | Displaying the time scale for the Chart object | bool |
| OBJPROP\_PRICE\_SCALE | Displaying the price scale for the Chart object | bool |
| OBJPROP\_CHART\_SCALE | The scale for the Chart object | int   value in the range 0–5 |
| OBJPROP\_BGCOLOR | The background color for  OBJ\_EDIT, OBJ\_BUTTON, OBJ\_RECTANGLE\_LABEL | color |
| OBJPROP\_CORNER | The corner of the chart to link a graphical object | [ENUM\_BASE\_CORNER](../Chart-Corner/Chart-Corner.md) |
| OBJPROP\_BORDER\_TYPE | Border type for the "Rectangle label" object | [ENUM\_BORDER\_TYPE](Object-Properties.md#enum_border_type) |
| OBJPROP\_BORDER\_COLOR | Border color for the OBJ\_EDIT and OBJ\_BUTTON objects | color |

When using [chart operations](../../../Chart-Operations/Chart-Operations.md) for the "Chart" object ([OBJ\_CHART](../Object-Types/Object-Types.md)), the following limitations are imposed:

- It cannot be closed using [ChartClose()](../../../Chart-Operations/ChartClose/ChartClose.md);
- Symbol/period cannot be changed using the [ChartSetSymbolPeriod()](../../../Chart-Operations/ChartSetSymbolPeriod/ChartSetSymbolPeriod.md) function;
- The following properties are ineffective CHART\_SCALE, CHART\_BRING\_TO\_TOP, CHART\_SHOW\_DATE\_SCALE and CHART\_SHOW\_PRICE\_SCALE ([ENUM\_CHART\_PROPERTY\_INTEGER](../../Chart-Constants/Chart-Properties/Chart-Properties.md#enum_chart_property_integer)).

 

You can set a special mode of image display for [OBJ\_BITMAP\_LABEL](../Object-Types/Object-Types.md) and [OBJ\_BITMAP](../Object-Types/Object-Types.md) objects. In this mode, only part of an original image (at which a rectangular visible area is applied) is displayed, while the rest of the image becomes invisible. The size of this area should be set using the properties OBJPROP\_XSIZE and OBJPROP\_YSIZE. The visible area can be "moved" only within the original image using the properties OBJPROP\_XOFFSET and OBJPROP\_YOFFSET.

 

For the fixed-sized objects: [OBJ\_BUTTON](../Object-Types/OBJ_BUTTON/OBJ_BUTTON.md), [OBJ\_RECTANGLE\_LABEL](../Object-Types/OBJ_RECTANGLE_LABEL/OBJ_RECTANGLE_LABEL.md), [OBJ\_EDIT](../Object-Types/OBJ_EDIT/OBJ_EDIT.md) and [OBJ\_CHART](../Object-Types/OBJ_CHART/OBJ_CHART.md), properties OBJPROP\_XDISTANCE and OBJPROP\_YDISTANCE set the position of the top left point of the object relative to the chart corner (OBJPROP\_CORNER), from which the X and Y coordinates will be counted in pixels.

 

For functions [ObjectSetDouble()](../../../Object-Functions/ObjectSetDouble/ObjectSetDouble.md) and [ObjectGetDouble()](../../../Object-Functions/ObjectGetDouble/ObjectGetDouble.md)

ENUM\_OBJECT\_PROPERTY\_DOUBLE

| Identifier | Description | Property Type |
| --- | --- | --- |
| OBJPROP\_PRICE | Price coordinate | double    modifier=number of anchor point |
| OBJPROP\_LEVELVALUE | Level value | double    modifier=level number |
| OBJPROP\_SCALE | Scale (properties of Gann objects and Fibonacci Arcs) | double |
| OBJPROP\_ANGLE | Angle.  For the objects with no angle specified, created from a program, the value is equal to [EMPTY\_VALUE](../../Named-Constants/Other-Constants/Other-Constants.md) | double |
| OBJPROP\_DEVIATION | Deviation for the Standard Deviation Channel | double |

 

For functions [ObjectSetString()](../../../Object-Functions/ObjectSetString/ObjectSetString.md) and [ObjectGetString()](../../../Object-Functions/ObjectGetString/ObjectGetString.md)

ENUM\_OBJECT\_PROPERTY\_STRING

| Identifier | Description | Property Type |
| --- | --- | --- |
| OBJPROP\_NAME | Object name | string |
| OBJPROP\_TEXT | Description of the object (the text contained in the object) | string |
| OBJPROP\_TOOLTIP | The text of a tooltip. If the property is not set, then the tooltip generated automatically by the terminal is shown. A tooltip can be disabled by setting the "\n" (line feed) value to it | string |
| OBJPROP\_LEVELTEXT | Level description | string    modifier=level number |
| OBJPROP\_FONT | Font | string |
| OBJPROP\_BMPFILE | The name of BMP-file for Bitmap Label. See also [Resources](../../../MQL5-programs/Resources/Resources.md) | string    modifier: 0-state ON, 1-state OFF |
| OBJPROP\_SYMBOL | Symbol for the Chart object | string |

 

For the OBJ\_RECTANGLE\_LABEL object ("Rectangle label") one of the three design modes can be set, to which the following values of ENUM\_BORDER\_TYPE correspond.

ENUM\_BORDER\_TYPE

| Identifier | Description |
| --- | --- |
| BORDER\_FLAT | Flat form |
| BORDER\_RAISED | Prominent form |
| BORDER\_SUNKEN | Concave form |

 

For the OBJ\_EDIT object ("Edit") and for the [ChartScreenShot()](../../../Chart-Operations/ChartScreenShot/ChartScreenShot.md) function, you can specify the horizontal alignment type using the values of the ENUM\_ALIGN\_MODE enumeration.

ENUM\_ALIGN\_MODE

| Identifier | Description |
| --- | --- |
| ALIGN\_LEFT | Left alignment |
| ALIGN\_CENTER | Centered (only for the Edit object) |
| ALIGN\_RIGHT | Right alignment |

Example:

|  |
| --- |
| #define  UP          "\x0431"  //+------------------------------------------------------------------+  //| Script program start function                                    |  //+------------------------------------------------------------------+  void OnStart()    {  //---     string label\_name="my\_OBJ\_LABEL\_object";     if(ObjectFind(0,label\_name)<0)       {        Print("Object ",label\_name," not found. Error code = ",GetLastError());        //--- create Label object        ObjectCreate(0,label\_name,OBJ\_LABEL,0,0,0);                   //--- set X coordinate        ObjectSetInteger(0,label\_name,OBJPROP\_XDISTANCE,200);        //--- set Y coordinate        ObjectSetInteger(0,label\_name,OBJPROP\_YDISTANCE,300);        //--- define text color        ObjectSetInteger(0,label\_name,OBJPROP\_COLOR,clrWhite);        //--- define text for object Label        ObjectSetString(0,label\_name,OBJPROP\_TEXT,UP);        //--- define font        ObjectSetString(0,label\_name,OBJPROP\_FONT,"Wingdings");        //--- define font size        ObjectSetInteger(0,label\_name,OBJPROP\_FONTSIZE,10);        //--- 45 degrees rotation clockwise        ObjectSetDouble(0,label\_name,OBJPROP\_ANGLE,-45);        //--- disable for mouse selecting        ObjectSetInteger(0,label\_name,OBJPROP\_SELECTABLE,false);        //--- draw it on the chart        ChartRedraw(0);                                             }    } |
