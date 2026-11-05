# Price Charts

# CChart

CChart is a class for simplified access to "Chart" graphic object properties.

### Description

CChart class provides access to "Chart" object properties.

### Declaration

```cpp
   class CChart : public CObject
```

### Title

```cpp
   #include <Charts\Chart.mqh>
```

|  |
| --- |
| Inheritance hierarchy    [CObject](../Basic-Class-CObject/Basic-Class-CObject.md)        CChart |

### Class Methods by Groups

| Access to protected data |  |
| --- | --- |
| [ChartID](ChartID/ChartID.md) | Gets identifier of the chart |
| General properties |  |
| [Mode](Mode/Mode.md) | Gets/sets the value of "Mode" property (bars, candles, or line) |
| [Foreground](Foreground/Foreground.md) | Gets/sets the value of "Foreground" property |
| [Shift](Shift/Shift.md) | Gets/sets the value of "Shift" property |
| [ShiftSize](ShiftSize/ShiftSize.md) | Gets/sets the value of "ShiftSize" property (in percents) |
| [AutoScroll](AutoScroll/AutoScroll.md) | Gets/sets the value of "AutoScroll" property |
| [Scale](Scale/Scale.md) | Gets/sets the value of "Scale" property |
| [ScaleFix](ScaleFix/ScaleFix.md) | Gets/sets the value of "ScaleFix" property (fixed chart scale or not) |
| [ScaleFix\_11](ScaleFix_11/ScaleFix_11.md) | Gets/sets the value of "ScaleFix\_11" property (chart scale is 1:1, or not) |
| [FixedMax](FixedMax/FixedMax.md) | Gets/sets the value of "FixedMax" property (fixed maximal price) |
| [FixedMin](FixedMin/FixedMin.md) | Gets/sets the value of "FixedMin" property (fixed minimal price) |
| [ScalePPB](ScalePPB/ScalePPB.md) | Gets/sets the value of "ScalePPB" property (scale is "point per bar" or not) |
| [PointsPerBar](PointsPerBar/PointsPerBar.md) | Gets/sets the value of "PointsPerBar" property (in points per bar) |
| Show properties |  |
| [ShowOHLC](ShowOHLC/ShowOHLC.md) | Gets/sets the value of "ShowOHLC" property |
| [ShowLineBid](ShowLineBid/ShowLineBid.md) | Gets/sets the value of "ShowLineBid" property |
| [ShowLineAsk](ShowLineAsk/ShowLineAsk.md) | Gets/sets the value of "ShowLineAsk" property |
| [ShowLastLine](ShowLastLine/ShowLastLine.md) | Gets/sets the value of "ShowLastLine" property |
| [ShowPeriodSep](ShowPeriodSep/ShowPeriodSep.md) | Gets/sets the value of "ShowPeriodSep" property (show period separators) |
| [ShowGrid](ShowGrid/ShowGrid.md) | Gets/sets the value of "ShowGrid" property |
| [ShowVolumes](ShowVolumes/ShowVolumes.md) | Gets/sets the value of "ShowVolumes" property (color for volumes and levels of opened positions) |
| [ShowObjectDescr](ShowObjectDescr/ShowObjectDescr.md) | Gets/sets the value of "ShowObjectDescr" property (show description for graphic objects) |
| [ShowDateScale](ShowDateScale/ShowDateScale.md) | Sets the value of "ShowDateScale" property (date scale of the chart) |
| [ShowPriceScale](ShowPriceScale/ShowPriceScale.md) | Sets the value of "ShowPriceScale" property (price scale of the chart) |
| Color properties |  |
| [ColorBackground](ColorBackground/ColorBackground.md) | Gets/sets the value of "ColorBackground" property (background color of the chart) |
| [ColorForeground](ColorForeground/ColorForeground.md) | Gets/sets the value of "ColorForeground" property (color of axes, scale and OHLC strings of the chart) |
| [ColorGrid](ColorGrid/ColorGrid.md) | Gets/sets the value of "ColorGrid" property (color of the grid) |
| [ColorBarUp](ColorBarUp/ColorBarUp.md) | Gets/sets the value of "ColorBarUp" property (color for bull bars, their shadow and candle body outlines) |
| [ColorBarDown](ColorBarDown/ColorBarDown.md) | Gets/sets the value of "ColorBarDown" property (color for bear bars, their shadow and candle body outlines) |
| [ColorCandleBull](ColorCandleBull/ColorCandleBull.md) | Gets/sets the value of "ColorCandleBull" property (body color of the bull candle) |
| [ColorCandleBear](ColorCandleBear/ColorCandleBear.md) | Gets/sets the value of "ColorCandleBear" property (body color of the bear candle) |
| [ColorChartLine](ColorChartLine/ColorChartLine.md) | Gets/sets the value of "ColorChartLine" property (color for line chart and Doji candles) |
| [ColorVolumes](ColorVolumes/ColorVolumes.md) | Gets/sets the value of "ColorVolumes" property (color for volumes and levels of opened positions) |
| [ColorLineBid](ColorLineBid/ColorLineBid.md) | Gets/sets the value of "ColorLineBid" property (color of Bid line) |
| [ColorLineAsk](ColorLineAsk/ColorLineAsk.md) | Gets/sets the value of "ColorLineAsk" property (color of Ask line) |
| [ColorLineLast](ColorLineLast/ColorLineLast.md) | Gets/sets the value of "ColorLineLast" property (color of the last deal price line) |
| [ColorStopLevels](ColorStopLevels/ColorStopLevels.md) | Gets/sets the value of "ColorStopLevels" property (color of the SL and TP levels) |
| Read only properties |  |
| [VisibleBars](VisibleBars/VisibleBars.md) | Gets total number of visible chart bars |
| [WindowsTotal](WindowsTotal/WindowsTotal.md) | Gets total number of chart windows, including the chart indicator subwindows |
| [WindowIsVisible](WindowIsVisible/WindowIsVisible.md) | Gets visibility flag of the specified chart subwindow |
| [WindowHandle](WindowHandle/WindowHandle.md) | Gets window handle of the chart (HWND) |
| [FirstVisibleBar](FirstVisibleBar/FirstVisibleBar.md) | Gets the number of the first visible bar of the chart |
| [WidthInBars](WidthInBars/WidthInBars.md) | Gets window width in bars. |
| [WidthInPixels](WidthInPixels/WidthInPixels.md) | Gets subwindow width in pixels. |
| [HeightInPixels](HeightInPixels/HeightInPixels.md) | Gets subwindow height in pixels. |
| [PriceMin](PriceMin/PriceMin.md) | Gets minimal price of the specified subwindow |
| [PriceMax](PriceMax/PriceMax.md) | Gets maximal price of the specified subwindow |
| Properties |  |
| [Attach](Attach/Attach.md) | Assigns the current chart to the class instance |
| [FirstChart](FirstChart/FirstChart.md) | Assigns the first chart of the client terminal to the class instance |
| [NextChart](NextChart/NextChart.md) | Assigns the next chart of the client terminal to the class instance |
| [Open](Open/Open.md) | Opens chart with specified parameters and assign it to the class instance |
| [Detach](Detach/Detach.md) | Detaches chart from the class instance |
| [Close](Close/Close.md) | Closes chart assigned to the class instance |
| [BringToTop](BringToTop/BringToTop.md) | Show chart on top of other charts |
| [EventObjectCreate](EventObjectCreate/EventObjectCreate.md) | Sets a flag to send notifications of an event of new object creation on a chart |
| [EventObjectDelete](EventObjectDelete/EventObjectDelete.md) | Sets a flag to send notifications of an event of object deletion on a chart |
| Indicators |  |
| [IndicatorAdd](IndicatorAdd/IndicatorAdd.md) | Adds an indicator with the specified handle into a specified chart subwindow |
| [IndicatorDelete](IndicatorDelete/IndicatorDelete.md) | Removes an indicator with a specified name from the specified chart subwindow |
| [IndicatorsTotal](IndicatorsTotal/IndicatorsTotal.md) | Returns the number of all indicators applied to the specified chart subwindow |
| [IndicatorName](IndicatorName/IndicatorName.md) | Returns the short name of the indicator on the specified chart subwindow |
| Navigation |  |
| [Navigate](Navigate/Navigate.md) | Navigates the chart |
| Access to MQL5 API |  |
| [Symbol](Symbol/Symbol.md) | Gets symbol of the chart |
| [Period](Period/Period.md) | Gets period of the chart |
| [Redraw](Redraw/Redraw.md) | Redraws chart, assigned to the class instance |
| [GetInteger](GetInteger/GetInteger.md) | The function returns the value of the corresponding object property |
| [SetInteger](SetInteger/SetInteger.md) | Sets new value for the property of the integer type |
| [GetDouble](GetDouble/GetDouble.md) | The function returns the value of the corresponding object property |
| [SetDouble](SetDouble/SetDouble.md) | Sets new value for the property of the double type |
| [GetString](GetString/GetString.md) | The function returns the value of the corresponding object property |
| [SetString](SetString/SetString.md) | Sets new value for the property of the string type |
| [SetSymbolPeriod](SetSymbolPeriod/SetSymbolPeriod.md) | Changes symbol and period of the chart assigned to the class instance |
| [ApplyTemplate](ApplyTemplate/ApplyTemplate.md) | Applies specified template to the chart |
| [ScreenShot](ScreenShot/ScreenShot.md) | Creates screenshot of the specified chart and saves it to .gif file |
| [WindowOnDropped](WindowOnDropped/WindowOnDropped.md) | Gets chart subwindow number corresponding to the object (expert or script) drop point |
| [PriceOnDropped](PriceOnDropped/PriceOnDropped.md) | Gets price coordinate corresponding to the object (expert or script) drop point |
| [TimeOnDropped](TimeOnDropped/TimeOnDropped.md) | Gets time coordinate corresponding to the object (expert or script) drop point |
| [XOnDropped](XOnDropped/XOnDropped.md) | Gets X coordinate corresponding to the object (expert or script) drop point |
| [YOnDropped](YOnDropped/YOnDropped.md) | Gets Y coordinate corresponding to the object (expert or script) drop point |
| Input/Output |  |
| virtual [Save](Save/Save.md) | Saves object parameters to file |
| virtual [Load](Load/Load.md) | Loads object parameters from file |
| virtual [Type](Type/Type.md) | Gets graphic object type identifier |

|  |
| --- |
| Methods inherited from class CObject  Prev, Prev, Next, Next, [Compare](../Basic-Class-CObject/Compare/Compare.md) |