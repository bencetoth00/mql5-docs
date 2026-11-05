# TextSetFont

TextSetFont

The function sets the font for displaying the text using drawing methods and returns the result of that operation. Arial font with the size -120 (12 pt) is used by default.

|  |
| --- |
| bool  TextSetFont(     const string  name,            // font name or path to font file on the disk     int           size,            // font size     uint          flags,           // combination of flags     int           orientation=0    // text slope angle     ); |

Parameters

name

[in]  Font name in the system or the name of the resource containing the font or the path to font file on the disk.

size

[in]  The font size that can be set using positive and negative values. In case of positive values, the size of a displayed text does not depend on the operating system's font size settings. In case of negative values, the value is set in tenths of a point and the text size depends on the operating system settings ("standard scale" or "large scale"). See the Note below for more information about the differences between the modes.

flags

[in]  Combination of [flags](TextSetFont.md#font_type_flags) describing font style.

orientation

[in]  Text's horizontal inclination to X axis, the unit of measurement is 0.1 degrees. It means that orientation=450 stands for inclination equal to 45 degrees.

Return Value

Returns true if the current font is successfully installed, otherwise false. Possible code errors:

- ERR\_INVALID\_PARAMETER(4003) - name presents NULL or "" (empty string),
- ERR\_INTERNAL\_ERROR(4001) - operating system error (for example, an attempt to create a non-existent font).

Note

If "::" is used in font name, the font is downloaded from [EX5 resource](../../MQL5-programs/Resources/Resources.md). If name font name is specified with an extension, the font is downloaded from the file, if the path starts from "\" or "/", the file is searched relative to MQL5 directory. Otherwise, it is searched relative to the path of EX5 file which called TextSetFont() function.

The font size is set using positive or negative values. This fact defines the dependence of the text size from the operating system settings (size scale).

- If the size is specified using a positive number, this size is transformed into physical measurement units of a device (pixels) when changing a logical font into a physical one, and this size corresponds to the height of the symbol glyphs picked from the available fonts. This case is not recommended when the texts displayed by [TextOut()](../TextOut/TextOut.md) function and the ones displayed by [OBJ\_LABEL](../../Constants,-Enumerations-and-Structures/Objects-Constants/Object-Types/Object-Types.md) ("Label") graphical object are to be used together on the chart.
- If the size is specified using a negative number, this number is supposed to be set in tenths of a logical point and is divided by 10 (for example, -350 is equal to 35 logical points). An obtained value is then transformed into physical measurement units of a device (pixels) and corresponds to the absolute value of the height of a symbol picked from the available fonts. Multiply the font size specified in the object properties by -10 to make the size of a text on the screen similar to the one in [OBJ\_LABEL](../../Constants,-Enumerations-and-Structures/Objects-Constants/Object-Types/Object-Types.md) object.

The flags can be used as the combination of style flags with one of the flags specifying the font width. Flag names are shown below.

Flags for specifying font style

| Flag | Description |
| --- | --- |
| FONT\_ITALIC | Italic |
| FONT\_UNDERLINE | Underline |
| FONT\_STRIKEOUT | Strikeout |

 

Flags for specifying font width

| Flag |
| --- |
| FW\_DONTCARE |
| FW\_THIN |
| FW\_EXTRALIGHT |
| FW\_ULTRALIGHT |
| FW\_LIGHT |
| FW\_NORMAL |
| FW\_REGULAR |
| FW\_MEDIUM |
| FW\_SEMIBOLD |
| FW\_DEMIBOLD |
| FW\_BOLD |
| FW\_EXTRABOLD |
| FW\_ULTRABOLD |
| FW\_HEAVY |
| FW\_BLACK |

 

Example:

|  |
| --- |
| #property copyright "Copyright 2025, MetaQuotes Ltd."  #property link      "https://www.mql5.com"  #property version   "1.00"     #define   COORD\_X    200  #define   COORD\_Y    100  #define   OBJ\_NAME   "TestTextGetSizeBitmapLabel"  #define   RES\_NAME   "TestTextGetSizeResource"  #define   COLOR\_NULL 0x00FFFFFF  //+------------------------------------------------------------------+  //| Script program start function                                    |  //+------------------------------------------------------------------+  void OnStart()    {  //--- current chart ID     long   chart\_id= ChartID();          string font\_names[] ={"Arial", "Tahoma", "Calibri"};     uint   flags\_array[]={0, FONT\_ITALIC, FONT\_UNDERLINE, FONT\_STRIKEOUT};     uint   fw\_array[]={FW\_DONTCARE, FW\_THIN, FW\_EXTRALIGHT, FW\_ULTRALIGHT, FW\_LIGHT,                        FW\_NORMAL, FW\_REGULAR, FW\_MEDIUM, FW\_SEMIBOLD, FW\_DEMIBOLD,                        FW\_BOLD, FW\_EXTRABOLD, FW\_ULTRABOLD, FW\_HEAVY, FW\_BLACK};       //--- disable drawing any attributes of the price chart     ChartSetInteger(chart\_id, CHART\_SHOW, false);       //--- declare the parameters of the graphical resource     uint rc\_width =(int)ChartGetInteger(chart\_id, CHART\_WIDTH\_IN\_PIXELS);      uint rc\_height=(int)ChartGetInteger(chart\_id, CHART\_HEIGHT\_IN\_PIXELS);      uint rc\_data[];      uint rc\_size=rc\_width\*rc\_height;      //--- create a graphical resource for text output     if(!CreateResource(chart\_id, rc\_data, rc\_width, rc\_height))        return;       //--- loop through font names     for(int i=0; i<(int)font\_names.Size(); i++)       {        //--- loop through font flags        for(int j=0; j<(int)flags\_array.Size(); j++)          {           //--- draw text with the font and style flag obtained from the array           DrawText(font\_names[i], flags\_array[j], rc\_data, rc\_width, rc\_height);           Sleep(800);           ArrayInitialize(rc\_data, COLOR\_NULL);          }        Sleep(800);        ArrayInitialize(rc\_data, COLOR\_NULL);       }       //--- after outputting all texts with different font sizes and styles,  //--- show text with different font width flags     for(int i=0; i<(int)fw\_array.Size(); i++)       {        //--- set the font size and name for displaying text with width flags        string font\_name="Tahoma";        int    size=-140;        TextSetFont(font\_name, size, fw\_array[i]);                //--- create a drawn text string, output it to the resource pixel array, and update the resource        string text=StringFormat("Text%d: Font name: \"%s%s\", size: %d (%d)", i+1, font\_name, FlagWidthDescription(fw\_array[i]), size, size/-10);        TextOut(text, COORD\_X, COORD\_Y, ANCHOR\_LEFT\_UPPER, rc\_data, rc\_width, rc\_height, ColorToARGB(clrDodgerBlue), COLOR\_FORMAT\_ARGB\_NORMALIZE);        Update(RES\_NAME, rc\_data, rc\_width, rc\_height, true);        //--- wait a second        Sleep(1000);        ArrayInitialize(rc\_data, COLOR\_NULL);       }       //--- wait five seconds, then free the resource and delete the graphical object     Sleep(5000);     ResourceFree(RES\_NAME);     ObjectDelete(chart\_id, OBJ\_NAME);       //--- allow drawing any attributes of the price chart     ChartSetInteger(chart\_id, CHART\_SHOW, true);     ChartRedraw(chart\_id);     /\*     Text messages are displayed on the chart as a result of the script execution.     The texts have different fonts, as well as style and width flags     \*/     }  //+------------------------------------------------------------------+  //| Display five text strings of different                           |  //| sizes with the specified font and flags                          |  //+------------------------------------------------------------------+  void DrawText(const string font\_name, uint flags, uint &pixels\_array[], uint res\_width, uint res\_height)    {  //--- output five strings of text with different font sizes     for(int i=0; i<5; i++)       {        //--- calculate the font size and set the font for text output using drawing methods        int size=-140+10\*i;        TextSetFont(font\_name, size, flags);                //--- create a drawn text string, output it to the resource pixel array, and update the resource        string text=StringFormat("Text%d: Font name: \"%s%s\", size: %d (%d)", i+1, font\_name, FlagDescription(flags), size, size/-10);        TextOut(text, COORD\_X, COORD\_Y+22\*i, ANCHOR\_LEFT\_UPPER, pixels\_array, res\_width, res\_height, ColorToARGB(clrDodgerBlue), COLOR\_FORMAT\_ARGB\_NORMALIZE);        Update(RES\_NAME, pixels\_array, res\_width, res\_height, true);        //--- wait a bit        Sleep(800);       }    }  //+------------------------------------------------------------------+  //| Return a description of the font style flags                     |  //+------------------------------------------------------------------+  string FlagDescription(const uint flag)    {     switch(flag)       {        case FONT\_ITALIC     :  return(" Italic");        case FONT\_UNDERLINE  :  return(" Underline");        case FONT\_STRIKEOUT  :  return(" Strikeout");       }     return("");    }  //+------------------------------------------------------------------+  //| Return the description of the font width flags                   |  //+------------------------------------------------------------------+  string FlagWidthDescription(const uint flag)    {     switch(flag)       {        case FW\_DONTCARE  :  return(" Dontcare");        case FW\_THIN      :  return(" Thin");        case FW\_EXTRALIGHT:  return(" Extralight");        case FW\_ULTRALIGHT:  return(" Ultralight");        case FW\_LIGHT     :  return(" Light");        case FW\_NORMAL    :  return(" Normal");        case FW\_REGULAR   :  return(" Regular");        case FW\_MEDIUM    :  return(" Medium");        case FW\_SEMIBOLD  :  return(" Semibold");        case FW\_DEMIBOLD  :  return(" Demibold");        case FW\_BOLD      :  return(" Bold");        case FW\_EXTRABOLD :  return(" Extrabold");        case FW\_ULTRABOLD :  return(" Ultrabold");        case FW\_HEAVY     :  return(" Heavy");        case FW\_BLACK     :  return(" Black");       }     return("");    }  //+------------------------------------------------------------------+  //| Create a graphical resource for the entire chart                 |  //+------------------------------------------------------------------+  bool CreateResource(const long chart\_id, uint &pixel\_data[], const uint width, const uint height)    {  //--- set the size of the pixel array     ResetLastError();      uint size=width\*height;     if(ArrayResize(pixel\_data, size)!=size)        {         PrintFormat("%s: ArrayResize() failed. Error code %d",\_\_FUNCTION\_\_, GetLastError());         return(false);        }   //--- fill the pixel array with a transparent color and create a graphical resource based on it     ArrayInitialize(pixel\_data, COLOR\_NULL);      if(!ResourceCreate(RES\_NAME, pixel\_data, width, height, 0, 0, 0, COLOR\_FORMAT\_ARGB\_NORMALIZE))        {         PrintFormat("%s: ResourceCreate() failed. Error code ",\_\_FUNCTION\_\_, GetLastError());         return(false);        }       //--- create the Graphic Label object at the coordinates of the upper left corner of the chart     if(!ObjectCreate(0, OBJ\_NAME, OBJ\_BITMAP\_LABEL, 0, 0, 0))        {         PrintFormat("%s: ObjectCreate() failed. Error code %d",\_\_FUNCTION\_\_, GetLastError());         return(false);        }   //--- set the width and height of the created bitmap object equal to the width and height of the graphical resource.  //--- set the object anchor point to its center.     if(!ObjectSetInteger(chart\_id, OBJ\_NAME, OBJPROP\_XSIZE, width))       {        PrintFormat("%s: ObjectSetInteger() failed. Error code %d",\_\_FUNCTION\_\_, GetLastError());         return(false);        }     if(!ObjectSetInteger(chart\_id, OBJ\_NAME, OBJPROP\_YSIZE, height))       {        PrintFormat("%s: ObjectSetInteger() failed. Error code %d",\_\_FUNCTION\_\_, GetLastError());         return(false);        }  //--- specify the previously created graphical resource for the bitmap object as an image file  //--- in this case, in order to indicate the name of the graphical resource used, we need to add "::" before its name     if(!ObjectSetString(chart\_id, OBJ\_NAME, OBJPROP\_BMPFILE, "::"+RES\_NAME))       {        PrintFormat("%s: ObjectSetString() failed. Error code %d",\_\_FUNCTION\_\_, GetLastError());         return(false);        }        //--- all is fine     return(true);    }  //+------------------------------------------------------------------+   //| Update graphical resource data                                   |  //+------------------------------------------------------------------+   void Update(const string res\_name, const uint &pixel\_data[], const uint width, const uint height, const bool redraw)     {   //--- leave if zero dimensions are passed     if(width==0 || height==0)         return;   //--- update resource data and redraw the chart     if(ResourceCreate(res\_name, pixel\_data, width, height, 0, 0, 0, COLOR\_FORMAT\_ARGB\_NORMALIZE) && redraw)         ChartRedraw();     } |

 

See also

[Resources](../../MQL5-programs/Resources/Resources.md), [ResourceCreate()](../../Common-Functions/ResourceCreate/ResourceCreate.md), [ResourceSave()](../../Common-Functions/ResourceSave/ResourceSave.md), [TextOut()](../TextOut/TextOut.md)
