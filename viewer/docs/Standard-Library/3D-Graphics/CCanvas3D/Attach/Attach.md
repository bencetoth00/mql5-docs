# Attach


Gets the graphical resource from an [OBJ\_BITMAP\_LABEL](../../../../Constants,-Enumerations-and-Structures/Objects-Constants/Object-Types/OBJ_BITMAP_LABEL/OBJ_BITMAP_LABEL.md) object and attaches it to an instance of the CCanvas class.

```cpp
bool  Attach(
   const long         chart_id,                              // chart ID
   const string       objname,                               // object name
   ENUM_COLOR_FORMAT  clrfmt=COLOR_FORMAT_XRGB_NOALPHA       // color handling method
   )
```

Creates a graphical [resource](../../../../MQL5-programs/Resources/Resources.md) for an [OBJ\_BITMAP\_LABEL](../../../../Constants,-Enumerations-and-Structures/Objects-Constants/Object-Types/OBJ_BITMAP_LABEL/OBJ_BITMAP_LABEL.md) object and attaches it to an instance of the CCanvas class.

```cpp
bool  Attach(
   const long         chart_id,                              // chart ID
   const string       objname,                               // object name
   const int          width,                                 // image width in pixels
   const int          height,                                // image height in pixels
   ENUM_COLOR_FORMAT  clrfmt=COLOR_FORMAT_XRGB_NOALPHA       // color handling method
   )
```

Parameters

chart\_id

[in]  Chart ID.

objname

[in]  Name of the graphical object.

width

[in]  Frame width in a resource.

height

[in]  Frame height.

clrfmt=COLOR\_FORMAT\_XRGB\_NOALPHA

[in]  Color handling method. See [ResourceCreate()](../../../../Common-Functions/ResourceCreate/ResourceCreate.md) function description to learn more about color handling methods.

Note

true – if successful, false - if failed to add a graphic object.