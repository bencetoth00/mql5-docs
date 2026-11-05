# CHistogramChart

CHistogramChart

Class for plotting histograms.

Description

All methods for working with the plotting of histograms are implemented in this class. They can be used to set the column width and for configuring the work with data series. The methods for working with gradient filling of histogram columns are included, which allow to visualize the data more clearly.

![ccanvas_histogramchart](../../../assets/ccanvas_histogramchart.png)

The code of the above figure is provided [below](CHistogramChart.md#sample).

Declaration

|  |
| --- |
| class CHistogramChart : public CChartCanvas |

Title

|  |
| --- |
| #include <Canvas\Charts\HistogramChart.mqh> |

|  |
| --- |
| Inheritance hierarchy    [CCanvas](../CCanvas/CCanvas.md)        [CChartCanvas](../CChartCanvas/CChartCanvas.md)            CHistogramChart |

Class methods

| Method | Action |
| --- | --- |
| [Gradient](Gradient/Gradient.md) | Sets the flag indicating whether the gradient fill of the histogram columns will be applied. |
| [BarGap](BarGap/BarGap.md) | Set the value of the histogram offset from the origin. |
| [BarMinSize](BarMinSize/BarMinSize.md) | Sets the minimum width of the histogram columns. |
| [BarBorder](BarBorder/BarBorder.md) | Sets the flag indicating the need to draw the border for each column. |
| [Create](Create/Create.md) | Virtual method that creates a graphical resource. |
| [SeriesAdd](SeriesAdd/SeriesAdd.md) | Adds a new data series. |
| [SeriesInsert](SeriesInsert/SeriesInsert.md) | Inserts data series to the chart. |
| [SeriesUpdate](SeriesUpdate/SeriesUpdate.md) | Updates data series on the chart. |
| [SeriesDelete](SeriesDelete/SeriesDelete.md) | Deletes data series from the chart. |
| [ValueUpdate](ValueUpdate/ValueUpdate.md) | Updates the element value in the specified series. |
| [DrawData](DrawData/DrawData.md) | Virtual method that plots a histogram for the specified series. |
| [DrawBar](DrawBar/DrawBar.md) | Draws a histogram column as a filled rectangle. |
| [GradientBrush](GradientBrush/GradientBrush.md) | Creates a brush for the gradient fill. |

| Methods inherited from class CCanvas  [CreateBitmap](../CCanvas/CreateBitmap/CreateBitmap.md), [CreateBitmap](../CCanvas/CreateBitmap/CreateBitmap.md), [CreateBitmapLabel](../CCanvas/CreateBitmapLabel/CreateBitmapLabel.md), [CreateBitmapLabel](../CCanvas/CreateBitmapLabel/CreateBitmapLabel.md), [Attach](../CCanvas/Attach/Attach.md), [Attach](../CCanvas/Attach/Attach.md), [Destroy](../CCanvas/Destroy/Destroy.md), [ChartObjectName](../CCanvas/ChartObjectName/ChartObjectName.md), [ResourceName](../CCanvas/ResourceName/ResourceName.md), [Width](../CCanvas/Width/Width.md), [Height](../CCanvas/Height/Height.md), [Update](../CCanvas/Update/Update.md), [Resize](../CCanvas/Resize/Resize.md), [Erase](../CCanvas/Erase/Erase.md), [PixelGet](../CCanvas/PixelGet/PixelGet.md), [PixelSet](../CCanvas/PixelSet/PixelSet.md), [LineVertical](../CCanvas/LineVertical/LineVertical.md), [LineHorizontal](../CCanvas/LineHorizontal/LineHorizontal.md), [Line](../CCanvas/Line/Line.md), [Polyline](../CCanvas/Polyline/Polyline.md), [Polygon](../CCanvas/Polygon/Polygon.md), [Rectangle](../CCanvas/Rectangle/Rectangle.md), [Triangle](../CCanvas/Triangle/Triangle.md), [Circle](../CCanvas/Circle/Circle.md), [Ellipse](../CCanvas/Ellipse/Ellipse.md), [Arc](../CCanvas/Arc/Arc.md), [Arc](../CCanvas/Arc/Arc.md), [Arc](../CCanvas/Arc/Arc.md), [Pie](../CCanvas/Pie/Pie.md), [Pie](../CCanvas/Pie/Pie.md), [FillRectangle](../CCanvas/FillRectangle/FillRectangle.md), [FillTriangle](../CCanvas/FillTriangle/FillTriangle.md), [FillPolygon](../CCanvas/FillPolygon/FillPolygon.md), [FillCircle](../CCanvas/FillCircle/FillCircle.md), [FillEllipse](../CCanvas/FillEllipse/FillEllipse.md), [Fill](../CCanvas/Fill/Fill.md), [Fill](../CCanvas/Fill/Fill.md), [PixelSetAA](../CCanvas/PixelSetAA/PixelSetAA.md), [LineAA](../CCanvas/LineAA/LineAA.md), [PolylineAA](../CCanvas/PolylineAA/PolylineAA.md), [PolygonAA](../CCanvas/PolygonAA/PolygonAA.md), [TriangleAA](../CCanvas/TriangleAA/TriangleAA.md), [CircleAA](../CCanvas/CircleAA/CircleAA.md), [EllipseAA](../CCanvas/EllipseAA/EllipseAA.md), [LineWu](../CCanvas/LineWu/LineWu.md), [PolylineWu](../CCanvas/PolylineWu/PolylineWu.md), [PolygonWu](../CCanvas/PolygonWu/PolygonWu.md), [TriangleWu](../CCanvas/TriangleWu/TriangleWu.md), [CircleWu](../CCanvas/CircleWu/CircleWu.md), [EllipseWu](../CCanvas/EllipseWu/EllipseWu.md), [LineThickVertical](../CCanvas/LineThickVertical/LineThickVertical.md), [LineThickHorizontal](../CCanvas/LineThickHorizontal/LineThickHorizontal.md), [LineThick](../CCanvas/LineThick/LineThick.md), [PolylineThick](../CCanvas/PolylineThick/PolylineThick.md), [PolygonThick](../CCanvas/PolygonThick/PolygonThick.md), [PolylineSmooth](../CCanvas/PolylineSmooth/PolylineSmooth.md), [PolygonSmooth](../CCanvas/PolygonSmooth/PolygonSmooth.md), [FontSet](../CCanvas/FontSet/FontSet.md), [FontNameSet](../CCanvas/FontNameSet/FontNameSet.md), [FontSizeSet](../CCanvas/FontSizeSet/FontSizeSet.md), [FontFlagsSet](../CCanvas/FontFlagsSet/FontFlagsSet.md), [FontAngleSet](../CCanvas/FontAngleSet/FontAngleSet.md), [FontGet](../CCanvas/FontGet/FontGet.md), [FontNameGet](../CCanvas/FontNameGet/FontNameGet.md), [FontSizeGet](../CCanvas/FontSizeGet/FontSizeGet.md), [FontFlagsGet](../CCanvas/FontFlagsGet/FontFlagsGet.md), [FontAngleGet](../CCanvas/FontAngleGet/FontAngleGet.md), [TextOut](../CCanvas/TextOut/TextOut.md), [TextWidth](../CCanvas/TextWidth/TextWidth.md), [TextHeight](../CCanvas/TextHeight/TextHeight.md), [TextSize](../CCanvas/TextSize/TextSize.md), [GetDefaultColor](../CCanvas/GetDefaultColor/GetDefaultColor.md), [TransparentLevelSet](../CCanvas/TransparentLevelSet/TransparentLevelSet.md), [LoadFromFile](../CCanvas/LoadFromFile/LoadFromFile.md), LineStyleGet, [LineStyleSet](../CCanvas/LineStyleSet/LineStyleSet.md) |
| --- |
| Methods inherited from class CChartCanvas  [ColorBackground](../CChartCanvas/ColorBackground/ColorBackground.md), [ColorBackground](../CChartCanvas/ColorBackground/ColorBackground.md), [ColorBorder](../CChartCanvas/ColorBorder/ColorBorder.md), [ColorBorder](../CChartCanvas/ColorBorder/ColorBorder.md), [ColorText](../CChartCanvas/ColorText/ColorText.md), [ColorText](../CChartCanvas/ColorText/ColorText.md), [ColorGrid](../CChartCanvas/ColorGrid/ColorGrid.md), [ColorGrid](../CChartCanvas/ColorGrid/ColorGrid.md), [MaxData](../CChartCanvas/MaxData/MaxData.md), [MaxData](../CChartCanvas/MaxData/MaxData.md), [MaxDescrLen](../CChartCanvas/MaxDescrLen/MaxDescrLen.md), [MaxDescrLen](../CChartCanvas/MaxDescrLen/MaxDescrLen.md), [AllowedShowFlags](../CChartCanvas/AllowedShowFlags/AllowedShowFlags.md), [ShowFlags](../CChartCanvas/ShowFlags/ShowFlags.md), [ShowFlags](../CChartCanvas/ShowFlags/ShowFlags.md), [IsShowLegend](../CChartCanvas/IsShowLegend/IsShowLegend.md), [IsShowScaleLeft](../CChartCanvas/IsShowScaleLeft/IsShowScaleLeft.md), [IsShowScaleRight](../CChartCanvas/IsShowScaleRight/IsShowScaleRight.md), [IsShowScaleTop](../CChartCanvas/IsShowScaleTop/IsShowScaleTop.md), [IsShowScaleBottom](../CChartCanvas/IsShowScaleBottom/IsShowScaleBottom.md), [IsShowGrid](../CChartCanvas/IsShowGrid/IsShowGrid.md), [IsShowDescriptors](../CChartCanvas/IsShowDescriptors/IsShowDescriptors.md), [IsShowPercent](../CChartCanvas/IsShowPercent/IsShowPercent.md), [ShowLegend](../CChartCanvas/ShowLegend/ShowLegend.md), [ShowScaleLeft](../CChartCanvas/ShowScaleLeft/ShowScaleLeft.md), [ShowScaleRight](../CChartCanvas/ShowScaleRight/ShowScaleRight.md), [ShowScaleTop](../CChartCanvas/ShowScaleTop/ShowScaleTop.md), [ShowScaleBottom](../CChartCanvas/ShowScaleBottom/ShowScaleBottom.md), [ShowGrid](../CChartCanvas/ShowGrid/ShowGrid.md), [ShowDescriptors](../CChartCanvas/ShowDescriptors/ShowDescriptors.md), [ShowValue](../CChartCanvas/ShowValue/ShowValue.md), [ShowPercent](../CChartCanvas/ShowPercent/ShowPercent.md), [LegendAlignment](../CChartCanvas/LegendAlignment/LegendAlignment.md), [Accumulative](../CChartCanvas/Accumulative/Accumulative.md), [VScaleMin](../CChartCanvas/VScaleMin/VScaleMin.md), [VScaleMin](../CChartCanvas/VScaleMin/VScaleMin.md), [VScaleMax](../CChartCanvas/VScaleMax/VScaleMax.md), [VScaleMax](../CChartCanvas/VScaleMax/VScaleMax.md), [NumGrid](../CChartCanvas/NumGrid/NumGrid.md), [NumGrid](../CChartCanvas/NumGrid/NumGrid.md), [VScaleParams](../CChartCanvas/VScaleParams/VScaleParams.md), [DataOffset](../CChartCanvas/DataOffset/DataOffset.md), [DataOffset](../CChartCanvas/DataOffset/DataOffset.md), [DataTotal](../CChartCanvas/DataTotal/DataTotal.md), [DescriptorUpdate](../CChartCanvas/DescriptorUpdate/DescriptorUpdate.md), [ColorUpdate](../CChartCanvas/ColorUpdate/ColorUpdate.md) |

Example

|  |
| --- |
| //+------------------------------------------------------------------+  //|                                         HistogramChartSample.mq5 |  //|                   Copyright 2009-2017, MetaQuotes Software Corp. |  //|                                              http://www.mql5.com |  //+------------------------------------------------------------------+  #property copyright   "2009-2017, MetaQuotes Software Corp."  #property link        "http://www.mql5.com"  #property description "Example of using histogram"  //---  #include <Canvas\Charts\HistogramChart.mqh>  //+------------------------------------------------------------------+  //| inputs                                                           |  //+------------------------------------------------------------------+  input bool Accumulative=true;  //+------------------------------------------------------------------+  //| Script program start function                                    |  //+------------------------------------------------------------------+  int OnStart(void)    {     int k=100;     double arr[10];  //--- create chart     CHistogramChart chart;     if(!chart.CreateBitmapLabel("SampleHistogramChart",10,10,600,450))       {        Print("Error creating histogram chart: ",GetLastError());        return(-1);       }     if(Accumulative)       {        chart.Accumulative();        chart.VScaleParams(20\*k\*10,-10\*k\*10,20);       }     else        chart.VScaleParams(20\*k,-10\*k,20);     chart.ShowValue(true);     chart.ShowScaleTop(false);     chart.ShowScaleBottom(false);     chart.ShowScaleRight(false);     chart.ShowLegend();     for(int j=0;j<5;j++)       {        for(int i=0;i<10;i++)          {           k=-k;           if(k>0)              arr[i]=k\*(i+10-j);           else              arr[i]=k\*(i+10-j)/2;          }        chart.SeriesAdd(arr,"Item"+IntegerToString(j));       }  //--- play with values     while(!IsStopped())       {        int i=rand()%5;        int j=rand()%10;        k=rand()%3000-1000;        chart.ValueUpdate(i,j,k);        Sleep(200);       }  //--- finish     chart.Destroy();     return(0);    } |
