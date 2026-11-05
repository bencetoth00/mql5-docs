# CChartCanvas


Base class for implementing classes, which are used for drawing charts and their elements.  

### Description

This class includes methods for working with the basic elements of any chart: coordinate axes and their marks, chart legend, grid, background, etc. Here you can customize the options for displaying elements: visibility, text color, etc.

### Declaration

```cpp
   class CChartCanvas : public CCanvas
```

### Title

```cpp
   #include <Canvas\Charts\ChartCanvas.mqh>
```

|  |
| --- |
| Inheritance hierarchy    [CCanvas](../CCanvas/CCanvas.md)        CChartCanvas  Direct descendants  [CHistogramChart](../CHistogramChart/CHistogramChart.md), [CLineChart](../CLineChart/CLineChart.md), [CPieChart](../CPieChart/CPieChart.md) |

### Class methods

| Method | Action |
| --- | --- |
| [ColorBackground](ColorBackground/ColorBackground.md) | Returns and sets the background color. |
| [ColorBorder](ColorBorder/ColorBorder.md) | Returns and sets the border color. |
| [ColorText](ColorText/ColorText.md) | Returns and sets the text color. |
| [ColorGrid](ColorGrid/ColorGrid.md) | Returns and sets the grid color. |
| [MaxData](MaxData/MaxData.md) | Returns and sets the maximum amount of data (series) allowed. |
| [MaxDescrLen](MaxDescrLen/MaxDescrLen.md) | Returns and sets the maximum length of the descriptors. |
| [ShowFlags](ShowFlags/ShowFlags.md) | Returns and sets the visibility flag of the chart elements. |
| [IsShowLegend](IsShowLegend/IsShowLegend.md) | Returns and sets the visibility flag of the legend on the chart. |
| [IsShowScaleLeft](IsShowScaleLeft/IsShowScaleLeft.md) | Returns the visibility flag of the scale of values on the left. |
| [IsShowScaleRight](IsShowScaleRight/IsShowScaleRight.md) | Returns the visibility flag of the scale of values on the right. |
| [IsShowScaleTop](IsShowScaleTop/IsShowScaleTop.md) | Returns the visibility flag of the scale of values at the top. |
| [IsShowScaleBottom](IsShowScaleBottom/IsShowScaleBottom.md) | Returns the visibility flag of the scale of values at the bottom. |
| [IsShowGrid](IsShowGrid/IsShowGrid.md) | Returns the visibility flag of the grid on the chart. |
| [IsShowDescriptors](IsShowDescriptors/IsShowDescriptors.md) | Returns the visibility flag of the descriptors on the chart. |
| [IsShowPercent](IsShowPercent/IsShowPercent.md) | Returns the visibility flag of the percentages on the chart. |
| [VScaleMin](VScaleMin/VScaleMin.md) | Returns and sets the minimum on the vertical scale of values. |
| [VScaleMax](VScaleMax/VScaleMax.md) | Returns and sets the maximum on the vertical scale of values. |
| [NumGrid](NumGrid/NumGrid.md) | Returns and sets the number of vertical scale divisions when plotting the chart grid. |
| [DataOffset](DataOffset/DataOffset.md) | Returns and sets the data offset value. |
| [DataTotal](DataTotal/DataTotal.md) | Returns the total number of data series on the chart. |
| [DrawDescriptors](DrawDescriptors/DrawDescriptors.md) | Virtual method for drawing descriptors. |
| [DrawData](DrawData/DrawData.md) | Virtual method for drawing data series at the specified index. |
| [Create](Create/Create.md) | Virtual method that creates a graphical resource. |
| [AllowedShowFlags](AllowedShowFlags/AllowedShowFlags.md) | Sets the set of allowed visibility flags for chart elements. |
| [ShowLegend](ShowLegend/ShowLegend.md) | Sets the visibility flag for the legend. |
| [ShowScaleLeft](ShowScaleLeft/ShowScaleLeft.md) | Sets the visibility flag for the left scale. |
| [ShowScaleRight](ShowScaleRight/ShowScaleRight.md) | Sets the visibility flag for the right scale. |
| [ShowScaleTop](ShowScaleTop/ShowScaleTop.md) | Sets the visibility flag for the top scale. |
| [ShowScaleBottom](ShowScaleBottom/ShowScaleBottom.md) | Sets the visibility flag for the bottom scale. |
| [ShowGrid](ShowGrid/ShowGrid.md) | Sets the visibility flag for the grid. |
| [ShowDescriptors](ShowDescriptors/ShowDescriptors.md) | Sets the visibility flag for the descriptors. |
| [ShowValue](ShowValue/ShowValue.md) | Sets the visibility flag for the values. |
| [ShowPercent](ShowPercent/ShowPercent.md) | Sets the visibility flag for the percentages. |
| [LegendAlignment](LegendAlignment/LegendAlignment.md) | Sets the text alignment for the legend. |
| [Accumulative](Accumulative/Accumulative.md) | Sets the value accumulation flag for the series. |
| [VScaleParams](VScaleParams/VScaleParams.md) | Sets the parameters for the vertical scale of values. |
| [DescriptorUpdate](DescriptorUpdate/DescriptorUpdate.md) | Updates the value of the series descriptor (at the specified position). |
| [ColorUpdate](ColorUpdate/ColorUpdate.md) | Updates the series colors (at the specified position). |
| [ValuesCheck](ValuesCheck/ValuesCheck.md) | Performs internal calculations for plotting the chart. |
| [Redraw](Redraw/Redraw.md) | Redraw the chart. |
| [DrawBackground](DrawBackground/DrawBackground.md) | Draws the background. |
| [DrawLegend](DrawLegend/DrawLegend.md) | Redraws the legend. |
| [DrawLegendVertical](DrawLegendVertical/DrawLegendVertical.md) | Draws a vertical legend. |
| [DrawLegendHorizontal](DrawLegendHorizontal/DrawLegendHorizontal.md) | Draws a horizontal legend. |
| [CalcScales](CalcScales/CalcScales.md) | Calculates the coordinates of the scale. |
| [DrawScales](DrawScales/DrawScales.md) | Redraws all scales of values. |
| [DrawScaleLeft](DrawScaleLeft/DrawScaleLeft.md) | Redraws the left scale of values. |
| [DrawScaleRight](DrawScaleRight/DrawScaleRight.md) | Redraws the right scale of values. |
| [DrawScaleTop](DrawScaleTop/DrawScaleTop.md) | Redraws the top scale of values |
| [DrawScaleBottom](DrawScaleBottom/DrawScaleBottom.md) | Redraws the bottom value scale. |
| [DrawGrid](DrawGrid/DrawGrid.md) | Redraw the chart. |
| [DrawChart](DrawChart/DrawChart.md) | Redraw the chart. |

