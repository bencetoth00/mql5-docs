# CCanvas


CCanvas is a class for simplified creation of custom images.

### Description

CCanvas provides creation of a graphical resource (with or without binding to a chart object) and drawing graphic primitives.

### Declaration

```cpp
   class CCanvas
```

### Title

```cpp
   #include <Canvas\Canvas.mqh>
```

|  |
| --- |
| Inheritance hierarchy    CCanvas  Direct descendants  [CChartCanvas](../CChartCanvas/CChartCanvas.md), CFlameCanvas |

### Class methods by groups

| Creating |  |
| --- | --- |
| [Attach](Attach/Attach.md) | Attaches the OBJ\_BITMAP\_LABEL object to an instance of the CCanvas class |
| [Create](Create/Create.md) | Creates a graphical resource without binding to a chart object |
| [CreateBitmap](CreateBitmap/CreateBitmap.md) | Create a graphical resource bound to a chart object |
| [CreateBitmapLabel](CreateBitmapLabel/CreateBitmapLabel.md) | Create a graphical resource bound to a chart object |
| [Destroy](Destroy/Destroy.md) | Destroys a graphical resource |
| Properties |  |
| [ChartObjectName](ChartObjectName/ChartObjectName.md) | Gets the name of a bound chart object |
| [ResourceName](ResourceName/ResourceName.md) | Gets the name of a graphical resource |
| [Width](Width/Width.md) | Gets the width of a graphical resource |
| [Height](Height/Height.md) | Gets the height of a graphical resource |
| [LineStyleSet](LineStyleSet/LineStyleSet.md) | Sets the line style |
| Updates an object on the screen |  |
| [Update](Update/Update.md) | Displays changes on the screen |
| [Resize](Resize/Resize.md) | Resizes a graphical resource |
| Erasing/Filling with color |  |
| [Erase](Erase/Erase.md) | Erases or fills with the specified color |
| Data access |  |
| [PixelGet](PixelGet/PixelGet.md) | Gets a color of the dot with the specified coordinates |
| [PixelSet](PixelSet/PixelSet.md) | Sets color of the dot with the specified coordinates |
| Draws primitives |  |
| [LineVertical](LineVertical/LineVertical.md) | Draws a vertical line |
| [LineHorizontal](LineHorizontal/LineHorizontal.md) | Draws a horizontal line |
| [Line](Line/Line.md) | Draws a freehand line |
| [Polyline](Polyline/Polyline.md) | Draws a polyline |
| [Polygon](Polygon/Polygon.md) | Draws a polygon |
| [Rectangle](Rectangle/Rectangle.md) | Draws a rectangle |
| [Circle](Circle/Circle.md) | Draws a circle |
| [Triangle](Triangle/Triangle.md) | Draws a triangle |
| [Ellipse](Ellipse/Ellipse.md) | Draws an ellipse |
| [Arc](Arc/Arc.md) | Draws an ellipse arc |
| [Pie](Pie/Pie.md) | Draws an ellipse sector |
| Draws filled primitives |  |
| [FillRectangle](FillRectangle/FillRectangle.md) | Draws a filled rectangle |
| [FillCircle](FillCircle/FillCircle.md) | Draws a filled circle |
| [FillTriangle](FillTriangle/FillTriangle.md) | Draws a filled triangle |
| [FillPolygon](FillPolygon/FillPolygon.md) | Draws a filled polygon |
| [FillEllipse](FillEllipse/FillEllipse.md) | Draws a filled ellipse |
| [Fill](Fill/Fill.md) | Fills an area |
| Draws primitives with antialiasing |  |
| [PixelSetAA](PixelSetAA/PixelSetAA.md) | Draws a pixel |
| [LineAA](LineAA/LineAA.md) | Draws a line |
| [PolylineAA](PolylineAA/PolylineAA.md) | Draws a polyline |
| [PolygonAA](PolygonAA/PolygonAA.md) | Draws a polygon |
| [TriangleAA](TriangleAA/TriangleAA.md) | Draws a triangle |
| [CircleAA](CircleAA/CircleAA.md) | Draws a circle |
| [EllipseAA](EllipseAA/EllipseAA.md) | Draws an ellipse |
| [LineWu](LineWu/LineWu.md) | Draws a line |
| [PolylineWu](PolylineWu/PolylineWu.md) | Draws a polyline |
| [PolygonWu](PolygonWu/PolygonWu.md) | Draws a polygon |
| [TriangleWu](TriangleWu/TriangleWu.md) | Draws a triangle |
| [CircleWu](CircleWu/CircleWu.md) | Draws a circle |
| [EllipseWu](EllipseWu/EllipseWu.md) | Draws an ellipse |
| [LineThick](LineThick/LineThick.md) | Draws a segment of a freehand line having a specified width using antialiasing algorithm. |
| [LineThickVertical](LineThickVertical/LineThickVertical.md) | Draws a vertical segment of a freehand line having a specified width using antialiasing algorithm. |
| [LineThickHorizontal](LineThickHorizontal/LineThickHorizontal.md) | Draws a horizontal segment of a freehand line having a specified width using antialiasing algorithm. |
| [PolygonSmooth](PolygonSmooth/PolygonSmooth.md) | Draws a polygon with a specified width using two antialiasing algorithms |
| [PolygonThick](PolygonThick/PolygonThick.md) | Draws a polygon with a specified width using antialiasing algorithm |
| [PolylineSmooth](PolylineSmooth/PolylineSmooth.md) | Draws a polyline with a specified width using two antialiasing algorithms |
| [PolylineThick](PolylineThick/PolylineThick.md) | Draws a polyline with a specified width using antialiasing algorithm |
| Text |  |
| [FontSet](FontSet/FontSet.md) | Sets font parameters |
| [FontNameSet](FontNameSet/FontNameSet.md) | Sets font name |
| [FontSizeSet](FontSizeSet/FontSizeSet.md) | Sets font size |
| [FontFlagsSet](FontFlagsSet/FontFlagsSet.md) | Sets font flags |
| [FontAngleSet](FontAngleSet/FontAngleSet.md) | Sets font slope angle |
| [FontGet](FontGet/FontGet.md) | Gets font parameters |
| [FontNameGet](FontNameGet/FontNameGet.md) | Gets font name |
| [FontSizeGet](FontSizeGet/FontSizeGet.md) | Gets font size |
| [FontFlagsGet](FontFlagsGet/FontFlagsGet.md) | Gets font flags |
| [FontAngleGet](FontAngleGet/FontAngleGet.md) | Gets font slope angle |
| [TextOut](TextOut/TextOut.md) | Displays text |
| [TextWidth](TextWidth/TextWidth.md) | Gets the text width |
| [TextHeight](TextHeight/TextHeight.md) | Gets the text height |
| [TextSize](TextSize/TextSize.md) | Gets the text size |
| Transparency |  |
| [TransparentLevelSet](TransparentLevelSet/TransparentLevelSet.md) | Sets transparency level |
| Input/output |  |
| [LoadFromFile](LoadFromFile/LoadFromFile.md) | Reads an image from a BMP file |