# LineThick


Draws a segment of a freehand line having a specified width using antialiasing algorithm.

```cpp
void  LineThick(
   const int      x1,            // X coordinate of the segment's first point
   const int      y1,            // Y coordinate of the segment's first point
   const int      x2,            // X coordinate of the segment's second point
   const int      y2,            // Y coordinate of the segment's second point
   const uint     clr,           // color
   const int      size,          // line width
   const uint     style,         // line style
   ENUM_LINE_END  end_style      // line ends style
   )
```

Parameters

x1

[in]  X coordinate of the segment's first point.

y1

[in]  Y coordinate of the segment's first point.

x2

[in]  X coordinate of the segment's second point.

y2

[in]  Y coordinate of the segment's second point.

clr

[in]  Color in ARGB format.

size

[in]  Line width.

style

[in]  Line style is one of the ENUM\_LINE\_STYLE enumeration's values or a custom value.

end\_style

[in]  Line style is one of the ENUM\_LINE\_END enumeration's values

ENUM\_LINE\_END

| ID | Description |
| --- | --- |
| LINE\_END\_ROUND | Line ends are rounded. |
| LINE\_END\_BUTT | Line ends are cut. |
| LINE\_END\_SQUARE | A line ends in a filled rectangle. |