# CWndClient


CWndClient is a class of the "Client area" complex control (with dependent controls). It is a base class for creation of scroll bars area.

### Description

CWndClient implements the functionality for creation of client area with scroll bars.

### Declaration

```cpp
   class CWndClient : public CWndContainer
```

### Title

```cpp
   #include <Controls\WndClient.mqh>
```

|  |
| --- |
| Inheritance hierarchy    [CObject](../../Basic-Class-CObject/Basic-Class-CObject.md)        [CWnd](../CWnd/CWnd.md)            [CWndContainer](../CWndContainer/CWndContainer.md)                CWndClient  Direct descendants  [CCheckGroup](../CCheckGroup/CCheckGroup.md), [CListView](../CListView/CListView.md), [CRadioGroup](../CRadioGroup/CRadioGroup.md) |

### Class Methods by Groups

| Create |  |
| --- | --- |
| [Create](Create/Create.md) | Creates control |
| Chart event handler |  |
| [OnEvent](OnEvent/OnEvent.md) | Event handler of all chart events |
| Properties |  |
| [ColorBackground](ColorBackground/ColorBackground.md) | Sets background color |
| [ColorBorder](ColorBorder/ColorBorder.md) | Sets border color |
| [BorderType](BorderType/BorderType.md) | Sets border type |
| Settings |  |
| [VScrolled](VScrolled/VScrolled.md) | Gets/sets the flag indicating that vertical scroll bar is used |
| [HScrolled](HScrolled/HScrolled.md) | Gets/sets the flag indicating that horizontal scroll bar is used |
| Dependent controls |  |
| [CreateBack](CreateBack/CreateBack.md) | Creates background for scroll bar |
| [CreateScrollV](CreateScrollV/CreateScrollV.md) | Creates vertical scroll bar |
| [CreateScrollH](CreateScrollH/CreateScrollH.md) | Creates horizontal scroll bar |
| Internal event handlers |  |
| [OnResize](OnResize/OnResize.md) | "Resize" internal event handler |
| Dependent controls event handlers |  |
| [OnVScrollShow](OnVScrollShow/OnVScrollShow.md) | "Show" internal event handler (virtual) of VScroll dependent control |
| [OnVScrollHide](OnVScrollHide/OnVScrollHide.md) | "Hide" internal event handler (virtual) of VScroll dependent control |
| [OnHScrollShow](OnHScrollShow/OnHScrollShow.md) | "Show" internal event handler (virtual) of HScroll dependent control |
| [OnHScrollHide](OnHScrollHide/OnHScrollHide.md) | "Hide" internal event handler (virtual) of HScroll dependent control |
| [OnScrollLineDown](OnScrollLineDown/OnScrollLineDown.md) | "ScrollLineDown" internal event handler (virtual) of VScroll dependent control |
| [OnScrollLineUp](OnScrollLineUp/OnScrollLineUp.md) | "ScrollLineUp" internal event handler (virtual) of VScroll dependent control |
| [OnScrollLineLeft](OnScrollLineLeft/OnScrollLineLeft.md) | "ScrollLineLeft" internal event handler (virtual) of HScroll dependent control |
| [OnScrollLineRight](OnScrollLineRight/OnScrollLineRight.md) | "ScrollLineRight" internal event handler (virtual) of HScroll dependent control |
| Resize |  |
| [Rebound](Rebound/Rebound.md) | Sets new parameters of the control using CRect class coordinates |

| Methods inherited from class CObject  Prev, Prev, Next, Next, [Type](../../Basic-Class-CObject/Type/Type.md), [Compare](../../Basic-Class-CObject/Compare/Compare.md) |
| --- |
| Methods inherited from class CWnd  [Name](../CWnd/Name/Name.md), [ControlsTotal](../CWnd/ControlsTotal/ControlsTotal.md), [Control](../CWnd/Control/Control.md), [Rect](../CWnd/Rect/Rect.md), [Left](../CWnd/Left/Left.md), [Left](../CWnd/Left/Left.md), [Top](../CWnd/Top/Top.md), [Top](../CWnd/Top/Top.md), [Right](../CWnd/Right/Right.md), [Right](../CWnd/Right/Right.md), [Bottom](../CWnd/Bottom/Bottom.md), [Bottom](../CWnd/Bottom/Bottom.md), [Width](../CWnd/Width/Width.md), [Width](../CWnd/Width/Width.md), [Height](../CWnd/Height/Height.md), [Height](../CWnd/Height/Height.md), Size, Size, Size, [Contains](../CWnd/Contains/Contains.md), [Contains](../CWnd/Contains/Contains.md), [Alignment](../CWnd/Alignment/Alignment.md), [Align](../CWnd/Align/Align.md), [Id](../CWnd/Id/Id.md), [IsEnabled](../CWnd/IsEnabled/IsEnabled.md), [IsVisible](../CWnd/IsVisible/IsVisible.md), [Visible](../CWnd/Visible/Visible.md), [IsActive](../CWnd/IsActive/IsActive.md), [Activate](../CWnd/Activate/Activate.md), [Deactivate](../CWnd/Deactivate/Deactivate.md), [StateFlags](../CWnd/StateFlags/StateFlags.md), [StateFlags](../CWnd/StateFlags/StateFlags.md), [StateFlagsSet](../CWnd/StateFlagsSet/StateFlagsSet.md), [StateFlagsReset](../CWnd/StateFlagsReset/StateFlagsReset.md), [PropFlags](../CWnd/PropFlags/PropFlags.md), [PropFlags](../CWnd/PropFlags/PropFlags.md), [PropFlagsSet](../CWnd/PropFlagsSet/PropFlagsSet.md), [PropFlagsReset](../CWnd/PropFlagsReset/PropFlagsReset.md), [MouseX](../CWnd/MouseX/MouseX.md), [MouseX](../CWnd/MouseX/MouseX.md), [MouseY](../CWnd/MouseY/MouseY.md), [MouseY](../CWnd/MouseY/MouseY.md), [MouseFlags](../CWnd/MouseFlags/MouseFlags.md), [MouseFlags](../CWnd/MouseFlags/MouseFlags.md), [MouseFocusKill](../CWnd/MouseFocusKill/MouseFocusKill.md), BringToTop |
| Methods inherited from class CWndContainer  [Destroy](../CWndContainer/Destroy/Destroy.md), [OnMouseEvent](../CWndContainer/OnMouseEvent/OnMouseEvent.md), [ControlsTotal](../CWndContainer/ControlsTotal/ControlsTotal.md), [Control](../CWndContainer/Control/Control.md), [ControlFind](../CWndContainer/ControlFind/ControlFind.md), [MouseFocusKill](../CWndContainer/MouseFocusKill/MouseFocusKill.md), [Add](../CWndContainer/Add/Add.md), [Add](../CWndContainer/Add/Add.md), [Delete](../CWndContainer/Delete/Delete.md), [Delete](../CWndContainer/Delete/Delete.md), [Move](../CWndContainer/Move/Move.md), [Move](../CWndContainer/Move/Move.md), [Shift](../CWndContainer/Shift/Shift.md), [Enable](../CWndContainer/Enable/Enable.md), [Disable](../CWndContainer/Disable/Disable.md), [Hide](../CWndContainer/Hide/Hide.md), [Save](../CWndContainer/Save/Save.md), [Load](../CWndContainer/Load/Load.md) |