# CGraphic


CGraphic is a base class for creating custom charts.

### Description

The CGraphic class provides numerous aspects of working with custom charts.

The class stores the main chart elements, sets their parameters and performs plotting.

Also, the class stores the curves for the chart and provides various display options.  

### Declaration

```cpp
   class CGraphic
```

### Title

```cpp
   #include <Graphics\Graphic.mqh>
```

### Class methods

| Method | Description |
| --- | --- |
| [Create](Create/Create.md) | Create a graphical resource bound to a chart object |
| [Destroy](Destroy/Destroy.md) | Remove a chart and destroy a graphical resource |
| [Update](Update/Update.md) | Display implemented changes |
| [ChartObjectName](ChartObjectName/ChartObjectName.md) | Get the name of an object bound to a chart |
| [ResourceName](ResourceName/ResourceName.md) | Get the graphical resource name |
| [XAxis](XAxis/XAxis.md) | Get the pointer to the X axis |
| [YAxis](YAxis/YAxis.md) | Get the pointer to the Y axis |
| [GapSize](GapSize/GapSize.md) | Get/set the size of indents between the chart elements |
| [BackgroundColor](BackgroundColor/BackgroundColor.md) | Get/set a background color |
| [BackgroundMain](BackgroundMain/BackgroundMain.md) | Get/set a chart header |
| [BackgroundMainSize](BackgroundMainSize/BackgroundMainSize.md) | Get/set a sub-header font size |
| [BackgroundMainColor](BackgroundMainColor/BackgroundMainColor.md) | Get/set a chart header color |
| [BackgroundSub](BackgroundSub/BackgroundSub.md) | Get/set a sub-header |
| [BackgroundSubSize](BackgroundSubSize/BackgroundSubSize.md) | Get/set a sub-header font size |
| [BackgroundSubColor](BackgroundSubColor/BackgroundSubColor.md) | Get/set a chart sub-header color |
| [GridLineColor](GridLineColor/GridLineColor.md) | Get/set a grid line color |
| [GridBackgroundColor](GridBackgroundColor/GridBackgroundColor.md) | Get/set a grid background color |
| [GridCircleRadius](GridCircleRadius/GridCircleRadius.md) | Get/set the dot radius in the grid nodes |
| [GridCircleColor](GridCircleColor/GridCircleColor.md) | Get/set the dot color in the grid nodes |
| [GridHasCircle](GridHasCircle/GridHasCircle.md) | Get/set the dot plotting flag in the grid nodes |
| [GridAxisLineColor](GridAxisLineColor/GridAxisLineColor.md) | Get the value of a real chart axes color. |
| [HistoryNameWidth](HistoryNameWidth/HistoryNameWidth.md) | Get/set the maximum allowed length for displaying a curve name |
| [HistoryNameSize](HistoryNameSize/HistoryNameSize.md) | Get/set the font size of a curve name |
| [HistorySymbolSize](HistorySymbolSize/HistorySymbolSize.md) | Get/set a size of notational convention symbols |
| [TextAdd](TextAdd/TextAdd.md) | Add a text to the chart |
| [LineAdd](LineAdd/LineAdd.md) | Add a line to the chart |
| [CurveAdd](CurveAdd/CurveAdd.md) | Create and add a curve to the chart |
| [CurvePlot](CurvePlot/CurvePlot.md) | Plot a previously created curve by index |
| [CurvePlotAll](CurvePlotAll/CurvePlotAll.md) | Plot all previously created curves |
| [CurveGetByIndex](CurveGetByIndex/CurveGetByIndex.md) | Get a curve by a specified index |
| [CurveGetByName](CurveGetByName/CurveGetByName.md) | Get a curve by a specified name |
| [CurveRemoveByIndex](CurveRemoveByIndex/CurveRemoveByIndex.md) | Remove a curve by a specified index. |
| [CurveRemoveByName](CurveRemoveByName/CurveRemoveByName.md) | Remove a curve by a specified name. |
| [CurvesTotal](CurvesTotal/CurvesTotal.md) | Get the number of curves for the given chart. |
| [MarksToAxisAdd](MarksToAxisAdd/MarksToAxisAdd.md) | Add a scale mark to the chart axis |
| [MajorMarkSize](MajorMarkSize/MajorMarkSize.md) | Get/set the size of the scale's ticks on the chart axis |
| [FontSet](FontSet/FontSet.md) | Set the current font parameters |
| [FontGet](FontGet/FontGet.md) | Get the current font parameters |
| [Attach](Attach/Attach.md) | Get/set a graphical resource and bind it to the CGraphic class instance |
| [CalculateMaxMinValues](CalculateMaxMinValues/CalculateMaxMinValues.md) | Calculate (re-calculate) minimum and maximum chart values on both axes. |
| [Height](Height/Height.md) | Get a chart height in pixels. |
| [IndentDown](IndentDown/IndentDown.md) | Get/set a chart indent from the lower border. |
| [IndentLeft](IndentLeft/IndentLeft.md) | Get/set a chart indent from the left border. |
| [IndentRight](IndentRight/IndentRight.md) | Get/set a chart indent from the right border. |
| [IndentUp](IndentUp/IndentUp.md) | Get/set a chart indent from the upper border. |
| [Redraw](Redraw/Redraw.md) | Redraw the chart. |
| [ResetParameters](ResetParameters/ResetParameters.md) | Reset the chart redrawing parameters. |
| [ScaleX](ScaleX/ScaleX.md) | Scale the value by X axis. |
| [ScaleY](ScaleY/ScaleY.md) | Scale the value by Y axis. |
| [SetDefaultParameters](SetDefaultParameters/SetDefaultParameters.md) | Set the chart parameters to default values. |
| [Width](Width/Width.md) | Get the chart width in pixels. |