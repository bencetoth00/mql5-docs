# CWndObj


CWndObj is a base class for simple controls (based on chart objects) of the Standard Library.

### Description

CWndObj class implements base methods of the simple control.

### Declaration

```cpp
   class CWndObj : public CWnd
```

### Title

```cpp
   #include <Controls\WndObj.mqh>
```

|  |
| --- |
| Inheritance hierarchy    [CObject](../../Basic-Class-CObject/Basic-Class-CObject.md)        [CWnd](../CWnd/CWnd.md)            CWndObj  Direct descendants  [CBmpButton](../CBmpButton/CBmpButton.md), [CButton](../CButton/CButton.md), [CEdit](../CEdit/CEdit.md), [CLabel](../CLabel/CLabel.md), [CPanel](../CPanel/CPanel.md), [CPicture](../CPicture/CPicture.md) |

### Class Methods by Groups

| Chart events processing |  |
| --- | --- |
| [OnEvent](OnEvent/OnEvent.md) | Event handler of all chart events |
| Properties |  |
| [Text](Text/Text.md) | Gets/sets the [OBJPROP\_TEXT](../../../Constants,-Enumerations-and-Structures/Objects-Constants/Object-Properties/Object-Properties.md#enum_object_property_string) property of the chart object |
| [Color](Color/Color.md) | Gets/sets the [OBJPROP\_COLOR](../../../Constants,-Enumerations-and-Structures/Objects-Constants/Object-Properties/Object-Properties.md#enum_object_property_integer) property of the chart object |
| [ColorBackground](ColorBackground/ColorBackground.md) | Gets/sets the [OBJPROP\_BGCOLOR](../../../Constants,-Enumerations-and-Structures/Objects-Constants/Object-Properties/Object-Properties.md#enum_object_property_integer) property of the chart object |
| [ColorBorder](ColorBorder/ColorBorder.md) | Gets/sets the [OBJPROP\_BORDER\_COLOR](../../../Constants,-Enumerations-and-Structures/Objects-Constants/Object-Properties/Object-Properties.md#enum_object_property_integer) property of the chart object |
| [Font](Font/Font.md) | Gets/sets the [OBJPROP\_FONT](../../../Constants,-Enumerations-and-Structures/Objects-Constants/Object-Properties/Object-Properties.md#enum_object_property_string) property of the chart object |
| [FontSize](FontSize/FontSize.md) | Gets/sets the [OBJPROP\_FONTSIZE](../../../Constants,-Enumerations-and-Structures/Objects-Constants/Object-Properties/Object-Properties.md#enum_object_property_integer) property of the chart object |
| [ZOrder](ZOrder/ZOrder.md) | Gets/sets the [OBJPROP\_ZORDER](../../../Constants,-Enumerations-and-Structures/Objects-Constants/Object-Properties/Object-Properties.md#enum_object_property_integer) property of the chart object |
| Chart objects event handlers |  |
| [OnObjectCreate](OnObjectCreate/OnObjectCreate.md) | [CHARTEVENT\_OBJECT\_CREATE](../../../Constants,-Enumerations-and-Structures/Chart-Constants/Types-of-Chart-Events/Types-of-Chart-Events.md) event handler |
| [OnObjectChange](OnObjectChange/OnObjectChange.md) | [CHARTEVENT\_OBJECT\_CHANGE](../../../Constants,-Enumerations-and-Structures/Chart-Constants/Types-of-Chart-Events/Types-of-Chart-Events.md) event handler |
| [OnObjectDelete](OnObjectDelete/OnObjectDelete.md) | [CHARTEVENT\_OBJECT\_DELETE](../../../Constants,-Enumerations-and-Structures/Chart-Constants/Types-of-Chart-Events/Types-of-Chart-Events.md) event handler |
| [OnObjectDrag](OnObjectDrag/OnObjectDrag.md) | [CHARTEVENT\_OBJECT\_DRAG](../../../Constants,-Enumerations-and-Structures/Chart-Constants/Types-of-Chart-Events/Types-of-Chart-Events.md) event handler |
| Properties change event handlers |  |
| [OnSetText](OnSetText/OnSetText.md) | "SetText" event handler |
| [OnSetColor](OnSetColor/OnSetColor.md) | "SetColor" event handler |
| [OnSetColorBackground](OnSetColorBackground/OnSetColorBackground.md) | "SetColorBackground" event handler |
| [OnSetFont](OnSetFont/OnSetFont.md) | "SetFont" event handler |
| [OnSetFontSize](OnSetFontSize/OnSetFontSize.md) | "SetFontSize" event handler |
| [OnSetZOrder](OnSetZOrder/OnSetZOrder.md) | "SetZOrder" event handler |
| Internal event handlers |  |
| [OnDestroy](OnDestroy/OnDestroy.md) | "Destroy" internal event handler |
| [OnChange](OnChange/OnChange.md) | "Change" internal event handler |

| Methods inherited from class CObject  Prev, Prev, Next, Next, [Save](../../Basic-Class-CObject/Save/Save.md), [Load](../../Basic-Class-CObject/Load/Load.md), [Type](../../Basic-Class-CObject/Type/Type.md), [Compare](../../Basic-Class-CObject/Compare/Compare.md) |
| --- |
| Methods inherited from class CWnd  [Create](../CWnd/Create/Create.md), [Destroy](../CWnd/Destroy/Destroy.md), [OnMouseEvent](../CWnd/OnMouseEvent/OnMouseEvent.md), [Name](../CWnd/Name/Name.md), [ControlsTotal](../CWnd/ControlsTotal/ControlsTotal.md), [Control](../CWnd/Control/Control.md), [ControlFind](../CWnd/ControlFind/ControlFind.md), [Rect](../CWnd/Rect/Rect.md), [Left](../CWnd/Left/Left.md), [Left](../CWnd/Left/Left.md), [Top](../CWnd/Top/Top.md), [Top](../CWnd/Top/Top.md), [Right](../CWnd/Right/Right.md), [Right](../CWnd/Right/Right.md), [Bottom](../CWnd/Bottom/Bottom.md), [Bottom](../CWnd/Bottom/Bottom.md), [Width](../CWnd/Width/Width.md), [Width](../CWnd/Width/Width.md), [Height](../CWnd/Height/Height.md), [Height](../CWnd/Height/Height.md), Size, Size, Size, [Move](../CWnd/Move/Move.md), [Move](../CWnd/Move/Move.md), [Shift](../CWnd/Shift/Shift.md), [Contains](../CWnd/Contains/Contains.md), [Contains](../CWnd/Contains/Contains.md), [Alignment](../CWnd/Alignment/Alignment.md), [Align](../CWnd/Align/Align.md), [Id](../CWnd/Id/Id.md), [Id](../CWnd/Id/Id.md), [IsEnabled](../CWnd/IsEnabled/IsEnabled.md), [Enable](../CWnd/Enable/Enable.md), [Disable](../CWnd/Disable/Disable.md), [IsVisible](../CWnd/IsVisible/IsVisible.md), [Visible](../CWnd/Visible/Visible.md), [Show](../CWnd/Show/Show.md), [Hide](../CWnd/Hide/Hide.md), [IsActive](../CWnd/IsActive/IsActive.md), [Activate](../CWnd/Activate/Activate.md), [Deactivate](../CWnd/Deactivate/Deactivate.md), [StateFlags](../CWnd/StateFlags/StateFlags.md), [StateFlags](../CWnd/StateFlags/StateFlags.md), [StateFlagsSet](../CWnd/StateFlagsSet/StateFlagsSet.md), [StateFlagsReset](../CWnd/StateFlagsReset/StateFlagsReset.md), [PropFlags](../CWnd/PropFlags/PropFlags.md), [PropFlags](../CWnd/PropFlags/PropFlags.md), [PropFlagsSet](../CWnd/PropFlagsSet/PropFlagsSet.md), [PropFlagsReset](../CWnd/PropFlagsReset/PropFlagsReset.md), [MouseX](../CWnd/MouseX/MouseX.md), [MouseX](../CWnd/MouseX/MouseX.md), [MouseY](../CWnd/MouseY/MouseY.md), [MouseY](../CWnd/MouseY/MouseY.md), [MouseFlags](../CWnd/MouseFlags/MouseFlags.md), [MouseFlags](../CWnd/MouseFlags/MouseFlags.md), [MouseFocusKill](../CWnd/MouseFocusKill/MouseFocusKill.md), BringToTop |