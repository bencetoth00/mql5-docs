# TriangleAA


Draws a triangle using antialiasing algorithm.

```cpp
void  TriangleAA(
   const int   x1,                 // X coordinate
   const int   y1,                 // Y coordinate
   const int   x2,                 // X coordinate
   const int   y2,                 // Y coordinate
   const int   x3,                 // X coordinate
   const int   y3,                 // Y coordinate
   const uint  clr,                // color
   const uint  style=UINT_MAX      // line style
   );
```

Parameters

x1

[in]  X coordinate of the triangle's first corner.

y1

[in]  Y coordinate of the triangle's first corner.

x2

[in]  X coordinate of the triangle's second corner.

y2

[in]  Y coordinate of the triangle's second corner.

x3

[in]  X coordinate of the triangle's third corner.

y3

[in]  Y coordinate of the triangle's third corner.

clr

[in]  Color in ARGB format.

style=UINT\_MAX

[in]  Line style is one of [ENUM\_LINE\_STYLE](../../../../Constants,-Enumerations-and-Structures/Indicator-Constants/Drawing-Styles/Drawing-Styles.md#enum_line_style) enumeration's values or a custom value.