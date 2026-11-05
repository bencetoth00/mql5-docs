# CDialog


CDialog is class of the Dialog complex control.

### Description

CDialog class is intended to combine the controls with different functions in the group.

### Declaration

```cpp
   class CDialog : public CWndContainer
```

### Title

```cpp
   #include <Controls\Dialog.mqh>
```

|  |
| --- |
| Inheritance hierarchy    [CObject](../../Basic-Class-CObject/Basic-Class-CObject.md)        [CWnd](../CWnd/CWnd.md)            [CWndContainer](../CWndContainer/CWndContainer.md)                CDialog  Direct descendants  [CAppDialog](../CAppDialog/CAppDialog.md) |

### Class Methods by Groups

| Create |  |
| --- | --- |
| [Create](Create/Create.md) | Creates control |
| Chart event handlers |  |
| [OnEvent](OnEvent/OnEvent.md) | Event handler of all chart events |
| Properties |  |
| [Caption](Caption/Caption.md) | Gets/sets the value of the "Caption" property |
| Add |  |
| [Add](Add/Add.md) | Adds control to the client area |
| Dependent controls |  |
| [CreateWhiteBorder](CreateWhiteBorder/CreateWhiteBorder.md) | Creates dependent control (white border) |
| [CreateBackground](CreateBackground/CreateBackground.md) | Creates dependent control (background) |
| [CreateCaption](CreateCaption/CreateCaption.md) | Creates dependent control (caption) |
| [CreateButtonClose](CreateButtonClose/CreateButtonClose.md) | Creates dependent control (close button) |
| [CreateClientArea](CreateClientArea/CreateClientArea.md) | Creates dependent control (client area) |
| Dependent controls event handlers |  |
| [OnClickCaption](OnClickCaption/OnClickCaption.md) | "ClickCaption" internal event handler |
| [OnClickButtonClose](OnClickButtonClose/OnClickButtonClose.md) | "ClickButtonClose" internal event handler |
| Access to client area properties |  |
| [ClientAreaVisible](ClientAreaVisible/ClientAreaVisible.md) | Sets a value indicating whether the client area is visible |
| [ClientAreaLeft](ClientAreaLeft/ClientAreaLeft.md) | Gets X coordinate of the upper-left corner of the control client area |
| [ClientAreaTop](ClientAreaTop/ClientAreaTop.md) | Gets Y coordinate of the upper-left corner of the control client area |
| [ClientAreaRight](ClientAreaRight/ClientAreaRight.md) | Gets X coordinate of the lower-right corner of the control client area |
| [ClientAreaBottom](ClientAreaBottom/ClientAreaBottom.md) | Gets Y coordinate of the lower-right corner of the control client area |
| [ClientAreaWidth](ClientAreaWidth/ClientAreaWidth.md) | Gets the client area width |
| [ClientAreaHeight](ClientAreaHeight/ClientAreaHeight.md) | Gets the client area height |
| Drag event handlers |  |
| [OnDialogDragStart](OnDialogDragStart/OnDialogDragStart.md) | "DialogDragStart" event handler (virtual) |
| [OnDialogDragProcess](OnDialogDragProcess/OnDialogDragProcess.md) | "DialogDragProcess" event handler (virtual) |
| [OnDialogDragEnd](OnDialogDragEnd/OnDialogDragEnd.md) | "DialogDragEnd" event handler (virtual) |

| Methods inherited from class CObject  Prev, Prev, Next, Next, [Type](../../Basic-Class-CObject/Type/Type.md), [Compare](../../Basic-Class-CObject/Compare/Compare.md) |
| --- |
| Methods inherited from class CWnd  [Name](../CWnd/Name/Name.md), [ControlsTotal](../CWnd/ControlsTotal/ControlsTotal.md), [Control](../CWnd/Control/Control.md), [Rect](../CWnd/Rect/Rect.md), [Left](../CWnd/Left/Left.md), [Left](../CWnd/Left/Left.md), [Top](../CWnd/Top/Top.md), [Top](../CWnd/Top/Top.md), [Right](../CWnd/Right/Right.md), [Right](../CWnd/Right/Right.md), [Bottom](../CWnd/Bottom/Bottom.md), [Bottom](../CWnd/Bottom/Bottom.md), [Width](../CWnd/Width/Width.md), [Width](../CWnd/Width/Width.md), [Height](../CWnd/Height/Height.md), [Height](../CWnd/Height/Height.md), Size, Size, Size, [Contains](../CWnd/Contains/Contains.md), [Contains](../CWnd/Contains/Contains.md), [Alignment](../CWnd/Alignment/Alignment.md), [Align](../CWnd/Align/Align.md), [Id](../CWnd/Id/Id.md), [IsEnabled](../CWnd/IsEnabled/IsEnabled.md), [IsVisible](../CWnd/IsVisible/IsVisible.md), [Visible](../CWnd/Visible/Visible.md), [IsActive](../CWnd/IsActive/IsActive.md), [Activate](../CWnd/Activate/Activate.md), [Deactivate](../CWnd/Deactivate/Deactivate.md), [StateFlags](../CWnd/StateFlags/StateFlags.md), [StateFlags](../CWnd/StateFlags/StateFlags.md), [StateFlagsSet](../CWnd/StateFlagsSet/StateFlagsSet.md), [StateFlagsReset](../CWnd/StateFlagsReset/StateFlagsReset.md), [PropFlags](../CWnd/PropFlags/PropFlags.md), [PropFlags](../CWnd/PropFlags/PropFlags.md), [PropFlagsSet](../CWnd/PropFlagsSet/PropFlagsSet.md), [PropFlagsReset](../CWnd/PropFlagsReset/PropFlagsReset.md), [MouseX](../CWnd/MouseX/MouseX.md), [MouseX](../CWnd/MouseX/MouseX.md), [MouseY](../CWnd/MouseY/MouseY.md), [MouseY](../CWnd/MouseY/MouseY.md), [MouseFlags](../CWnd/MouseFlags/MouseFlags.md), [MouseFlags](../CWnd/MouseFlags/MouseFlags.md), [MouseFocusKill](../CWnd/MouseFocusKill/MouseFocusKill.md), BringToTop |
| Methods inherited from class CWndContainer  [Destroy](../CWndContainer/Destroy/Destroy.md), [OnMouseEvent](../CWndContainer/OnMouseEvent/OnMouseEvent.md), [ControlsTotal](../CWndContainer/ControlsTotal/ControlsTotal.md), [Control](../CWndContainer/Control/Control.md), [ControlFind](../CWndContainer/ControlFind/ControlFind.md), [MouseFocusKill](../CWndContainer/MouseFocusKill/MouseFocusKill.md), [Add](../CWndContainer/Add/Add.md), [Add](../CWndContainer/Add/Add.md), [Delete](../CWndContainer/Delete/Delete.md), [Delete](../CWndContainer/Delete/Delete.md), [Move](../CWndContainer/Move/Move.md), [Move](../CWndContainer/Move/Move.md), [Shift](../CWndContainer/Shift/Shift.md), [Id](../CWndContainer/Id/Id.md), [Enable](../CWndContainer/Enable/Enable.md), [Disable](../CWndContainer/Disable/Disable.md), [Show](../CWndContainer/Show/Show.md), [Hide](../CWndContainer/Hide/Hide.md) |