|  |
| --- |
| Methods inherited from class CCanvas  [CreateBitmap](../CCanvas/CreateBitmap/CreateBitmap.md), [CreateBitmap](../CCanvas/CreateBitmap/CreateBitmap.md), [CreateBitmapLabel](../CCanvas/CreateBitmapLabel/CreateBitmapLabel.md), [CreateBitmapLabel](../CCanvas/CreateBitmapLabel/CreateBitmapLabel.md), [Attach](../CCanvas/Attach/Attach.md), [Attach](../CCanvas/Attach/Attach.md), [Destroy](../CCanvas/Destroy/Destroy.md), [ChartObjectName](../CCanvas/ChartObjectName/ChartObjectName.md), [ResourceName](../CCanvas/ResourceName/ResourceName.md), [Width](../CCanvas/Width/Width.md), [Height](../CCanvas/Height/Height.md), [Update](../CCanvas/Update/Update.md), [Resize](../CCanvas/Resize/Resize.md), [Erase](../CCanvas/Erase/Erase.md), [PixelGet](../CCanvas/PixelGet/PixelGet.md), [PixelSet](../CCanvas/PixelSet/PixelSet.md), [LineVertical](../CCanvas/LineVertical/LineVertical.md), [LineHorizontal](../CCanvas/LineHorizontal/LineHorizontal.md), [Line](../CCanvas/Line/Line.md), [Polyline](../CCanvas/Polyline/Polyline.md), [Polygon](../CCanvas/Polygon/Polygon.md), [Rectangle](../CCanvas/Rectangle/Rectangle.md), [Triangle](../CCanvas/Triangle/Triangle.md), [Circle](../CCanvas/Circle/Circle.md), [Ellipse](../CCanvas/Ellipse/Ellipse.md), [Arc](../CCanvas/Arc/Arc.md), [Arc](../CCanvas/Arc/Arc.md), [Arc](../CCanvas/Arc/Arc.md), [Pie](../CCanvas/Pie/Pie.md), [Pie](../CCanvas/Pie/Pie.md), [FillRectangle](../CCanvas/FillRectangle/FillRectangle.md), [FillTriangle](../CCanvas/FillTriangle/FillTriangle.md), [FillPolygon](../CCanvas/FillPolygon/FillPolygon.md), [FillCircle](../CCanvas/FillCircle/FillCircle.md), [FillEllipse](../CCanvas/FillEllipse/FillEllipse.md), [Fill](../CCanvas/Fill/Fill.md), [Fill](../CCanvas/Fill/Fill.md), [PixelSetAA](../CCanvas/PixelSetAA/PixelSetAA.md), [LineAA](../CCanvas/LineAA/LineAA.md), [PolylineAA](../CCanvas/PolylineAA/PolylineAA.md), [PolygonAA](../CCanvas/PolygonAA/PolygonAA.md), [TriangleAA](../CCanvas/TriangleAA/TriangleAA.md), [CircleAA](../CCanvas/CircleAA/CircleAA.md), [EllipseAA](../CCanvas/EllipseAA/EllipseAA.md), [LineWu](../CCanvas/LineWu/LineWu.md), [PolylineWu](../CCanvas/PolylineWu/PolylineWu.md), [PolygonWu](../CCanvas/PolygonWu/PolygonWu.md), [TriangleWu](../CCanvas/TriangleWu/TriangleWu.md), [CircleWu](../CCanvas/CircleWu/CircleWu.md), [EllipseWu](../CCanvas/EllipseWu/EllipseWu.md), [LineThickVertical](../CCanvas/LineThickVertical/LineThickVertical.md), [LineThickHorizontal](../CCanvas/LineThickHorizontal/LineThickHorizontal.md), [LineThick](../CCanvas/LineThick/LineThick.md), [PolylineThick](../CCanvas/PolylineThick/PolylineThick.md), [PolygonThick](../CCanvas/PolygonThick/PolygonThick.md), [PolylineSmooth](../CCanvas/PolylineSmooth/PolylineSmooth.md), [PolygonSmooth](../CCanvas/PolygonSmooth/PolygonSmooth.md), [FontSet](../CCanvas/FontSet/FontSet.md), [FontNameSet](../CCanvas/FontNameSet/FontNameSet.md), [FontSizeSet](../CCanvas/FontSizeSet/FontSizeSet.md), [FontFlagsSet](../CCanvas/FontFlagsSet/FontFlagsSet.md), [FontAngleSet](../CCanvas/FontAngleSet/FontAngleSet.md), [FontGet](../CCanvas/FontGet/FontGet.md), [FontNameGet](../CCanvas/FontNameGet/FontNameGet.md), [FontSizeGet](../CCanvas/FontSizeGet/FontSizeGet.md), [FontFlagsGet](../CCanvas/FontFlagsGet/FontFlagsGet.md), [FontAngleGet](../CCanvas/FontAngleGet/FontAngleGet.md), [TextOut](../CCanvas/TextOut/TextOut.md), [TextWidth](../CCanvas/TextWidth/TextWidth.md), [TextHeight](../CCanvas/TextHeight/TextHeight.md), [TextSize](../CCanvas/TextSize/TextSize.md), [GetDefaultColor](../CCanvas/GetDefaultColor/GetDefaultColor.md), [TransparentLevelSet](../CCanvas/TransparentLevelSet/TransparentLevelSet.md), [LoadFromFile](../CCanvas/LoadFromFile/LoadFromFile.md), LineStyleGet, [LineStyleSet](../CCanvas/LineStyleSet/LineStyleSet.md) |