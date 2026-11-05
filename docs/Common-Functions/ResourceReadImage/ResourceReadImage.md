# ResourceReadImage

ResourceReadImage

The function reads data from the graphical resource [created by ResourceCreate() function](../ResourceCreate/ResourceCreate.md#dynamic_resourcecreate) or [saved in EX5 file during compilation](../../MQL5-programs/Resources/Resources.md#resource_include).

|  |
| --- |
| bool  ResourceReadImage(     const string      resource\_name,       // graphical resource name for reading     uint&             data[],              // array for receiving data from the resource     uint&             width,               // for receiving the image width in the resource     uint&             height,              // for receiving the image height in the resource     ); |

Parameters

resource\_name

[in]  Name of the graphical resource containing an image. To gain access to its own resources, the name is used in brief form "::resourcename". If we download a resource from a compiled EX5 file, the full name should be used with the path relative to MQL5 directory, file and resource names – "path\\filename.ex5::resourcename".

data[][]

[in]  One- or two-dimensional array for receiving data from the graphical resource.

img\_width

[out]  Graphical resource image width in pixels.

img\_height

[out]  Graphical resource image height in pixels.

Return Value

true if successful, otherwise false. To get information about the error, call the [GetLastError()](../../Checkup/GetLastError/GetLastError.md) function.

Note

If data[] array is then to be used for [creating a graphical resource](../ResourceCreate/ResourceCreate.md#enum_color_format),  [COLOR\_FORMAT\_ARGB\_NORMALIZE or COLOR\_FORMAT\_XRGB\_NOALPHA](../ResourceCreate/ResourceCreate.md#enum_color_format) color formats should be used.

If data[] array is two-dimensional and its second dimension is less than X(width) graphical resource size, ResourceReadImage() function returns false and reading is not performed. But if the resource exists, actual image size is returned to width and height parameters.  This will allow making another attempt to receive data from the resource.

 

Example:

|  |
| --- |
| //+------------------------------------------------------------------+  //| Script program start function                                    |  //+------------------------------------------------------------------+  void OnStart()    {  //--- declare the parameters of the graphical resource     string rc\_name="Resource";     uint   rc\_width=100;     uint   rc\_height=100;     uint   rc\_data[];     uint   rc\_size=rc\_width\*rc\_height;        ResetLastError();  //--- set the size of the pixel array     if(ArrayResize(rc\_data,rc\_size)!=rc\_size)       {        Print("ArrayResize() failed. Error code: ",GetLastError());        return;       }  //--- fill the pixel array with a transparent color and create a graphical resource based on it     ArrayInitialize(rc\_data,0x00FFFFFF);     if(!ResourceCreate(rc\_name,rc\_data,rc\_width,rc\_height,0,0,0,COLOR\_FORMAT\_ARGB\_NORMALIZE))       {        Print("ResourceCreate() failed. Error code: ",GetLastError());        return;       }     Print("Size of created recource array: ",rc\_data.Size());     //--- check the created graphical resource.  //--- get the time and price data of the current bar     MqlTick tick={};     if(!SymbolInfoTick(Symbol(),tick))       {        Print("SymbolInfoTick() failed. Error code: ",GetLastError());        return;       }  //--- create the Bitmap object using the coordinates of the last tick price and time     string obj\_name="Bitmap";     if(!ObjectCreate(0,obj\_name,OBJ\_BITMAP,0,tick.time,tick.bid))       {        Print("ObjectCreate() failed. Error code: ",GetLastError());        return;       }  //--- set the width and height of the created bitmap object equal to the width and height of the graphical resource.  //--- set the object anchor point to its center.     ObjectSetInteger(0,obj\_name,OBJPROP\_XSIZE,rc\_width);     ObjectSetInteger(0,obj\_name,OBJPROP\_YSIZE,rc\_height);     ObjectSetInteger(0,obj\_name,OBJPROP\_ANCHOR,ANCHOR\_CENTER);  //--- specify the previously created graphical resource for the bitmap object as an image file  //--- In this case, in order to indicate the name of the graphical resource used, we need to add "::" before its name     ObjectSetString(0,obj\_name,OBJPROP\_BMPFILE,"::"+rc\_name);       //--- set the DodgerBlue color with the transparency of 200     uint clr=ColorToARGB(clrDodgerBlue,200);  //--- fill the entire array of pixels of the graphical resource with the set color     ArrayInitialize(rc\_data,clr);  //--- update the graphical resource data     Update(rc\_name,rc\_data,rc\_width,rc\_height,true);       //--- wait 3 seconds before reading the graphical resource data      Print("Wait 3 seconds before ResourceReadImage()");     Sleep(3000);  //--- read the image from the resource into a new array of pixels     uint rc\_data\_copy[];     uint w=0,h=0;     ResetLastError();     if(!ResourceReadImage("::"+rc\_name,rc\_data\_copy,w,h))       {        Print("ResourceReadImage() failed. Error code: ",GetLastError());        return;       }     //--- set the OrangeRed color with the transparency of 200     clr=ColorToARGB(clrOrangeRed,200);  //--- fill the entire array of pixels of the graphical resource with the set color and create a new graphical resource based on it     ArrayInitialize(rc\_data\_copy,clr);     if(!ResourceCreate(rc\_name+"Copy",rc\_data\_copy,rc\_width,rc\_height,0,0,0,COLOR\_FORMAT\_ARGB\_NORMALIZE))       {        Print("New ResourceCreate() failed. Error code: ",GetLastError());        return;       }     Print("Size of created new recource array: ",rc\_data\_copy.Size());       //--- create the "Graphical label" object using the coordinates of the last tick price and time     string obj\_name2="BitmapLabel";     if(!ObjectCreate(0,obj\_name2,OBJ\_BITMAP\_LABEL,0,0,0))       {        Print("ObjectCreate() failed. Error code: ",GetLastError());        return;       }  //--- get screen coordinates using the previously received price and time     int x=0,y=0;     if(!ChartTimePriceToXY(0,0,tick.time,tick.bid,x,y))       {        Print("New ChartTimePriceToXY() failed. Error code: ",GetLastError());        return;       }  //--- set the width and height of the created graphical label object equal to the width and height of the graphical resource.  //--- set the object anchor point to its center.     ObjectSetInteger(0,obj\_name2,OBJPROP\_XSIZE,rc\_width);     ObjectSetInteger(0,obj\_name2,OBJPROP\_YSIZE,rc\_height);     ObjectSetInteger(0,obj\_name2,OBJPROP\_ANCHOR,ANCHOR\_LEFT\_UPPER);     ObjectSetInteger(0,obj\_name2,OBJPROP\_XDISTANCE,x);     ObjectSetInteger(0,obj\_name2,OBJPROP\_YDISTANCE,y);  //--- set the copied graphical resource as an image file for the graphical label object  //--- in this case, in order to indicate the name of the graphical resource used, we need to add "::" before its name     ObjectSetString(0,obj\_name2,OBJPROP\_BMPFILE,"::"+rc\_name+"Copy");       //--- change the color of the new graphical label object     Print("Wait 3 seconds before changing color to GreenYellow");     Sleep(3000);  //--- set the GreenYellow color with the transparency of 200     clr=ColorToARGB(clrGreenYellow,200);  //--- fill the entire array of pixels of the new graphical resource with the set color     ArrayInitialize(rc\_data\_copy,clr);  //--- update the graphical resource data      Update(rc\_name+"Copy",rc\_data\_copy,rc\_width,rc\_height,true);       //--- wait three seconds and delete resources and both objects     Print("Wait 3 seconds before deleting both objects");     Sleep(3000);     Print("Deleting Resource and all Bitmap objects");     ResourceFree("::"+rc\_name);     ResourceFree("::"+rc\_name+"Copy");     ObjectDelete(0,obj\_name);     ObjectDelete(0,obj\_name2);    }  //+------------------------------------------------------------------+  //| Update graphical resource data                                   |  //+------------------------------------------------------------------+  void Update(const string res\_name,const uint &pixel\_data[],const uint width,const uint height,const bool redraw)    {  //--- leave if zero dimensions are passed     if(width==0 || height==0)        return;  //--- update resource data and redraw the chart     if(ResourceCreate(res\_name,pixel\_data,width,height,0,0,0,COLOR\_FORMAT\_ARGB\_NORMALIZE) && redraw)        ChartRedraw();    } |

See also

[Resource](../../MQL5-programs/Resources/Resources.md), [ObjectCreate()](../../Object-Functions/ObjectCreate/ObjectCreate.md), [ObjectSetString()](../../Object-Functions/ObjectSetString/ObjectSetString.md), [OBJPROP\_BMPFILE](../../Constants,-Enumerations-and-Structures/Objects-Constants/Object-Properties/Object-Properties.md#enum_object_property_string)
