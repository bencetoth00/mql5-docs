# Object Functions


This is the group of functions intended for working with graphic objects relating to any specified chart.

The functions defining the properties of graphical objects, as well as [ObjectCreate()](ObjectCreate/ObjectCreate.md) and [ObjectMove()](ObjectMove/ObjectMove.md) operations for creating and moving objects along the chart are actually used for sending commands to the chart. If these functions are executed successfully, the command is included in the common queue of the chart events. Visual changes in the properties of graphical objects are implemented when handling the queue of the chart events.

Thus, do not expect an immediate visual update of graphical objects after calling these functions. Generally, the graphical objects on the chart are updated automatically by the terminal following the change events - a new quote arrival, resizing the chart window, etc. Use [ChartRedraw()](../Chart-Operations/ChartRedraw/ChartRedraw.md) function to forcefully update the graphical objects.

| Function | Action |
| --- | --- |
| [ObjectCreate](ObjectCreate/ObjectCreate.md) | Creates an object of the specified type in a specified chart |
| [ObjectName](ObjectName/ObjectName.md) | Returns the name of an object of the corresponding type in the specified chart (specified chart subwindow) |
| [ObjectDelete](ObjectDelete/ObjectDelete.md) | Removes the object with the specified name from the specified chart (from the specified chart subwindow) |
| [ObjectsDeleteAll](ObjectsDeleteAll/ObjectsDeleteAll.md) | Removes all objects of the specified type from the specified chart (from the specified chart subwindow) |
| [ObjectFind](ObjectFind/ObjectFind.md) | Searches for an object with the specified ID by the name |
| [ObjectGetTimeByValue](ObjectGetTimeByValue/ObjectGetTimeByValue.md) | Returns the time value for the specified object price value |
| [ObjectGetValueByTime](ObjectGetValueByTime/ObjectGetValueByTime.md) | Returns the price value of an object for the specified time |
| [ObjectMove](ObjectMove/ObjectMove.md) | Changes the coordinates of the specified object anchor point |
| [ObjectsTotal](ObjectsTotal/ObjectsTotal.md) | Returns the number of objects of the specified type in the specified chart (specified chart subwindow) |
| [ObjectGetDouble](ObjectGetDouble/ObjectGetDouble.md) | Returns the double value of the corresponding object property |
| [ObjectGetInteger](ObjectGetInteger/ObjectGetInteger.md) | Returns the integer value of the corresponding object property |
| [ObjectGetString](ObjectGetString/ObjectGetString.md) | Returns the string value of the corresponding object property |
| [ObjectSetDouble](ObjectSetDouble/ObjectSetDouble.md) | Sets the value of the corresponding object property |
| [ObjectSetInteger](ObjectSetInteger/ObjectSetInteger.md) | Sets the value of the corresponding object property |
| [ObjectSetString](ObjectSetString/ObjectSetString.md) | Sets the value of the corresponding object property |
| [TextSetFont](TextSetFont/TextSetFont.md) | Sets the font for displaying the text using drawing methods (Arial 20 used by default) |
| [TextOut](TextOut/TextOut.md) | Transfers the text to the custom array (buffer) designed for creation of a graphical [resource](../Common-Functions/ResourceCreate/ResourceCreate.md) |
| [TextGetSize](TextGetSize/TextGetSize.md) | Returns the string's width and height at the current [font settings](TextSetFont/TextSetFont.md) |

Every graphical object should have a name unique within one [chart](../Chart-Operations/Chart-Operations.md), including its subwindows. Changing of a name of a graphic object generates two events: event of deletion of an object with the old name, and event of creation of an object with a new name.

After an object is created or an [object property](../Constants,-Enumerations-and-Structures/Objects-Constants/Object-Properties/Object-Properties.md) is modified it is recommended to call the [ChartRedraw()](../Chart-Operations/ChartRedraw/ChartRedraw.md) function, which commands the client terminal to forcibly draw a chart (and all [visible](../Constants,-Enumerations-and-Structures/Objects-Constants/Visibility-of-Objects/Visibility-of-Objects.md) objects in it).
