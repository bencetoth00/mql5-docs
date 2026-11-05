# ResourceCreate

ResourceCreate

Creates an image resource based on a data set. There are two variants of the function:  
Creating a resource based on a file

|  |
| --- |
| bool  ResourceCreate(     const string      resource\_name,       // Resource name     const string      path                 // A relative path to the file     ); |

Creating a resource based on the array of pixels

|  |
| --- |
| bool  ResourceCreate(     const string      resource\_name,       // Resource name     const uint&       data[],              // Data set as an array     uint              img\_width,           // The width of the image resource     uint              img\_height,          // The height of the image resource     uint              data\_xoffset,        // The horizontal rightward offset of the upper left corner of the image     uint              data\_yoffset,        // The vertical downward offset of the upper left corner of the image     uint              data\_width,          // The total width of the image based on the data set     ENUM\_COLOR\_FORMAT color\_format         // Color processing method     ); |

Parameters

resource\_name

[in]  Resource name.

data[][]

[in]  A one-dimensional or two-dimensional array for creating a complete image.

img\_width

[in]  The width of the rectangular image area in pixels to be placed in the resource in the form of an image. It cannot be greater than the data\_width value.

img\_height

[in]  The height of the rectangular image area in pixels to be placed in the resource in the form of an image.

data\_xoffset

[in]  The horizontal rightward offset of the rectangular area of the image.

data\_yoffset

[in]  The vertical downward offset of the rectangular area of the image.

data\_width

[in]  Required only for one-dimensional arrays. It denotes the full width of the image from the data set. If data\_width=0, it is assumed to be equal to img\_width. For two-dimensional arrays the parameter is ignored and is assumed to be equal to the second dimension of the data[] array.

color\_format

[in]  Color processing method, from a value from the [ENUM\_COLOR\_FORMAT](ResourceCreate.md#enum_color_format) enumeration.

Return Value

Returns true if successful, otherwise false. To get information about the error call the [GetLastError()](../../Checkup/GetLastError/GetLastError.md) function. The following errors may occur:

- 4015 – ERR\_RESOURCE\_NAME\_DUPLICATED (identical names of the dynamic and the [static](../../MQL5-programs/Resources/Resources.md) resource)
- 4016 – ERR\_RESOURCE\_NOT\_FOUND (the resource is not found)
- 4017 – ERR\_RESOURCE\_UNSUPPORTED\_TYPE (this type of resource is not supported)
- 4018 – ERR\_RESOURCE\_NAME\_IS\_TOO\_LONG (the name of the resource is too long)

Note

If the second version of the function is called for creating the same resource with different width, height and shift parameters, it does not create a new resource, but simply updates the existing one.

The first version of the function is used for uploading images and sounds from files, and the second version is used only for the dynamic creation of images.

Images must be in the BMP format with a color depth of 24 or 32 bits. Sounds can only be in the WAV format. The size of the resource should not exceed 16 Mb.  
 

ENUM\_COLOR\_FORMAT

| Identifier | Description |
| --- | --- |
| COLOR\_FORMAT\_XRGB\_NOALPHA | The component of the alpha channel is ignored |
| COLOR\_FORMAT\_ARGB\_RAW | Color components are not handled by the terminal (must be correctly set by the user in premultiplied ARGB format). Use the [ColorToPRGB](../../Conversion-Functions/ColorToPRGB/ColorToPRGB.md) function to convert color to premultiplied ARGB |
| COLOR\_FORMAT\_ARGB\_NORMALIZE | Color components are handled by the terminal |

 

Example:

|  |
| --- |
| //+------------------------------------------------------------------+  //| Update graphical resource data                                   |  //+------------------------------------------------------------------+  void Update(const string res\_name,const uint &pixel\_data[],const uint width,const uint height,const bool redraw)    {  //--- leave if zero dimensions are passed     if(width==0 || height==0)        return;  //--- Update resource data and redraw the chart     if(ResourceCreate(res\_name,pixel\_data,width,height,0,0,0,COLOR\_FORMAT\_ARGB\_NORMALIZE) && redraw)        ChartRedraw();    }  //+------------------------------------------------------------------+  //| Script program start function                                    |  //+------------------------------------------------------------------+  void OnStart()    {  //--- declare the parameters of the graphical resource     string rc\_name="Resource";     uint   rc\_width=100;     uint   rc\_height=100;     uint   rc\_data[];     uint   rc\_size=rc\_width\*rc\_height;        ResetLastError();  //--- set the size of the pixel array     if(ArrayResize(rc\_data,rc\_size)!=rc\_size)       {        Print("ArrayResize() failed. Error code: ",GetLastError());        return;       }  //--- fill the pixel array with a transparent color and create a graphical resource based on it     ArrayInitialize(rc\_data,0x00FFFFFF);     if(!ResourceCreate(rc\_name,rc\_data,rc\_width,rc\_height,0,0,0,COLOR\_FORMAT\_ARGB\_NORMALIZE))       {        Print("ResourceCreate() failed. Error code: ",GetLastError());        return;       }     Print("Size of created recource array: ",rc\_data.Size());     //--- check the created graphical resource.  //--- get the time and price data of the current bar     MqlTick tick={};     if(!SymbolInfoTick(Symbol(),tick))       {        Print("SymbolInfoTick() failed. Error code: ",GetLastError());        return;       }  //--- create the Bitmap object using the coordinates of the last tick price and time     string obj\_name="Bitmap";     if(!ObjectCreate(0,obj\_name,OBJ\_BITMAP,0,tick.time,tick.bid))       {        Print("ObjectCreate() failed. Error code: ",GetLastError());        return;       }  //--- set the width and height of the created bitmap object equal to the width and height of the graphical resource.  //--- set the object anchor point to its center.     ObjectSetInteger(0,obj\_name,OBJPROP\_XSIZE,rc\_width);     ObjectSetInteger(0,obj\_name,OBJPROP\_YSIZE,rc\_height);     ObjectSetInteger(0,obj\_name,OBJPROP\_ANCHOR,ANCHOR\_CENTER);  //--- specify the previously created graphical resource for the bitmap object as an image file  //--- in this case, in order to indicate the name of the graphical resource used, we need to add "::" before its name     ObjectSetString(0,obj\_name,OBJPROP\_BMPFILE,"::"+rc\_name);       //--- set the DodgerBlue color with the transparency of 200     uint clr=ColorToARGB(clrDodgerBlue,200);  //--- fill the entire array of pixels of the graphical resource with the set color     ArrayInitialize(rc\_data,clr);  //--- update the graphical resource data     Update(rc\_name,rc\_data,rc\_width,rc\_height,true);    } |

See also

[Resources](../../MQL5-programs/Resources/Resources.md), [ObjectCreate()](../../Object-Functions/ObjectCreate/ObjectCreate.md), [ObjectSetString()](../../Object-Functions/ObjectSetString/ObjectSetString.md), [OBJPROP\_BMPFILE](../../Constants,-Enumerations-and-Structures/Objects-Constants/Object-Properties/Object-Properties.md#enum_object_property_string)
