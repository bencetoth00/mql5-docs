# LineThickHorizontal

LineThickHorizontal

Draws a horizontal segment of a freehand line having a specified width antialiasing.

|  |
| --- |
| void  LineThickHorizontal(     const int      x1,            // X coordinate of the segment's first point     const int      x2,            // X coordinate of the segment's second point     const int      y,             // Y coordinate of the segment     const uint     clr,           // color     const int      size,          // line width     const uint     style,         // line style     ENUM\_LINE\_END  end\_style      // line ends style     ) |

Parameters

x1

[in]  X coordinate of the segment's first point.

x2

[in]  X coordinate of the segment's second point.

y

[in]  Segment's Y coordinate.

clr

[in]  Color in ARGB format.

size

[in]  Line width.

style

[in]  Line style is one of the ENUM\_LINE\_STYLE enumeration's values or a custom value.

end\_style

[in]  Line style is one of the [ENUM\_LINE\_END](../LineThick/LineThick.md#enum_line_end) enumeration's values.
