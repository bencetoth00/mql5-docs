# CScroll

CScroll

CScroll is a base class for creation of scroll bars.

Description

CScroll is a complex control (with dependent controls), it contains the base functionality for creation of scroll bars. The base class itself is not used as a separate control, two of its heirs ([CScrollV](../CScrollV/CScrollV.md) and [CScrollH](../CScrollH/CScrollH.md) classes) are used as controls.

Declaration

|  |
| --- |
| class CScroll : public CWndContainer |

Title

|  |
| --- |
| #include <Controls\Scrolls.mqh> |

|  |
| --- |
| Inheritance hierarchy    [CObject](../../Basic-Class-CObject/Basic-Class-CObject.md)        [CWnd](../CWnd/CWnd.md)            [CWndContainer](../CWndContainer/CWndContainer.md)                CScroll  Direct descendants  [CScrollH](../CScrollH/CScrollH.md), [CScrollV](../CScrollV/CScrollV.md) |

Class Methods by Groups

| Create |  |
| --- | --- |
| [Create](Create/Create.md) | Creates control |
| Chart object event handlers |  |
| [OnEvent](OnEvent/OnEvent.md) | Event handler of all chart events |
| Properties |  |
| [MinPos](MinPos/MinPos.md) | Gets/sets the minimal position |
| [MaxPos](MaxPos/MaxPos.md) | Gets/sets the maximal position |
| [CurrPos](CurrPos/CurrPos.md) | Gets/sets the current position |
| Dependent controls creation |  |
| [CreateBack](CreateBack/CreateBack.md) | Creates background button |
| [CreateInc](CreateInc/CreateInc.md) | Creates increment button of the scroll bar |
| [CreateDec](CreateDec/CreateDec.md) | Creates decrement button of the scroll bar |
| [CreateThumb](CreateThumb/CreateThumb.md) | Creates thumb button (can be dragged) of the scroll bar |
| Dependent controls event handlers |  |
| [OnClickInc](OnClickInc/OnClickInc.md) | Event handler used for handling increment button events |
| [OnClickDec](OnClickDec/OnClickDec.md) | Event handler used for handling decrement button events |
| Internal event handlers |  |
| [OnShow](OnShow/OnShow.md) | "Create" internal event handler |
| [OnHide](OnHide/OnHide.md) | "Hide" internal event handler |
| [OnChangePos](OnChangePos/OnChangePos.md) | "ChangePosition" internal event handler |
| Object drag handlers |  |
| [OnThumbDragStart](OnThumbDragStart/OnThumbDragStart.md) | "ThumbDragStart" event handler |
| [OnThumbDragProcess](OnThumbDragProcess/OnThumbDragProcess.md) | "ThumbDragProcess" event handler |
| [OnThumbDragEnd](OnThumbDragEnd/OnThumbDragEnd.md) | "ThumbDragEnd" event handler |
| Position |  |
| [CalcPos](CalcPos/CalcPos.md) | Gets scroll bar position by coordinate |

| Methods inherited from class CObject  Prev, Prev, Next, Next, [Type](../../Basic-Class-CObject/Type/Type.md), [Compare](../../Basic-Class-CObject/Compare/Compare.md) |
| --- |
| Methods inherited from class CWnd  [Name](../CWnd/Name/Name.md), [ControlsTotal](../CWnd/ControlsTotal/ControlsTotal.md), [Control](../CWnd/Control/Control.md), [Rect](../CWnd/Rect/Rect.md), [Left](../CWnd/Left/Left.md), [Left](../CWnd/Left/Left.md), [Top](../CWnd/Top/Top.md), [Top](../CWnd/Top/Top.md), [Right](../CWnd/Right/Right.md), [Right](../CWnd/Right/Right.md), [Bottom](../CWnd/Bottom/Bottom.md), [Bottom](../CWnd/Bottom/Bottom.md), [Width](../CWnd/Width/Width.md), [Width](../CWnd/Width/Width.md), [Height](../CWnd/Height/Height.md), [Height](../CWnd/Height/Height.md), Size, Size, Size, [Contains](../CWnd/Contains/Contains.md), [Contains](../CWnd/Contains/Contains.md), [Alignment](../CWnd/Alignment/Alignment.md), [Align](../CWnd/Align/Align.md), [Id](../CWnd/Id/Id.md), [IsEnabled](../CWnd/IsEnabled/IsEnabled.md), [IsVisible](../CWnd/IsVisible/IsVisible.md), [Visible](../CWnd/Visible/Visible.md), [IsActive](../CWnd/IsActive/IsActive.md), [Activate](../CWnd/Activate/Activate.md), [Deactivate](../CWnd/Deactivate/Deactivate.md), [StateFlags](../CWnd/StateFlags/StateFlags.md), [StateFlags](../CWnd/StateFlags/StateFlags.md), [StateFlagsSet](../CWnd/StateFlagsSet/StateFlagsSet.md), [StateFlagsReset](../CWnd/StateFlagsReset/StateFlagsReset.md), [PropFlags](../CWnd/PropFlags/PropFlags.md), [PropFlags](../CWnd/PropFlags/PropFlags.md), [PropFlagsSet](../CWnd/PropFlagsSet/PropFlagsSet.md), [PropFlagsReset](../CWnd/PropFlagsReset/PropFlagsReset.md), [MouseX](../CWnd/MouseX/MouseX.md), [MouseX](../CWnd/MouseX/MouseX.md), [MouseY](../CWnd/MouseY/MouseY.md), [MouseY](../CWnd/MouseY/MouseY.md), [MouseFlags](../CWnd/MouseFlags/MouseFlags.md), [MouseFlags](../CWnd/MouseFlags/MouseFlags.md), [MouseFocusKill](../CWnd/MouseFocusKill/MouseFocusKill.md), BringToTop |
| Methods inherited from class CWndContainer  [Destroy](../CWndContainer/Destroy/Destroy.md), [OnMouseEvent](../CWndContainer/OnMouseEvent/OnMouseEvent.md), [ControlsTotal](../CWndContainer/ControlsTotal/ControlsTotal.md), [Control](../CWndContainer/Control/Control.md), [ControlFind](../CWndContainer/ControlFind/ControlFind.md), [MouseFocusKill](../CWndContainer/MouseFocusKill/MouseFocusKill.md), [Add](../CWndContainer/Add/Add.md), [Add](../CWndContainer/Add/Add.md), [Delete](../CWndContainer/Delete/Delete.md), [Delete](../CWndContainer/Delete/Delete.md), [Move](../CWndContainer/Move/Move.md), [Move](../CWndContainer/Move/Move.md), [Shift](../CWndContainer/Shift/Shift.md), [Id](../CWndContainer/Id/Id.md), [Enable](../CWndContainer/Enable/Enable.md), [Disable](../CWndContainer/Disable/Disable.md), [Show](../CWndContainer/Show/Show.md), [Hide](../CWndContainer/Hide/Hide.md), [Save](../CWndContainer/Save/Save.md), [Load](../CWndContainer/Load/Load.md) |
