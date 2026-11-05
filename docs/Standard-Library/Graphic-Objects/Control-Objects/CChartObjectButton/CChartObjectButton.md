# CChartObjectButton

CChartObjectButton

CChartObjectButton is a class for simplified access to "Button" graphical object properties.

Description

CChartObjectButton class provides access to "Button" object properties.

Declaration

|  |
| --- |
| class CChartObjectButton : public CChartObjectEdit |

Title

|  |
| --- |
| #include <ChartObjects\ChartObjectsTxtControls.mqh> |

|  |
| --- |
| Inheritance hierarchy    [CObject](../../../Basic-Class-CObject/Basic-Class-CObject.md)        [CChartObject](../../CChartObject/CChartObject.md)            [CChartObjectText](../CChartObjectText/CChartObjectText.md)                [CChartObjectLabel](../CChartObjectLabel/CChartObjectLabel.md)                    [CChartObjectEdit](../CChartObjectEdit/CChartObjectEdit.md)                        CChartObjectButton  Direct descendants  CChartObjectPanel |

Class Methods by Groups

| Create |  |
| --- | --- |
| [Create](../CChartObjectEdit/Create/Create.md) | Inherited form [CChartObjectEdit](../CChartObjectEdit/CChartObjectEdit.md) class |
| Properties |  |
| [State](State/State.md) | Gets/sets button state (Pressed/Depressed) |
| Input/output |  |
| virtual [Save](Save/Save.md) | Virtual method for writing to file |
| virtual [Load](Load/Load.md) | Virtual method for reading from file |
| virtual [Type](Type/Type.md) | Virtual method of identification |

