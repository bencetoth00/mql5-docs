# CWndContainer


CWndContainer is a base class for a complex control (containing dependent controls) of the Standard library.

### Description

CWndContainer class implements base methods of the complex control.

### Declaration

```cpp
   class CWndContainer : public CWnd
```

### Title

```cpp
   #include <Controls\WndContainer.mqh>
```

|  |
| --- |
| Inheritance hierarchy    [CObject](../../Basic-Class-CObject/Basic-Class-CObject.md)        [CWnd](../CWnd/CWnd.md)            CWndContainer  Direct descendants  [CCheckBox](../CCheckBox/CCheckBox.md), [CComboBox](../CComboBox/CComboBox.md), CDateDropList, CDatePicker, [CDialog](../CDialog/CDialog.md), [CRadioButton](../CRadioButton/CRadioButton.md), [CScroll](../CScroll/CScroll.md), [CSpinEdit](../CSpinEdit/CSpinEdit.md), [CWndClient](../CWndClient/CWndClient.md) |

### Class Methods by Groups

| Destroy |  |
| --- | --- |
| [Destroy](Destroy/Destroy.md) | Destroys all the container controls |
| Chart event handlers |  |
| [OnEvent](OnEvent/OnEvent.md) | Event handler of all chart events |
| [OnMouseEvent](OnMouseEvent/OnMouseEvent.md) | The [CHARTEVENT\_MOUSE\_MOVE](../../../Constants,-Enumerations-and-Structures/Chart-Constants/Types-of-Chart-Events/Types-of-Chart-Events.md) event handler |
| Access to container |  |
| [ControlsTotal](ControlsTotal/ControlsTotal.md) | Gets the number of controls in the container |
| [Control](Control/Control.md) | Gets control by index |
| [ControlFind](ControlFind/ControlFind.md) | Gets control by ID |
| Add/Delete |  |
| [Add](Add/Add.md) | Adds control to a group (container) |
| [Delete](Delete/Delete.md) | Deletes control from a group (container) |
| Geometry |  |
| [Move](Move/Move.md) | Performs a absolute displacement of an element group |
| [Shift](Shift/Shift.md) | Performs a relative displacement of an element group |
| Identification |  |
| [Id](Id/Id.md) | Sets the ID for all controls of the container |
| State |  |
| [Enable](Enable/Enable.md) | Enables all controls of the container |
| [Disable](Disable/Disable.md) | Disables all controls of the container |
| [Show](Show/Show.md) | Shows all controls of the container |
| [Hide](Hide/Hide.md) | Hides all controls of the container |
| Mouse operations |  |
| [MouseFocusKill](MouseFocusKill/MouseFocusKill.md) | Kills mouse focus |
| File operations |  |
| [Save](Save/Save.md) | Saves container information to file |
| [Load](Load/Load.md) | Loads container information from file |
| Internal event handlers |  |
| [OnResize](OnResize/OnResize.md) | "Resize" event handler |
| [OnActivate](OnActivate/OnActivate.md) | "Activate" event handler |
| [OnDeactivate](OnDeactivate/OnDeactivate.md) | "Deactivate" event handler |

| Methods inherited from class CObject  Prev, Prev, Next, Next, [Type](../../Basic-Class-CObject/Type/Type.md), [Compare](../../Basic-Class-CObject/Compare/Compare.md) |
| --- |
| Methods inherited from class CWnd  [Create](../CWnd/Create/Create.md), [Name](../CWnd/Name/Name.md), [ControlsTotal](../CWnd/ControlsTotal/ControlsTotal.md), [Control](../CWnd/Control/Control.md), [Rect](../CWnd/Rect/Rect.md), [Left](../CWnd/Left/Left.md), [Left](../CWnd/Left/Left.md), [Top](../CWnd/Top/Top.md), [Top](../CWnd/Top/Top.md), [Right](../CWnd/Right/Right.md), [Right](../CWnd/Right/Right.md), [Bottom](../CWnd/Bottom/Bottom.md), [Bottom](../CWnd/Bottom/Bottom.md), [Width](../CWnd/Width/Width.md), [Width](../CWnd/Width/Width.md), [Height](../CWnd/Height/Height.md), [Height](../CWnd/Height/Height.md), Size, Size, Size, [Contains](../CWnd/Contains/Contains.md), [Contains](../CWnd/Contains/Contains.md), [Alignment](../CWnd/Alignment/Alignment.md), [Align](../CWnd/Align/Align.md), [Id](../CWnd/Id/Id.md), [IsEnabled](../CWnd/IsEnabled/IsEnabled.md), [IsVisible](../CWnd/IsVisible/IsVisible.md), [Visible](../CWnd/Visible/Visible.md), [IsActive](../CWnd/IsActive/IsActive.md), [Activate](../CWnd/Activate/Activate.md), [Deactivate](../CWnd/Deactivate/Deactivate.md), [StateFlags](../CWnd/StateFlags/StateFlags.md), [StateFlags](../CWnd/StateFlags/StateFlags.md), [StateFlagsSet](../CWnd/StateFlagsSet/StateFlagsSet.md), [StateFlagsReset](../CWnd/StateFlagsReset/StateFlagsReset.md), [PropFlags](../CWnd/PropFlags/PropFlags.md), [PropFlags](../CWnd/PropFlags/PropFlags.md), [PropFlagsSet](../CWnd/PropFlagsSet/PropFlagsSet.md), [PropFlagsReset](../CWnd/PropFlagsReset/PropFlagsReset.md), [MouseX](../CWnd/MouseX/MouseX.md), [MouseX](../CWnd/MouseX/MouseX.md), [MouseY](../CWnd/MouseY/MouseY.md), [MouseY](../CWnd/MouseY/MouseY.md), [MouseFlags](../CWnd/MouseFlags/MouseFlags.md), [MouseFlags](../CWnd/MouseFlags/MouseFlags.md), [MouseFocusKill](../CWnd/MouseFocusKill/MouseFocusKill.md), BringToTop |