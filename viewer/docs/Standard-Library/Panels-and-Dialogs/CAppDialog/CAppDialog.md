# CAppDialog


CAppDialog is a class of Application Dialog complex control (with dependent controls).

### Description

CAppDialog class is intended to combine the controls with different functions in the group inside the MQL5 program.

### Declaration

```cpp
   class CAppDialog : public CDialog
```

### Title

```cpp
   #include <Controls\Dialog.mqh>
```

|  |
| --- |
| Inheritance hierarchy    [CObject](../../Basic-Class-CObject/Basic-Class-CObject.md)        [CWnd](../CWnd/CWnd.md)            [CWndContainer](../CWndContainer/CWndContainer.md)                [CDialog](../CDialog/CDialog.md)                    CAppDialog |

### Class Methods by Groups

| Create and destroy |  |
| --- | --- |
| [Create](Create/Create.md) | Creates control |
| [Destroy](Destroy/Destroy.md) | Destroys control |
| Events processing |  |
| [OnEvent](OnEvent/OnEvent.md) | Event handler of all chart events |
| Run |  |
| [Run](Run/Run.md) | Runs control |
| Chart events processing |  |
| [ChartEvent](ChartEvent/ChartEvent.md) | Event handler of all chart events |
| Settings |  |
| [Minimized](Minimized/Minimized.md) | Sets a value indicating whether the control is minimized |
| Save/Load |  |
| [IniFileSave](IniFileSave/IniFileSave.md) | Saves the control state to file |
| [IniFileLoad](IniFileLoad/IniFileLoad.md) | Loads the control state from file |
| [IniFileName](IniFileName/IniFileName.md) | Sets the file name for loading/saving the control state |
| [IniFileExt](IniFileExt/IniFileExt.md) | Sets the file extension for loading/saving the control state |
| Initialization |  |
| [CreateCommon](CreateCommon/CreateCommon.md) | Common initialization method |
| [CreateExpert](CreateExpert/CreateExpert.md) | Initialization method for working in Expert Advisors |
| [CreateIndicator](CreateIndicator/CreateIndicator.md) | Initialization method for working in indicators |
| Dependent controls |  |
| [CreateButtonMinMax](CreateButtonMinMax/CreateButtonMinMax.md) | Creates dependent controls (minimize/maximize buttons) |
| Dependent controls event handlers |  |
| [OnClickButtonClose](OnClickButtonClose/OnClickButtonClose.md) | "ClickButtonClose" internal event handler (virtual) |
| [OnClickButtonMinMax](OnClickButtonMinMax/OnClickButtonMinMax.md) | "ClickButtonMinMax" internal event handler (virtual) |
| External events |  |
| [OnAnotherApplicationClose](OnAnotherApplicationClose/OnAnotherApplicationClose.md) | Event handler of external events (virtual) |
| Methods |  |
| [Rebound](Rebound/Rebound.md) | Sets new coordinates of the control using CRect class coordinates |
| [Minimize](Minimize/Minimize.md) | Shows the control in the minimized state |
| [Maximize](Maximize/Maximize.md) | Shows the control in the maximized (restored) state |
| [CreateInstanceId](CreateInstanceId/CreateInstanceId.md) | Creates a unique Id for the names of the control objects |
| [ProgramName](ProgramName/ProgramName.md) | Gets the name of MQL5 program, at which the control is used |
| [SubwinOff](SubwinOff/SubwinOff.md) | Get the Y offset of the control subwindow |

| Methods inherited from class CObject  Prev, Prev, Next, Next, [Type](../../Basic-Class-CObject/Type/Type.md), [Compare](../../Basic-Class-CObject/Compare/Compare.md) |
| --- |
| Methods inherited from class CWnd  [Name](../CWnd/Name/Name.md), [ControlsTotal](../CWnd/ControlsTotal/ControlsTotal.md), [Control](../CWnd/Control/Control.md), [Rect](../CWnd/Rect/Rect.md), [Left](../CWnd/Left/Left.md), [Left](../CWnd/Left/Left.md), [Top](../CWnd/Top/Top.md), [Top](../CWnd/Top/Top.md), [Right](../CWnd/Right/Right.md), [Right](../CWnd/Right/Right.md), [Bottom](../CWnd/Bottom/Bottom.md), [Bottom](../CWnd/Bottom/Bottom.md), [Width](../CWnd/Width/Width.md), [Width](../CWnd/Width/Width.md), [Height](../CWnd/Height/Height.md), [Height](../CWnd/Height/Height.md), Size, Size, Size, [Contains](../CWnd/Contains/Contains.md), [Contains](../CWnd/Contains/Contains.md), [Alignment](../CWnd/Alignment/Alignment.md), [Align](../CWnd/Align/Align.md), [Id](../CWnd/Id/Id.md), [IsEnabled](../CWnd/IsEnabled/IsEnabled.md), [IsVisible](../CWnd/IsVisible/IsVisible.md), [Visible](../CWnd/Visible/Visible.md), [IsActive](../CWnd/IsActive/IsActive.md), [Activate](../CWnd/Activate/Activate.md), [Deactivate](../CWnd/Deactivate/Deactivate.md), [StateFlags](../CWnd/StateFlags/StateFlags.md), [StateFlags](../CWnd/StateFlags/StateFlags.md), [StateFlagsSet](../CWnd/StateFlagsSet/StateFlagsSet.md), [StateFlagsReset](../CWnd/StateFlagsReset/StateFlagsReset.md), [PropFlags](../CWnd/PropFlags/PropFlags.md), [PropFlags](../CWnd/PropFlags/PropFlags.md), [PropFlagsSet](../CWnd/PropFlagsSet/PropFlagsSet.md), [PropFlagsReset](../CWnd/PropFlagsReset/PropFlagsReset.md), [MouseX](../CWnd/MouseX/MouseX.md), [MouseX](../CWnd/MouseX/MouseX.md), [MouseY](../CWnd/MouseY/MouseY.md), [MouseY](../CWnd/MouseY/MouseY.md), [MouseFlags](../CWnd/MouseFlags/MouseFlags.md), [MouseFlags](../CWnd/MouseFlags/MouseFlags.md), [MouseFocusKill](../CWnd/MouseFocusKill/MouseFocusKill.md), BringToTop |
| Methods inherited from class CWndContainer  [OnMouseEvent](../CWndContainer/OnMouseEvent/OnMouseEvent.md), [ControlsTotal](../CWndContainer/ControlsTotal/ControlsTotal.md), [Control](../CWndContainer/Control/Control.md), [ControlFind](../CWndContainer/ControlFind/ControlFind.md), [MouseFocusKill](../CWndContainer/MouseFocusKill/MouseFocusKill.md), [Add](../CWndContainer/Add/Add.md), [Add](../CWndContainer/Add/Add.md), [Delete](../CWndContainer/Delete/Delete.md), [Delete](../CWndContainer/Delete/Delete.md), [Move](../CWndContainer/Move/Move.md), [Move](../CWndContainer/Move/Move.md), [Shift](../CWndContainer/Shift/Shift.md), [Id](../CWndContainer/Id/Id.md), [Enable](../CWndContainer/Enable/Enable.md), [Disable](../CWndContainer/Disable/Disable.md), [Show](../CWndContainer/Show/Show.md), [Hide](../CWndContainer/Hide/Hide.md) |
| Methods inherited from class CDialog  [Caption](../CDialog/Caption/Caption.md), [Caption](../CDialog/Caption/Caption.md), [Add](../CDialog/Add/Add.md), [Add](../CDialog/Add/Add.md) |