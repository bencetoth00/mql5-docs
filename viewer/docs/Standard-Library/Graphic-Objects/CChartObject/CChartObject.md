# CChartObject


CChartObject is a base class for the classes of chart graphical objects of the Standard MQL5 library.

### Description

CChartObject class provides the simplified access to MQL5 API functions for all of its descendants.

### Declaration

```cpp
   class CChartObject : public CObject
```

### Title

```cpp
   #include <ChartObjects\ChartObject.mqh>
```

|  |
| --- |
| Inheritance hierarchy    [CObject](../../Basic-Class-CObject/Basic-Class-CObject.md)        CChartObject  Direct descendants  [CChartObjectArrow](../Arrow-Objects/CChartObjectArrow/CChartObjectArrow.md), [CChartObjectBitmap](../Control-Objects/CChartObjectBitmap/CChartObjectBitmap.md), [CChartObjectBmpLabel](../Control-Objects/CChartObjectBmpLabel/CChartObjectBmpLabel.md), [CChartObjectCycles](../Line-Objects/CChartObjectCycles/CChartObjectCycles.md), [CChartObjectElliottWave3](../Elliott-Tools/CChartObjectElliottWave3/CChartObjectElliottWave3.md), [CChartObjectEllipse](../Shape-Objects/CChartObjectEllipse/CChartObjectEllipse.md), [CChartObjectFiboArc](../Fibonacci-Tools/CChartObjectFiboArc/CChartObjectFiboArc.md), [CChartObjectFiboFan](../Fibonacci-Tools/CChartObjectFiboFan/CChartObjectFiboFan.md), [CChartObjectFiboTimes](../Fibonacci-Tools/CChartObjectFiboTimes/CChartObjectFiboTimes.md), [CChartObjectHLine](../Line-Objects/CChartObjectHLine/CChartObjectHLine.md), [CChartObjectRectangle](../Shape-Objects/CChartObjectRectangle/CChartObjectRectangle.md), [CChartObjectSubChart](../Control-Objects/CChartObjectSubChart/CChartObjectSubChart.md), [CChartObjectText](../Control-Objects/CChartObjectText/CChartObjectText.md), [CChartObjectTrend](../Line-Objects/CChartObjectTrend/CChartObjectTrend.md), [CChartObjectTriangle](../Shape-Objects/CChartObjectTriangle/CChartObjectTriangle.md), [CChartObjectVLine](../Line-Objects/CChartObjectVLine/CChartObjectVLine.md) |

### Class Methods by Groups

| Attributes |  |
| --- | --- |
| [ChartId](ChartId/ChartId.md) | Gets the ID of the chart a graphical object belongs to |
| [Window](Window/Window.md) | Gets the number of a chart window where a graphical object is located |
| [Name](Name/Name.md) | Gets/sets the name of a graphical object |
| [NumPoints](NumPoints/NumPoints.md) | Gets the number of anchor points |
| Assign |  |
| [Attach](Attach/Attach.md) | Binds a chart graphical object |
| [SetPoint](SetPoint/SetPoint.md) | Sets the anchor point parameters |
| Delete |  |
| [Delete](Delete/Delete.md) | Deletes a chart graphical object |
| [Detach](Detach/Detach.md) | Detaches a chart graphical object |
| Shift |  |
| [ShiftObject](ShiftObject/ShiftObject.md) | The relative object shift |
| [ShiftPoint](ShiftPoint/ShiftPoint.md) | The relative object point shift |
| Object properties |  |
| [Time](Time/Time.md) | Gets/sets the time coordinates of an object point |
| [Price](Price/Price.md) | Gets/sets the price coordinate of an object point |
| [Color](Color/Color.md) | Gets/sets the color of the object |
| [Style](Style/Style.md) | Gets/sets the object line style |
| [Width](Width/Width.md) | Gets/sets the object line width |
| [BackGround](Background/Background.md) | Gets/sets the flag of drawing an object in the background |
| [Selected](Selected/Selected.md) | Gets/sets the "selected" flag of a graphical object |
| [Selectable](Selectable/Selectable.md) | Gets/sets the selectable object flag |
| [Description](Description/Description.md) | Gets/sets the text of the object |
| [Tooltip](Tooltip/Tooltip.md) | Gets/sets the tooltip of the object |
| [Timeframes](Timeframes/Timeframes.md) | Gets/sets the mask of the object visibility flags |
| [Z\_Order](Z_Order/Z_Order.md) | Gets/sets the graphical object priority for receiving an event of mouse clicking on a chart |
| [CreateTime](CreateTime/CreateTime.md) | Gets the time of the object creation |
| Object level properties |  |
| [LevelsCount](LevelsCount/LevelsCount.md) | Gets/sets the number of object levels |
| [LevelColor](LevelColor/LevelColor.md) | Gets/sets the level line color |
| [LevelStyle](LevelStyle/LevelStyle.md) | Gets/sets the level line style |
| [LevelWidth](LevelWidth/LevelWidth.md) | Gets/sets the level line width |
| [LevelValue](LevelValue/LevelValue.md) | Gets/sets the level |
| [LevelDescription](LevelDescription/LevelDescription.md) | Gets/sets the level text |
| Access to API MQL5 functions |  |
| [GetInteger](GetInteger/GetInteger.md) | Gets the value of the object property |
| [SetInteger](SetInteger/SetInteger.md) | Sets the value of the object property |
| [GetDouble](GetDouble/GetDouble.md) | Gets the value of the object property |
| [SetDouble](SetDouble/SetDouble.md) | Sets the value of the object property |
| [GetString](GetString/GetString.md) | Gets the value of the object property |
| [SetString](SetString/SetString.md) | Sets the value of the object property |
| Input/Output |  |
| virtual [Save](Save/Save.md) | Virtual method of writing to a file |
| virtual [Load](Load/Load.md) | Virtual method of reading from a file |
| virtual [Type](Type/Type.md) | Virtual method of identification |

|  |
| --- |
| Methods inherited from class CObject  Prev, Prev, Next, Next, [Compare](../../Basic-Class-CObject/Compare/Compare.md) |