| Methods inherited from class CObject  Prev, Prev, Next, Next, [Compare](../../../Basic-Class-CObject/Compare/Compare.md) |
| --- |
| Methods inherited from class CChartObject  [ChartId](../../CChartObject/ChartId/ChartId.md), [Window](../../CChartObject/Window/Window.md), [Name](../../CChartObject/Name/Name.md), [Name](../../CChartObject/Name/Name.md), [NumPoints](../../CChartObject/NumPoints/NumPoints.md), [Attach](../../CChartObject/Attach/Attach.md), [SetPoint](../../CChartObject/SetPoint/SetPoint.md), [Delete](../../CChartObject/Delete/Delete.md), [Detach](../../CChartObject/Detach/Detach.md), [Time](../../CChartObject/Time/Time.md), [Time](../../CChartObject/Time/Time.md), [Price](../../CChartObject/Price/Price.md), [Price](../../CChartObject/Price/Price.md), [Color](../../CChartObject/Color/Color.md), [Color](../../CChartObject/Color/Color.md), [Style](../../CChartObject/Style/Style.md), [Style](../../CChartObject/Style/Style.md), [Width](../../CChartObject/Width/Width.md), [Width](../../CChartObject/Width/Width.md), [Background](../../CChartObject/Background/Background.md), [Background](../../CChartObject/Background/Background.md), Fill, Fill, [Z\_Order](../../CChartObject/Z_Order/Z_Order.md), [Z\_Order](../../CChartObject/Z_Order/Z_Order.md), [Selected](../../CChartObject/Selected/Selected.md), [Selected](../../CChartObject/Selected/Selected.md), [Selectable](../../CChartObject/Selectable/Selectable.md), [Selectable](../../CChartObject/Selectable/Selectable.md), [Description](../../CChartObject/Description/Description.md), [Description](../../CChartObject/Description/Description.md), [Tooltip](../../CChartObject/Tooltip/Tooltip.md), [Tooltip](../../CChartObject/Tooltip/Tooltip.md), [Timeframes](../../CChartObject/Timeframes/Timeframes.md), [Timeframes](../../CChartObject/Timeframes/Timeframes.md), [CreateTime](../../CChartObject/CreateTime/CreateTime.md), [LevelsCount](../../CChartObject/LevelsCount/LevelsCount.md), [LevelsCount](../../CChartObject/LevelsCount/LevelsCount.md), [LevelColor](../../CChartObject/LevelColor/LevelColor.md), [LevelColor](../../CChartObject/LevelColor/LevelColor.md), [LevelStyle](../../CChartObject/LevelStyle/LevelStyle.md), [LevelStyle](../../CChartObject/LevelStyle/LevelStyle.md), [LevelWidth](../../CChartObject/LevelWidth/LevelWidth.md), [LevelWidth](../../CChartObject/LevelWidth/LevelWidth.md), [LevelValue](../../CChartObject/LevelValue/LevelValue.md), [LevelValue](../../CChartObject/LevelValue/LevelValue.md), [LevelDescription](../../CChartObject/LevelDescription/LevelDescription.md), [LevelDescription](../../CChartObject/LevelDescription/LevelDescription.md), [GetInteger](../../CChartObject/GetInteger/GetInteger.md), [GetInteger](../../CChartObject/GetInteger/GetInteger.md), [SetInteger](../../CChartObject/SetInteger/SetInteger.md), [SetInteger](../../CChartObject/SetInteger/SetInteger.md), [GetDouble](../../CChartObject/GetDouble/GetDouble.md), [GetDouble](../../CChartObject/GetDouble/GetDouble.md), [SetDouble](../../CChartObject/SetDouble/SetDouble.md), [SetDouble](../../CChartObject/SetDouble/SetDouble.md), [GetString](../../CChartObject/GetString/GetString.md), [GetString](../../CChartObject/GetString/GetString.md), [SetString](../../CChartObject/SetString/SetString.md), [SetString](../../CChartObject/SetString/SetString.md), [ShiftObject](../../CChartObject/ShiftObject/ShiftObject.md), [ShiftPoint](../../CChartObject/ShiftPoint/ShiftPoint.md) |
| Methods inherited from class CChartObjectText  [Angle](../CChartObjectText/Angle/Angle.md), [Angle](../CChartObjectText/Angle/Angle.md), [Font](../CChartObjectText/Font/Font.md), [Font](../CChartObjectText/Font/Font.md), [FontSize](../CChartObjectText/FontSize/FontSize.md), [FontSize](../CChartObjectText/FontSize/FontSize.md), [Anchor](../CChartObjectText/Anchor/Anchor.md), [Anchor](../CChartObjectText/Anchor/Anchor.md), [Create](../CChartObjectText/Create/Create.md) |
| Methods inherited from class CChartObjectLabel  [X\_Distance](../CChartObjectLabel/X_Distance/X_Distance.md), [X\_Distance](../CChartObjectLabel/X_Distance/X_Distance.md), [Y\_Distance](../CChartObjectLabel/Y_Distance/Y_Distance.md), [Y\_Distance](../CChartObjectLabel/Y_Distance/Y_Distance.md), [X\_Size](../CChartObjectLabel/X_Size/X_Size.md), [Y\_Size](../CChartObjectLabel/Y_Size/Y_Size.md), [Corner](../CChartObjectLabel/Corner/Corner.md), [Corner](../CChartObjectLabel/Corner/Corner.md), [Time](../CChartObjectLabel/Time/Time.md), [Price](../CChartObjectLabel/Price/Price.md), [Create](../CChartObjectLabel/Create/Create.md) |
| Methods inherited from class CChartObjectEdit  [X\_Size](../CChartObjectEdit/X_Size/X_Size.md), [Y\_Size](../CChartObjectEdit/Y_Size/Y_Size.md), [BackColor](../CChartObjectEdit/BackColor/BackColor.md), [BackColor](../CChartObjectEdit/BackColor/BackColor.md), [BorderColor](../CChartObjectEdit/BorderColor/BorderColor.md), [BorderColor](../CChartObjectEdit/BorderColor/BorderColor.md), ReadOnly, ReadOnly, [TextAlign](../CChartObjectEdit/TextAlign/TextAlign.md), [TextAlign](../CChartObjectEdit/TextAlign/TextAlign.md), [Angle](../CChartObjectEdit/Angle/Angle.md), [Create](../CChartObjectEdit/Create/Create.md) |

See also

[Object types](../../../../Constants,-Enumerations-and-Structures/Objects-Constants/Object-Types/Object-Types.md), [Object properties](../../../../Constants,-Enumerations-and-Structures/Objects-Constants/Object-Properties/Object-Properties.md), [Chart angle](../../../../Constants,-Enumerations-and-Structures/Objects-Constants/Chart-Corner/Chart-Corner.md), [Methods of object binding](../../../../Constants,-Enumerations-and-Structures/Objects-Constants/Methods-of-Object-Binding/Methods-of-Object-Binding.md), [Graphic objects](../../../../Object-Functions/Object-Functions.md)
