# Create


Creates a graphic resource for rendering a 3D scene without binding to a chart object.

```cpp
virtual bool  Create(
   const string       name,                                 // graphical object name
   const int          width,                                // width
   const int          height,                               // height
   ENUM_COLOR_FORMAT  clrfmt=COLOR_FORMAT_XRGB_NOALPHA      // color format
   );
```

Parameters

name

[in]  Graphical object name.

width

[in]  Frame width.

height

[in]  Frame height.

clrfmt=COLOR\_FORMAT\_XRGB\_NOALPHA

[in]  Color handling method. See [ResourceCreate()](../../../../Common-Functions/ResourceCreate/ResourceCreate.md) function description to learn more about color handling methods.

Note

true - if a resource is created, otherwise - false.