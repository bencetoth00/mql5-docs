# CWnd


CWnd is a base class for all Standard Library controls.

### Description

CWnd class is the implementation of the base control class.

### Declaration

```cpp
   class CWnd : public CObject
```

### Title

```cpp
   #include <Controls\Wnd.mqh>
```

|  |
| --- |
| Inheritance hierarchy    [CObject](../../Basic-Class-CObject/Basic-Class-CObject.md)        CWnd  Direct descendants  CDragWnd, [CWndContainer](../CWndContainer/CWndContainer.md), [CWndObj](../CWndObj/CWndObj.md) |

### Class Methods by Groups

| Create and destroy |  |
| --- | --- |
| [Create](Create/Create.md) | Creates control |
| [Destroy](Destroy/Destroy.md) | Destroys control |
| Chart event handlers |  |
| [OnEvent](OnEvent/OnEvent.md) | Event handler of all chart events |
| [OnMouseEvent](OnMouseEvent/OnMouseEvent.md) | Event handler for the [CHARTEVENT\_MOUSE\_MOVE](../../../Constants,-Enumerations-and-Structures/Chart-Constants/Types-of-Chart-Events/Types-of-Chart-Events.md) event |
| Name |  |
| [Name](Name/Name.md) | Gets control name |
| Access to container |  |
| [ControlsTotal](ControlsTotal/ControlsTotal.md) | Gets the number of controls in the container |
| [Control](Control/Control.md) | Gets the control by index |
| [ControlFind](ControlFind/ControlFind.md) | Gets the control by ID |
| Geometry |  |
| [Rect](Rect/Rect.md) | Gets the control coordinates |
| [Left](Left/Left.md) | Gets/sets the X coordinate of the upper-left corner |
| [Top](Top/Top.md) | Gets/sets the Y coordinate of the upper-left corner |
| [Right](Right/Right.md) | Gets/sets the X coordinate of the lower-right corner |
| [Bottom](Bottom/Bottom.md) | Gets/sets the Y coordinate of the lower-right corner |
| [Width](Width/Width.md) | Gets/sets the control width |
| [Height](Height/Height.md) | Gets/sets the control height |
| [Move](Move/Move.md) | Control absolute displacement |
| [Shift](Shift/Shift.md) | Control relative displacement |
| [Resize](Resize/Resize.md) | Changes control size |
| [Contains](Contains/Contains.md) | Checks if the point/control is inside the control area |
| Align |  |
| [Alignment](Alignment/Alignment.md) | Sets alignment properties of the control |
| [Align](Align/Align.md) | Performs control alignment in the specified chart area |
| Identification |  |
| [Id](Id/Id.md) | Gets/sets the control ID |
| State |  |
| [IsEnabled](IsEnabled/IsEnabled.md) | Checks the control ability to respond to user's actions |
| [Enable](Enable/Enable.md) | Enables the control ability to respond to user's actions |
| [Disable](Disable/Disable.md) | Disables the control ability to respond to user's actions |
| [IsVisible](IsVisible/IsVisible.md) | Checks the visibility flag |
| [Visible](Visible/Visible.md) | Sets the visibility flag |
| [Show](Show/Show.md) | Shows the control |
| [Hide](Hide/Hide.md) | Hides the control |
| [IsActive](IsActive/IsActive.md) | Checks the control activity |
| [Activate](Activate/Activate.md) | Activates the control |
| [Deactivate](Deactivate/Deactivate.md) | Deactivates the control |
| State flags |  |
| [StateFlags](StateFlags/StateFlags.md) | Gets/sets the control state flags |
| [StateFlagsSet](StateFlagsSet/StateFlagsSet.md) | Sets the control state flags |
| [StateFlagsReset](StateFlagsReset/StateFlagsReset.md) | Resets the control state flags |
| Properties flags |  |
| [PropFlags](PropFlags/PropFlags.md) | Gets/sets the control properties flags |
| [PropFlagsSet](PropFlagsSet/PropFlagsSet.md) | Sets the control properties flags |
| [PropFlagsReset](PropFlagsReset/PropFlagsReset.md) | Resets the control properties flags |
| Mouse operations |  |
| [MouseX](MouseX/MouseX.md) | Gets/saves the mouse X coordinate |
| [MouseY](MouseY/MouseY.md) | Gets/saves the mouse Y coordinate |
| [MouseFlags](MouseFlags/MouseFlags.md) | Gets/saves the mouse buttons state |
| [MouseFocusKill](MouseFocusKill/MouseFocusKill.md) | Kills mouse focus |
| Internal event handlers |  |
| [OnCreate](OnCreate/OnCreate.md) | "Create" event handler |
| [OnDestroy](OnDestroy/OnDestroy.md) | "Destroy" event handler |
| [OnMove](OnMove/OnMove.md) | "Move" event handler |
| [OnResize](OnResize/OnResize.md) | "Resize" event handler |
| [OnEnable](OnEnable/OnEnable.md) | "Enable" event handler |
| [OnDisable](OnDisable/OnDisable.md) | "Disable" event handler |
| [OnShow](OnShow/OnShow.md) | "Show" event handler |
| [OnHide](OnHide/OnHide.md) | "Hide" event handler |
| [OnActivate](OnActivate/OnActivate.md) | "Activate" event handler |
| [OnDeactivate](OnDeactivate/OnDeactivate.md) | "Deactivate" event handler |
| [OnClick](OnClick/OnClick.md) | "Click" event handler |
| [OnChange](OnChange/OnChange.md) | "Change" event handler |
| Mouse event handlers |  |
| [OnMouseDown](OnMouseDown/OnMouseDown.md) | "MouseDown" event handler |
| [OnMouseUp](OnMouseUp/OnMouseUp.md) | "MouseUp" event handler |
| Drag event handlers |  |
| [OnDragStart](OnDragStart/OnDragStart.md) | "DragStart" event handler |
| [OnDragProcess](OnDragProcess/OnDragProcess.md) | "DragProcess" event handler |
| [OnDragEnd](OnDragEnd/OnDragEnd.md) | "DragEnd" event handler |
| Drag object |  |
| [DragObjectCreate](DragObjectCreate/DragObjectCreate.md) | Creates drag object |
| [DragObjectDestroy](DragObjectDestroy/DragObjectDestroy.md) | Destroys drag object |

|  |
| --- |
| Methods inherited from class CObject  Prev, Prev, Next, Next, [Save](../../Basic-Class-CObject/Save/Save.md), [Load](../../Basic-Class-CObject/Load/Load.md), [Type](../../Basic-Class-CObject/Type/Type.md), [Compare](../../Basic-Class-CObject/Compare/Compare.md) |