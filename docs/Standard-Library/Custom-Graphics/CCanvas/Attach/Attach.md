# Attach

Attach

Gets the graphical resource from an [OBJ\_BITMAP\_LABEL](../../../../Constants,-Enumerations-and-Structures/Objects-Constants/Object-Types/OBJ_BITMAP_LABEL/OBJ_BITMAP_LABEL.md) object and attaches it to an instance of the CCanvas class.

|  |
| --- |
| bool  Attach(     const long         chart\_id,                              // chart identifier     const string       objname,                               // object name     ENUM\_COLOR\_FORMAT  clrfmt=COLOR\_FORMAT\_XRGB\_NOALPHA       // color processing method |

Creates a graphical [resource](../../../../MQL5-programs/Resources/Resources.md) for an [OBJ\_BITMAP\_LABEL](../../../../Constants,-Enumerations-and-Structures/Objects-Constants/Object-Types/OBJ_BITMAP_LABEL/OBJ_BITMAP_LABEL.md) object and attaches it to an instance of the CCanvas class.

|  |
| --- |
| bool  Attach(     const long         chart\_id,                              // chart identifier     const string       objname,                               // object name     const int          width,                                 // image width in pixels     const int          height,                                // image height in pixels     ENUM\_COLOR\_FORMAT  clrfmt=COLOR\_FORMAT\_XRGB\_NOALPHA       // color processing method |

 

Parameters

chart\_id

[out]  Chart identifier.

objname

[in]  Name of the graphical object.

width

[in]  Image width in the resource.

height

[in]  Image height in the resource.

clrfmt=COLOR\_FORMAT\_XRGB\_NOALPHA

[in]  Alpha channel processing method. The alpha channel is ignored by default.

Return Value

true – if successful, false - if failed to attach the object.
