# OnMouseEvent


Mouse event handler (the [CHARTEVENT\_MOUSE\_MOVE](../../../../Constants,-Enumerations-and-Structures/Chart-Constants/Types-of-Chart-Events/Types-of-Chart-Events.md) chart event).

```cpp
virtual bool  OnMouseEvent(
   const int  x,         // x coordinate
   const int  y,         // y coordinate
   const int  flags      // flags
   )
```

Parameters

x

[in]  X coordinate of the mouse cursor relative to the upper-left corner of the chart.

y

[in]  Y coordinate of the mouse cursor relative to the upper-left corner of the chart.

flags

[in]  Flag of mouse buttons states.

Return Value

true - event has been processed, otherwise - false.