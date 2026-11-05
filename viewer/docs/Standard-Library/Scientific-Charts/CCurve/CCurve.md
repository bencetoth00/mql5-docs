# CCurve


The CCurve class works with the properties of the curves generated on the chart.

### Description

The CCurve class sets, installs and receives the coordinates and various properties of the curves when working with the CGraphic class.

There are three curve plotting modes: dots, lines and histogram. Separate parameters are implemented for each plotting mode in the class.

### Declaration

```cpp
   class CCurve : public CObject
```

### Title

```cpp
   #include <Graphics\Curve.mqh>
```

|  |
| --- |
| Inheritance hierarchy    [CObject](../../Basic-Class-CObject/Basic-Class-CObject.md)        CCurve |

### Class methods

| Method | Description |
| --- | --- |
| [Type](Type/Type.md) | Get the curve type |
| [Name](Name/Name.md) | Get the curve name |
| [Color](Color/Color.md) | Get the curve color |
| [XMax](XMax/XMax.md) | Get the maximum value of the X function |
| [XMin](XMin/XMin.md) | Get the minimum value of the X function |
| [YMax](YMax/YMax.md) | Get the maximum value of the Y function |
| [YMin](YMin/YMin.md) | Get the minimum value of the Y function |
| [Size](Size/Size.md) | Get the number of dots defining a curve |
| [PointsSize](PointsSize/PointsSize.md) | Get/set the linear size of dots defining a curve |
| [PointsFill](PointsFill/PointsFill.md) | Get/set the flag for filling dots defining a curve |
| [PointsColor](PointsColor/PointsColor.md) | Get/set the dot filling color |
| [GetX](GetX/GetX.md) | Gets X values of all curve dots to the array |
| [GetY](GetY/GetY.md) | Gets Y values of all curve dots to the array |
| [LinesStyle](LinesStyle/LinesStyle.md) | Get/set a line style when plotting a curve using lines |
| [LinesIsSmooth](LinesIsSmooth/LinesIsSmooth.md) | Get/set the smoothing flag when drawing using lines |
| [LinesSmoothTension](LinesSmoothTension/LinesSmoothTension.md) | Get/set the curve smoothing parameter when drawing using lines |
| [LinesSmoothStep](LinesSmoothStep/LinesSmoothStep.md) | Get/set the length of the approximating lines for smoothing when plotting by lines |
| [LinesWidth](LinesWidth/LinesWidth.md) | Get/set a line width when plotting a curve using lines |
| [HistogramWidth](HistogramWidth/HistogramWidth.md) | Get/set the width of columns when plotting using a histogram |
| [CustomPlotCBData](CustomPlotCBData/CustomPlotCBData.md) | Get/set the pointer to the object to be used in the custom curve plotting mode. |
| [CustomPlotFunction](CustomPlotFunction/CustomPlotFunction.md) | Get/set the pointer to the function implementing the custom curve plotting mode. |
| [PointsType](PointsType/PointsType.md) | Get/set the flag pointing at the type of dots used when plotting a dotted curve. |
| [StepsDimension](StepsDimension/StepsDimension.md) | Get/set the value indicating the dimension used in step-type curve rendering. |
| [TrendLineCoefficients](TrendLineCoefficients/TrendLineCoefficients.md) | Get/set trend line ratios for writing them into an array. |
| [TrendLineColor](TrendLineColor/TrendLineColor.md) | Get/set a color of a trend line for a curve. |
| [TrendLineVisible](TrendLineVisible/TrendLineVisible.md) | Get/set the trend line visibility flag. |
| [Update](Update/Update.md) | Update the curve coordinates. |
| [Visible](Visible/Visible.md) | Get/set the flag defining if a function is visible on the chart. |

|  |
| --- |
| Methods inherited from class CObject  Prev, Prev, Next, Next, [Save](../../Basic-Class-CObject/Save/Save.md), [Load](../../Basic-Class-CObject/Load/Load.md), [Compare](../../Basic-Class-CObject/Compare/Compare.md) |